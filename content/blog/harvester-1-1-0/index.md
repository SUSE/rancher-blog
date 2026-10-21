---
title: "Harvester 1.1.0: The Latest Hyperconverged Infrastructure Solution"
date: 2022-10-26T21:01:36
slug: "harvester-1-1-0"
authors: ["William Jimenez"]
image: "images/images.png"
products: ["Harvester"]
tags: ["virtualization"]
content_type: "release"
draft: false
migration:
  wp_id: 96244
  original_url: "https://www.suse.com/c/rancher_blog/harvester-1-1-0/"
  disposition: migrate
  commercial: false
  outdated_reason: "Harvester 1.1.0 release notes"
  redirect_target: ""
---

The [Harvester](https://www.suse.com/products/harvester/) team is pleased to announce the [next release of our open source hyperconverged infrastructure product.](https://github.com/harvester/harvester/releases/tag/v1.1.0) For those unfamiliar with how Harvester works, I invite you to check out this [blog from our 1.0 launch](https://www.suse.com/c/harvester-ga-announcement/) that explains it further. This next version of Harvester adds several new and important features to help our users get more value out of Harvester. It reflects the efforts of many people, both at SUSE and in the open source community, who have contributed to the product thus far. Let’s dive into some of the key features.  

## GPU and PCI device pass-through

The GPU and PCI device pass-through experimental features are some of the most requested features this year and are officially live. These features enable Harvester users to run applications in VMs that need to take advantage of PCI devices on the physical host. Most notably, GPUs are an ever-increasing use case to support the growing demand for Machine Learning, Artificial Intelligence and analytics workloads. Our users have learned that both container and VM workloads need to access GPUs to power their businesses. This feature also can support a variety of other use cases that need PCI; for instance, SR-IOV-enabled Network Interface Cards can expose virtual functions as PCI devices, which Harvester can then attach to VMs. In the future, we plan to extend this function to support advanced forms of device passthrough, such as vGPU technologies.  

## VM Import Operator

Many Harvester users maintain other HCI solutions with a various array of VM workloads. And for some of these use cases, they want to migrate these VMs to Harvester. To make this process easier, we created the VM Import Operator, which automates the migration of VMs from existing HCI to Harvester. It currently supports two popular flavors: OpenStack and VMware vSphere. The operator will connect to either of those systems and copy the virtual disk data for each VM to Harvester’s datastore. Then it will translate the metadata that configures the VM to the comparable settings in Harvester.   

## Storage network

Harvester runs on various hardware profiles, some clusters being more compute-optimized and others optimized for storage performance. In the case of workloads needing high-performance storage, one way to increase efficiency is to dedicate a network to storage replication. For this reason, we created the Storage Network feature. A dedicated storage network removes I/O contention between workload traffic (pod-to-pod communication, VM-to-VM, etc.) and the storage traffic, which is latency sensitive. Additionally, higher capacity network interfaces can be procured for storage, such as 40 or 100 GB Ethernet.  

## Storage tiering

When supporting workloads requiring different types of storage, it is important to be able to define classes or tiers of storage that a user can choose from when provisioning a VM. Tiers can be labeled with convenient terms such as “fast” or “archival” to make them user-friendly. In turn, the administrator can then map those storage tiers to specific disks on the bare metal system. Both node and disk label selectors define the mapping, so a user can specify a unique combination of nodes and disks on those nodes that should be used to back a storage tier. Some of our Harvester users want to use this feature to utilize slower magnetic storage technologies for parts of the application where IOPS is not a concern and low-cost storage is preferred.

In summary, the past year has been an important chapter in the evolution of Harvester. As we look to the future, we expect to see more features and enhancements in store. Harvester plans to have two feature releases next year, allowing for a more rapid iteration of the ideas in our roadmap. You can download the latest version of Harvester on [Github](https://github.com/harvester/harvester/releases/tag/v1.1.0). Please continue to share your feedback with us through our community slack or your SUSE account representative.  

## Learn more

Download our FREE [eBook](https://more.suse.com/6-reasons-harvester-accelerates.html), *6 Reasons Why Harvester Accelerates IT Modernization Initiatives.* This eBook identifies the top drivers of IT modernization, outlines an IT modernization framework and introduces Harvester, an open, interoperable hyperconverged infrastructure (HCI) solution.
