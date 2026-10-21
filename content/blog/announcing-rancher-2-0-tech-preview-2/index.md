---
title: "Announcing Rancher 2.0 Tech Preview 2"
date: 2018-01-24T09:00:00
slug: "announcing-rancher-2-0-tech-preview-2"
author: "Rancher Admin"
products: ["Rancher Manager"]
tags: []
content_type: "release"
draft: false
migration:
  wp_id: 85798
  original_url: "https://www.suse.com/c/rancher_blog/announcing-rancher-2-0-tech-preview-2/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.0 tech preview 2 announcement"
  redirect_target: ""
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)

Today we released the second tech preview of Rancher 2.0, our next major Rancher product release. We’ve been hard at work since the last tech preview release in September 2017, driven by the overwhelmingly positive response to our Rancher 2.0 vision and a great deal of feedback we have received.

The Tech Preview 2 release contains many significant changes and enhancements:

1. Rancher server is now 100% written in Go and no longer requires a MySQL database.
2. You can deploy Rancher server on any Docker host as before, or you can deploy Rancher server on an existing Kubernetes cluster.
3. You can create new Kubernetes clusters using Rancher Kubernetes Engine (RKE) or cloud-managed Kubernetes services such as GKE. Rancher automates both RKE and GKE cluster provisioning. Support for additional cloud-managed Kubernetes services such as EKS and AKS will be added in the future.
4. You can manage all your Kubernetes clusters from a unified cluster management interface. Rancher implements centralized authentication and authorization across all Kubernetes clusters, regardless where these Kubernetes clusters are hosted.
5. Rancher provides a simple workload management interface across all your Kubernetes clusters. This is still a work in progress. We continue to offer an intuitive Rancher 1.0-style container-centric interface. We are working on adding many advanced workload management features such as the app catalog, CI/CD and monitoring integration, sophisticated stats, and centralized logging.

If you are interested in more technical details, take a look at the [updated Rancher 2.0 Architecture Document](https://cdn2.hubspot.net/hubfs/468859/Whitepapers/Rancher-2.0-Architecture-v0.6-jan-2018.pdf), [The Quick Start Guide](https://rancher.com/docs/rancher/v2.0/en/quick-start-guide/), and the [Technical Release 2 page](https://github.com/rancher/rancher/releases) on Github.

Also, enjoy the [recording](https://www.youtube.com/watch?v=ld7ctOg3waM&t=5753s) of the online meetup where we gave a live demo.

Again, Rancher 2.0 is a work-in-progress. We’ll be rolling out new features in the coming days and weeks as we get ready for our Beta release next month. You can [register here](https://info.rancher.com/rancher2-beta-user-community-registration) to be part of the Beta User Community.

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)
