---
title: "VMware vs Docker Comparison"
date: 2019-03-07T09:04:00
slug: "vmware-vs-docker-comparison"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_storage.svg"
products: ["Docker/containers (generic)"]
tags: ["virtualization"]
content_type: "explainer"
draft: true
migration:
  wp_id: 85847
  original_url: "https://www.suse.com/c/rancher_blog/vmware-vs-docker-comparison/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Generic dated comparison"
  redirect_target: "https://www.rancher.com/blog/"
---

## Introduction

Servers are expensive. And in single-application installations, most servers spend the majority of their time waiting. Making the most of these expensive assets led to virtualization, and making the most of virtualization has led to multiple options for virtualizing applications.

[VMware](https://www.vmware.com/) and [Docker](https://www.docker.com/) offer competing methods for virtualizing applications. Both technologies work to make the most of limited hardware resources, but they do so in significantly different ways. This post will help you understand how they differ and how those differences affect which scenarios each is best suited for. In particular, we’ll take a brief look at how each works, what the differences mean for the application and the deploying team, and how those differences can have an impact on operations, security, and application performance.

This article on VMware vs Docker is aimed at both IT operations and application development leaders who want to expand the options in their deployment toolkit. The information will help those leaders make more informed decisions and explain those decisions to colleagues and executives.

## The Limits of Virtualization

VMware is a company with a wide variety of products, from those that virtualize a single application to those that manage entire data centers or clouds. In this article, we use “VMware” to refer to VMware vSphere, used to virtualize entire operating systems; many different operating systems, from various Linux distributions to Windows Server can be virtualized on a single physical server.

VMware is a type-1 hypervisor, meaning it sits between the virtualized operating system and the server hardware; a number of different operating systems can run on a single VMware installation, with OS-specific applications running on each OS instance.

Docker is a system for orchestrating, or managing, application containers. An application container virtualizes an application and the software libraries, services, and operating system components required to run it. All of the Docker containers in a deployment will run on a single operating system because they’ll share commonly used resources from that operating system. Sharing the resources means that the application container is much smaller than the full virtualized operating system created in VMware. That smaller software image in a container can typically be created much more quickly than the VMware operating system image — on the scale of seconds rather than minutes.

The key question for the deployment team deciding on VMware vs Docker is why virtualization is being considered in the first place. If the point of the shift is at the operating system level — to provide each user or user population with its own operating environment while requiring as few physical servers as possible — then VMware is the logical choice. If the focus is on the application, with the operating system hidden or irrelevant to the user, then Docker containers become a realistic option for deployment.

## The Scale of Reuse

How much of each application do you want to reuse? The methods and scales of resource sharing are different for VMware and Docker containers, as one reuses images of operating systems while the other shares functions and resources from a single image. Those differences can translate to huge storage and memory requirements for applications.

Each time VMware creates a instance of an operating system, it creates a full copy of that operating system. All of the components of the operating system, and any resources used by applications running within the instance, are used only within that particular instance — there is no sharing among running operating systems. This means that there can be incredible customization of the environment within each operating system and applications can be run without concern about effecting (or being effected by) applications running in other virtual operating systems.

When a Docker container is created, it is a unique instance of the application with all of the libraries and code the application depends on included. While the application code is bundled within the container image, the application relies on — and is managed by — the host system’s kernel. This reduces the resources required to run containers and allows them to start very quickly.

Docker’s speed at creating new instances of an application makes it a solution commonly used in the development environment, where quickly launching, testing, and deleting copies of an application can make for much greater efficiencies. VMware’s ability to author a single “golden copy” of a fully patched and updated operating system and then use that image to create every new instance makes it popular in enterprise production deployments.

In both VMware and Docker containers, a “master copy” of the original environment is created and used to deploy multiple copies. The question for the operations team is whether the resource efficiency of Docker matches the needs of the application and the user base, or whether those needs require a unique copy of the operating system to be launched and deployed for each instance.

## Automation as a Principle

While the processes of creating and tearing down operating system images can be automated, automation is baked into the very heart of Docker. Orchestration, as part of the DevOps toolbox, is a major differentiator for Docker containers versus VMware.

Docker is itself the orchestration mechanism for creating new application instances on demand and then shutting them down when the requirement ends. There are API integrations that allow Docker to be controlled by a number of different automation systems. And for large computing environments that use Docker containers, additional layers of automation and management have been developed. One well-known platform is Kubernetes, which was developed to manage clusters of Docker containers that may be spread across many different servers.

VMware has a wide variety of automation tools as well, but those tools are, when discussing the vSphere family of products, responsible for creating new instances of operating systems, not applications. This means that the time to create an entirely new operating system image must be considered when planning rapid-response cloud and virtual system application environments. VMware can certainly work to support those environments; it’s used in many commercial operations to do just that. But it requires additional applications or frameworks to automate and orchestrate the process, adding complexity and expense to the solution.

It’s important to note that both Docker containers and VMware can operate quite successfully without automation. When it comes to a commercial installation, though, each becomes much more powerful when the tasks of creating and deleting new operating system and application instances are controlled by software rather than human hands. From rapid response to increased user demand, to large-scale automated application testing, system automation is important. Knowing what’s required for that automation is critical when deciding between technologies.

## Separation — or Not

If speed of deployment and execution or limitations on resource usage aren’t critical differentiators for your deployments, then hard separation between applications and instances might be. Just as orchestration is baked into Docker, separation is baked into VMware.

Each instance of an operating system virtualized under VMware is a complete operating system image running on hardware resources that are not shared logically with any other instance of the operating system. VMware partitions the hardware resources in ways that make each operating system instance believe that it’s the only OS running on the server.

This means that, barring a critical hypervisor vulnerability, there is no realistic way for an application running on one virtual server to reach across into another virtual server for data or resources. It also means that things can go awfully, terribly wrong in one virtual server and it can be shut down without endangering the operation of any of the other virtual servers running under VMware.

While proponents of Docker have spoken of similar separation being part of the container system’s architecture, recent vulnerability reports (such as [CVE-2019-5736](https://nvd.nist.gov/vuln/detail/CVE-2019-5736)) indicate that Docker’s separation might not be as complete as operational IT specialists would hope.

Separation is not as high of a priority for Docker containers as it is for VMware operating system instances. Application containers will share resources; and where there is sharing, there are limits on separation.

## Conclusion

There are significant differences between the virtualization and deployment of VMware and Docker, each with its uses. Readers should now have a basic understanding of the basic nature and capability of each platform and of the factors that could make each preferable in a given situation.

Where speed of deployment and most effective use of limited resources are the highest priorities, Docker containers show a great deal of strength. In situations like development groups or the rapid iteration of a fully functioning [DevOps environment](https://rancher.com/introducing-containers-devops-processes-five-considerations/), containers can be tremendously valuable.

If security and stability are critically important in your production environment, VMware offers both. For both Docker containers and VMware, multiple products are available to extend their functionality through automation, orchestration, and other functions.

You can find more information on deploying Docker [in this blog post](https://rancher.com/top-5-challenges-with-deploying-container-in-production/). The article presents both best practices and hands-on details for putting the platforms in the field, as well as information on how to include each within a DevOps methodology.

### Sign up for online training

To go deeper and understand how you can manage complex container applications using Kubernetes, a container orchestration system, and Rancher, [join](https://rancher.com/training) our weekly online training sessions. These free online training classes cover essential container orchestration and management concepts through live discussion and demonstrations.
