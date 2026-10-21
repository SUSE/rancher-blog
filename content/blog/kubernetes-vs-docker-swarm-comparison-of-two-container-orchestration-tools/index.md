---
title: "Kubernetes vs Docker Swarm: Comparison of Two Container Orchestration Tools"
date: 2019-02-11T09:07:00
slug: "kubernetes-vs-docker-swarm-comparison-of-two-container-orchestration-tools"
author: "Rancher Admin"
image: "images/rancher_blog_online-meetups-site-feature.svg"
products: ["Docker/containers (generic)"]
tags: []
content_type: "explainer"
draft: true
migration:
  wp_id: 85883
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-vs-docker-swarm-comparison-of-two-container-orchestration-tools/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Docker Swarm discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)

With the rise of containerization technology and increased attention from enterprises and technologists in general, more and more containerized applications have been deployed to the cloud. Moreover, [research conducted by 451 Research](https://451research.com/images/Marketing/press_releases/Application-container-market-will-reach-2-7bn-in-2020_final_graphic.pdf) predicts that the application container market will grow dramatically through 2020, which will continue to expand the number of containerized applications being deployed to the cloud.

When the scale and complexity of production-critical containers rises, container orchestration tools come into the picture and become an indispensable part of enterprises’ container management toolbox. Kubernetes and Docker Swarm are two famous, leading players in the container orchestration market and become the essential part of microservices of many enterprises. This article will give you an overview of each container orchestrator and offer a comparison of Kubernetes vs Docker Swarm based on:

- Cluster Setup and Configuration
- Administration
- Auto-scaling
- Load Balancing
- Storage
- Market Share

## Overview of Kubernetes

[Kubernetes](https://rancher.com/kubernetes "Why Kubernetes?") is an open-source, community-driven Container Orchestration Engine (COE) inspired by a Google project called Borg. Kubernetes is used to orchestrate fleets of containers representing instances of applications that are decoupled from the machines they run on. As the number of containers in a cluster increases to hundreds or thousands of instances, with application components deployed as separate containers, Kubernetes comes to the rescue by providing a framework for deployment, management, auto-scaling, high availability, and related tasks.

Kubernetes allows you to handle various container orchestration related tasks such as scaling containers up or down, automatic failover, distributing workloads among containers hosted on different machines.

Kubernetes follows the traditional client-server type of architecture where the Master node has the global view of the cluster and is responsible for the decision making. Users can interact with the Master node through the REST API, the web UI, and the command line interface (CLI). The Master node interacts with the Worker nodes that host the containerized applications.

Some of the common terminology used within the Kubernetes ecosystem are:

- **Container:** Containers are the units of packaging used to bundle application binaries together with their dependencies, configuration, framework, and libraries.
- **Pods:** Pods are the deployment units in Kubernetes ecosystem which contains one or more containers together on the same node. Group of containers can work together and share the resources to achieve the same goal.
- **Node:** A node is the representation of a single machine in the cluster running Kubernetes applications. A node can be a physical, bare metal machine or a virtual machine.
- **Cluster:** Several Nodes are connected to each other to form a cluster to pool resources that are shared by the applications deployed onto the cluster.
- **Persistent Volume:** Since the containers can join and leave the computing environment dynamically, local data storage can be volatile. Persistent volumes help store container data more permanently.

## Overview of Docker Swarm

Docker Swarm is an alternative, Docker-native Container Orchestration Engine that coordinates container placement and management among multiple Docker Engine hosts. Docker Swarm allows you to communicate directly with swarm instead of communicating with each Docker Engine individually. Docker Swarm architecture comprises two types of nodes called Managers and Workers.

Below are the common terminology used in the Docker Swarm ecosystem:

- **Node:** A node is a machine that runs an instance of Docker Engine
- **Swarm:** A cluster of Docker Engine instances.
- **Manager Node:** Manager nodes distribute and schedule incoming tasks onto the Worker nodes and maintains the cluster state. Manager Nodes can also optionally run services for Worker nodes.
- **Worker Node:** Worker nodes are instances of Docker Engine responsible for running applications in containers.
- **Service:** A service is an image of a microservice, such as web or database servers.
- **Task:** A service scheduled to run on a Worker node.

## Comparison of Kubernetes vs Docker Swarm Features

Both Kubernetes and Docker Swarm COEs have advantages and disadvantages, and the best fit will largely depend on your requirements. Below we compare a few features they share.

| Feature | Kubernetes | Docker Swarm | Notes |
| --- | --- | --- | --- |
| **Cluster Setup and Configuration** | Challenging to install and setup a cluster manually. Several components such as networking, storage, ports, and IP ranges for Pods require proper configuration and fine-tuning. Each of these pieces require planning, effort, and careful attention to instructions. | Simple to install and setup a cluster with fewer complexities. A single set of tools is used to setup and configure the cluster. | Setting up and configuring a cluster with **Kubernetes** is more challenging and complicated as it requires more steps that must be carefully followed.  Setting up a cluster with **Docker Swarm** is quite simple, requiring only two commands once Docker Engine is installed. |
| **Administration** | Provides a CLI, REST API, and Dashboard to control and monitor a variety of services. | Provides a CLI to interact with the services. | **Kubernetes** has a large set of commands to manage a cluster, leading to a steep learning curve. However, these commands provide great flexibility and you also have access to the dashboard GUI to manage your clusters.  **Docker Swarm** is bound to Docker API commands and has a relatively small learning curve to start managing a cluster. |
| **Auto-scaling** | Supports auto-scaling policies by monitoring incoming server traffic and automatically scaling up or down based on the resource utilization. | Supports scaling up or down with commands. | From a technical perspective, it is not practical to manually scale containers up or down. Therefore, **Kubernetes** is clearly the winner. |
| **Load-balancing** | Load balancing must be configured manually unless Pods are exposed as services. | Uses ingress load balancing and also assigns ports to services automatically. | Manual configuration for load balancing in **Kubernetes** is an extra step, but not very complicated. Automatic load balancing in **Docker Swarm** is very flexible. |
| **Storage** | Allows sharing storage volumes between containers within the same Pod. | Allows sharing data volumes with any other container on other nodes. | **Kubernetes** deletes the storage volume if the Pod is killed. **Docker Swarm** deletes storage volume when the container is killed. |
| **Market Share** | According to Google Trends, as of February 2019, the popularity of the Kubernetes in worldwide web and YouTube searches are about 79% and 75% of peak values, respectively, for the past 12 months. | According to Google Trends, as of February 2019, the popularity of Docker Swarm in worldwide web and YouTube searches is at about 5% of peak values for the past 12 months. | As can be seen in the Google Trends report, **Kubernetes** leads the market share in the popularity of web and YouTube searches. **Kubernetes** dominates this category compared to the less popular Docker Swarm. |

## Conclusion

The Kubernetes vs Docker Swarm comparison shows that each container orchestrator has advantages and disadvantages:

If you require a quick setup and have simple configuration requirements, **Docker Swarm** may be a good option due to its simplicity and shallow learning curve.

If your application is complex and utilizes hundreds of thousands of containers in production, **Kubernetes**, with its auto scaling capabilities and high availability policies, is almost certainly the right choice. However, its steep learning curve and longer setup and configuration time can be a bad fit for some users. With additional tooling, like Rancher, some of these administration and maintenance pain points can be mitigated, making the platform more accessible.

## More Resources

A good next step in learning about container orchestration and what Kubernetes can do is to book a spot in our weekly Intro to Rancher and Kubernetes Online Training. An engineer will walk you through Kubernetes architecture, components and setup, and then show you the value that Rancher adds on top of Kubernetes. [Register for the online class now.](https://rancher.com/training)

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)
