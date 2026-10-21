---
title: "Container Ecosystem Trends You Need to Know"
date: 2017-05-02T10:16:00
slug: "container-ecosystem-trends-you-need-to-know"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["developer-experience"]
content_type: "explainer"
draft: true
migration:
  wp_id: 86582
  original_url: "https://www.suse.com/c/rancher_blog/container-ecosystem-trends-you-need-to-know/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Swarm and Mesos era trends"
  redirect_target: "https://rancher.com/blog (hub)"
---

Since Docker launched in 2013, it has brought a level of excitement and

innovation to software development that’s contagious. It has rallied

support from every corner—enterprises to startups, developers to IT

folk, plus the open source community, ISVs, the biggest public cloud

vendors, and every tool across the software stack. Since the launch of

Docker, many major milestones have served to advance the container

revolution. Let’s look at some of them.

#### Container Orchestration Options

Getting started with your first container is fairly simple. All it takes

is your laptop and a Docker client. However, running a microservices app

is a whole other beast. The most difficult part is in creating,

managing, and automating clusters of ephemeral containers. The first

major tool to address this challenge was Mesos with its Marathon

orchestrator. Having powered distributed infrastructure even before

Docker, Marathon is in use in production workloads at Twitter, and in

other large-scale web applications. The next orchestration tool to gain

prominence was Kubernetes. In fact, today, Kubernetes leads the pack of

Docker orchestration tools because of how extensible it is. It supports

a broad list of programming languages, infrastructure options, and

enjoys tremendous support from the container ecosystem. It isolates the

application layer from the infrastructure layer, thus enabling true

portability across multiple cloud vendors, and infrastructure setups.

Docker Swarm, which joined the container orchestration party late, has

considerable ground to cover to catch up, and initial signs point to

[the battle already shifting the way of Kubernetes](http://www.infoworld.com/article/3118345/cloud-computing/why-kubernetes-is-winning-the-container-war.html),

even though Swarm is the easiest to get started with, and is well

integrated with the rest of the Docker platform. Orchestration is key to

the adoption and success of containers in the enterprise. Though neither

of these three are bad options, you should consider [which best suits your needs](https://rancher.com/comparing-rancher-orchestration-engine-options/).

#### Container Security is Improving Fast

Containers started out with weak isolation defaults. This has been

changing with time. One of the key developments related to container

security is the emergence of multiple capable container registries. A

registry stores and scans container images and repositories for

vulnerabilities. This is an important part of [Docker security](https://www.suse.com/c/six-essential-docker-security-best-practices-for-safe-containers/), as

publicly available repositories from unverified publishers are a big

security threat. This is one of the downsides of an open ecosystem where

container images are shared easily. But having security checks in place

using registries mitigates this risk. Docker Hub is the default and most

popular container registry that most Docker users get started with. The

major IaaS providers have their own container registries. This makes

sense, especially if you’re heavily invested in AWS, Azure, or Google

Cloud. They come with the default repository scanning, more mature

access controls, and a suite of other tools for networking, storage, and

monitoring. Apart from this, third-party registries like Quay, and

GitLab container registry are also gaining popularity. The options for

registries are more numerous than orchestration tools, and the market is

wide open. Apart from registries, third-party container security

services like [TwistLock](https://www.twistlock.com/) and [Aqua Security](https://www.aquasec.com/) provide security beyond the

defaults.

#### Native Docker clients for Windows and Mac

Docker was initially a Linux-only technology that depended on special

features built into the Linux kernel (those features were available only

on Linux, not other Unix-like kernels). If you wanted to run Docker on

Windows or a Mac, you had to use a virtual machine engine like

VirtualBox and a Linux-based virtual machine for hosting your Docker

environment. This setup was handy for developers who wanted to test

Docker apps on Windows or Mac machines, but it was not practical as a

Docker server deployment solution. Things changed in early 2016 with the

release of [native Docker support for Windows](https://blog.docker.com/2016/09/build-your-first-docker-windows-server-container/).

This was a major development as a lot of enterprise workloads run on

Windows Server. The demand to use Docker in these environments was

strong. For now, there are still some major limitations to Docker when

running natively on Windows. Networking is not yet fully implemented,

and only Windows Server 2016 and Windows 10 are supported. But the fact

that Docker has gone Windows-native opens up a host of new opportunities

for Docker in the Windows ecosystem.

#### Built-in vs. Open Source Docker Components

Docker, Inc. has built enterprise offerings (including Docker

Datacenter, which is now integrated into Docker’s new Enterprise Edition

platform), and they’re comprised of components from Docker itself,

including the Swarm orchestrator, which is not built into Docker Engine.

Docker’s interest in using its own tools to build a container stack,

rather than partnering with other organizations in the container

ecosystem, initially raised some concerns that Docker would ignore

community standards. There was even [talk last August](https://thenewstack.io/docker-fork-talk-split-now-table/) of

forking Docker because of these concerns. (The fork never happened.)

More recently, these tensions have calmed as Docker has taken steps to

assure customers that it isn’t out to monopolize the industry. Its

active contributions to the [CNCF](https://www.cncf.io/), including most

recently the open sourcing of the underlying containerd technology, are

steps in this direction. And at DockerCon last month, the company moved

to make its main project more modular and accessible to the community by

transferring code to the [Moby Project](https://mobyproject.org/) and

introducing [LinuxKit](https://github.com/linuxkit/linuxkit) (you can

read how these changes impact Rancher Labs, its products, and its users

[here](https://rancher.com/rancher-moby-project/) and

[here](https://rancher.com/dockercon-2017-thought-impressions/)). To be

sure, Docker still has its critics. But the Docker technology stack is

now more broadly open and integrated with the rest of the ecosystem than

it was a year ago.

#### Conclusion

The container ecosystem is still in flux with improvements and changes

happening by the day. New standards are being put in place as we figure

out what Docker means for applications across all types of

organizations. The trends highlighted in this post are indicators of a

fast-maturing ecosystem. How Docker and the various vendors in this

space progress from here is something to keep an eye on. *Twain began his career at Google, where, among other things, he was involved in technical support for the AdWords team. His work involved reviewing stack traces, resolving issues affecting both customers and the Support team, and handling escalations. Later, he built branded social media applications and automation scripts to help startups better manage their marketing operations. Today, as a technology journalist, he helps IT magazines and startups change the way teams build and ship applications.*
