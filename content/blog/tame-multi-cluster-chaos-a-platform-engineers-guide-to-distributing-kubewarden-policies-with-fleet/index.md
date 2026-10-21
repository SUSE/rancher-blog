---
title: "Tame multi-cluster chaos. A Platform Engineer's guide to distributed Kubewarden Policies with Fleet"
date: 2025-11-19T08:00:27
slug: "tame-multi-cluster-chaos-a-platform-engineers-guide-to-distributing-kubewarden-policies-with-fleet"
author: "Mario Manno"
image: "images/from-chaos-to-control.png"
products: ["Kubewarden"]
tags: ["policy", "gitops", "multi-cluster"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 170243
  original_url: "https://www.suse.com/c/rancher_blog/tame-multi-cluster-chaos-a-platform-engineers-guide-to-distributing-kubewarden-policies-with-fleet/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "PSP-based policy example"
  redirect_target: ""
---

For platform engineers managing multiple Kubernetes clusters, maintaining policy consistency is a constant struggle. Manually applying security rules across a growing fleet of clusters is inefficient and error-prone. This approach creates significant risks:

- **Policy Drift:** A policy is temporarily disabled in one cluster and never re-enabled. A new cluster is provisioned without baseline security rules. These inconsistencies, known as drift, create security holes and compliance gaps.
- **Lack of Visibility:** Answering "Which clusters are enforcing the image signing policy?" becomes a difficult task involving scripts, spreadsheets, and guesswork.
- **Operational Toil:** Every new policy or cluster increases the manual workload, preventing your team from focusing on building a more resilient, automated platform.

As your environment scales, this operational burden becomes unsustainable. Each out-of-sync policy represents a potential security gap, increasing the cluster's attack surface.

## **Automating policy distribution with a GitOps workflow**

It's time to treat your security policies like your applications: as code stored in Git. By combining Kubewarden, a Kubernetes Policy Engine, with Fleet, a GitOps tool, you can automate policy distribution and enforcement.

The principle is to make Git your single source of truth. You define Kubewarden policies in a Git repository, and Fleet ensures they are automatically deployed and enforced across all target clusters.

- **Kubewarden:** A universal policy engine that enforces your rules inside each cluster.
- **Fleet:** A lightweight, pull-based GitOps tool for multi-cluster management. Agents in each managed cluster pull their configuration from the Fleet controller, meaning the management cluster does not initiate connections to downstream clusters.

## **Bootstrap Kubewarden across your clusters with Fleet**

Before you can distribute policies, Kubewarden itself must be installed on your target clusters. Instead of managing the Kubewarden Helm charts within your own Git repository, you can use Fleet's `HelmOp` feature to deploy them directly from the official Helm repository. This is a simpler and more direct approach for third-party applications.

We'll create three `HelmOp` resources, one for each component of the Kubewarden stack. We'll use the `dependsOn` field to ensure they are installed in the correct order: CRDs first, then the controller, and finally the defaults.

### **Apply the following manifest to your Fleet management cluster:**

`--- apiVersion: fleet.cattle.io/v1alpha1 kind: HelmOp metadata:   name: helmop-kubewarden-crds spec:   defaultNamespace: kubewarden # This is the target namespace on the downstream clusters.   helm:     repo: https://charts.kubewarden.io     chart: kubewarden-crds   targets:   - clusterSelector:       matchLabels: {} --- apiVersion: fleet.cattle.io/v1alpha1 kind: HelmOp metadata:   name: helmop-kubewarden-controller spec:   defaultNamespace: kubewarden   dependsOn:   - name: "helmop-kubewarden-crds"   helm:     repo: https://charts.kubewarden.io     chart: kubewarden-controller   targets:   - clusterSelector:       matchLabels: {} --- apiVersion: fleet.cattle.io/v1alpha1 kind: HelmOp metadata:   name: helmop-kubewarden-defaults spec:   defaultNamespace: kubewarden   dependsOn:   - name: "helmop-kubewarden-controller"   helm:     repo: https://charts.kubewarden.io     chart: kubewarden-defaults     # Enable the defaults     # values:     #   recommendedPolicies:     #     enabled: true   targets:   - clusterSelector:       matchLabels: {}`

With this in place, any new cluster registered with Fleet will automatically have the full Kubewarden stack installed in the correct sequence.

## Step-by-step instructions to build your policy distribution pipeline

With Kubewarden installed across your clusters, you can now focus on distributing your own policies using a `GitRepo`. If you do not need custom policies, you could enable the `recommendedPolicies` in the HelmOps resource and can skip to the end of this post.

While the default policies are a great start, many organizations have unique security and compliance requirements. For scenarios where you need to write, manage, and distribute your own custom policies, Fleet’s `GitRepo` resource provides a powerful policy-as-code solution.

### **Structure Your Git Repository**

To avoid repetition, we'll define a single shared configuration file (`options.yaml`) and place each policy manifest in its own directory. This structure is clean and scales easily as you add more policies.

```
policies/
├── psp-policies/
│   ├── disallow-root-user/
│   │   └── policy.yaml
│   └── another-psp-policy/
│       └── policy.yaml
├── other-policies/
│   └── some-other-policy/
│       └── policy.yaml
└── options.yaml  # Shared configuration for all policies
```

### **Define the Kubewarden Policy as Code**

Each policy manifest is a standard Kubewarden `ClusterAdmissionPolicy`.

```
# policies/psp-policies/disallow-root-user/policy.yaml
apiVersion: policies.kubewarden.io/v1
kind: ClusterAdmissionPolicy
metadata:
  name: disallow-root-user
spec:
  module: registry://ghcr.io/kubewarden/policies/user-group-psp:v0.4.9
  rules:
  - apiGroups: [""]
    apiVersions: ["v1"]
    resources: ["pods"]
    operations:
    - CREATE
    - UPDATE
  mutating: true
  settings:
    run_as_user:
      rule: MustRunAsNonRoot
```

### **Create a Shared** **options.yaml** **for deployment**

This file contains the common deployment settings, such as the `defaultNamespace` and `rolloutStrategy`, that will be applied to all policies.

```
# policies/options.yaml
defaultNamespace: kubewarden
# This strategy deploys the policy to all target clusters simultaneously, prioritizing speed over a phased rollout.
rolloutStrategy:
  maxUnavailable: 100%
  autoPartitionSize: 100%
```

### **Create the** **GitRepo** **resource with the driven format**

Finally, create a `GitRepo` resource using Fleet's `bundles` (driven) format. This allows you to explicitly declare each policy as a bundle, referencing its `base` directory and the shared `options.yaml` file. This approach is more declarative and scalable than scanning paths.

```
apiVersion: fleet.cattle.io/v1alpha1
kind: GitRepo
metadata:
  namespace: fleet-default
  name: kubewarden-security-policies
spec:
  repo: "https://github.com/your-org/kubernetes-policies.git"
  branch: main
  # Define each policy as an explicit bundle, referencing the shared options file.
  bundles:
    - base: policies/psp-policies/disallow-root-user
      options: ../../options.yaml
    - base: policies/psp-policies/another-psp-policy
      options: ../../options.yaml
    - base: policies/other-policies/some-other-policy
      options: ../../options.yaml
  # Enable drift correction
  correctDrift:
    enabled: true
  targets:
  - clusterSelector:
      matchLabels: {}
```

Once you apply this `GitRepo`, Fleet's controller processes each defined bundle and the `fleet-agent` on each target cluster applies the corresponding `ClusterAdmissionPolicy`.

### **The payoff is consistent, auditable, and scalable governance**

Adopting this GitOps workflow transforms policy management from a manual task into a streamlined, automated process with immediate benefits:

- **Eliminate Policy Drift:** Git is now the source of truth. If a policy is manually modified or deleted on a downstream cluster, Fleet’s drift correction feature automatically reverts the change, restoring the desired state from the repository. New clusters are automatically brought into compliance.
- **Gain Full Auditability:** Every change to a policy goes through a Git commit and pull request, providing a clear, auditable history of who changed what, when, and why.

**Scale Effortlessly:** This architecture scales from a few clusters to hundreds without increasing operational overhead. Adding a new policy is as simple as adding a new folder to your Git repository, and onboarding a new cluster is as simple as registering it with Fleet.

### **Get started with automated policy management**

Ready to stop chasing policy drift and start building a scalable governance model?

- **Explore the Docs:** Dive deeper into the features and capabilities of [Kubewarden](https://docs.kubewarden.io/) and [Fleet](https://fleet.rancher.io/).
- **Try it Yourself:** Follow the steps in this guide to set up your first policy-as-code pipeline.
- **Join the Community:** Have questions or want to share your experience? Join the conversation in the #kubewarden channel on the Kubernetes Slack.

Take control of your multi-cluster environment today and build a more secure, consistent, and automated Kubernetes platform.
