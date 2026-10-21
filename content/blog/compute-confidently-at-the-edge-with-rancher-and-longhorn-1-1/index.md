---
title: "Compute Confidently at the Edge with Rancher and Longhorn 1.1"
date: 2021-01-26T10:13:00
slug: "compute-confidently-at-the-edge-with-rancher-and-longhorn-1-1"
authors: ["Wendie Cheung"]
image: "images/rancher_blog_longhorn-1-1-featured.png"
products: ["Longhorn"]
tags: ["storage", "edge"]
content_type: "release"
draft: false
migration:
  wp_id: 86483
  original_url: "https://www.suse.com/c/rancher_blog/compute-confidently-at-the-edge-with-rancher-and-longhorn-1-1/"
  disposition: migrate
  commercial: false
  outdated_reason: "Longhorn 1.1 release announcement"
  redirect_target: ""
---

Today’s announcement of [Longhorn 1.1](https://longhorn.io/), a Cloud Native Computing Foundation (CNCF) Sandbox project, is exciting news for users of [Rancher](https://rancher.com/products/rancher), SUSE’s Kubernetes management platform, and the Kubernetes community. Longhorn is an enterprise-grade, cloud native container storage solution that went GA in June 2020. Since then, adoption has increased by 235 percent. Now Longhorn is the first cloud native storage solution designed and built for the edge, with ARM64 support, new self-healing capabilities and increased performance visibility.

The ability for our users to “Compute Everywhere” has always been a key differentiator between Rancher and other solutions on the market. This strategy cemented the foundations for successful projects like K3s and Longhorn, which were originally built by Rancher product teams to address the infrastructure needs of multinational organizations with globally distributed and often resource-constrained environments. The success of these projects eventually led to their donation to the open source community through the CNCF.

The latest Longhorn release supports this “Compute Everywhere” legacy and offers the following new features and improvements to Rancher users and the Kubernetes community at large. These include:

## Robust Kubernetes-Native Storage at the Edge

The latest Longhorn release gives Rancher access to the first Kubernetes-native edge storage solution. With ARM64 support, Longhorn was designed to help teams store data reliably within even the most hostile and resource-constrained environments. Together, Longhorn and Rancher provide users with a powerful Kubernetes-native management and storage solution designed for the edge.

## Driving Efficient Container Performance

Longhorn has significantly improved its performance with **ReadWriteMany** support, which was a highly requested feature from the community. This feature gives developers an efficient persistent storage solution that enables volumes to be read and written across multiple containers at any time. It also lets teams share volume storage between different paths on different nodes. ReadWriteMany support adds to Longhorn’s enterprise-grade benefits so you can use Longhorn in production with confidence.

## Enhanced Visibility, Operations Support and Maintenance Functionality

Longhorn 1.1 brings better insights and functionality to an organization’s storage infrastructure without compromising on its user-friendly simplicity and reliability. This is through:

- New integrated support for Prometheus monitoring
- New support for CSI Snapshotter, which enables users to easily create and restore backups via kubectl
- Enhanced node maintenance capabilities with support for Kubernetes drain operations

These improvements give Rancher users complete access to real-time metrics of their storage health and let them maintain their storage volumes alongside managing their Kubernetes clusters. This can all be operated within the Longhorn console, which is easily accessible via the Rancher platform.

![Image 02](images/rancher_blog_image-01.jpg)
Longhorn’s comprehensive real-time view of performance metrics

## Increased Resilience

Longhorn 1.1 also builds resilience into resource-constrained Kubernetes environments like the edge with its new Data Locality feature. Rancher users can have confidence about storage and performance at the edge, as this new Longhorn feature keeps a storage replica local to the workload - ensuring storage will not be lost even if connectivity is lost.

## Rancher and Longhorn Together

Together with the Rancher Kubernetes management platform, Longhorn makes the deployment of highly available enterprise-grade persistent storage easy, fast and reliable. As the first cloud native storage built for the edge, Longhorn empowers users to do more with their Kubernetes environments.

Existing Rancher users can download and install Longhorn directly from Rancher’s app catalog. Longhorn remains an open source CNCF project and is free to download and use. Rancher customers can now purchase premium support through [SUSE Support Services](https://www.suse.com/support/). There are no licensing fees, and node-based subscription pricing keeps costs to a minimum.

[Join the next community meetup](https://more.suse.com/fy21-global-event-rancher-online-meetup-february2021) where we will explore how Rancher users can leverage the new Longhorn features across their edge environments.
