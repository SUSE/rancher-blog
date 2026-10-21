---
title: "What is a CaaS? Containers as a Service, Defined"
date: 2017-10-17T10:15:00
slug: "what-is-a-caas-containers-as-a-service-defined"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_storage.svg"
products: ["Docker/containers (generic)"]
tags: ["cloud"]
content_type: "explainer"
draft: false
migration:
  wp_id: 86538
  original_url: "https://www.suse.com/c/rancher_blog/what-is-a-caas-containers-as-a-service-defined/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

When public clouds first began gaining popularity, it seemed that
providers were quick to append the phrase “as a service” to everything
imaginable, as a way of indicating that a given application, service, or
infrastructure component was designed to run in the cloud.

It should therefore come as no surprise that “Containers as a Service,” or CaaS,
refers to a cloud-based container environment. But there is a bit more
to the CaaS story than this. CaaS is not just a marketing fad. Below, I
explain what CaaS means, and why it’s valuable.

## CaaS Differentiators

Containers as a Service offerings are often about more than just giving
IT pros a way of running their containerized applications in the cloud.
Each cloud provider is free to create its own flavor of CaaS—and some
CaaS platforms don’t run in a major public cloud. There are two main
areas in which CaaS providers try to differentiate their offerings.
First, there is the user interface. On-premises container environments
tend to be managed through the Docker command line. However, some IT
pros prefer a GUI-based management interface over the command line. As
such, some cloud providers allow subscribers to point-and-click their
way through container creation and management.

A second key
differentiator between CaaS providers is orchestration, and the
supplementary services that are attached to the orchestration engine. A
provider may use an orchestration engine, for example, to achieve
automatic scaling for containerized workloads, based on the parameters
that the administrator has established. Similarly, a cloud provider’s
orchestration engine may be used to handle container lifecycle
management tasks, or the creation of container-related reports. It is
worth noting that public cloud container services can be somewhat rigid
with regard to orchestrator selection. Microsoft Azure, for example,
allows you to choose between DC/OS, Kubernetes, and Swarm. No other
selections are available. In contrast, other container management
platforms, such as Rancher, are designed to be modular rather than
limiting you to using a few pre-defined choices.

## The Advantages of Using CaaS

Many of the advantages that Containers as a Services brings to the table are similar to the
benefits of general container usage. However, there are at least two
extra benefits that CaaS provides. The first of these benefits is that
CaaS makes it much easier to run applications in the cloud than it might
otherwise be. Applications that were designed for on-premises use do not
always behave as expected when installed on a cloud-based virtual
machine. Because containers allow for true application portability,
however, it is possible to create an application container, test the
newly containerized application on-premises, and then upload the
application to the public cloud. The containerized application should
work in the same way in the cloud as it does on-premises. Another
advantage to using CaaS is that doing so allows organizations to achieve
a greater degree of agility. Agility is one of those overused IT
buzzwords that has kind of lost its meaning. However, I tend to think of
agility as the ability to roll out a new production workload as quickly
as possible. Given this definition, CaaS definitely delivers. Imagine
for a moment that an organization’s development staff is building a new
application, and that there is a pressing need for the application to be
rolled out quickly. The developers could containerize the application,
but what if the organization is not yet using containers in production?
Better still, what happens if the organization’s container environment
lacks the capacity to host the application? This is where CaaS really
shines. Public cloud providers usually let you deploy a container
environment with just a few mouse clicks. This eliminates time-consuming
tasks such as deploying container hosts, building clusters, or testing
the container infrastructure. Cloud providers use automation to
provision for their subscribers’ container environments that have been
proven to be configured correctly. This automation eliminates the
time-consuming setup and testing process, and therefore allows the
organization to begin rolling out containerized applications almost
immediately.

## Multi-Cloud Solutions

Although it is tempting to think of CaaS as solely being a service that
a cloud provider offers to its customers, it is becoming increasingly
common for organizations to host containers on multiple clouds. Doing so
can help with resilience to failure, and with load balancing. Yet
hosting containers on multiple clouds also introduces significant
challenges related to cross-cloud container management, and cross-cloud
workload scaling. These challenges can be addressed by using management
tools such as those from [Rancher](https://rancher.com/), which can
manage containers both on-premises and in the cloud.
