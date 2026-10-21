---
title: "Migrate Your Windows 2003 Applications to Kubernetes"
date: 2020-02-18T09:53:00
slug: "migrate-your-windows-2003-applications-to-kubernetes"
author: "Rancher Admin"
image: "images/rancher_blog_Migrate-Kubernetes.png"
products: ["Kubernetes (generic)"]
tags: ["windows"]
content_type: "explainer"
draft: true
migration:
  wp_id: 86214
  original_url: "https://www.suse.com/c/rancher_blog/migrate-your-windows-2003-applications-to-kubernetes/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Windows 2003 and 2020-era Windows support"
  redirect_target: "rancher.com/blog (hub)"
---

## Introduction

There’s no one-size-fits-all migration path for moving legacy Windows applications to the cloud. These applications typically reside on either physical servers, virtual machines or on premises. While the goal is generally to rearchitect or redesign an application to leverage cloud-native services, it’s not always the answer. Re-architecting an existing application to a microservice architecture or to cloud native presents several challenges in terms of cost, complexity and application dependencies.

While there are major benefits to modernizing your application, many organizations still have existing services running on Windows 2003 Servers. Microsoft’s support withdrawal for Windows 2003 presents several challenges. For one, it’s forcing decisions about what to do with said application — especially given that Windows 2008 end of life isn’t far off.

Organizations want to move to a modern architecture to gain increased flexibility, security and availability in their applications. This is where containers provide the flexibility to modernize the applications and move it to cloud-native services. In this article, we’ll focus on applications that can move to containers – typically .Net, web, SQL and other applications that don’t have a dependency to run only on Windows 2003. You can move these applications to containers without code changes, making them portable for the future. And you’ll get the benefit of running the containers on Kubernetes, which provides orchestration, availability, increased resiliency and density.

**Note:** not all applications or services can run in containers. There are still core dependencies for some applications which will need to be addressed, such as database and storage requirements. In addition, the business needs to decide on the ongoing life of the application.

## Business Benefits of Moving to Kubernetes

There are some key business reasons for moving these applications to containers, including:

- Return on Investment
- Portability of older web-based services
- Increased application security
- Time for the business to re-evaluate existing applications

Now that Kubernetes supports Windows worker nodes, you can migrate legacy Windows applications to a modern architecture. Windows workers and Linux workers can co-exist within the same Kubernetes platform, allowing operations teams to use a common set of tools, practices and procedures.

## Step 1: Analyse Your Move From Windows to Kubernetes

Migrating a legacy Windows application to Kubernetes requires a significant amount of analysis and planning. However, some key practices are emerging. These include:

- **Break down** the application to its original form to understand what components are running, how they are running and their dependencies
- **Discover** what services the application provides and what calls it makes in terms of data, network and interlacing
- **Decouple** the data layer from the application
- **Determine** and map service dependencies
- **Test**, test and test again

## Step 2: Plan Your Move from Windows to Kubernetes

Migrating your Windows application to a containerized .Net-based platform is a multi-step process that requires some key decisions. The following high-level process provides some guidance on requirments to migrate legacy Windows systems to run on Kubernetes.

- **Determine** what operating system your container needs — either Server Core or Nano Server. The application’s dependencies will dictate this choice.
- **Follow compatibility guidelines.** Running Windows containers adds strict compatibility rules for the OS version of the host and the base image the container is running. They must run Windows 2019 because the container and the underlying host share a single kernel. Currently, (at the time of writing this article) only Server Process Isolation is supported. However, Hyper-V isolation is expected soon (timing unknown), which will assist in compatibility between the host and the container.
- **Package** your legacy application
- **Build out** your initial Docker-based container with the application package
- **Deploy** a new Docker container to a repository of your choice
- **Leverage** existing DevOps toolsets (CI/CD build and release pipelines)
- **Deploy** the new Windows Application to your Windows-supported Kubernetes environment
- **Test**, test and test again

## Key Outcomes of Moving Windows Applications to Kubernetes

By moving from Windows to Kubernetes, your legacy applications will share the benefits of your existing container-based applications. In addition, your Windows applications will benefit from the Kubernetes platform itself. What’s more, they can use additional tools and systems within the Kubernetes ecosystem, including security, service mesh, monitoring/alerting, etc.

Together, these benefits put you in a good position to make key decisions about your applications and develop a business use case. For applications that can’t be migrated, you still need to decide what to do with them, given the lack of support for the underlying Operating System. Since no further patches or security remediations available, your organizations is exposed to vulnerabilities and exploits. So the time to act is now.

## Key Takeaways for Migrating from Windows to Kubernetes

- Container-based solutions provide cost savings.
- Containers reduce dependencies and provide portability for applications.
- While Docker is the de facto standard for running Containers, Kubernetes is the de facto container orchestration engine.
- Kubernetes can host scalable, reliable and resilient Windows Containers–based applications alongside Linux-based applications.
- Organizations running a Kubernetes platform can integrate the legacy applications into their DevOps culture and toolsets.
- Leveraging native and ecosystem-based tools for Kubernetes increases security and adds extra layers of protection for legacy applications

## More Kubernetes Resources

Want to learn more about strategy and planning a Kubernetes move? [Get our white paper](https://more.suse.com/fy21-global-web-landing-page-how-to-build-enterprise-kubernetes-strategy): How to Build an Enterprise Kubernetes Strategy.
