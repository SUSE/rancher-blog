---
title: "Rancher Glossary: 1.6 to 2.0 Terms and Concepts"
date: 2018-04-11T11:15:00
slug: "rancher-glossary-1-6-to-2-0-terms-and-concepts"
author: "Rancher Admin"
image: "images/rancher_blog_1-6-to-2-0-terms-and-concepts.svg"
products: ["Rancher 1.x"]
tags: []
content_type: "explainer"
draft: true
migration:
  wp_id: 86923
  original_url: "https://www.suse.com/c/rancher_blog/rancher-glossary-1-6-to-2-0-terms-and-concepts/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.6 to 2.0 terminology"
  redirect_target: "docs.rancher.com"
---

How to Migrate from Rancher 1.6 to Rancher 2.1 Online MeetupKey terminology differences, implementing key elements, and transforming Compose to YAML[Watch the video](https://rancher.com/events/2018/2018-10-23-october-online-meetup-rancher1x-to-rancher2x/)

As we near the end of the development process for Rancher 2.0, we thought it might be useful to provide a glossary of terms that will help Rancher users understand the fundamental concepts in Kubernetes and Rancher.

In the move from Rancher 1.6 to Rancher 2.0, we have aligned more with the Kubernetes naming standard. This shift could be confusing for people who have only used Cattle environments under Rancher 1.6.

This article aims to help you understand the new concepts in Rancher 2.0. It can also act as an easy reference for terms and concepts between the container orchestrators Cattle and Kubernetes.

## Rancher 1.6 Cattle compared with Rancher 2.0 Kubernetes

Rancher 1.6 offered Cattle as a container orchestrator and many users chose to use it. In Cattle, you have an **environment** , which is both an administrative and a compute boundary, i.e., the lowest level at which you can assign permissions; importantly, all hosts in that environment were dedicated to that environment and that environment alone. Then, to organize your containers, you had a **Stack** , which was a logical grouping of a collection of services, with a service being a particular running image.

So, how does this structure look under under 2.0?

If you are working in the container space, then it is unlikely that you haven't heard some of the buzz words around Kubernetes, such as **pods, namespaces** and **nodes**. What this article aims to do is ease the transition from Cattle to Kubernetes by aligning the terms of both orchestrators. Along with some of the names changing, some of the capabilities have changed as well.

#### The following table gives a definition of some of the core Kubernetes concepts

| **Concept** | **Definition** |
| --- | --- |
| Cluster | Collection of machines that run containerized applications managed by Kubernetes |
| Namespace | A virtual cluster, multiple of which can be supported by a single physical cluster |
| Node | One of the physical (virtual) machines that make up a cluster |
| Pod | The smallest and simplest Kubernetes object. A Pod represents a set of running [containers](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/#why-containers) on your cluster |
| Deployment | An API object that manages a replicated application |
| Workload | Units of work that are running on the cluster, these can be pods, or deployments. |

> *More detailed information on Kubernetes concepts can be found at
> <https://kubernetes.io/docs/concepts/>*

### ENVIRONMENTS

The environment in Rancher 1.6 represented 2 things:

- The Compute boundary
- The administrative boundary

In 2.0 the environment concept doesn't exist, instead it becomes replaced by:

- **Cluster** – The compute boundary
- **Project** – An administrative boundary

A **Project** is an administrative layer introduced by Rancher to ease the burden of administration in Kubernetes.

### HOST

In Cattle, a host could only belong to one environment, things are similar in that **nodes** (the new name for hosts!) can only belong to one **cluster**. What used to be an environment with hosts, is now a cluster with nodes.

### STACK

A stack in Rancher 1.6 is a way to group a number of services. In Rancher 2.0 this is done via **namespaces**.

### SERVICE

In Rancher 1.6, a service was defined as one or more instances of the same container running. In Rancher 2.0, one or more instances of the same container running are defined as a **workload** , where a **workload** can be made up of a **pod** (s) running with a controller.

### CONTAINER

A container image is a lightweight, stand-alone, executable package of a piece of software that includes everything needed to run it: code, runtime, system tools, system libraries, settings, etc. Within Rancher 1.6, a container was the minimal definition required to run an application. Under Kubernetes, a pod is the minimal definition. A **pod** can be a single image, or it can be a number of images that all share the same storage/network and description of how they interact. **Pod** contents are always co-located and co-scheduled, and run in a shared context.

### LOAD BALANCER

In Rancher 1.6, a Load Balancer was used to expose your applications from within the Rancher environment for access externally. In Rancher 2.0, the concept is the same. There is a Load Balancer option to expose your services. In the language of Kubernetes, this function is more often referred to as an **Ingress**. In short, Load Balancer and Ingress play the same role.

## Conclusion

In terms of concepts, Cattle was the closest orchestrator to Kubernetes out of all of the orchestrators. Hopefully this article will act as an easy reference for people moving from Rancher 1.6 to 2.0. Plus, the similarity between the two orchestrators should allow for an easier transition.

#### The following table gives a quick reference for the old versus new terms.

| **Rancher 1.6** | **Rancher 2.0** |
| --- | --- |
| Container | Pod |
| Services | Workload |
| Load Balancer | Ingress |
| Stack | Namespace |
| Environment | Project (Administration)/Cluster (Compute) |
| Host | Node |
| Catalog | Helm |

> *For further reading and training, check out our free online training series: [Introduction to Kubernetes and Rancher](https://rancher.com/training/).*

How to Migrate from Rancher 1.6 to Rancher 2.1 Online MeetupKey terminology differences, implementing key elements, and transforming Compose to YAML[Watch the video](https://rancher.com/events/2018/2018-10-23-october-online-meetup-rancher1x-to-rancher2x/)
