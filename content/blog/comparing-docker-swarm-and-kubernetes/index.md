---
title: "Comparing Docker Swarm and Kubernetes"
date: 2017-08-07T10:16:00
slug: "comparing-docker-swarm-and-kubernetes"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["developer-experience"]
content_type: "explainer"
draft: true
migration:
  wp_id: 86573
  original_url: "https://www.suse.com/c/rancher_blog/comparing-docker-swarm-and-kubernetes/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Docker Swarm comparison with Kubernetes 1.3"
  redirect_target: "https://rancher.com/blog (hub)"
---

For teams building and deploying containerized applications using

Docker, selecting the right orchestration engine can be a challenge.

The decision affects not only deployment and management, but how

applications are architected as well. DevOps teams need to think about

details like how data is persisted, how containerized services

communicate with one another, load balancing, service discovery,

packaging and more. It turns out that the choice of orchestration

engine is critical to all these areas. While Rancher has the nice

property that it can support multiple orchestration engines

concurrently, choosing the right solution is still important. Rather

than attempting to *boil the ocean* by looking at many orchestrators, we

chose to look at two likely to be on the short list for most

organizations - **Kubernetes** and **Docker Swarm**.

## Evolving at a rapid clip

To say these frameworks are evolving quickly is an understatement. In

the just the past year there have been four major releases of Docker

(1.12, 1.13, 17.03 and 17.06) with dozens of new features and a

wholesale change to the Swarm architecture. Kubernetes has been

evolving at an even more frenetic pace. Since Kubernetes 1.3 was

introduced in July of 2016 there have been four additional major

releases and no less than a dozen minor releases. Kubernetes is at

version 1.7.2 at the time of this writing with 1.8.0 now in alpha 2.

Check out the Kubernetes

[changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md)

to get a sense of the pace of development. \*Comparing Kubernetes and

Docker Swarm is a little like trying to compare two Rocket ships

speeding along on separate trajectories. By the time you catch up with

one and get close enough to see what’s happening, the other is in a

whole different place! \*

## Points of comparison

Despite the challenges posed by their rapid evolution, we decided to

take a crack at comparing Swarm and Kubernetes in some detail, taking a

fresh look at new capabilities in each solution. At a high-level the

two solutions do broadly similar things, but they differ substantially

in their implementation. We took both solutions out for a test drive

(using Rancher running in AWS), got into the weeds, and compared them

systematically in these areas:

- Architecture
- User experience
- Ease-of-use
- Networking model
- Storage management
- Scheduling
- Service discovery
- Load balancing
- Healthchecks
- Scalability

## Lots for DevOps teams to ponder

Both Swarm and Kubernetes are impressive, capable solutions. Depending

on their needs, organizations could reasonably choose either solution.

If you are new to one solution or the other, understanding the

strengths and weaknesses of different solutions, and differences in how

they are implemented, can help you make a more informed decision. Swarm

is impressive for its simplicity and seamless integration with Docker.

For those experienced with Docker, evolving to use Swarm is simple.

Swarm’s new DAB format for multi-host, multi-service applications

extends naturally from docker-compose, and the Swarm command set is now

part of Docker Engine, so administrators face a minimal learning curve.

Customers considering larger, more complex deployments will want to look

at Kubernetes. Docker users will need to invest a little more time to

get familiar with Kubernetes, but even if you don’t use all the features

out of the gate, the features are there for good reason. Kubernetes has

its own discrete command set, API and an architecture that is discrete

from Docker. For Kubernetes, the watchword is flexibility. Kubernetes

is extensible and configurable and can be deployed in a variety of ways.

It introduces concepts like Pods, Replica Sets and Stateful Sets not

found in Swarm along with features like autoscaling. While Kubernetes

is a little more complex to learn and master, for users with more

sophisticated requirements, Kubernetes has the potential to simplify

management by reducing the need for ongoing manual interventions.

## About the whitepaper

Our comparison was done using Rancher’s container management framework

to deploy separate environments for Docker Swarm and Kubernetes. Rather

than focus on Rancher however, comparisons are made at the level of

Swarm and Kubernetes themselves. Whether you are using Rancher or a

different container management framework, the observations should still

be useful. Included in the paper are:

- Detailed comparisons between Kubernetes and Swarm
- Considerations when deploying both orchestrators in Rancher
- Considerations for application designers
- High-level guidance on what orchestrator to consider when

**[Download the free whitepaper](https://info.rancher.com/comparing-kubernetes-swarm) for an up to date look at Kubernetes and Docker Swarm.** As always, we

appreciate your thoughts and feedback!
