---
title: "Introducing k3s: The Lightweight Kubernetes Distribution Built for the Edge"
date: 2019-02-26T09:04:00
slug: "introducing-k3s-the-lightweight-kubernetes-distribution-built-for-the-edge"
author: "Rancher Admin"
image: "images/rancher_blog_k3s-feature.svg"
products: ["K3s"]
tags: ["edge"]
content_type: "release"
draft: false
migration:
  wp_id: 85841
  original_url: "https://www.suse.com/c/rancher_blog/introducing-k3s-the-lightweight-kubernetes-distribution-built-for-the-edge/"
  disposition: migrate
  commercial: false
  outdated_reason: "K3s launch announcement, history"
  redirect_target: ""
---

k3s Demo and MeetupJWatch the meetup introducing k3s, a live demo of its features, and devoted Q&A time..[View Recording](https://more.suse.com/fy21-global-event-rancher-meetup-k3s-lightweight-kubernetes)

Today Rancher Labs is announcing a new open source project, k3s, which is a lightweight, easy to install Kubernetes distribution geared towards resource-constrained environments and low touch operations. Some use cases in which k3s really shines are edge, ARM, IoT, and CI. The work for k3s started as a component of Rio, an experimental project we started last year. We started seeing real demand for Kubernetes on the edge and a growing interest in k3s itself, so we decided to pull it out of Rio and make it a first-class open source project.

k3s is packaged as a single binary which is about 40 megabytes in size. Bundled in that single binary is everything needed to run Kubernetes, including the container runtime and any important host utilities like iptables, socat, and du. The only OS dependencies are the Linux kernel itself and a proper dev, proc, and sysfs mounts (this is done automatically on all modern distros).

k3s bundles the Kubernetes components (kube-apiserver, kube-controller-manager, kube-scheduler, kubelet, kube-proxy) into combined processes that are presented as a simple server and agent model. Running `k3s server` will start the Kubernetes server and automatically register the local host as an agent. This will create a one node Kubernetes cluster. To add more nodes to the cluster just run `k3s agent --server ${URL} --token ${TOKEN}` on another host and it will join the cluster. It’s really that simple to set up a Kubernetes cluster with k3s.

Besides the core Kubernetes components, we also run containerd, Flannel, CoreDNS, Traefik ingress controller, and a simple host port based service load balancer. All of these components are optional and can be swapped out for your implementation of choice. With these included components you get a fully functional and CNCF conformant cluster so you can start running apps right away.

k3s started as an embedded component of Rio. Rio is an experimental project that focuses on applications, serverless, and service mesh. Rio runs on top of Kubernetes and we wanted the simplest way possible to get Rio running so we embedded a full Kubernetes cluster inside of Rio. We weren’t happy with the memory footprint of Rio so we started looking at what components of Kubernetes we could remove to make it smaller. We started by removing all the features we didn’t need. During this effort, we noticed three things. First, running Rio ended up being the simplest way we knew to run a Kubernetes cluster, even if you didn’t want any features of Rio. Second, we started getting more and more requests from customers to run Kubernetes on the edge. Examples of this are companies that run a lot of retail stores. Companies want to offer more services in stores and running cloud-based software is often infeasible. It makes more sense to run a Kubernetes cluster locally in the store. Third, since we developed this in the open, people stumbled upon this component of Rio and were really interested in a lighter weight Kubernetes, and especially something that would run easily on ARM.

Based on these observations we realized that k3s should be a top-level Rancher open source project. Initially, we focused on just the features that Rio needed but we wanted to increase the scope to be a fully compliant Kubernetes cluster. As we looked at what we had done to decrease the size of Kubernetes we found out that the biggest impact was removing the legacy and alpha functionality. In the end, we now have k3s which is a fully certified Kubernetes distribution that runs in about one fourth the memory of vanilla Kubernetes. A single node v1.13.3 Kubernetes cluster with Docker uses a little over 1GiB of memory whereas the equivalent k3s setup takes a little over 260MiB of memory and that includes an ingress controller and service load balancer not present in the upstream cluster.

We are excited to release k3s today to the world. We are really just beginning to find all the various use cases for k3s and are excited to see what users will do with it. k3s is available for x86\_64, ARMv7 and ARM64 at <https://k3s.io> today. Also, look out for Rio which will have some exciting new updates in the coming months. k3s is the simplest Kubernetes cluster out there and Rio will be the simplest way to run any application on Kubernetes. Stay tuned.

k3s Demo and MeetupJWatch the meetup introducing k3s, a live demo of its features, and devoted Q&A time..[View Recording](https://more.suse.com/fy21-global-event-rancher-meetup-k3s-lightweight-kubernetes)
