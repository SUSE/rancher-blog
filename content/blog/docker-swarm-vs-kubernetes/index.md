---
title: "Docker Swarm vs. Kubernetes"
date: 2019-09-10T20:39:44
slug: "docker-swarm-vs-kubernetes"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: []
content_type: "explainer"
draft: true
migration:
  wp_id: 87325
  original_url: "https://www.suse.com/c/rancher_blog/docker-swarm-vs-kubernetes/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Docker Swarm discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

## Introduction

With the rise of the containerization technology and increased attention from enterprises and technologists in general, more and more containerized applications have been deployed to the cloud. Moreover, [research conducted by 451 Research](https://451research.com/images/Marketing/press_releases/Application-container-market-will-reach-2-7bn-in-2020_final_graphic.pdf) predicts that the application container market will grow dramatically through 2020, which will continue to expand the number of containerized applications in the cloud.

When the scale and complexity of production-critical containers rises, container orchestration tools step into the picture and fill an important gap in the container management toolbox. **Kubernetes** and **Docker Swarm** are two well-known, leading players in the container orchestration market that are an essential part of container story for many enterprises.

## Overview of Kubernetes

[Kubernetes](https://rancher.com/kubernetes "Why Kubernetes?") is an open-source, community-driven Container Orchestration Engine (COE) inspired by a Google project called Borg. Kubernetes is used to orchestrate fleets of containers representing instances of applications decoupled from the machines they run on. As the number of containers in a cluster increases to hundreds or thousands, with application components deployed as separate containers, Kubernetes comes to the rescue by providing a framework for deployment, management, auto-scaling, high availability, and related tasks.

Kubernetes allows you to handle various container orchestration-related tasks such as scaling containers up or down, automatic failover, distributing workloads among containers hosted on different machines.

Kubernetes follows a traditional client-server architecture where the Master node has the global view of the cluster and is responsible for decision making, allocating resources, and scheduling containers. Users can interact with the Master node through the REST API, the web UI, and the command line interface (CLI). The Master node interacts with the Worker nodes that host the containerized applications.

Some of the common terminology used within the Kubernetes ecosystem are:

- **Container:** Containers are the units of packaging used to bundle application binaries together with their dependencies, configuration, framework, and libraries.
- **Pods:** Pods are the deployment units in Kubernetes ecosystem which contains one or more containers together on the same node. Group of containers can work together and share the resources to achieve the same goal.
- **Node:** A node is the representation of a single machine in the cluster running Kubernetes applications. A node can be a physical, bare metal machine or a virtual machine.
- **Cluster:** Several nodes are connected to each other to form a cluster to pool resources that are shared by the applications deployed onto the cluster.
- **Persistent Volume:** Since the containers can join and leave the computing environment dynamically, local data storage can be volatile. Persistent volumes help store container data more permanently.

## Overview of Docker Swarm

Docker Swarm is an alternative, Docker-native Container Orchestration Engine that coordinates container placement and management among multiple Docker Engine hosts. Docker Swarm allows you to communicate directly with swarm instead of communicating with each Docker Engine individually. Docker Swarm architecturally is comprised of two types of nodes called Managers and Workers.

Below are some the common terms used in the Docker Swarm ecosystem:

- **Node:** A node is a machine that runs an instance of Docker Engine.
- **Swarm:** A cluster of Docker Engine instances.
- **Manager Node:** Manager nodes distribute and schedule incoming tasks onto the Worker nodes and maintain the cluster state. Manager Nodes can also optionally run services for Worker nodes.
- **Worker Node:** Worker nodes are instances of Docker Engine responsible for running applications in containers.
- **Service:** A service is an image of a microservice, such as web or database servers.
- **Task:** A service scheduled to run on a Worker node.

## Comparison of Kubernetes vs Docker Swarm Features

Both Kubernetes and Docker Swarm COEs have advantages and disadvantages and the best fit will largely depend on your requirements. Below, we compare a few features they share.

| Feature | Kubernetes | Docker Swarm | Notes |
| --- | --- | --- | --- |
| **Cluster Setup and Configuration** | Challenging to install and setup a cluster manually. Several components such as networking, storage, ports, and IP ranges for Pods require proper configuration and fine-tuning. Each of these pieces require planning, effort, and careful attention to instructions. | Simple to install and setup a cluster with fewer complexities. A single set of tools is used to setup and configure the cluster. | Setting up and configuring a cluster with **Kubernetes** is more challenging and complicated as it requires more steps that must be carefully followed. Setting up a cluster with **Docker Swarm** is quite simple, requiring only two commands once Docker Engine is installed. |
| **Administration** | Provides a CLI, REST API, and Dashboard to control and monitor a variety of services. | Provides a CLI to interact with the services. | **Kubernetes** has a large set of commands to manage a cluster, leading to a steep learning curve. However, these commands provide great flexibility and the GUI dashboard is also available to help you manage your clusters. **Docker Swarm** is bound to Docker API commands and has a relatively small learning curve to start managing a cluster. |
| **Auto-scaling** | Supports auto-scaling policies by monitoring incoming server traffic and automatically scaling up or down based on the resource utilization. | Supports scaling up or down with commands. | From a technical perspective, it is not practical to manually scale containers up or down. Therefore, **Kubernetes** is clearly the winner in this category. |
| **Load-balancing** | Load balancing must be configured manually unless Pods are exposed as services. | Uses ingress load balancing and also assigns ports to services automatically. | Manual configuration for load balancing in **Kubernetes** is an extra step, but not very complicated. Automatic load balancing in **Docker Swarm** is very flexible. |
| **Storage** | Allows sharing storage volumes between containers within the same Pod. | Allows sharing data volumes with any other container on other nodes. | **Kubernetes** deletes the non-persistent storage volumes if the Pod is killed. **Docker Swarm** deletes storage volume when the container is killed. |
| **Market Share** | According to Google Trends, as of February 2019, the popularity of the Kubernetes in worldwide web and YouTube searches are about 79% and 75% of peak values, respectively, for the past 12 months. | According to Google Trends, as of February 2019, the popularity of Docker Swarm in worldwide web and YouTube searches is at about 5% of peak values for the past 12 months. | As can be seen in the Google Trends report, **Kubernetes** leads the market share in the popularity of web and YouTube searches. **Kubernetes** dominates this category compared to the less popular Docker Swarm. |

## Conclusion

In summary, both Kubernetes and Docker Swarm have advantages and disadvantages.

If you require a quick setup and have simple configuration requirements, **Docker Swarm** may be a good option due to its simplicity and shallow learning curve.

If your application is complex and utilize dozens to thousands of containers in production, **Kubernetes**, with its auto scaling capabilities and high availability policies, is almost certainly the right choice. Its steep learning curve and longer setup and configuration time can be a bad fit for some users, but with additional tooling, like Rancher, some of these administration and maintenance pain points can be mitigated, making the platform more accessible.
