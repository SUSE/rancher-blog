---
title: "Windows Containers and Rancher 2.3"
date: 2019-10-08T09:43:00
slug: "windows-containers-and-rancher-2-3"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_storage.svg"
products: ["Rancher Manager"]
tags: ["windows"]
content_type: "release"
draft: false
migration:
  wp_id: 85928
  original_url: "https://www.suse.com/c/rancher_blog/windows-containers-and-rancher-2-3/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.3 Windows announcement"
  redirect_target: ""
---

Container technology is transforming the face of business and application development. 70% of on-premises workloads today are running on the Windows Server operating system and enterprise customers are looking to modernize these workloads and make use of containers.

We have introduced support for Windows Containers in Windows Server 2016 and graduated support for Windows Server worker nodes in Kubernetes 1.14 clusters. With Windows Server 2019 we have expanded support in Kubernetes 1.16.

For our customers one of the preferred ways to increase the adoption of containers and Kubernetes is to work to make it easier for operators to deploy it and for developers to use it.

Towards that end Microsoft has invested in AKS and Windows Container support with this goal in mind while working with partners such as Rancher Labs who has built their organization on the principle of “Run Kubernetes Everywhere”.

With the release of Rancher 2.3, Rancher is the first to have graduated Windows support to GA and can now deploy Kubernetes clusters with Windows support from within the user experience.

Using Rancher 2.3 users can deploy Windows Kubernetes clusters in AKS, Azure Cloud, any other cloud computing provider or on-premises using the supported and proven network components in Windows Server as well as Kubernetes.

Rancher 2.3 will support Flannel as the CNI plugin and Overlay Networking with VxLAN to enable communication between Windows and Linux containers, services, and applications.

[Learn more about Rancher 2.3 and its functionality](http://rancher.com/products/rancher/2.3/).
