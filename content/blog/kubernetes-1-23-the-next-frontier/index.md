---
title: "Kubernetes 1.23: The Next Frontier    "
date: 2021-12-07T20:37:06
slug: "kubernetes-1-23-the-next-frontier"
authors: ["Rey Lejano"]
products: ["Kubernetes (generic)"]
tags: ["security"]
content_type: "release"
draft: true
migration:
  wp_id: 93064
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-1-23-the-next-frontier/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Kubernetes 1.23 release"
  redirect_target: "rancher.com/blog (hub)"
---

I had the honor and privilege to lead the Kubernetes 1.23 release on December 7, 2021.Including myself, 41 people on the 1.23 release team managed the day-to-day work required to release Kubernetes. The release team is part of the Kubernetes Special Interest Group (SIG) Release.

The 1.23 release cycle started on August 23, 2021, and ran for 16 weeks. For 1.23, there were contributions from 1,084 contributors.

[![](https://media1-production-mightynetworks.imgix.net/asset/32036991/kubernetes-1.23-the-next-frontier.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)](https://media1-production-mightynetworks.imgix.net/asset/32036991/kubernetes-1.23-the-next-frontier.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format)

Since Kubernetes 1.10, each release has a theme and logo.

"The Next Frontier" theme represents the new and graduated enhancements in 1.23, Kubernetes' history of Star Trek references, and the growth of community members in the release team.

Kubernetes has a history of Star Trek references. The original code name for Kubernetes within Google is Project 7, a reference to Seven of Nine initially from Star Trek Voyager and the seven spokes in the Kubernetes logo. And, of course, Borg, the predecessor to Kubernetes. "The Next Frontier" is a fusion of two Star Trek titles, Star Trek V: The Final Frontier and Star Trek: The Next Generation. Many new Kubernetes contributors apprentice in a release team and have shadow roles. This is their first contribution to their respective open source frontier for many.

## What's New in Kubernetes 1.23?

The 1.23 release consists of 47 enhancements, with 11 enhancements graduating to stable, 17 enhancements moving to beta, 19 enhancements entered as alpha, and one deprecated feature.

Here are some of my favorites:

**Dual-stack IPv4/IPv6 Networking Graduates to Stable**Dual-stack was introduced as alpha in 1.15 and refactored in 1.20. Before 1.20, you had to have a service for each IP family model to implement dual-stack. In 1.20, the Service API supports dual-stack. In 1.21, clusters enabled dual-stack by default. In 1.23 the final move to graduate to stable is removing the *IPv6DualStack* feature flag.

**PodSecurity Admission Graduates to Beta**

If you haven't heard, PodSecurityPolicy (PSP) is deprecated as of 1.21, and the plan is to remove PSP in 1.25. PodSecurity Admission replaces PSP. PodSecurity is an admission controller that evaluates Pods against a predefined set of [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) to either *admit* or *deny* the Pod from running. Pod Security Standards (PSS) define privilege, baseline, and restricted policies. There are three policy modes that PodSecurity can be set to: *enforce*, *audit*, and *warn*.

**Supply-chain Levels for Software Artifacts (SLSA) Level 1 Compliance**

[SLSA](https://slsa.dev/) is an end-to-end framework to ensure the integrity of the software artifacts. Kubernetes 1.23 meets SLSA Level 1 compliance meaning that the build is scripted and the release provides provenance attestation files that describe the staging and release phases of the release process. The artifacts are verified as they are handed over from one phase to the next.

**Defend Against Logging Secrets via Static Analysis Graduates to Stable**

The 2019 third-party security audit for Kubernetes (I am currently the lead of the third-party audit subproject for Kubernetes) revealed that secrets were exposed to logs or execution environments. The Kubernetes project uses the [*go-flow-levee*](https://github.com/google/go-flow-levee) taint propagation analysis tool for Go to fix this. Taint propagation analysis inspects how data is spread and consumed in a program, which is used to harden boundaries for the data. This enhancement graduating to stable means that the analysis runs as a blocking pre-submit test. When this enhancement was in beta, the analysis was validated to run at scale with no false positives, test failures, or other issues.

**HorizontalPodAutoscaler (HPA) v2 API Graduates to Stable**

The HorizontalPodAutoscaler *autoscaling/v2* stable API is GA, which supports multiple and custom metrics used by HPA. This means that the *autoscaling/v2beta2* API is deprecated. There are no plans to deprecate the *autoscaling/v1* API. There is no current plan to remove the *autoscaling/v2beta1* and *autoscaling/v2beta2* API, but the earliest they can be removed is in 1.24 and 1.27, respectively.

**TTL "After Finished" Controller Graduates to Stable**

There's a new stable controller: the TTL Controller cleans up Jobs and Pods after they finish. If a Job or Pod isn't controlled by a higher-level resource e.g. CronJob for Jobs or Jobs for Pods, it can be hard for users to clean up over time. Finished Jobs and Pods can accumulate and fill up resource quotas. To use this feature, set a Job's *.spec.ttlSecondsAfterFinished* field to the number of seconds to clean up after. The TTL Controller watches all Jobs. If the Job is finished, the TTL Controller checks if the Job's *.spec.ttlSecondsAfterFinished* is set; if it's not set then the TTL Controller doesn't do anything else. If *.spec.ttlSecondsAfterFinished* is set then the TTL Controller compares the *.spec.ttlSecondsAfterFinished* with the Job's finished time (*.status.conditions.lastTransistionTime*). The Job is deleted if it's later than the current time.

**Kubelet CRI API Moves to Beta**

This move is essential because Dockershim is targeted to be removed in 1.24. For Dockershim to be removed in 1.24, the Kubelet CRI API needs to be in beta in 1.23, so it can graduate to stable in 1.24 when Dockershim is removed. So a CRI-compliant container runtime (e.g. containerd, cri-o, Docker with cri-dockerd ) is required for 1.24. Users that use RKE, RKE2, and K3s are not affected. RKE2 and K3s use containerd, while RKE uses Docker with cri-dockerd, not Dockershim.

**Ephemeral Containers Graduates to Beta**

With the *kubectl debug* command, an ephemeral container is launched in a running Pod to troubleshoot or observe the containers of the Pod.

**Topology Aware Hints Graduates to Beta**

The EndpointSlice controller can help keep network traffic in the same zone for better performance and in some cases increase cost savings by reducing cross-zone networking costs. The EndpointSlice controller reads the *topology.kubernetes.io/zone* label on Nodes to determine which zone a Pod is running on. A *service.kubernetes.io/topology-aware-routing: Auto* annotation on a Service is required to enable Topology Aware Routing. The EndpointSlice controller provides zone hints for each endpoint.

**Auto Remove PersistentVolumeClaims (PVCs) from StatefuleSets is Introduced as Alpha**

PVCs from StatefulSets can be auto-deleted if the StatefulSet is deleted or scaled down. There are new fields in the StatefulSet spec:

- *.spec.PersistentVolumeClaimPolicy.OnSetDeletion* specifies if the PVC is deleted when the StatefulSet is deleted with the value *Delete*, the other option is *Retain*

- *.spec.PersistentVolumeClaimPolicy.OnSCaleDown* specifies if the PVC is deleted when the StatefulSet is scaled down with the value *Delete,* the other option is *Retain*

**The *kubectl events* Command is Introduced as Alpha**

*Kubectl events* have limits like sorting and the --watch option, which can enhance the event's functionality. The output is sorted by default. Events can be sorted with other criteria and can be listed in a timeline of the last *n* minutes. The *--watch* option is also sorted.

**OpenAPI v3 is Introduced as Alpha**

There’s a new endpoint to publish OpenAPI v3.0 spec for all Kubernetes types. OpenAPIv2 strips several fields while OpenAPI v3 is more transparent. A separate spec is published per Kubernetes group version at the *$cluster/openapi/v3/apis/<group>/<version>* endpoint for improved performance and discovery, all group versions can be found at *$cluster/openapi/v3*. OpenAPI v3 is more expressive than v2.
