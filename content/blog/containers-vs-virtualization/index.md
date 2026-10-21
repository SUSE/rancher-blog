---
title: "Containers vs. Virtualization"
date: 2019-09-10T18:16:44
slug: "containers-vs-virtualization"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["virtualization"]
content_type: "explainer"
draft: false
migration:
  wp_id: 87324
  original_url: "https://www.suse.com/c/rancher_blog/containers-vs-virtualization/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

## Introduction

Servers are expensive. And in single-application installations, most servers spend the majority of their time waiting. An attempt to make the most of these expensive assets led to the development of virtualization. In turn, making the most of virtualization has led to multiple options for virtualizing applications.

Hardware virtualization, like [VMware](https://www.vmware.com/), and process virtualization through containers, like [Docker](https://www.docker.com/), offer competing methods for virtualizing applications. Both technologies work to make the most of limited hardware resources, but they do so in significantly different ways. In this guide, we will help you understand how they differ and how those differences affect which scenarios each is best suited for. In particular, we’ll take a brief look at how each works, what the differences mean for the application and the deploying team, and how those differences can have an impact on operations, security, and application performance.

This article is aimed at both IT operations and application development leaders who want to expand the options in their deployment toolkit. The information will help those leaders make more informed decisions and explain those decisions to colleagues and executives.

## The Limits of Hardware Virtualization

Hardware virtualization virtualizes an entire computer system at the hardware level. The virtual computer can then be treated as if it were a physical machine, allowing you to install an operating system, control its resources, and perform work.

Hardware virtualization is managed by a *hypervisor* which is either installed directly on the host system or as an application within the host system’s operating system. The hypervisor is responsible for managing and allocating resources as well as creating and running the actual virtual machines.

To make a comparison, we can take a look at Docker. Docker is a system for orchestrating, or managing, application containers. An application container virtualizes an application and the software libraries, services, and operating system components required to run it. All of the Docker containers in a deployment will run on a single operating system because they’ll share commonly used resources from that operating system. Sharing the resources means that the application container is much smaller than the full virtualized operating system created with hardware virtualization. That smaller software image in a container can typically be created much more quickly than the virtual machine operating system image — on the scale of seconds rather than minutes.

The key question for the deployment team is why virtualization is being considered. If the point of the shift is at the operating system level — to provide each user or user population with its own operating environment while requiring as few physical servers as possible — then hardware virtualization is a logical choice. If the focus is on the application, with the operating system hidden or irrelevant to the user, then Docker or a similar container-based system becomes a realistic option for deployment.

## The Scale of Reuse

How much of each application do you want to reuse? The methods and scales of resource sharing are different for hardware virtualization and containers, as one reuses images of operating systems while the other shares functions and resources from a single image. Those differences can translate to huge storage and memory requirements for applications.

Each time a virtual machine manager creates a new guest machine, it creates a full copy of that operating system and marks certain resources for its use. All of the components of the operating system, and any resources used by applications running within the instance, are used only within that particular instance — there is no sharing among running operating systems. This means that there can be incredible customization of the environment within each operating system and applications can be run without concern about effecting (or being effected by) applications running in other virtual operating systems.

When a container is created, it is a unique instance of the application with all of the libraries and code the application depends on included. While the application code is bundled within the container image, the application relies on — and is managed by — the host system’s kernel. This reduces the resources required to run containers and allows them to start very quickly.

Docker’s speed at creating new instances of an application makes it a solution commonly used in the development environment, where quickly launching, testing, and deleting copies of an application can make for much greater efficiencies. Hardware virtualization’s ability to author a single “golden copy” of a fully patched and updated operating system and then use that image to create every new instance makes it popular in enterprise production deployments.

In both traditional virtualization and containers, a “master copy” of the original environment is created and used to deploy multiple copies. The question for the operations team is whether the resource efficiency of Docker matches the needs of the application and the user base, or whether those needs require a unique copy of the operating system to be launched and deployed for each instance.

## Automation as a Principle

While the processes of creating and tearing down operating system images can be automated, automation is baked into the very heart of Docker. Orchestration, as part of the DevOps toolbox, is a major differentiator for Docker containers versus hardware virtualization.

Docker is itself the orchestration mechanism for creating new application instances on demand and then shutting them down when the requirement ends. There are API integrations that allow Docker to be controlled by a number of different automation systems. And for large computing environments that use Docker containers, additional layers of automation and management have been developed. One well-known platform is Kubernetes, which was developed to manage clusters of Docker containers that may be spread across many different servers.

Virtual machines have a wide variety of automation tools as well, but those tools are typically responsible for creating new instances of operating systems, not applications. This means that the time to create an entirely new operating system image must be considered when planning rapid-response cloud and virtual system application environments. Hardware virtualization can certainly work to support those environments; it’s used in many commercial operations to do just that. But it requires additional applications or frameworks to automate and orchestrate the process, adding complexity and expense to the solution.

It’s important to note that both Docker containers and hardware virtualization can operate quite successfully without automation. When it comes to a commercial installation, though, each becomes much more powerful when the tasks of creating and deleting new operating system and application instances are controlled by software rather than human hands. From rapid response to increased user demand, to large-scale automated application testing, system automation is important. Knowing what’s required for that automation is critical when deciding between technologies.

## Separation — or Not

If speed of deployment and execution or limitations on resource usage aren’t critical differentiators for your deployments, then hard separation between applications and instances might be. Just as orchestration is baked into Docker, separation is baked into hardware virtualization solutions.

Each instance of an operating system under hardware virtualization is a complete operating system image running on hardware resources that are not shared logically with any other instance of the operating system. Virtual machines partitions the hardware resources in ways that make each operating system instance believe that it’s the only OS running on the server.

This means that, barring a critical hypervisor vulnerability, there is no realistic way for an application running on one virtual server to reach across into another virtual server for data or resources. It also means that things can go awfully, terribly wrong in one virtual server and it can be shut down without endangering the operation of any of the other virtual servers running on the hypervisor.

While proponents of Docker have spoken of similar separation being part of the container system’s architecture, recent vulnerability reports (such as [CVE-2019-5736](https://nvd.nist.gov/vuln/detail/CVE-2019-5736)) indicate that Docker’s separation might not be as complete as operational IT specialists would hope.

Separation is not as high of a priority for Docker containers as it is for hardware virtualization. Application containers will share resources; and where there is sharing, there are limits on separation.

## Conclusion

There are significant differences between the virtualization and deployment of hardware virtualization and Docker, each with its uses. Readers should now have a basic understanding of the basic nature and capability of each platform and of the factors that could make each preferable in a given situation.

Where speed of deployment and most effective use of limited resources are the highest priorities, Docker containers show a great deal of strength. In situations like development groups or the rapid iteration of a fully functioning DevOps environment, containers can be tremendously valuable.

If security and stability are critically important in your production environment, hardware virtualization offers both. For both Docker containers and virtual machines, multiple products are available to extend their functionality through automation, orchestration, and other functions
