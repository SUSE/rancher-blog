---
title: "Upstream Momentum: A Technical Spotlight on K3s, Kubewarden, and Longhorn"
date: 2026-11-24T12:00:00
slug: "upstream-momentum-technical-spotlight"
authors: ["Davide Iori", "François-Xavier Houard", "Matthew Denham"]
products: ["Kubewarden", "K3s", "Longhorn"]
tags: ["open source"]
description: "An overview of the recent technical achievements and upstream momentum of CNCF cornerstone projects K3s, Kubewarden, and Longhorn."
draft: false
---

The cloud native landscape thrives on open source velocity, architectural standards, and strong community stewardship. Today, we are shining a technical spotlight on our three cornerstone projects within the CNCF - K3s, Kubewarden, and Longhorn - and examining their recent technical achievements.

## K3s: Lightweight Kubernetes at Scale

As the world’s most widely deployed lightweight Kubernetes distribution, K3s continues to expand its footprint from edge locations and IoT environments to core enterprise workloads. As of today, K3s boasts:


- 10 Million+ Monthly Downloads: K3s has experienced massive community adoption and operational reliance across diverse computing environments.
- 0 Critical CVEs: K3s is engineered with strict vulnerability management, maintaining zero critical CVEs across core release air-gap tarballs.

Recent architectural enhancements to K3s focus heavily on performance and flexibility. By integrating Spegel, an embedded distributed registry, K3s enables peer-to-peer image distribution across nodes, significantly cutting external registry bandwidth and accelerating pod start times. Simultaneously, expanded native NVIDIA GPU support powers demanding AI/ML workloads at the edge, and across the wider K3s ecosystem, k3k runs virtual K3s clusters on existing infrastructure for isolated development and multi-tenant environments.

The latest releases build on that foundation. Starting with v1.37, K3s bundles the Kubernetes Gateway API CRDs as their own system chart, so teams can define routes with either the Ingress API or Gateway API without installing CRDs by hand. Since v1.36.3, --tls-san accepts wildcard domains such as *.example.com, so adding a hostname under that domain no longer means reissuing the API server certificate. K3s releases are also now published as immutable GitHub releases, so assets can’t be swapped out after publication.


## Kubewarden: Cloud Native Security from Admission to Runtime

Kubewarden, a CNCF sandbox project originally built around policies compiled to WebAssembly (Wasm), has evolved from pre-deployment admission control into an end-to-end security platform protecting Kubernetes workloads across their entire lifecycle. Its components allow operators to enforce security policies before deployment, monitor running workloads and restrict unexpected behavior.

- Runtime and Network Security: The new Runtime Enforcer uses eBPF to monitor and restrict process execution within containers, while the experimental Network Enforcer generates network security policies based on observed workload traffic.
- Software Supply Chain Security: SBOM Scanner, added in 2025, identifies vulnerabilities in container images and Kubernetes workloads, providing security insights that admission policies can use to enforce before deployment.

Kubewarden's Admission Controller remains at the core of the project, supporting policies written in Rust, Go, Rego and CEL, compiled to WebAssembly and distributed as OCI artifacts. SBOM Scanner complements the Admission controller by scanning container images and workloads pre-deployment. The newly added Runtime Enforcer and Network Enforcer introduce a three-phase Learn–Monitor–Protect workflow, allowing operators to first establish expected application behavior, then detect violations and finally block unauthorized executables or network traffic.

Runtime Enforcer leverages eBPF for monitoring and blocking of executables whereas Network Enforcer interacts directly with the Kubernetes networking stack including Calico (via Goldmane), Cilium (Hubble Relay), and Istio Ambient (ztunnel). Both Enforcers support exporting policy violations as OpenTelemetry events, integrating with Kubewarden’s pre-deployment SBOM Scanner, v1 CRDs, and modular PolicyGroups to provide full defense-in-depth. We’re committed to developing the future of cloud native security in the open with our donation of the Runtime & Network Enforcer subproject to the Cloud Native Computing Foundation. Read more about it [here](https://www.suse.com/blog/kubecon-na-2026-community-kubewarden/).


## Longhorn: High-Performance Distributed Cloud Native Storage

Longhorn continues to set the benchmark for open source, cloud native block storage, providing resilient persistent storage for Kubernetes clusters everywhere.

- 276,000+ Nodes: Powering mission-critical storage workloads globally across thousands of production clusters.
- 21,000+ Active Nodes on v1.13.0: Rapid production adoption of the v1.13.0 release with proven performance and stability.

Longhorn's recent technical updates emphasize speed, resilience, and operational efficiency. The general availability of the V2 Data Engine leverages the Storage Performance Development Kit (SPDK) to lower I/O latency and boost overall throughput. From version 1.12.2 to v1.13.1+, users can smoothly transition thanks to live upgrades between engine versions, default CPU isolation, and an event-driven interrupt mode that optimizes CPU consumption. On the management side, volume group snapshot CRDs, coming in v1.14.0, enable consistent multi-volume backups with automated retention policies, complemented by custom Scheduler Extenders for intelligent replica placement. Reaffirming the project's commitment to vendor neutrality and community governance, Longhorn also welcomes new maintainer Jinhong Kim from NAVER.

Across Kubernetes orchestration, policy enforcement, and distributed storage, K3s, Kubewarden, and Longhorn demonstrate remarkable upstream momentum. Through rigorous security benchmarks, WebAssembly innovation, and high-performance data engines, these projects offer a resilient, production-ready foundation for the open source community.

Ready to dive deeper or contribute? Explore the upstream repositories, join the community discussions, and start building with K3s, Kubewarden, and Longhorn today:

- K3s: Visit the [K3s website](https://k3s.io) or check out the repository on [GitHub](https://github.com/k3s-io/k3s).
- Kubewarden: Explore policy templates and docs at [kubewarden.io](http://kubewarden.io) or join the project on [GitHub](https://github.com/kubewarden).
- Longhorn: Get started with cloud native storage at [longhorn.io](https://longhorn.io) and connect with maintainers on [GitHub](https://github.com/longhorn/longhorn).
