---
title: "Hyperconverged Infrastructure and Harvester"
date: 2021-08-02T20:40:42
slug: "hyperconverged-infrastructure-and-harvester"
author: "Matthew Casperson"
image: "images/Harvester-Symbol.png"
products: ["Harvester"]
tags: ["virtualization"]
content_type: "explainer"
draft: false
migration:
  wp_id: 87650
  original_url: "https://www.suse.com/c/rancher_blog/hyperconverged-infrastructure-and-harvester/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Virtual machines (VMs) have transformed infrastructure deployment and management. VMs are so ubiquitous that I can’t think of a single instance where I deployed production code to a bare metal server in my many years as a professional software engineer.

VMs provide secure, isolated environments hosting your choice of operating system while sharing the resources of the underlying server. This allows resources to be allocated more efficiently, reducing the cost of over-provisioned hardware.

Given the power and flexibility provided by VMs, it is common to find many VMs deployed across many servers. However, managing VMs at this scale introduces challenges.

## Managing VMs at Scale

Hypervisors provide comprehensive management of the VMs on a single server. The ability to create new VMs, start and stop them, clone them, and back them up are exposed through simple management consoles or command-line interfaces (CLIs).

But what happens when you need to manage two servers instead of one? Suddenly you find yourself having first to gain access to the appropriate server to interact with the hypervisor. You’ll also quickly find that you want to move VMs from one server to another, which means you’ll need to orchestrate a sequence of shutdown, backup, file copy, restore and boot operations.

Routine tasks performed on one server become just that little bit more difficult with two, and quickly become overwhelming with 10, 100 or 1,000 servers.

Clearly, administrators need a better way to manage VMs at scale.

## Hyperconverged Infrastructure

This is where Hyperconverged Infrastructure (HCI) comes in. HCI is a marketing term rather than a strict definition. Still, it is typically used to describe a software layer that abstracts the compute, storage and network resources of multiple (often commodity or whitebox) servers to present a unified view of the underlying infrastructure. By building on top of the virtualization functionality included in all major operating systems, HCI allows many systems to be managed as a single, shared resource.

With HCI, administrators no longer need to think in terms of VMs running on individual servers. New hardware can be added and removed as needed. VMs can be provisioned wherever there is appropriate capacity, and operations that span servers, such as moving VMs, are as routine with 2 servers as they are with 100.

## Harvester

Harvester, created by Rancher, is open source HCI software built using Kubernetes.

While Kubernetes has become the defacto standard for container orchestration, it may seem like an odd choice as the foundation for managing VMs. However, when you think of Kubernetes as an extensible orchestration platform, this choice makes sense.

Kubernetes provides authentication, authorization, high availability, fault tolerance, CLIs, software development kits (SDKs), application programming interfaces (APIs), declarative state, node management, and flexible resource definitions. All of these features have been battle tested over the years with many large-scale clusters.

More importantly, Kubernetes orchestrates many kinds of resources beyond containers. Thanks to the use of custom resource definitions (CRDs), and custom operators, Kubernetes can describe and provision any kind of resource.

By building on Kubernetes, Harvester takes advantage of a well tested and actively developed platform. With the use of [KubeVirt](https://kubevirt.io/) and [Longhorn](https://longhorn.io/), Harvester extends Kubernetes to allow the management of bare metal servers and VMs.

Harvester is not the first time [VM management](https://www.suse.com/c/the-total-virtual-machine-management-guide/) has been built on top of Kubernetes; Rancher’s own [RancherVM](https://rancher.com/introducing-ranchervm-package-and-run-virtual-machines-as-docker-containers/) is one such example. [But these solutions have not been as popular as hoped:](https://rancher.com/blog/2020/announcing-harvester-open-source-hyperconverged-infrastructure-software)
> We believe the reason for this lack of popularity is that all efforts to date to manage VMs in container platforms require users to have substantial knowledge of container platforms. Despite Kubernetes becoming an industry standard, knowledge of it is not widespread among VM administrators.

To address this, Harvester does not expose the underlying Kubernetes platform to the end user. Instead, it presents more familiar concepts like VMs, NICs, ISO images and disk volumes. This allows Harvester to take advantage of Kubernetes while giving administrators a more traditional view of their infrastructure.

## Managing VMs at Scale

The fusion of Kubernetes and VMs provides the ability to perform common tasks such as VM creation, backups, restores, migrations, SSH-Key injection and more across multiple servers from one centralized administration console.

Consolidating virtualized resources like CPU, memory, network, and storage allows for greater resource utilization and simplified administration, allowing Harvester to satisfy the core premise of HCI.

## Conclusion

HCI abstracts the resources exposed by many individual servers to provide administrators with a unified and seamless management interface, providing a single point to perform common tasks like VM provisioning, moving, cloning, and backups.

Harvester is an HCI solution leveraging popular open source projects like Kubernetes, KubeVirt, and Longhorn, but with the explicit goal of not exposing Kubernetes to the end user.

The end result is an HCI solution built on the best open source platforms available while still providing administrators with a familiar view of their infrastructure.

Download Harvester from the [project website](https://harvesterhci.io/) and learn more from the [project documentation.](https://docs.harvesterhci.io/)

Meet the Harvester developer team! [Join our free Summer is Open session on Harvester: Tuesday, July 27 at 12pm PT and on demand.](https://community.suse.com/courses/5382798/feed) Get details about the project, watch a demo, ask questions and get a challenge to complete offline.
