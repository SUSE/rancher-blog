---
title: "Enterprise and Edge Scale Security with NeuVector Container Security 5.1"
date: 2022-12-19T15:10:36
slug: "enterprise-and-edge-scale-security-with-neuvector-container-security-5-1"
authors: ["Glen Kosaka"]
image: "images/Screen-Shot-2022-05-12-at-9.48.24-AM-1.png"
products: ["NeuVector"]
tags: ["security", "multi-cluster"]
content_type: "release"
draft: true
migration:
  wp_id: 97791
  original_url: "https://www.suse.com/c/rancher_blog/enterprise-and-edge-scale-security-with-neuvector-container-security-5-1/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "NeuVector 5.1 release"
  redirect_target: "suse.com (new URL pending)"
---

I’m excited to announce the general availability of the SUSE NeuVector container security platform version 5.1. With the 5.1 release, customers will benefit from more efficient and powerful vulnerability scanning and admission controls across multiple clusters through centralized enterprise scanning, auto-scaling scanners and support for the new Kubernetes (1.25+) pod security admission (PSA) standard. The release also supports the Cilium network plug-in. This will provide Cilium users with advanced security capabilities, including zero trust security automation and full layer 7 firewall protection with WAF (Web Application Firewall), DLP (Data Leakage Prevention), DPI (Deep Packet Inspection), among others. This will enable security controls to scale across clusters and clouds which may have different or multiple types of CNI plugins. In addition, the release of open source build tools for NeuVector is now available for community users to create and build their own versions. 

## **Enterprise-scale vulnerability scanning**

As container clusters explode across an enterprise, the need to efficiently secure and manage these clusters from a central point becomes critical. NeuVector 5.1 delivers innovative centralized multi-cluster vulnerability scanning, where a Federation leader can scan image repositories once. The scan results (CVEs, CIS benchmarks) can then be shared among multiple downstream clusters. This capability is critical to efficiently manage an enterprise-wide vulnerability management architecture that combines performance optimizations with cluster-level admission controls. Performance is optimized by scanning an image only once, with results available enterprise-wide. This can reduce network bandwidth, local cluster CPU/memory usage, and requests to the image registry. In addition, NeuVector now supports auto-scaling scanner pods to increase scanner bandwidth when needed for scanning or re-scanning huge image repositories. 

## **Edge security enhancements**

Containers and Kubernetes are being increasingly deployed in edge environments, where network, compute and memory resources can be constrained. Still, security requirements are as important to address as in a data center. With NeuVector 5.1, edge deployments can be supported with performance tuning to match the security requirements at the edge with the most critical security features required. Security automation is also critical for edge management, where hundreds of remote clusters can deploy, configure and update security protections. NeuVector leads the market with security automation capabilities through its Helm charts, configMaps, rest API and custom resource definitions (CRDs). 

## **Stronger admission controls**

This release enhances the flexibility of admission controls, which are the key gatekeepers securely deploying workloads to a cluster. This supports defining admission control rules based on flexible criteria and resource objects found in typical deployment yaml files. In addition, to support the new Pod Security Admission (PSA) standards in Kubernetes 1.25, NeuVector 5.1 also evaluates pod deployments by service accounts with high-risk RBAC roles.  

SUSE NeuVector 5.1 allows users to address major security use cases across the entire application lifecycle, as [container security](https://www.suse.com/c/what-is-container-security/) continues to be a critical need for organizations building and running Kubernetes applications. This includes deep network visibility and protection, vulnerability management, configuration auditing, compliance and supply chain security. To learn more, visit the SUSE [NeuVector](https://www.suse.com/products/neuvector/) site or review the [documentation.](https://open-docs.neuvector.com/)
