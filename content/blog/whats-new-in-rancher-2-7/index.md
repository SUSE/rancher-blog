---
title: "What's New in Rancher 2.7"
date: 2022-11-24T08:03:07
slug: "whats-new-in-rancher-2-7"
authors: ["Wendie Cheung"]
products: ["Rancher Manager"]
tags: ["upgrades"]
content_type: "release"
draft: false
migration:
  wp_id: 97630
  original_url: "https://www.suse.com/c/rancher_blog/whats-new-in-rancher-2-7/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.7 release announcement"
  redirect_target: ""
---

The Rancher Team is excited to announce the general availability of Rancher v2.7.  Rancher v2.7 is a monumental milestone in the lifecycle of Rancher and introduces the ability to be a truly interoperable, extensible platform through the concept of extensions. The extensions now allow users to build extensions on top of Rancher with complete autonomy. By using the extensions catalog, administrators can now view the list of installed extensions, update or roll back existing extensions, and install new extensions as desired. For more information on how to use Rancher extensions, please see the [documentation here.](https://docs.ranchermanager.rancher.io/integrations-in-rancher/rancher-extensions)

Another big call out is the general availability of K3s provisioning on x86 architectures from within Rancher, this will greatly aid Rancher deployments running on edge workloads. Rancher also now supports Kubernetes v1.24.6 by default and Kubernetes v1.23.12 in this major version. However, support for v1.20, v1.21 & v1.22 is no longer supported.

### **Some other major items in this release include:**

> The ‘Manage Cluster Members’ and ‘Manage Project Members’ roles have been updated to align ber with common expectations regarding privilege escalation. Users in this role must now have any privilege they wish to assign to others.  
> The ‘Diagnostics’ page now shows more detailed information for troubleshooting performance issues.  
> Authentication for OCI-based registries is now supported. Please note that the structure of the fleet.yaml is the same, and the credentials are provided as a Kubernetes secret which is described in the Private Helm Repo box in the Repo Structure docs.

### **In this release, Rancher v2.7 continues to fix underlying product bugs, most notably :**

> When deploying an RKE2/K3s custom cluster that uses a proxy, the registration now completes as expected.  
> When navigating to the ‘Continuous Delivery’ page from the ‘Cluster Management’ page or home page, the clusters now show up per the selected namespace as expected.  
> Kubernetes versions 1.24.x are no longer appearing as “experimental” when provisioning AKS clusters, as 1.24.x versions are fully supported for AKS cluster  
> RKE v1.3.10-v1.3.13 in Rancher v2.6.7-v2.6.8 no longer removes user add-ons during an upgrade before redeploying them. Previously this would cause issues with RKE1 cluster upgrades if the user add-ons template has cattle-\* or other system namespaces.  
> Fixed an issue where user-defined EKS security groups were configured as the only node group security groups rather than being appended to the cluster default security group.  
> Fixed the issue which saw OPA Gatekeeper become stuck when uninstalled.  
> Web socket disconnections no longer result in multiple notifications.  
> CPU and memory usage are now displayed properly for EKS nodes.

Learn more about this latest release and keep up to date via our [GitHub](https://github.com/rancher/rancher/releases/tag/v2.7.0) or community [Slack](https://slack.rancher.io/).
