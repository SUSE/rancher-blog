---
title: "Managing Your Hyperconverged Network with Harvester"
date: 2022-07-22T19:26:20
slug: "managing-your-hyperconverged-network-with-harvester"
author: "SUSE"
image: "images/Harvester-Symbol.png"
products: ["Harvester"]
tags: ["networking", "virtualization"]
content_type: "explainer"
draft: false
migration:
  wp_id: 93131
  original_url: "https://www.suse.com/c/rancher_blog/managing-your-hyperconverged-network-with-harvester/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Harvester 2022 networking UI"
  redirect_target: ""
---

Hyperconverged infrastructure (HCI) is a data center architecture that uses software to provide a scalable, efficient, cost-effective way to deploy and manage resources. HCI virtualizes and combines storage, computing, and networking into a single system that can be easily scaled up or down as required.

A hyperconverged network, a networking architecture component of the HCI stack, helps simplify network management for your IT infrastructure and reduce costs by virtualizing your network. Network virtualization is the most complicated among the storage, compute and network components because you need to virtualize the physical controllers and switches while dividing the network isolation and bandwidth required by the storage and compute. HCI allows organizations to simplify their IT infrastructure via a single control pane while reducing costs and setup time.

This article will dive deeper into HCI with a new tool from [SUSE](https://www.suse.com/) called [Harvester](https://www.suse.com/products/harvester/). By using [Kubernetes'](https://kubernetes.io/) Container Network Interface (CNI) mechanisms, Harvester enables you to better manage the network in an HCI. You’ll learn the key features of Harvester and how to use it with your infrastructure.

## **Why you should use Harvester**

The data center market offers plenty of proprietary virtualization platforms, but generally, they aren’t open source and enterprise-grade. Harvester fills that gap. The HCI solution built on Kubernetes has garnered [about 2,200 GitHub stars](https://github.com/harvester/harvester) as of this article.

In addition to traditional virtual machines (VMs), Harvester supports containerized environments, bridging the gap between legacy and cloud native IT. Harvester allows enterprises to replicate HCI instances across remote locations while managing these resources through a single pane.

Following are several reasons why Harvester could be ideal for your organization.

### **Open source solution**

Most HCI solutions are proprietary, requiring complicated licenses, high fees and support plans to implement across your data centers. Harvester is a free, open source solution with no license fees or vendor lock-in, and it supports environments ranging from core to edge infrastructure. You can also submit a feature request or issue on the GitHub repository. Engineers check the recommendations, unlike other proprietary software that updates too slowly for market demands and only offers support for existing versions.

There is an active community that helps you adopt Harvester and offers to troubleshoot. If needed, you can buy a support plan to receive round-the-clock assistance from support engineers at SUSE.

### **Rancher integration**

[Rancher](https://rancher.com/) is an open source platform from SUSE that allows organizations to run containers in clusters while simplifying operations and providing security features. Harvester and Rancher, developed by the same engineering team, work together to manage VMs and Kubernetes clusters across environments in a single pane.

Importing an existing Harvester installation is as easy as clicking a few buttons on the Rancher virtualization management page. The tight integration enables you to use authentication and role-based access control for multitenancy support across Rancher and Harvester.

This integration also allows for multicluster management and load balancing of persistent storage resources in both VM and container environments. You can deploy workloads to existing VMs and containers on edge environments to take advantage of edge processing and data analytics.

### **Lightweight architecture**

Harvester was built with the ethos and design principles of the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/), so it’s lightweight with a small footprint. Despite that, it’s powerful enough to orchestrate VMs and support edge and core use cases.

The three main components of Harvester are:

- **[Kubernetes](https://kubernetes.io/):** Used as the Harvester base to produce an enterprise-grade HCI.
- **[Longhorn](https://longhorn.io/):** Provides distributed block storage for your HCI needs.
- **[KubeVirt](https://kubevirt.io/):** Provides a VM management kit on top of Kubernetes for your virtualization needs.

The best part is that you don’t need experience in these technologies to use Harvester.

## **What Harvester offers**

As an HCI solution, Harvester is powerful and easy to use, with a web-based dashboard for managing your infrastructure. It offers a comprehensive set of features, including the following:

### **VM lifecycle management**

If you’re creating Windows or Linux VMs on the host, Harvester supports cloud-init, which allows you to assign a startup script to a VM instance that runs when the VM boots up.

The custom cloud-init startup scripts can contain custom user data or network configuration and are inserted into a VM instance using a temporary disc. Using the QEMU guest agent means you can dynamically inject SSH keys through the dashboard to your VM via cloud-init.

Destroying and creating a VM is a click away with a clearly defined UI.

### **VM live migration support**

VMs inside Harvester are created on hosts or bare-metal infrastructure. One of the essential tasks in any infrastructure is reducing downtime and increasing availability. Harvester offers a high-availability solution with VM live migration.

If you want to move your VM to Host 1 while maintaining Host 2, you only need to click **m****igrate**. After the migration, your memory pages and disc block are transferred to the new host.

### **Supported VM backup and restore**

Backing up a VM allows you to restore it to a previous state if something goes wrong. This backup is crucial if you’re running a business or other critical application on the machine; otherwise, you could lose data or necessary workflow time if the machine goes down.

Harvester allows you to easily back up your machines in [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) or network-attached storage (NAS) devices. After configuring your backup target, click **Take Backup** on the virtual machine page. You can use the backup to replace or restore a failed VM or create a new machine on a different cluster.

### **Network interface controllers**

Harvester offers a CNI plug-in to connect network providers and configuration management networks. There are two network interface controllers available, and you can choose either or both, depending on your needs.

#### **Management network**

This is the default networking method for a VM, using the eth0 interface. The network configures using [Canal](https://projectcalico.docs.tigera.io/getting-started/kubernetes/flannel/flannel) CNI plug-ins. A VM using this network changes IP after a reboot while only allowing access within the cluster nodes because there’s no DHCP server.

#### **Secondary network**

The secondary network controller uses the [Multus](https://github.com/k8snetworkplumbingwg/multus-cni) and [bridge](https://www.cni.dev/plugins/current/main/bridge/) CNI plug-ins to implement its customized Layer 2 bridge VLAN. VMs are connected to the host network via a Linux bridge and are assigned IPv4 addresses.

IPv4 addresses' VMs are accessed from internal and external networks using the physical switch.

## **When to use Harvester**

There are multiple use cases for Harvester. The following are some examples:

### **Host management**

Harvester dashboards support viewing infrastructure nodes from the host page. Kubernetes has HCI built-in, which makes live migrations, like Features, possible. And Kubernetes provides fault tolerance to keep your workloads in other nodes running if one node goes down.

### **VM management**

Harvester offers flexible VM management, with the ability to create Windows or Linux VMs easily and quickly. You can mount volumes to your VM if needed and switch between the administration and a secondary network, according to your strategy.

As noted above, live migration, backups, and cloud-init help manage VM infrastructure.

### **Monitoring**

Harvester has built-in monitoring integration with [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/), which installs automatically during setup. You can observe CPU, memory, storage metrics, and more detailed metrics, such as CPU utilization, load average, network I/O, and traffic. The metrics included are host level and specific VM level.

These stats help ensure your cluster is healthy and provide valuable details when troubleshooting your hosts or machines. You can also pop out the Grafana dashboard for more detailed metrics.

## **Conclusion**

[Harvester](https://www.suse.com/products/harvester/) is the HCI solution you need to manage and improve your hyperconverged infrastructure. The open source tool provides storage, network and computes in a single pane that’s scalable, reliable, and easy to use.

Harvester is the latest innovation brought to you by [SUSE](https://www.suse.com/). This open source leader provides enterprise Linux solutions, such as Rancher and K3s, designed to help organizations more easily achieve digital transformation.

## **Get started**

For more on Harvester or to get started, check the [official documentation](https://docs.harvesterhci.io/v1.0/).
