---
title: "Kubernetes vs Docker: What's the difference?"
date: 2018-10-09T09:03:00
slug: "kubernetes-vs-docker-whats-the-difference"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["developer-experience"]
content_type: "explainer"
draft: false
migration:
  wp_id: 85826
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-vs-docker-whats-the-difference/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "2018 comparison, Swarm references"
  redirect_target: ""
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)

## Docker vs Kubernetes: The Journey from Docker to Kubernetes

The need to deploy applications from one computing environment to another quickly, easily, and reliably has become a critical part of enterprise’s business requirements and DevOps team’s daily workflow.

It’s unsurprising then, that container technologies, which make application deployment and management easier for teams of all sizes, have risen dramatically in recent years. At the same time, however, virtual machines (VM) as computing resources have reached their [peak use in virtualized data centers](https://www.gartner.com/newsroom/id/3315817). Since VMs existed long before containers, you may wonder what the need is for containers and why they have become so popular.

## The Benefits and Limitations of Virtual Machines

Virtual machines allow you to run a full copy of an operating system on top of virtualized hardware as if it is a separate machine. In cloud computing, physical hardware on a bare metal server are virtualized and shared between virtual machines running on a host machine in a data center by the help of hypervisor (i.e. virtual machine manager).

Even though virtual machines bring us great deal of advantages such as running different operating systems or versions, VMs can consume a lot of system resources and also take longer boot time. On the other hand, containers share the same operating system kernel with collocated containers each one running as isolated processes. Containers are lightweight alternative by taking up less space (MBs) and can be provisioning rapidly (milliseconds) as opposed to VM’s slow boot time (minutes) and more storage space requirements (GBs). This allows containers to operate at an unprecedented scale and maximize the number of applications running on minimum number of servers. Therefore, containerization shined drastically in the recent years because of all these advantages for many software projects of enterprises.

## Need for Docker Containers and Container Orchestration Tools

Since its initial release in 2013, Docker has become the most popular container technology worldwide, despite a host of other options, including RKT from CoreOS, LXC, LXD from Canonical, OpenVZ, and Windows Containers.

However, Docker technology alone is not enough to reduce the complexity of managing containerized applications, as software projects get more and more complex and require the use tens of thousands of Docker containers. To address these larger container challenges, substantial number of container orchestration systems, such as Kubernetes and Docker Swarm, have exploded onto the scene shortly after the release of Docker.

There has been some confusion surrounding Docker and Kubernetes for awhile: “what they are?”, “what they are not?”, “where are they used?”, and “why are both needed?”

This post aims to explain the role of each technology and how each technology helps companies ease their software development tasks. By the end of this article, you’ll understand that the choice is not Docker vs Kubernetes, but Kubernetes vs alternative container orchestrators.

Let’s use a made-up company, NetPly (sounds familiar?), as a case study to highlight the issues we are addressing.

NetPly is an online and on-demand entertainment movie streaming company with 30 million members in over 100 countries. NetPly delivers video streams to your favorite devices and provides personalized movie recommendations to their customers based on their previous activities, such as sharing or rating a movie. To run their application globally, at scale, and provide quality of service to their customers, NetPly runs 15,000 production servers worldwide and follow agile methodology to deploy new features and bug fixes to the production environment at a fast clip.

However, NetPly has been struggling with two fundamental issues in their software development lifecycle:

*Issue 1-* Code that runs perfectly in a development box, sometimes fails on test and/or production environments. Therefore, NetPly would like to keep code and configuration consistent across their development, test, and production environments to reduce the issues arising from application hosting environments.

*Issue 2-* Viewers experience a lot of lags as well as poor quality and degraded performance for video streams during weekends, nights, and holidays, when incoming requests spike. To resolve this potentially-devastating issue, NetPly would like to use load-balancing and auto scaling techniques and automatically adjust the resource capacity (e.g. increase or decrease number of computing resources) to maintain application availability, provide stable application performance, and optimize operational costs as computing demand increases or decreases. These requests also require NetPly to manage the complexity of computing resources and the connections between the flood of these resources in production.

Docker can be used to resolve Issue 1 by following a container-based approach; in other words, packaging application code along with all of its dependencies, such as libraries, files, and necessary configurations, together in a Docker image.

Docker is an open-source operating system level virtualized containerization platform with a light-weight application engine to run, build and distribute applications in Docker containers that run nearly anywhere. Docker containers, as part of Docker, are portable and light-weight alternative to virtual machines, and eliminate the waste of esources and longer boot times of the virtual-machine approach. Docker containers are created using Docker images, which consist of a prebuilt application stack required to launch the applications inside the container.

With that explanation of a Docker container in mind, let’s go back our successful company that is under duress: NetPly. As more users simultaneously request movies to watch on the site, NetPly needs to scale up more Docker containers at a reasonably fast rate and scale down when the traffic lowers. However, Docker alone is not capable of taking care of this job, and writing simple shell scripts to scale the number of Docker containers up or down by monitoring the network traffic or number of requests that hit to the server would not be a viable and practicable solution.

As the number of containers increases to tens of hundreds to thousands, and the NetPly IT team starts managing fleets of containers across multiple heterogeneous host machines, it becomes a nightmare to execute Docker commands like “docker run”, “docker kill”, and “docker network” manually.

Right at the point where the team starts launching containers, wiring them together, ensuring high availability even when a host goes down, and distributing the incoming traffic to the appropriate containers, the team wishes they had something that handled all these manual tasks with no or minimal intervention. Exit human, enter program.

To sum up: Docker by itself is not enough to handle these resources demands at scale. Simple shell commands alone are not sufficient to handle tasks for a tremendous number of containers on a cluster of bare metal or virtual servers. Therefore, another solution is needed to handle all these hurdles for the NetPly team.

This is where the magic starts with Kubernetes. [Kubernetes](https://rancher.com/blog/2018/2018-09-07-introduction-to-kubernetes/) is as container orchestration engine (COE), originally developed by Google and used to resolve NetPly’s **Issue 2**. Kubernetes allows you to handle fleets of containers. Kubernetes automatically manages the deployment, scaling and networking of containers, as well as container failovers by launching a new one with ease.

The following are some of the fundamental features of Kubernetes.

- Load balancing
- Configuration management
- Automatic IP assignment
- Container scheduling
- Health checks and self healing
- Storage management
- Auto rollback and rollout
- Auto scaling

## Container Orchestration Alternatives

Although Kubernetes seems to solve the challenges our NetPly team faces, there are a good deal of container management tool alternatives for Kubernetes out there.

Docker Swarm, Marathon on Apache Mesos, and Nomad are all container orchestration engines that can also be used for managing your fleet of containers.

Why choose anything other than Kubernetes? Although Kubernetes has a lot of great qualities, it has challenges too. The most arresting issues people face with Kubernetes are:

1. the steep learning curve to its commands;
2. setting Kubernetes up for different operating systems.

As opposed to Kubernetes, Docker Swarm uses the Docker CLI to manage all container services. Docker Swarm is easy to set up, has less commands to learn to get started rapidly, and is cheaper to train employees. A drawback of Docker Swarm bounds you to the limitations of the Docker API.

Another option is the Marathon framework on Apache Mesos. It’s extremely fault-tolerant and scalable for thousands of servers. However, it may be too complicated to set up and manage small clusters with Marathon, making it impractical for many teams.

Each container management tool comes with its own set of advantages and disadvantages. However, Kubernetes with its heritage based in Google’s Borg system, has been greatly adopted and supported by the large community as well as industry for many years and become the most popular container management solution among other players. With the power of both Docker and Kubernetes, it seems like journey of the power and popularity of these technologies will continue to rise and being adopted by even larger communities.

In our next article in this series, we will compare in more depth Kubernetes and Docker Swarm.

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)
