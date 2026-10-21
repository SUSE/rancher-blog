---
title: "DockerCon 2017 – Thoughts and Impressions"
date: 2017-04-21T11:28:00
slug: "dockercon-2017-thoughts-and-impressions"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["installation"]
content_type: "event"
draft: true
migration:
  wp_id: 87221
  original_url: "https://www.suse.com/c/rancher_blog/dockercon-2017-thoughts-and-impressions/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "DockerCon 2017 recap"
  redirect_target: "https://rancher.com/blog (hub)"
---

We’ve just returned from DockerCon 2017, which was a fantastic
experience. I thought I’d share some of my thoughts and impressions of
the event, including my perspective on some of the key announcements,
while they are still fresh in my mind.

## **New open source projects**

Container adoption for production environments is very real. The
keynotes on both days included some exciting announcements that should
further accelerate adoption in the enterprise as well as foster
innovation in the open source community. Day 1 included demos of
multi-stage docker builds (introduced in Docker 17.04), which is an
incredibly cool feature. During the keynote, Docker also announced two
new open source projects for system builders who want to create their
own modular container-based systems. With the Moby Project, Docker has
essentially created a Fedora/RHEL split that enables users to
build container-based systems from a component library and reference
blueprints. Darren Shepherd, Chief Architect at Rancher Labs, provides
some more background and explanation about the Moby Project and how it
affects Rancher, RancherOS, and our users
[here](https://rancher.com/rancher-moby-project/). The second project,
LinuxKit, provides a way to build customized Linux subsystems for each
type of container, which is useful if you want to assemble your own
Linux distribution for specialized hardware or features. LinuxKit is
based on containerd, which Docker contributed to the CNCF project in
March of this year. Containerd gives each LinuxKit subsystem its own
Linux kernel and allows each system daemon or system service to be
allocated its own container. Docker’s announcement of LinuxKit generated
a lot of interest for RancherOS. Our [GA
announcement](https://rancher.com/press-release-rancheros-ga/) turned out
to be extremely well-timed! We’ve been working on the RancherOS for a
couple of years, so it’s great to see how much interest there is in
small footprint Linux operating systems. However, I would like to make
sure it’s clear that LinuxKit and RancherOS serve different purposes.
LinuxKit enables you to build your own static Linux distro. RancherOS
is a minimal stable Linux made from containers for containers, which
uses cloud-init to run container services. We plan to evaluate whether
we can use LinuxKit to build some RancherOS components.

## **Container orchestration**

In 2016, we invested a great deal to make Rancher the only product in
the market that supports multiple orchestrators. This has been a unique
differentiating attribute for the Rancher container management platform,
and has brought us a great deal of customer interest. As the
orchestrators become more complex, it is increasingly more important for
us to the provide high-quality support that our customers demand. I was
happy to see that the [Rancher Labs’
announcement](https://rancher.com/rancher-labs-partners-docker-ee/) to
embed Docker Enterprise Edition (EE) into the Rancher platform as well
as provide support was included in the keynote. This is an important
announcement for Rancher Labs as bundling Docker EE enables us to focus
our engineering efforts on Kubernetes, while still being able to offer
enterprise-grade support to Swarm customers. There was understandably
less talk about Kubernetes at this show. Still, the opportunity for
Kubernetes is very real. Last year the big challenge for Kubernetes was
how to set it up. The Rancher platform’s Kubernetes environment
addressed that problem beautifully. The big challenge this year,
however, is how to operate Kubernetes without a skilled SRE team.
Imagine being able to leave a Rancher Kubernetes environment running for
years without having to worry about host disconnecting, network
breaking, load balancer failures, or etcd problems! That’s what we’re
delivering this year. Many of Rancher users use Cattle, the integrated
container orchestration embedded within Rancher. Cattle is vitally
important as a bootstrap orchestrator for various infrastructure
services. We think of it more as a seamless extension of the “docker
run” experience than a complex orchestration framework with a steep
learning curve. We believe there is an opening for simple and
easy-to-use orchestration frameworks like Cattle.

## **Thanks for all the great feedback**

At previous DockerCon conferences many attendees heard about Rancher for
the first time. Most people I met at the booth this year have already
heard of Rancher and are already Rancher users. With over 33M downloads
Rancher is definitely gaining traction, and we were happy to receive so
much attention at the show. When we met with users and customers, while
the gave us plenty of compliments, they were also not shy about areas
they want Rancher to improve. By learning from our users and customers,
I have no doubt we can continue to improve the product in the coming
weeks and months. We will continue to delight our customers and users! I
also had a lot of conversations with storage industry people about
[Project Longhorn](https://rancher.com/microservices-block-storage/),
which we announced on Monday. The idea of microcontrollers for storage
resonated with many of them. Most application developers and operations
people, however, really just want to see a system that works better than
what they already have. Now that we have announced the project, the real
work begins. We intend to integrate Longhorn into Kubernetes and
Rancher, and demonstrate that it delivers unique value.

## **Rancher Labs at DockerCon**

Rancher Labs was a Gold Sponsor for DockerCon, and many attendees
stopped by our booth Monday evening through Wednesday afternoon to
request a demo or just to say hi. NetApp also had a demo in their booth
showing how to deploy nDVP using the Rancher catalog, which had a steady
stream of interest. The Rancher Labs team also spent some time in the
CNCF booth educating attendees on the value of the Foundation. During a
breakout session, Darren Shepherd, our Chief Architect, presented a
session titled “Using Containers Shouldn’t Be This Hard”. He spoke to
about 100 attendees about the complexities of using containers in
production and provided guidance on how to implement load balancers,
orchestrators, etc. We had multiple customers and users stop by our open
office hours on Tuesday afternoon. There were a variety of different
questions, from trouble shooting current implementations to discussing
support options. We also hosted guests from Japan at a Rancher JP
meetup, and many of you joined us to kick your heels up with Rancher
Labs and {code} by Dell EMC at Austin’s iconic Container Bar on Rainey
Street. This is a really exciting time for the Docker community. I look
forward to hearing about the next wave of innovations as well as sharing
some of our own at DockerCon Europe. We’ll see you in Copenhagen!
