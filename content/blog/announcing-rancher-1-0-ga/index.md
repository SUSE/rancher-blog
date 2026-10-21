---
title: "Announcing Rancher 1.0 GA"
date: 2016-03-29T09:00:00
slug: "announcing-rancher-1-0-ga"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["installation"]
content_type: "release"
draft: true
migration:
  wp_id: 85796
  original_url: "https://www.suse.com/c/rancher_blog/announcing-rancher-1-0-ga/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.0 GA, discontinued line"
  redirect_target: "rancher.com/blog (hub)"
---

![Rancher 1.0
Logo](images/rancher_blog_Rancher-1.0-Logo-300x110.png)Today we achieved a
major milestone by shipping Rancher 1.0, our first generally available
release. After more than one and a half years of development, Rancher
has reached the quality and feature completeness for production
deployment. We first unveiled a preview of Rancher to the world at the
November 2014 Amazon Re:invent conference. We followed that with a Beta
release in June 2015. I’d like to congratulate the entire Rancher
development team for this achievement.

As an open source project, Rancher was developed in close collaboration
with the user and developer community. Some of you have been with us
from the very beginning and have seen dramatic enhancements and changes
since our initial preview release. Some of you were even bold enough to
deploy Rancher in mission-critical production environments prior to our
GA release! Rancher simply would not be where it is today without your
feedback, suggestions, and contributions. With your help, Rancher has
now over a million downloads and over 2500 beta program participants.
We can’t thank our community enough and are looking forward to working
with each and every one of you as we continue to improve and shape
Rancher into the best container management platform.

In this blog post I would like to also reflect upon what we have built
by explaining what problems Rancher is designed to solve, how the
community is using Rancher in practice, why users find Rancher to be
uniquely suited for their applications, and how we plan to continue to
develop Rancher post 1.0 GA.

We’ve created a quick demo to introduce the new release.

###

The problem Rancher solves

Rancher is a complete and turn-key container management platform. As
organizations start to deploy Docker containers in production, the
immediate challenge becomes the integration of large collections of
open-source technologies. As illustrated in the following figure,
container management involves solving problems spanning across storage,
networking, monitoring, orchestration, and scheduling.

![container
management](images/rancher_blog_container-management.png)

Rancher develops, integrates, and distributes all of the technologies
necessary to run containers in production. At Rancher Labs, we integrate
and distribute market-leading container orchestration and scheduling
frameworks such as Docker Swarm and Kubernetes, while developing the
necessary app catalog, enterprise user management, access control,
container networking and storage technologies ourselves. The result is a
complete platform that offers superb developer and operator experience.
With Rancher, organizations no longer need to worry about keeping up
with and integrating a myriad of technologies from the fast-moving
container ecosystem. Instead, they deploy Rancher once and can then
focus on developing the applications that make their business better.

###

How organizations use Rancher

Most organizations today employ or are moving toward an agile software
development pipeline. As users adopt containers, tools like GitHub,
Jenkins, and Docker Hub solve the front-half of that pipeline. Users
deploy Rancher so that they can test, deploy, upgrade, and operate
containerized application on any public cloud or private data center.

![Container Devops
Pipeline](images/rancher_blog_Container-Devops-Pipeline.png)

###

Why Rancher is unique

We set out to build Rancher because we saw the need for a complete and
turn-key container management platform. The resulting product, Rancher,
has a number of unique qualities:

- **Open source**

  . Rancher is 100% open source. We believe leveraging the power of an
  open source community is the best way to build platform software,
  and we are confident that organizations will pay for enterprise
  support and thus help fund our development effort.
- **Easy to use**

  . Time and time again, developers have told us they love Rancher’s
  simple and intuitive experience which enables them to focus on
  building applications as opposed to having to build the underlying
  infrastructure software themselves.
- **Enterprise grade**

  . Rancher implements enterprise management features such as LDAP and
  AD integration, role based access control, unified infrastructure
  visibility and audit, and a unified application catalog.
- **Infrastructure agnostic**

  . Rancher runs on computing resources in the form of Linux servers,
  which are a commodity offered by all clouds and data centers.
  Rancher does not rely on proprietary features supported by one cloud
  provider and not others. Rancher builds a rich set of storage,
  networking, load balancing, DNS, and metadata services that work
  consistently for containers running on any cloud.
- **Support for both Swarm and Kubernetes**

  . Modern DevOps practices do not impose the choice of application
  frameworks across the organization. As a result different teams tend
  to choose their own container orchestration and scheduling
  frameworks. Rancher is the only container management platform today
  that can support both Swarm and Kubernetes.

###

What you can expect after 1.0

We are lucky to have passionate users and open source community members.
The community wants us to continue to improve networking and storage
features, implement richer enterprise-grade visibility and control
features, onboard and certify more application catalog entries, and
support additional container orchestration and scheduling frameworks.
You can get a good idea of what users and community members want by
looking at the Rancher [Forums](https://forums.rancher.com)

and the list of [open
issues](https://github.com/rancher/rancher/issues)

on Rancher’s GitHub page. With 1.0 behind us, you should expect the
feature development velocity to increase. While maintaining a stable
release branch, we will continue to release new features and
capabilities on an aggressive release schedule. Stay tuned!

To see Rancher 1.0 in action, join us this Wednesday at 1:00 pm Eastern
time for an Online Meetup on building your own Containers-as-a-Service
platform with Rancher 1.0. We’ll be joined by the container team at Sony
PlayStation, who will be sharing some of their experiences using
Rancher.
