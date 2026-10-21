---
title: "What's new in Kubernetes 1.12"
date: 2018-09-24T09:03:00
slug: "whats-new-in-kubernetes-1-12"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["upgrades"]
content_type: "release"
draft: true
migration:
  wp_id: 85825
  original_url: "https://www.suse.com/c/rancher_blog/whats-new-in-kubernetes-1-12/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Kubernetes 1.12 release preview"
  redirect_target: "rancher.com/blog (hub)"
---

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)

Kubernetes 1.12 [will be released](https://github.com/kubernetes/sig-release/blob/master/releases/release-1.12/README.md) this week on Thursday, September 27, 2018. Version 1.12 ships just three months after Kubernetes 1.11 and marks the third major release of this year. The short cycle is inline with the quarterly release cycle the project has followed since it’s GA in 2015.

**Kubernetes releases 2018**

```
| Kubernetes Release | Date               |
|--------------------|--------------------|
| 1.10               | March 26, 2018     |
| 1.11               | June 27, 2018      |
| 1.12               | September 27, 2018 |
```

Whether you are a developer using Kubernetes or an admin operating clusters, it’s worth getting an idea about the new features and fixes that you can expect in Kubernetes 1.12.

A total of [38 features](https://github.com/kubernetes/features/milestone/11) are included in this milestone. Let’s have a look at some of the highlights.

### Kubelet certificate rotation

Kubelet certificate rotation was promoted to [beta status](https://github.com/kubernetes/features/issues/267). This functionality allows for automated renewal of key and a certificate for the kubelet API server as the current certificate approaches expiration. Until the official 1.12 docs have been published, you can read the beta documentation on this feature [here](https://github.com/kubernetes/website/blob/release-1.12/content/en/docs/reference/command-line-tools-reference/kubelet-tls-bootstrapping.md#kubelet-configuration).

### Network Policies: CIDR selector and egress rules

Two formerly beta features have now reached [stable status](https://github.com/kubernetes/features/issues/366): One of them is the `ipBlock` selector, which allows specifying ingress/egress rules based on network addresses in CIDR notation. The second one adds support for filtering the traffic that is leaving the pods by specifying `egress` rules. The below example illustrates the use of both features:

```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      role: app
  policyTypes:
  - Egress
  egress:
  - to:
    - ipBlock:
        cidr: 10.0.0.0/24
(...)
```

As previoulsy beta features, both `egress` and `ipBlock` are already described in the official [network policies documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

### Mount namespace propagation

Mount namespace propagation, i.e. the ability to mount a volume `rshared` so that any mounts from inside the container are reflected in the root (= host) mount namespace, has been [promoted to stable](https://github.com/kubernetes/features/issues/432). You can read more about this feature in the [Kubernetes volumes docs](https://kubernetes.io/docs/concepts/storage/volumes/#mount-propagation).

### Taint nodes by condition

This feature introduced in 1.8 as early alpha has been [promoted to beta](https://github.com/kubernetes/features/issues/382). Enabling it’s featureflag causes the node controller to create taints based on node conditions and the scheduler to filter nodes based on taints instead of conditions. The official documentation is [available here](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/#taint-nodes-by-condition).

### Horizontal pod autoscaler with custom metrics

While support for custom metrics in HPA [continuous to be in beta status](https://github.com/kubernetes/features/issues/117), version 1.12 adds various enhancements like the the ability to select metrics based on the labels available in your monitoring pipeline. If you are interested in autoscaling pods based on application-level metrics provided by monitoring systems such as Prometheus, Sysdig or Datadog, I recommend to checkout the [design proposal for external metrics](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/autoscaling/hpa-external-metrics.md) in HPA.
If you are new to Kubernetes monitoring, check out our Intro to Kuberentes Monitoring. If you’re just getting underway with Kubernetes, read the [Introduction to Kubernetes Monitoring](https://rancher.com/blog/2018/2018-10-18-monitoring-kubernetes/), which will help you get the most out of the rest of this article. for a good primer.

### RuntimeClass

RuntimeClass is a new cluster-scoped resource “that surfaces container runtime properties to the control plane”. In other words: This [early alpha feature](https://github.com/kubernetes/features/issues/585) will enable users to select and configure (per pod) a specific container runtime (such as Docker, Rkt or Virtlet) by providing the `runtimeClass` field in the `PodSpec`. You can read more about it in [these docs](https://github.com/kubernetes/website/blob/release-1.12/content/en/docs/concepts/containers/runtime-class.md).

### Resource Quota by priority

[Resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas) allow administrators to limit the resource consumption in namespaces. This is especially practical in scenarios where the available compute and storage resources in a cluster are shared by several tenants (users, teams). The beta feature [Resource quota by priority](https://github.com/kubernetes/features/issues/612) allows admins to fine-tune resource allocation within the namespace by scoping quotas based on the PriorityClass of pods. You can find more details [here](https://kubernetes.io/docs/concepts/policy/resource-quotas/#resource-quota-per-priorityclass).

### Volume Snapshots

One of the most exciting new 1.12 features for storage is the [early alpha](https://github.com/kubernetes/features/issues/177) implementation of persistent volume snapshots. This feature allows users to create and restore snapshots at a particular point in time backed by any CSI storage provider. As part of this implementation three new API resources have been added:
`VolumeSnapshotClass` defines how snapshots for existing volumes are provisioned. `VolumeSnapshotContent` represents existing snapshots and `VolumeSnapshot` allows users to request a new snapshot of a persistent volume like so:

```
apiVersion: snapshot.storage.k8s.io/v1alpha1
kind: VolumeSnapshot
metadata:
  name: new-snapshot-test
spec:
  snapshotClassName: csi-hostpath-snapclass
  source:
    name: pvc-test
    kind: PersistentVolumeClaim
```

For the nitty gritty details take a look at the 1.12 [documentation branch](https://GitHub.com/kubernetes/website/blob/release-1.12/content/en/docs/concepts/storage/volume-snapshots.md) on Github.

### Topology aware dynamic provisioning

Another storage related feature, topology aware dynamic provisioning, was introduced in v1.11 and has been [promoted to beta in 1.12](https://github.com/kubernetes/features/issues/561). It addresses some limitations with dynamic provisioning of volumes in clusters spread across multiple zones where single-zone storage backends are not globally accessible from all nodes.

### Enhancements for Azure Cloud provider

These two improvements regarding running Kubernetes in Azure are shipping in 1.12:

#### Cluster autoscaler support

The [cluster autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) support for Azure was [promoted to stable](https://github.com/kubernetes/features/issues/514). This will allow for automatic scaling of the number of Azure nodes in Kubernetes clusters based on global resource usage.

#### Azure availability zone support

Kubernetes v1.12 adds alpha support for [Azure availability zones (AZ)](https://azure.microsoft.com/en-us/global-infrastructure/availability-zones/). Nodes in an availability zone will be added with label `failure-domain.beta.kubernetes.io/zone=<region>-<AZ>` , and topology-aware provisioning is added for Azure managed disks storage class.

### Anything else?

Kubernetes 1.12 contains many bug fixes and improvements of internal components, clearly focusing on stabilising the core, maturing existing beta features and improving the release velocity by adding more automated tests to the projects CI pipeline. A noteworthy example for the latter is the addition of [CI e2e conformance tests](https://github.com/kubernetes/features/issues/288) for arm, arm64, ppc64, s390x and windows platforms to the projects test harness.

For a full list of changes in 1.12 see the [release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.12.md).

---

*Rancher will support Kubernetes 1.12 on hosted clusters as soon as it becomes available on the particular provider. For RKE provisioned clusters it will be supported starting with Rancher 2.2.*

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)
