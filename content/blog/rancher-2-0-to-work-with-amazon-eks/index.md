---
title: "Rancher 2.0 to Work with Amazon EKS"
date: 2017-11-29T11:14:00
slug: "rancher-2-0-to-work-with-amazon-eks"
author: "Rancher Admin"
products: ["Rancher Manager"]
tags: ["aws", "cloud"]
content_type: "company-news"
draft: true
migration:
  wp_id: 86888
  original_url: "https://www.suse.com/c/rancher_blog/rancher-2-0-to-work-with-amazon-eks/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2017 EKS announcement reaction"
  redirect_target: "rancher.com/blog (hub)"
---

Today, Amazon

[announced](https://aws.amazon.com/blogs/aws/amazon-elastic-container-service-for-kubernetes/)

a managed Kubernetes service called Elastic Container Service for

Kubernetes (EKS). This means that all three major cloud

providers—AWS, Azure, and GCP—now offer managed Kubernetes services.

This is great news for Kubernetes users. Even though users always have

the option to stand up their own Kubernetes clusters, and new tools like

[Rancher Kubernetes Engine](https://rancher.com/announcing-rke-lightweight-kubernetes-installer/)

(RKE) make that process even easier, cloud-managed Kubernetes

installations should be the best choice for the majority of Kubernetes

users. At Rancher, we have been working towards a future where

Kubernetes becomes the standard infrastructure available from all

providers. With EKS, this vision is now a reality. We are excited about

the prospect of Rancher 2.0 managing Kubernetes clusters of any kind,

from any cloud provider. Rancher 2.0, currently under development and in

technical preview, consists of the following three major components:

1. **RKE.** Rancher’s own lightweight Kubernetes installer and distro

   installs Kubernetes on vSphere and bare-metal servers as well as on

   clouds that do not yet offer a managed Kubernetes service.
2. **Kubernetes cluster management.** With Rancher 2.0, users can now

   provision Kubernetes clusters created by RKE, EKS, Google Container

   Engine (GKE), Azure Container Service (AKS), or any other Kubernetes

   cluster. IT administrators can set up centralized user

   authentication integrated with their AD/LDAP. Rancher additionally

   provides centralized role-based access control (RBAC), cluster

   capacity management, and cost management.
3. **Application management**. Rancher offers an easy-to-use user

   interface on top of Kubernetes, and integrates cloud-native

   ecosystem technologies such as CI/CD, centralized monitoring, and

   logging.

All these capabilities are available in the [Rancher 2.0 tech preview 1.0](https://rancher.com/rancher2-0/) and

[RKE](https://rancher.com/announcing-rke-lightweight-kubernetes-installer/).

Please join our online meetup tomorrow to learn more about the latest

Rancher 2.0 enhancements, including RKE and our support for EKS. You

can register for the meetup

[here](https://info.rancher.com/november-2017-meetup).
