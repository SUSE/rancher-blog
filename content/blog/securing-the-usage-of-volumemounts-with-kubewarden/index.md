---
title: "Securing the Usage of volumeMounts with Kubewarden"
date: 2022-11-07T16:33:00
slug: "securing-the-usage-of-volumemounts-with-kubewarden"
author: "Víctor Cuadrado Juan"
image: "images/m7brY_b9_400x400.jpg"
products: ["Kubewarden"]
tags: ["security", "policy"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 96654
  original_url: "https://www.suse.com/c/rancher_blog/securing-the-usage-of-volumemounts-with-kubewarden/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Kubewarden 2022 policy version"
  redirect_target: ""
---

Securing a Kubernetes cluster is far from a simple task. How do you know if you have correctly configured volumeMounts in your in-cluster containers? And what about all those workload resources, such as Deployments, Jobs, Pods, etc? Luckily, you can use [Kubewarden](https://www.kubewarden.io/), an efficient Kubernetes policy engine that runs policies compiled to [Wasm](https://webassembly.org/). This means you can run powerful specifically-written policies, our reuse existing Rego policies for example.

If you prefer not to reuse policies, we present the new [volumeMounts Kubewarden Policy](https://artifacthub.io/packages/kubewarden/volumemounts-policy/volumemounts).  This Kubewarden policy inspects containers, init containers, and ephemeral containers and restricts their usage of volumes by checking the volume name used in the container's `volumeMounts[*].name`.

You can find the policy in [published in Artifact Hub](https://artifacthub.io/packages/kubewarden/volumemounts-policy/volumemounts). As usual, its artifact is signed with Sigstore in keyless mode, and if you are curious, you can peek into the policy’s [implementation in Rust here](https://github.com/kubewarden/volumemounts-policy).

This new policy joins the already existing [volumes-psp policy](https://artifacthub.io/packages/kubewarden/volumes-psp/volumes-psp), which provides an allowlist of volume types, and [hostpaths-psp policy](https://artifacthub.io/packages/kubewarden/hostpaths-psp/hostpaths-psp), with an allowlist of hostPath volumes.

## What is useful about the new volumeMounts policy?

The existing PSP policies restricted the usage of volumes as a cluster admin. The new volumeMounts policy has settings with 4 operators that enable you to check for compliance and migration use cases, even if you don’t have access to controlling the creation of Volumes in the cluster. Let’s see them:

- `reject: anyIn`: Works as a denylist of your usage of volumes. Since we are checking volume names, we can also filter [Out-Of-Tree volumes](https://kubernetes.io/docs/concepts/storage/volumes/#out-of-tree-volume-plugins):

  ```
  reject: anyIn
  volumeMountsNames:
  - my-secure-hostpath-volume
  - my-cache-volume
  - my-out-of-tree-volume
  ```
- `reject: anyNotIn`: Works as an allowlist.

  ```
  reject: anyNotIn
  volumeMountsNames:
  - my-secrets-volume
  - my-volume2
  ```
- `reject: allAreUsed`: The container cannot use all listed volumes at once. Helpful for enforcing migration between volumes, for example:

  ```
  reject: allAreUsed
  volumeMountsNames:
  - old-deprecated-volume
  - new-supported-volume
  ```
- `reject: notAllAreUsed`: The container can use all listed volumes at once, but only one of them. Helpful for enforcing backup operations, for example:

  ```
  reject: notAllAreUsed
  volumeMountsNames:
  - work-volume
  - backup-volume
  ```

## In action

Just instantiate an `AdmissionPolicy` or cluster-wide `ClusterAdmissionPolicy` with the policy module and settings. Here’s a definition of a policy that rejects any workload resource (Pods, Deployments, Cronjobs..) that doesn’t adhere to the provided `volumeMounts` allowlist:

```
kubectl apply -f - <<EOF
apiVersion: policies.kubewarden.io/v1
kind: ClusterAdmissionPolicy
metadata:
  name: volumemounts-policy
spec:
  module: ghcr.io/kubewarden/policies/volumemounts:v0.1.2
  mutating: false
  rules:
  - apiGroups: [""]
    apiVersions: ["v1"]
    resources: ["pods", "deployments", "replicasets", "daemonsets", "replicationcontrollers", "jobs", "cronjobs"]
    operations:
    - CREATE
    - UPDATE
  settings:
    reject: anyNotIn # as an allowlist
    volumeMountsNames:
    - my-volume
    - my-volume2
EOF
```

Let’s instantiate a Pod that uses a Volume with a name that is not in the allowlist:

```
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMountsNames:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir: {}
EOF
```

As expected, the Pod is rejected:

```
Error from server: error when creating "STDIN":
admission webhook "clusterwide-volumemounts-policy.kubewarden.admission" denied the request:
container test-container is invalid: volumeMount names not allowed: ["cache-volume"]
```

### **Try the policy for yourself!**

As usual, we look forward to your feedback! Have ideas for new policies? Would you like more features on existing ones? Drop us a line at [#kubewarden on Slack](https://kubernetes.slack.com/archives/C01T3GTC3L7)! :)
