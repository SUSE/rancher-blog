---
title: "Announcing Submariner, Kubernetes Multi-Cluster Network Connectivity"
date: 2019-03-12T09:05:00
slug: "announcing-submariner-kubernetes-multi-cluster-network-connectivity"
author: "Rancher Admin"
image: "images/rancher_blog_submariner-featured.svg"
products: ["Other"]
tags: ["networking", "multi-cluster"]
content_type: "release"
draft: true
migration:
  wp_id: 85851
  original_url: "https://www.suse.com/c/rancher_blog/announcing-submariner-kubernetes-multi-cluster-network-connectivity/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Submariner-era project"
  redirect_target: "rancher.com/blog (hub)"
---

Today we are proud to announce [Submariner](https://submariner.io), a new open-source project enabling network connectivity between Kubernetes clusters. We launched the project to provide network connectivity for microservices deployed in multiple Kubernetes clusters that need to communicate with each other. This new solution overcomes barriers to connectivity between Kubernetes clusters and allows for a host of new multi-cluster implementations, such as database replication within Kubernetes across geographic regions and deploying service mesh across clusters.

Organizations are looking for Kubernetes as the standard computing platform across all public and private cloud infrastructure. Submariner allows these organizations to seamlessly connect, scale, and migrate workloads across Kubernetes clusters deployed on any cloud.

## Network Connectivity Across Clusters with Submariner

Historically, Kubernetes deployments implement network virtualization, enabling containers to run on multiple nodes within the same cluster to communicate with each other. However, containers running in different Kubernetes clusters must communicate with each other through ingress controllers or node ports. Submariner now creates the necessary tunnels and routes needed to enable containers in different Kubernetes clusters to connect directly. Key features of Submariner include:

- **Compatibility and connectivity with existing clusters:** Users can deploy Submariner into existing Kubernetes clusters, with the addition of Layer-3 network connectivity between pods in different clusters.
- **Secure paths:** Encrypted network connectivity is implemented using IPSec tunnels.
- **Various connectivity mechanisms:** While IPsec is the default connectivity mechanism out of the box, Rancher will enable different interconnectivity plugins in the near future.
- **Centralized broker** : Users can register and maintain a set of healthy gateway nodes.
- **Flexible service discovery:** Submariner provides service discovery across multiple Kubernetes clusters.
- **CNI compatibility:** Works with popular CNI drivers such as Flannel and Calico.

Developers who are interested in downloading, installing and playing with this new networking solution should visit <https://submariner.io> or follow the project on <https://github.com/rancher/submariner>. Enterprises who need assistance in deploying and managing Submariner can contact info@rancher.com.

## Watch the Submariner Online Meetup and Demo

To learn more about Submariner and its roadmap, join Submariner lead engineer Chris Kim as they present Submariner in our online meetup. In this meetup, they discuss and demo:

- Example uses cases for Submariner.
- What you need to run Submariner across clusters.
- How to develop an architectural design for clusters connected using Submariner
- How to setup and manage high availability microservices connected through Submariner.

[Get the recorded meetup and slides.](https://info.rancher.com/meetup-introducing-submariner-multicluster-networking)
