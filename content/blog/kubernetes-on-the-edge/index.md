---
title: "Kubernetes on the Edge"
date: 2018-12-11T09:03:00
slug: "kubernetes-on-the-edge"
authors: ["Sheng Liang"]
products: ["Rancher Manager"]
tags: ["edge"]
content_type: "company-news"
draft: true
migration:
  wp_id: 85833
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-on-the-edge/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Arm partnership announcement, RKE1 and RancherOS"
  redirect_target: "rancher.com/blog (hub)"
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)

Today we announced a [partnership](https://rancher.com/press/2018-12-11-press-release-arm-partnership/) with Arm to create a Kubernetes-based platform for IoT, edge, and data center nodes, all powered by Arm servers. The platform includes a port of Rancher Kubernetes Engine (RKE) and RancherOS to Arm Neoverse-based servers. We have also enhanced Rancher 2.1 so that a single Rancher server can manage mixed x86 and Arm 64 nodes. Customers can therefore have x86 clusters running in the data center and Arm clusters running on the edge.

Rancher and Arm are working jointly on a Smart City project in China. In that project, Arm servers are installed in buildings across large organizations. These ARM servers are used to collect data from various sensors including human presence, ambient temperature, and air quality. Sensor data is then processed in centralized data centers which is then used to coordinate power distribution and HVAC controls. Each edge node runs a standalone Arm Kubernetes cluster. Standard x86 Kubernetes clusters running in central data centers are used to process and analyze a large amount of data collected from edge nodes. A single Rancher server is used to manage all x86 and Arm Kubernetes clusters.

We learned a lot in the process of planning and executing this project. In the beginning, I did not understand why this customer wanted to run an independent Kubernetes cluster on each edge node. It seemed to be quite wasteful to run a separate instance of etcd, Kubernetes master, and Kubelet on each edge node. Why couldn’t we manage all the edge nodes as one large Kubernetes cluster? It turned out edge nodes had spotty network connectivity and therefore were not able to form a resilient multi-node Kubernetes cluster. Then why did the customer want to setup a Kubernetes cluster on the edge in the first place? Why couldn’t they just run standard Linux nodes and deploy rpm packages to the edge nodes? It turned out the software stack they were trying to deploy was quite sophisticated. It involved multiple services and required service discovery. The components had to be updated from time to time. Kubernetes was a great platform to manage application deployment.

The main challenge this customer had was that they needed a platform that can manage multiple Kubernetes clusters. Rancher suited their needs very well. Even better, we enhanced Rancher 2.1 so that it can manage mixed x86 and Arm clusters. Today, we simply rebuild edge clusters when they fail. In Rancher 2.2, we will be able to backup and restore RKE clusters, so that users no longer need to worry about losing etcd databases on edge node failures.

Kubernetes was designed to be a scalable platform. Our experience shows that it also works well as a single-node edge computing platform. We do wish, however, that Kubernetes itself consumed less resources. The single-node Kubernetes platform worked well on nodes with more than 8GB of memory, but it struggled on 4GB nodes. We are exploring ways to create a special-purpose Kubernetes distro that consumes less resources. Darren Shepherd, our Chief Architect, has been working on a [minimal Kubernetes distro](https://github.com/ibuildthecloud/k3s). It is still a work in progress. I hope, when he’s done, we will be able to fit the entire Kubernetes platform (etcd, master, kubelet) in less than 1GB of memory, so that our edge-solution can work on 4GB nodes.

If you are interested in exploring Kubernetes on the edge or reduce the footprint of your Kubernetes distros, please reach out to us at info@rancher.com. We’d love to work with you. We are super excited about the potential for applying Kubernetes technology on the edge. Kubernetes holds the potential to be the common platform for the cloud and for the edge.

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)
