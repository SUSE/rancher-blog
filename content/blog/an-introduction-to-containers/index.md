---
title: "An Introduction to Containers"
date: 2019-05-30T09:04:00
slug: "an-introduction-to-containers"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_storage.svg"
products: ["Docker/containers (generic)"]
tags: []
content_type: "explainer"
draft: false
migration:
  wp_id: 85848
  original_url: "https://www.suse.com/c/rancher_blog/an-introduction-to-containers/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

## Introduction

Containers, along with containerization technology like [Docker](https://www.docker.com/) and [Kubernetes](https://kubernetes.io/), have become increasingly common components in many developers’ toolkits. The goal of containerization, at its core, is to offer a better way to create, package, and deploy software across different environments in a predictable and easy-to-manage way.

In this guide, we’ll take a look at what containers are, how they are different from other kinds of virtualization technologies, and what advantages they can offer for your development and operations processes. If you just want a quick overview of some of the core terms associated with containers, feel free to skip ahead to the [terminology section](#container-terminology).

## What Are Containers?

**Containers** are an operating system virtualization technology used to package applications and their dependencies and run them in isolated environments. They provide a lightweight method of packaging and deploying applications in a standardized way across many different types of infrastructure.

These goals make containers an attractive option for both developers and operations professionals. Containers run consistently on any container-capable host, so developers can test the same software locally that they will later deploy to full production environments. The container format also ensures that the application dependencies are baked into the image itself, simplifying the hand off and release processes. Because the hosts and platforms that run containers are generic, infrastructure management for container-based systems can be standardized.

Containers are created from **container images**: bundles that represent the system, applications, and environment of the container. Container images act like templates for creating specific containers, and the same image can be used to spawn any number of running containers.

This is similar to how *classes* and *instances* work in object-oriented programming; a single class can be used to create any number of instances just as a single container image can be used to create any number of containers. This analogy also holds true in regards to inheritance since container images can act as the parent for other, more customized container images. Users can download pre-built container from external sources or build their own images customized to their needs.

## What is Docker?

While Linux containers are a somewhat generic technology that can be implemented and managed in a number of different ways, [Docker](https://www.docker.com/) is by far the most common way of running building and running containers. **Docker** is a set of tools that allow users to create container images, push or pull images from external registries, and run and manage containers in many different environments. The surge in the popularity of containers on Linux can be directly attributed to Docker’s efforts following its release in 2013.

The `docker` command line tool plays many roles. It runs and manages containers, acting as a process manager for container workloads. It can create new container images by reading and executing commands from `Dockerfile` or by taking snapshots of containers that are already running. The command can also interact with [Docker Hub](https://hub.docker.com/), a container image registry, to pull down new container images or to push up local images to save or publish them.

While Docker provides only one of many implementations of containers on Linux, it has the distinction of being the most common entry point into the world of containers and the most commonly deployed solution. While [open standards](https://en.wikipedia.org/wiki/Open_Container_Initiative) have been developed for containers to ensure interoperability, most container-related platforms and tools treat Docker as their main target when testing and releasing software. Docker may not always be the most performant solution for a given environment, but it’s likely to be one of the most well-tested options.

Practically speaking, while there are alternatives for containers on Linux, it usually makes sense to learn Docker first because of its ubiquity and its influence on the terminology, standards, and tooling of the ecosystem.

## How Do Containers Work?

To understand how containers work, it is sometimes helpful to discuss how they differ from virtual machines.

### Virtual Machines vs Containers

**Virtual machines**, or VMs, are a hardware virtualization technology that allows you to fully virtualize the hardware and resources of a computer. A separate guest operating system manages the virtual machine, completely separate from the OS running on the host system. On the host system, a piece of software called a **hypervisor** is responsible for starting, stopping, and managing the virtual machines.

Because VMs are operated as completely distinct computers that, under normal operating conditions, cannot affect the host system or other VMs, virtual machines offer great isolation and security. However, they do have their drawbacks. For instance, virtualizing an entire computer requires VMs to use a significant amount of resources. Since the virtual machine is operated by a complete guest operating system, the virtual machine provisioning and boot times can be fairly slow. Likewise, since the VM operates as an independent machine, administrators often need to adopt infrastructure-like management tools and processes to update and run the individual environments.

In general, virtual machines let you subdivide a machine’s resources into smaller, individual computers, but the end result doesn’t differ significantly from managing a fleet of physical computers. The fleet membership expands and the responsibility of each host might become more focused, but the tools, strategies, and processes you employ and the capabilities of your system probably won’t noticeably change.

Containers take a different approach. Rather than virtualizing the entire computer, containers virtualize the operating system directly. They run as specialized processes managed by the host operating system’s kernel, but with a constrained and heavily manipulated view of the system’s processes, resources, and environment. Containers are unaware that they exist on a shared system and operate as if they were in full control of the computer.

Rather than treating containers as if they were full computers like with virtual machines, it is more common to manage containers more similarly to applications. For instance, while you can bundle an SSH server into a container, this isn’t a recommended pattern. Instead, debugging is generally performed through a logging interface, updates are applied by rolling new images, and service management is de-emphasized in favor of managing the entire container.

These characteristics mean that containers occupy a space that sits somewhere in between the strong isolation of virtual machines and the native management of conventional processes. Containers offer compartmentalization and process-focused virtualization, which provide a good balance of confinement, flexibility, and speed.

### Linux cgroups and Namespaces

The Linux kernel has a few features that make this possible. [Linux control groups](https://en.wikipedia.org/wiki/Cgroups), or **cgroups**, are a kernel feature that allow processes and their resources to be grouped, isolated, and managed as a unit. cgroups bundle processes together, determine which resources they can access, and provide a mechanism for managing and monitoring their behavior. They follow a hierarchical system that allows child processes to inherit the conditions of their parent and potentially adopt further constraints. cgroups provide the functionality needed to bundle processes together as a group and limit the resources they can access.

The other main kernel feature that containers rely on is [Linux namespaces](https://en.wikipedia.org/wiki/Linux_namespaces). **Namespaces** limit what processes can see of the rest of the system. Processes running inside namespaces are not aware of anything running outside of their namespace. Because namespaces define a distinct context that’s separate from the rest of the system, the namespace’s process tree needs to reflect that context. Inside the namespace, the main process becomes PID 1 (process ID 1), the PID traditionally reserved for the OS’s init system. This heavily manipulated virtual process tree constructed within the namespace allows processes running within containers to behave as if they were operating in a normal, unrestricted environment.

## Benefits of Containerization

Now that we’ve discussed some of the technologies that make containers possible, let’s take a look at some of their most important characteristics.

### Lightweight Virtualization

Compared to hardware virtualization with virtual machines, containers are extremely lightweight. Rather than virtualizing all of the hardware resources and running a completely independent operating system within that environment, containers use the host system’s kernel and run as compartmentalized processes within that OS.

From the perspective of the host, containers run like any other process, meaning they are quick to start and stop and use a limited amount of resources. The container can only view and access a subset of the host’s process space and resources, but is able to behave as if it were a completely independent operating system in most circumstances.

The container images themselves can also be very small. Minimal image sizes enable workflows that rely on pulling down the latest image at runtime without introducing significant delays. This is a requirement for many fault tolerant, self-healing distributed systems.

### Environmental Isolation

By using Linux kernel features like cgroups and namespaces, containers are isolated from the host environment and each other. This provides a level of functional confinement to help prevent container environments from interfering with one another.

While not robust enough to be considered full security sandboxing, this isolation does have advantages. Dependency and library conflicts are easier to avoid since the host and each container maintain software in separate filesystems. Since the networking environments can be separated, applications within the container can bind to their native ports without concern about conflicting with software on the host system or in other containers. The administrator can then choose how to map the container’s networking to the host networks according to their requirements.

### Standardized Packaging Format and Runtime Target

One of the most compelling benefits of containers is their ability to unify and simplify the process of packaging and deploying software. Container images allow you to bundle applications and all of their runtime requirements into a single unit that is deployable across diverse infrastructure.

Inside of containers, developers can install and use any libraries their applications require without fear of interfering with host system libraries. Dependencies are version locked when the image is created. Since the container runtime acts as a standard, stable deployment platform, developers do not need to know much about the specific machines where the containers will be running. As long as the container runtime is operational and adequate system resources are available, the container should run the same as it did in the development environment.

Similarly, from an operational perspective, containerization helps standardize the requirements of the deployment environment. Rather than having to provision and maintain unique environments based on the application language, runtime, and dependencies, administrators can focus on maintaining generic hosts that function as container platforms and allocating pools of resources those machines can access. Bundling all of the particular application idiosyncrasies within the container creates a natural boundary between the concerns of the application and that of the platform.

### Scalability

The container paradigm also allows you to scale your applications using relatively straightforward mechanisms. Lightweight image sizes, quick start up times, the ability to create, test, and deploy “golden images”, and the standardized runtime environment are all features that can be used to build highly scalable systems.

The scalability of a system is highly dependent on the application architecture and how the container images themselves are constructed. Designs that work well with the container paradigm recognize the strengths of the container format to achieve a good balance of speed, availability, and manageability. [Service-oriented architectures](https://en.wikipedia.org/wiki/Service-oriented_architecture), and specifically [microservices](https://en.wikipedia.org/wiki/Microservices), are incredibly popular in containerized environments because decomposing applications into discrete components with a focused purpose makes developing, scaling, and updating more straightforward.

## Container Terminology

Before we wrap up, let’s review some of the key terminology we’ve introduced in this guide and some new ones that you might come across as you continue learning.

- **Container:** In Linux, containers are an operating system virtualization technology used to package applications and their dependencies and run them in isolated environments.
- **Container Image:** Container images are static files that define the filesystem and behavior of specific container configurations. Container images are used as a template to create containers.
- **Container Orchestration:** Container orchestration is a term used to describe the processes and tooling required to manage fleets of containers across multiple hosts. Container orchestration typically controls scaling, fault tolerance, resource allocation, and scheduling using a container platform.
- **Container Runtime:** A container runtime is the component that actually runs and manages containers on a host. The minimum requirement is usually to be able to provision a container from a given image, but many runtimes bundle other functionality like process management, monitoring, and image management. Docker includes a container runtime within it’s `docker` command, but there are many other alternatives available for different use cases.
- **Docker:** Docker was the first technology to successfully popularize the idea Linux containers. Among others, Docker’s ecosystem of tools includes `docker`, a container runtime with extensive container and image management features, `docker-compose`, a system for defining and running multi-container applications, and [Docker Hub](https://hub.docker.com/), a container image registry.
- **Dockerfile:** A Dockerfile is a text file describing how to build a container image. It defines the base image, the commands to run within the system, and way that the runtime should start and manage the processes within the container. While not the only option, Dockerfiles are the most common format for defining container images, even when not using Docker’s image building functionality.
- **Kata Containers:** Kata containers are an approach to managing lightweight virtual machines using models, workflows, and tooling that replicates the experience of working with containers. Kata containers seek to capture the benefit of containers while offering more robust isolation and security.
- **Kubernetes:** Kubernetes is a powerful container orchestration platform that manages clusters of container hosts and the workloads that run on them. Kubernetes offers tooling and abstractions to deploy, scale, monitor, and manage containers in highly available production environments.
- **Linux cgroups:** Linux cgroups, or control groups, are a kernel feature that bundles processes together and determines their access to resources. Containers in Linux are implemented using cgroups in order to manage resources and separate processes.
- **Linux namespaces:** Linux namespaces are a kernel feature designed to limit the visibility for a process or cgroup to the rest of the system. Containers in Linux use namespaces to help isolate the workloads and their resources from other processes running on the system.
- **LXC:** LXC is a form of Linux containerization that predates Docker and many other technologies while relying on many of the same kernel technologies. Compared to Docker, LXC usually virtualizes an entire operating system rather than just the processes required to run an application, which can seem more similar to a virtual machine.
- **Virtual Machines:** Virtual machines, or VMs, are a hardware virtualization technology that emulates a full computer. A full operating system is installed within the virtual machine to manage the internal components and access the computing resources of the virtual machine.
- **Virtualization:** Virtualization is a process of creating, running, and managing virtual environments or computing resources. Virtualization is a way of abstracting physical resources and is often used to segment a pool of resources for different purposes.

## Conclusion

Containers are not a magic bullet, but they do offer some attractive advantages over running software on bare metal or using other virtualization technologies. By providing lightweight, functional isolation and developing a rich ecosystem of tools to help manage complexity, containers offer great flexibility and control both during development and throughout their operational life cycle.

## Next up: Online Training on Containers, Kubernetes, and Rancher

Join an intro to Kubernetes and Rancher online training. In these free weekly training sessions, you’ll learn about containerization, the basics of Kubernetes, and how to install and manage Kubernetes workloads with Rancher. [Join the free training.](https://rancher.com/training)
