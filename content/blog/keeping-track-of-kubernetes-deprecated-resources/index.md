---
title: "Keeping Track of Kubernetes Deprecated Resources"
date: 2022-11-09T23:12:30
slug: "keeping-track-of-kubernetes-deprecated-resources"
authors: ["Víctor Cuadrado Juan"]
image: "images/m7brY_b9_400x400.jpg"
products: ["Kubewarden"]
tags: ["policy", "upgrades", "security"]
content_type: "release"
draft: false
migration:
  wp_id: 96828
  original_url: "https://www.suse.com/c/rancher_blog/keeping-track-of-kubernetes-deprecated-resources/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Policy release, K8s 1.26 era"
  redirect_target: ""
---

It’s a fact of life: as the Kubernetes API evolves, it’s periodically reorganized or upgraded. This means some Kubernetes resources can be [deprecated and later removed](https://kubernetes.io/docs/reference/using-api/deprecation-policy/#deprecating-parts-of-the-api). We deserve to keep track of those deprecations and removals easily. For that, we have just released the new [deprecated-api-versions policy](https://github.com/kubewarden/deprecated-api-versions-policy/) for [Kubewarden,](https://www.kubewarden.io/) our efficient Kubernetes policy engine that runs policies compiled to [Wasm](https://webassembly.org/). This policy checks for the usage of Kubernetes resources that have been deprecated or removed from the Kubernetes API.

## A look at the deprecated-api-versions policy

This policy has two settings:

1. `kubernetes_version`: The starting version begins with where to detect deprecated or removed Kubernetes resources. This setting is mandatory.
2. `deny_on_deprecation:` If true, it will deny the operation on a resource that has been deprecated but not yet removed from the Kubernetes version specified by `kubernetes_version`. This setting is optional and is set to `true` by default.

As an example, `extensions/v1beta1/Ingress` was deprecated in Kubernetes `1.14.0`, and removed in `v1.22.0`.

With the following policy settings, the policy accepts an `extensions/v1beta1/Ingress` in the cluster, yet the policy logs this result:

```
kubernetes_version: "1.19.0"
deny_on_deprecation: false
```

In contrast, with these other settings, the policy blocks the Ingress object:

```
kubernetes_version: "1.19.0"
deny_on_deprecation: true # (the default)
```

## Don’t live in the past

Kubernetes deprecations evolve; we will update the policy as soon as there are new deprecations. The policy versioning scheme tells you up to what version of Kubernetes the policy knows about, e.g. `0.1.0-k8sv1.26.0` means that the policy knows about deprecations up to Kubernetes `v1.26.0`.

## Back to the future

You are about to update your cluster’s Kubernetes version and wonder, will your workloads keep working? Will you be in trouble because of deprecated or removed resources in the new version? **Check before updating**! Just instantiate the deprecated-api-versions policy with the targetted Kubernetes version and `deny_on_deprecation` set to false, and get an overview of future-you problems.

## In action

As usual, instantiate a `ClusterAdmissionPolicy` (cluster-wide) or `AdmissionPolicy` (namespaced) that makes use of the policy.

For this example, let’s work in a k8s cluster of version `1.24.0`.

Here’s a definition of a cluster-wide policy that rejects resources that were deprecated or removed in Kubernetes version `1.23.0` and earlier:

```
kubectl apply -f - <<EOF
apiVersion: policies.kubewarden.io/v1
kind: ClusterAdmissionPolicy
metadata:
  name: my-deprecated-api-versions-policy
spec:
  module: ghcr.io/kubewarden/policies/deprecated-api-versions:v0.1.0-k8sv1.26.0
  mutating: false
  rules:
  - apiGroups: ["*"]
    apiVersions: ["*"]
    resources: ["*"]
    operations:
    - CREATE
    - UPDATE
  settings:
    kubernetes_version: "1.23.0"
    deny_on_deprecation: true
EOF
```

> **Info:** In `spec.rules` we are checking every resource in every apiGroup and apiVersions. We are doing it for simplicity in this example, yet the policy [metadata.yaml](https://github.com/kubewarden/deprecated-api-versions-policy/blob/b26633515de367cf77b79fb909461a4df6e0e2aa/metadata.yml) comes with long and complete, machine-generated `spec.rules` that covers just the resources that are deprecated.  
> You can obtain the right rules by using the `kwctl scaffold` command.

Our cluster is on version `1.24.0`, so for example, without the policy, we could still instantiate an `autoscaling/v2beta2/HorizontalPodAutoscaler`, even if it is deprecated since `1.23.0` (and will be removed in `1.26.0`).

Now with the policy, trying to instantiate an `autoscaling/v2beta2/HorizontalPodAutoscaler` resource that is already deprecated will result in its rejection:

```
kubectl apply -f - <<EOF
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 10
EOF

Warning: autoscaling/v2beta2 HorizontalPodAutoscaler is deprecated in v1.23+, unavailable in v1.26+; use autoscaling/v2 HorizontalPodAutoscaler
Error from server: error when creating "STDIN":
admission webhook "clusterwide-my-deprecated-api-versions-policy.kubewarden.admission" denied the request:
autoscaling/v2beta2 HorizontalPodAutoscaler cannot be used. It has been deprecated starting from 1.23.0. It has been removed starting from 1.26.0. It has been replaced by autoscaling/v2.
```

**Have ideas for new policies? Would you like more features on existing ones? Drop us a line at [#kubewarden on Slack](https://kubernetes.slack.com/archives/C01T3GTC3L7)! We look forward to your feedback :)**
