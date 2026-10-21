---
title: "A Path to Legacy Application Modernization Through Kubernetes"
date: 2022-07-06T21:14:23
slug: "a-path-to-legacy-application-modernization-through-kubernetes"
author: "SUSE"
image: "images/Kubernetes-Logo.wine_.jpg"
products: ["Kubernetes (generic)"]
tags: ["virtualization", "storage"]
content_type: "explainer"
draft: false
migration:
  wp_id: 92759
  original_url: "https://www.suse.com/c/rancher_blog/a-path-to-legacy-application-modernization-through-kubernetes/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Modern application deployments rely heavily on containerization for its scalability, availability and ease of maintenance. Legacy applications implemented before the containerization era often use monolithic, hardware-centric architectures that are difficult to scale and manage.

These legacy applications may have multiple services bundled into the same deployment unit without a logical grouping. They’re challenging to maintain since changes to one part of the application require changing other tightly coupled parts, making it harder to add or modify features. Scaling such applications is also tricky because to do so requires adding more hardware instances connected to load balancers. This takes a lot of manual effort and is prone to errors.
Modernizing a legacy application requires you to visualize the architecture from a brand-new perspective, redesigning it to support horizontal scaling, high availability and code maintainability. This article explains how to modernize legacy applications using Kubernetes as the foundation and suggests three tools to make the process easier.

## Using Kubernetes to modernize legacy applications

A legacy application can only meet a modern-day application’s scalability and availability requirements if it’s redesigned as a collection of lightweight, independent services.
Another critical part of modern application architecture is the infrastructure. Adding more server resources to scale individual services can lead to a large overhead that you can’t automate, which is where containers can help. Containers are self-contained, lightweight packages that include everything needed for a service to run. Combine this with a cluster of hardware instances, and you have an infrastructure platform where you can deploy and scale the application runtime environment independently.
[Kubernetes](https://kubernetes.io/) can create a scalable and highly available infrastructure platform using container clusters. Moving legacy applications from physical or virtual machines to Kubernetes-hosted containers offers many advantages, including the flexibility to use on-premises and multi-cloud environments, automated container scheduling and load balancing, self-healing capability, and easy scalability.
Organizations generally adopt one of two approaches to deploy legacy applications on Kubernetes: using virtual machines and redesigning the application.

### Using virtual machines

A monolith application’s code and dependencies are embedded in a virtual machine (VM) so that images of the VM can run on Kubernetes. Frameworks like [Rancher](https://rancher.com/) provide a one-click solution to run applications this way. The disadvantage is that the monolith remains unchanged, which doesn’t achieve the fundamental principle of using lightweight container images. It is also possible to run part of the application in VMs and containerize the less complex ones. This hybrid approach helps to break down the monolith to a smaller extent without huge effort in refactoring the application. Tools like Harvester can help while managing the integration in this hybrid approach.

### Redesigning the application

Redesigning a monolithic application to support container-based deployment is a challenging task that involves separating the application’s modules and recreating them as stateless and stateful services. Containers, by nature, are stateless and require additional mechanisms to handle the storage of state information. It’s common to use the distributed storage of the container orchestration cluster or third-party services for such persistence.
Organizations are more likely to adopt the first approach when the legacy application needs to move to a Kubernetes-based solution as soon as possible. This way, they can have a Kubernetes-based solution running quickly with less business impact and then slowly move to a completely redesigned application. Although Kubernetes migration has its challenges, some tools can simplify this process. The following are three such solutions.

## Rancher

[Rancher](https://rancher.com/) provides a complete container management platform for Kubernetes, giving you the tools to successfully run Kubernetes anywhere. It’s designed to simplify the operational challenges of running multiple Kubernetes clusters across different infrastructure environments. Rancher provides developers with a complete Kubernetes environment, irrespective of the backend, including centralized authentication, access control and observability features:

- **Unified UI:** Most organizations have multiple Kubernetes clusters. DevOps engineers can sometimes face challenges when manually provisioning, managing, monitoring and securing thousands of cluster nodes while establishing compliance. Rancher lets engineers manage all these clusters from a single dashboard.
- **Multi-environment deployment:** Rancher helps you create Kubernetes clusters across multiple infrastructure environments like on-premises data centers, public clouds and edge locations without needing to know the nuances of each environment.
- **App catalog:** The Rancher app catalog offers different application templates. You can easily roll out complex application stacks on top of Kubernetes with the click of a button. One example is [Longhorn](https://rancher.com/products/longhorn), a distributed storage mechanism to help store state information.
- **Security policies and role-based access control:** Rancher provides a centralized authentication mechanism and role-based access control (RBAC) for all managed clusters. You can also create pod-level security policies.
- **Monitoring and alerts:** Rancher offers cluster monitoring facilities and the ability to generate alerts based on specific conditions. It can help transport Kubernetes logs to external aggregators.

## Harvester

[Harvester](https://harvesterhci.io/) is an open source, [hyperconverged infrastructure solution](https://www.suse.com/c/the-complete-hyperconverged-infrastructure-solutions-guide/). It combines [KubeVirt](https://kubevirt.io/), a virtual machine add-on, and [Longhorn](https://longhorn.io/), a cloud native, distributed block storage add-on along with many other cloud native open source frameworks. Additionally, Harvester is built on Kubernetes itself.
Harvester offers the following benefits to your Kubernetes cluster:

- **Support for VM workloads:** Harvester enables you to run VM workloads on Kubernetes. Running monolithic applications this way helps you quickly migrate your legacy applications without the need for complex cluster configurations.
- **Cost-effective storage:** Harvester uses directly connected storage drives instead of external SANs or cloud-based block storage. This helps significantly reduce costs.
- **Monitoring features:** Harvester comes with [Prometheus](https://prometheus.io/), an open source monitoring solution supporting time series data. Additionally, [Grafana](https://grafana.com/), an interactive visualization platform, is a built-in integration of Harvester. This means that users can see VM or Kubernetes cluster metrics from the Harvester UI.
- **Rancher integration:** Harvester comes integrated with Rancher by default, so you can manage multiple Harvester clusters from the Rancher management UI. It also integrates with Rancher’s centralized authentication and RBAC.

## Longhorn

[Longhorn](https://longhorn.io/) is a distributed cloud storage solution for Kubernetes. It’s an open source, cloud native project originally developed by Rancher Labs, and it integrates with the [Kubernetes persistent volume API](https://kubernetes.io/docs/concepts/storage/persistent-volumes/). It helps organizations use a low-cost persistent storage mechanism for saving container state information without relying on cloud-based object storage or expensive storage arrays. Since it’s deployed on Kubernetes, Longhorn can be used with any storage infrastructure.
Longhorn offers the following advantages:

- **High availability:** Longhorn’s microservice-based architecture and lightweight nature make it a highly available service. Its storage engine only needs to manage a single volume, dramatically simplifying the design of storage controllers. If there’s a crash, only the volume served by that engine is affected. The Longhorn engine is lightweight enough to support as many as 10,000 instances.
- **Incremental snapshots and backups:** Longhorn’s UI allows engineers to create scheduled jobs for automatic snapshots and backups. It’s possible to execute these jobs even when a volume is detached. There’s also an adequate provision to prevent existing data from being overwritten by new data.
- **Ease of use:** Longhorn comes with an intuitive dashboard that provides information about volume status, available storage and node status. The UI also helps configure nodes, set up backups and change operational settings.
- **Ease of deployment:** Setting up and deploying Longhorn just requires a single click from the Rancher marketplace. It's a simple process, even from the command-line interface, because it involves running only certain commands. Longhorn’s implementation is based on the container storage interface (CSI) as a CSI plug-in.
- **Disaster recovery:** Longhorn supports creating disaster recovery (DR) volumes in separate Kubernetes clusters. When the primary cluster fails, it can fail over to the DR volume. Engineers can configure recovery time and point objectives when setting up that volume.
- **Security:** Longhorn supports data encryption at rest and in motion. It uses Kubernetes secret storage for storing the encryption keys. By default, backups of encrypted volumes are also encrypted.
- **Cost-effectiveness:** Being open source and easily maintainable, Longhorn provides a cost-effective alternative to the cloud or other proprietary services.

## Conclusion

Modernizing legacy applications often involves converting them to containerized microservice-based architecture. Kubernetes provides an excellent solution for such scenarios, with its highly scalable and available container clusters.
The journey to Kubernetes-hosted, microservice-based architecture has its challenges. As you saw in this article, solutions are available to make this journey simpler.
[SUSE](https://www.suse.com/) is a pioneer in value-added tools for the Kubernetes ecosystem. [SUSE Rancher](https://www.suse.com/products/suse-rancher/) is a powerful Kubernetes cluster management solution. [Longhorn](https://www.suse.com/products/longhorn/) provides a storage add-on for Kubernetes and [Harvester](https://www.suse.com/products/harvester/) is the next generation of open source hyperconverged infrastructure solutions designed for modern cloud native environments.

## Get hands on with these tools

[Rancher Quick Start](https://www.suse.com/products/suse-rancher/get-started/)[Longhorn](https://longhorn.io/)[Harvester](https://www.suse.com/products/harvester/)
