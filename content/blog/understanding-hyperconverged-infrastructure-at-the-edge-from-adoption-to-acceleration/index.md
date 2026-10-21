---
title: "Understanding Hyperconverged Infrastructure at the Edge from Adoption to Acceleration"
date: 2022-09-29T14:08:12
slug: "understanding-hyperconverged-infrastructure-at-the-edge-from-adoption-to-acceleration"
author: "SUSE"
image: "images/levi-frey-x19nNMWeo5A-unsplash.jpg"
products: ["Harvester"]
tags: ["edge", "virtualization"]
content_type: "explainer"
draft: false
migration:
  wp_id: 94607
  original_url: "https://www.suse.com/c/rancher_blog/understanding-hyperconverged-infrastructure-at-the-edge-from-adoption-to-acceleration/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

You may be tired of the regular three-tiered infrastructure and the management issues it can bring in distributed systems and maintenance. Or perhaps you’ve looked at your infrastructure and realized that you need to move away from its current configuration. If that’s the case, hyperconverged infrastructure (HCI) may be a good solution because it removes a lot of management overhead, acting like a hypervisor that can handle networking and storage.

There are some key principles behind HCI that bring to light the advantages it has. Particularly, it can help simplify the deployment of new nodes and new applications. Because everything inside your infrastructure runs on normal [x86 servers](https://en.wikipedia.org/wiki/X86), adding nodes is as simple as spinning up a server and joining it to your HCI cluster. From here, applications can easily move around on the nodes as needed to optimize performance.

Once you’ve gotten your nodes deployed and added to your cluster, everything inside an HCI can be managed by policies, making it possible for you to strictly define the behavior of your infrastructure. This is one of the key benefits of HCI — it uses a single management interface. You don’t need to configure your networking in one place, your storage in another, and your compute in a third place; everything can be managed cohesively.

This cohesive management is possible because an HCI relies heavily on virtualization, making it feasible to converge the typical three tiers (compute, networking and storage) into a single plane, offering you flexibility.

While HCI might be an overkill for simple projects, it's becoming a best practice for various enterprise use cases. In this article, you’ll see some of the main use cases for wanting to implement HCI in your organization. We'll also introduce [Harvester](https://harvesterhci.io/) as a modern way to get started easier.

While reading through these use cases, remember that the use of HCI is not limited to them. To benefit most from this article, think about what principles of HCI make the use cases possible, and perhaps, you’ll be able to come up with additional use cases for yourself.

## **Why you need a hyperconverged infrastructure**

There are many use cases when it comes to HCI, and most of them are based on the fact that HCI is highly scalable and, more importantly, it’s *easy* to scale HCI. The concept started getting momentum [back in 2009](https://www.nutanix.com/uk/hyperconverged-infrastructure#:~:text=In%202009%2C%20engineers%20from%20several,concept%20of%20HCI%20was%20born), but it wasn’t [until 2014](https://trends.google.com/trends/explore?date=all&q=hyperconverged%20infrastructure) that it started gaining traction in the community at large. HCI is a proven and mature technology that, in its essence, has worked the same way for many years.

The past few decades have seen virtualization become the preferred method for users to optimize their resource usage and manage their infrastructure costs. However, introducing new technology, such as containers, has required operators to shift their existing virtualized-focused infrastructure to integrate with these modern cloud-based solutions, bringing new challenges for IT operators to tackle.

Managing virtualized resources (and specifically VMs) can be quite challenging. This is where HCI can help. By automating and simplifying the management of virtual resources, HCI makes it easy for developers and team leads to leverage virtualization to the fullest and reduce the time to market their product, a crucial factor in determining the success of a project.

Following are some of the most popular ways to use HCI currently:

### **Edge computing**

[Edge computing](https://www.techtarget.com/searchdatacenter/definition/edge-computing) is the principle of running workloads outside the primary data centers of a company. While there’s no single reason for wanting to use edge computing, the most popular reason is to decrease customer latency.

In edge computing, you don’t always need an extensive fleet of servers, and the amount of power you need will likely change based on the location. You’ll need more servers to serve New York City with a population of 8.3 million than you’d need to fill the entire country of Denmark with a population of 5.8 million. One of the most significant benefits of HCI is that it scales incredibly well and low. You’d typically want multiple nodes for reasons like backup, redundancy and high availability. But theoretically, it’s possible to scale down to a single node.

Given that HCI runs on normal hardware, it’s also possible for you to optimize your nodes for the workload you need. If your edge computing use case is to provide a cache for users, then you’d likely need more storage. However, if you’re implementing edge workers that need to execute small scripts, you’re more likely to need processing power and memory. With HCI, you can adapt the implementation to your needs.

### **Migrating to a Hybrid Cloud Model**

Over the past decade, the cloud has gotten more and more popular. Many companies move to the cloud and later realize their applications are better suited to run on-premises. You will also find companies that no longer want to run things in their data centers and instead want to move them to the cloud. In both these cases, HCI can be helpful.

If you want to leverage the cloud, HCI can provide a similar user experience on-premise. HCI is sometimes described as a “cloud in a box” because it can offer similar services one would expect in a public cloud. Examples of this include a consistent API for allocating compute resources dynamically, load balancers and storage services. Having a similar platform is a good foundation for being able to move applications between the public cloud and on-premise. You can even take advantage of tools like Rancher that can manage cloud infrastructure and on-prem HCI from a single pane of glass.

### **Modernization strategy**

Many organizations view HCI as an enabler in their modernization processes. However, [modernization is quite different from migration](https://www.sourcefuse.com/blog/cloud-migration-vs-modernization/).

Modernization focuses on redesigning existing systems and architecture to make the most efficient use of the new environment and its offerings. With its particular focus on simplifying the complex management of data, orchestration and workflows, HCI is perfect for modernization.

HCI enables you to consolidate your complex server architecture with all its storage, compute and network resources into smaller, easy-to-manage nodes. You can easily transform a node from a storage-first resource to a compute-first resource, allowing you to design your infrastructure how you want it while retaining simplicity.

Modern HCI solutions like Harvester can help you to run your virtualized and containerized workloads side by side, simplifying the operational and management components of infrastructure management while also providing the capabilities to manage workloads across distributed environments. Regarding automation, Harvester provides a unique approach by using cloud native APIs. This allows the user to automate using the same tools they would use to manage cloud native applications. Not switching between two “toolboxes” can increase product development velocity and decrease the overhead of managing complex systems. That means users of this approach get their product to market sooner and with less cost.

### **Virtual Desktop Infrastructure (VDI)**

Many organizations maintain fleets of virtual desktops that enable their employees to work remotely while maintaining standards of security and performance. Virtual desktops are desktop environments that are not limited to the hardware they're hosted in; they can be accessed remotely via the use of software. Organizations prefer them over hardware since they're easy to provision, scale, and destroy on demand.

Since compute and storage are two strongly connected and important resources in virtual desktops, HCI can easily manage virtual desktops. HCI's enhanced reliability provides VDI with increased fault tolerance and efficient capacity consumption. HCI also helps cut down costs for VDI as there is no need for separate storage arrays, dedicated storage networks, and related hardware.

### **Remote office/Branch office**

A remote office/branch office (ROBO) is one of the best reasons for using HCI. In case you’re not familiar, it’s typical for big enterprises to have a headquarters where they host their data and internal applications. Then the ROBOs will either have a direct connection to the headquarters to access the data and applications or have a replica in their own location. In both cases, you will introduce more management and maintenance and other factors, such as latency.

With HCI, you can spin up a few servers in the ROBOs and add them to an HCI cluster. Now, you’re managing all your infrastructure, even the infrastructure in remote locations, through a single interface. Not only can this result in a better experience for the employees, but depending on how much customer interaction they have, it can result in a better customer experience.

In addition, with HCI, you’re likely to lower your total cost of ownership. While you would typically have to put up an entire rack of hardware in a ROBO, you’re now expected to accomplish the same with just a few servers.

## **Conclusion**

After reading this article, you now know more about how HCI can be used to support a variety of use cases, and hopefully, you’ve come up with a few use cases yourself. This is just the beginning of how HCI can be used. Over the next decade or two, HCI will continue to play an important role in any infrastructure strategy, as it can be used in both on-premises data centers and the public cloud. The fact that it uses commodity x86 systems to run makes it suitable for many different use cases.

If you’re ready to start using HCI for yourself, take a look at [Harvester](https://harvesterhci.io/). Harvester is a solution developed by [SUSE](https://www.suse.com/), built for bare metal servers. It uses enterprise-grade technologies, such as [Kubernetes](https://kubernetes.io/), [KubeVirt](https://kubevirt.io/) and [Longhorn](https://longhorn.io/).

## **What's Next:**

Want to learn more about how Harvester and Rancher are helping enterprises modernize their stack speed? Sign up [here](https://more.suse.com/FY22Q4_CY_GLB_ECM_ALL_CLDNTV_WEB_Global_Online_Meetup_Harvester_RegistrationPage.html) to join our Global Online Meetup: Harvester on October 26th, 2022, at 11 AM EST.
