---
title: "Container Security Tools Breakdown"
date: 2017-08-01T10:16:00
slug: "container-security-tools-breakdown"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["security"]
content_type: "explainer"
draft: true
migration:
  wp_id: 86592
  original_url: "https://www.suse.com/c/rancher_blog/container-security-tools-breakdown/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2017 tool cheatsheet"
  redirect_target: "https://rancher.com/blog (hub)"
---

Container security was initially a big obstacle to many organizations in

adopting Docker. However, that has changed over the past year, as many

open source projects, startups, cloud vendors, and even Docker itself

have stepped up to the challenge by creating new solutions for hardening

Docker environments. Today, there is a wide range of security tools that

cater to every aspect of the container lifecycle. Docker security tools

fall into these categories:

- **Kernel security tools:** These tools have their origins in the

  work of the open source Linux community. They have been inherited by

  container systems like Docker as foundational security tools at the

  kernel level.
- **Image scanning tools:** Docker Hub is the most popular container

  registry, but there are many others, too. Most registries now have

  solutions for scanning container images for known vulnerabilities.
- **Orchestration security tools:** Kubernetes and Docker Swarm are

  the two most popular orchestrators, and their security features have

  been gaining strength over the past year.
- **Network security tools:** In a distributed system powered by

  containers, the network is more important than ever. Policy-based

  network security is gaining prominence over perimeter-based

  firewalls.
- **Security benchmark tools:** The Center for Internet Security (CIS)

  has provided guidelines for container security, which have been

  adopted by Docker Bench and similar benchmark security tools.
- **Security with CaaS platforms:** AWS ECS, GKE and other CaaS

  platforms build on the security features of their parent IaaS

  platform, and then add container-specific features or borrow

  security features from Docker or Kubernetes.
- **Purpose-built container security tools:** This is the most

  advanced option for [container security](https://www.suse.com/c/what-is-container-security/). In it, machine learning

  takes center stage as these tools look to build an intelligent

  solution to container security.

Here’s a cheatsheet of Docker security tools available as of mid-2017.

It’s organized according to which part of the Docker stack the tool

secures.

## Security tool

## What it does

#### Kernel security tools

[Namespaces](https://www.toptal.com/linux/separation-anxiety-isolating-your-system-with-linux-namespaces)

Isolates neighboring processes from each other. It limits what a

container can see, and thus prevents attacks from spreading.

[cgroups](http://man7.org/linux/man-pages/man7/cgroups.7.html)

Limits the resources used by a container. Restricts what a container can

use, and thus prevents infected containers from hogging all resources.

[SELinux](http://www.projectatomic.io/docs/docker-and-selinux/)

Provides access control to the kernel. It enforces mandatory access

control (MAC), which controls how containers access the kernel based on

policies.

[AppArmor](https://wiki.ubuntu.com/AppArmor)

Enables access controls on processes. Can be set to enforce policies, or

merely report on policy violations.

[Seccomp](https://docs.docker.com/engine/security/seccomp/)

Allows processes to interact with the kernel in a “secure” state, where

it can only make a few commands. If it goes beyond these commands, the

process is killed.

#### Image scanning tools

[Docker Hub Security Scanning](https://docs.docker.com/docker-cloud/builds/image-scan/)

Scans images that have been downloaded from Docker Hub against a list of

Common Vulnerabilities and Exposures (CVEs).

[Docker Content Trust](https://blog.docker.com/2015/08/content-trust-docker-1-8/)

Verifies images downloaded from third-party registries based on the

author. The author of an image can be an individual or an organization.

[Quay Security Scanner](https://coreos.com/quay-enterprise/docs/latest/security-scanning.html)

Powered by CoreOS Clair, this is Quay’s version of Docker Security

Scanning. It scans container images for vulnerabilities.

[AWS ECR](https://aws.amazon.com/ecr/)

Part of AWS ECS, ECR encrypts images at rest in S3, and in transit over

HTTPS. It Uses AWS IAM to manage access control to the registry.

#### Orchestration security tools

[Docker Swarm Secrets Management](https://blog.docker.com/2017/02/docker-secrets-management/)

Provides a safe way to store passwords, tokens and other confidential

data using Docker Swarm.

[Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

Secures containers and pods in a Kubernetes cluster. Provides access

control, and Linux kernel security modules like SELinux and AppArmor.

#### Network security tools

[Project Calico](https://www.projectcalico.org/)

Secures the container network by providing policy-based security that

ensures services can access only the services and resources they need

and not more.

[Weave](https://www.weave.works/)

Enforces policy-based security for the container network, and provides a

firewall for each container rather than firewalling the entire

environment.

[Canal](https://github.com/projectcalico/canal)

Integrates the security features of Project Calico and the connectivity

features of Flannel to provide a comprehensive networking solution for

containers.

#### Security benchmark tools

[Docker Bench](https://github.com/docker/docker-bench-security)

A script that checks containers in production against a list of

benchmarks created by the CIS (Center for Internet Security).

[Inspec](https://www.inspec.io/)

A test framework built by Chef that treats compliance and security as

code. It scans images, and has its own version of Docker Bench.

#### Security with CaaS platforms

[AWS ECS](https://aws.amazon.com/ecs/)

Runs containers inside a virtual machine, which provides the first layer

of security. Also adds AWS security features like IAM, security groups,

and network ACLs.

[Azure Container Service](https://azure.microsoft.com/en-us/services/container-service/)

Has its own Azure Container Registry for scanning images, and leverages

Azure’s default security features like IAM.

[GKE](https://cloud.google.com/container-engine/)

Adopts Kubernetes’ security features and adds some of its own Google

Cloud security features like IAM and RBAC.

#### Purpose-built container security tools

[Twistlock](https://www.twistlock.com/)

End-to-end security platform for containers. It leverages machine

learning to automatically profile applications.

[Aqua Security](https://www.aquasec.com/)

End-to-end security platform for containers. It provides a mature API

that can be easily extended.

[Anchore](https://anchore.com/)

Scans container images, and enforces security policies for container

platforms. Integrates with CI/CD workflows using Jenkins.

[NeuVector](http://neuvector.com/)

Secures container runtimes by enforcing policies for services. It can

automatically start and stop containers based on automated whitelists.

[Deepfence](http://deepfence.io/)

CI/CD integrated security tool that protects against known attacks.

[StackRox](https://www.stackrox.com/)

Container security tool that leverages machine learning to provide what

it calls “adaptive threat protection.”

[Tenable](https://www.tenable.com/products/tenable-io)

A hosted security solution that scans container images and even allows

enterprises to enforce security policies on their environments.

[Cavirin](https://www.cavirin.com/)

A continuous security assessment tool that scans for vulnerabilities

against the CIS benchmark, and more.

### Making Sense of the Docker Security Tool Landscape

![](images/rancher_blog_Kubernetes-Docker-Swarm-comparison-150x150.jpg) Compare architectures, feature

sets, and usability of Kubernetes and Docker Swarm. [Download the guide](https://info.rancher.com/comparing-kubernetes-swarm)

This is truly a diverse list of Docker security tools. What becomes

clear when we view this list is that [Docker security](https://www.suse.com/c/six-essential-docker-security-best-practices-for-safe-containers/) requires a

combination of many tools working together. Each tool has its own

strengths and focus areas. There are solutions available for every layer

of the container stack—kernel, registries, network, orchestration, and

CaaS platforms. And the best part is that most of these tools are great

at integrating with each other, or at least the most commonly used tools

in container workloads. By knowing each of the tools, and what makes

them unique from the others, you can ensure a bulletproof container

environment that can run production workloads at enterprise scale. That

was always the promise of Docker, and container security tools are

making that promise a reality. *Twain began his career at Google, where, among other things, he was involved in technical support for the AdWords team. His work involved reviewing stack traces, and resolving issues affecting both customers and the Support team, and handling escalations. Later, he built branded social media applications, and automation scripts to help startups better manage their marketing operations. Today, as a technology journalist he helps IT magazines, and startups change the way teams build and ship applications.*
