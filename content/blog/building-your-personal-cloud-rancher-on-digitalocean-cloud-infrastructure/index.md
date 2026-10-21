---
title: "Building Your Personal Cloud: Rancher on DigitalOcean Cloud Infrastructure"
date: 2017-10-12T10:15:00
slug: "building-your-personal-cloud-rancher-on-digitalocean-cloud-infrastructure"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["cloud", "installation"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86533
  original_url: "https://www.suse.com/c/rancher_blog/building-your-personal-cloud-rancher-on-digitalocean-cloud-infrastructure/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x on DigitalOcean"
  redirect_target: "docs.rancher.com"
---

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)

I’m not gonna tell you how to live your life—that’s for your doctor
to do. What I am gonna tell you is how a beautifully poetic dynamic duo
of DevOps delightfulness can make your next project shine brighter than
the sun and give you more marketable skills. We live in a world where
everything is becoming more modular. From your phone to your Keurig
coffee maker to your USB type-C laptop setup, modularity allows you to
do more and rearrange components of your life to best suit your needs.

Why should your software be any different?

Containerization is the basis
of modular software development, and it really opens your eyes to how
easy and [properly cost
scaling](https://rancher.com/using-containers-cost-effective-cloud/)
deployment can be when your applications remain agnostic to the OS,
hardware, and network on which they run. Of course, the modern software
developer now builds services to run on top of containers and, although
services offer a [neat
solution](https://rancher.com/focus-services-not-containers/) to a lot of
problems introduced through basic containers, deploying services out
into the world through our favorite cloud platforms can be difficult to
say the least. I needed a cloud that suited all of my conditions: it’s
at the right price point, has the features, instances, extra services I
love to use, and doesn’t tie me down to one particular company. I
should be able to pick and choose from all the cloud providers what kind
of instance I want, utilize the massive array of regions that spans
every popular cloud provider from New York to Australia, and even manage
DNS across multiple instances on multiple clouds.

The nature of the
cloud market is interesting because, for most developers, we pick one
provider and tend to stick with it. A provider may change its policies
or jack up its prices whenever it wants, and we’re forced to go along
with it because migrating to a new cloud takes a lot of hours and
effort.

What if there were some platform, independent of a cloud
provider, that would let *us, the developers,* be agnostic to a cloud
provider and focus on the product?

[Enter Rancher](https://rancher.com/).
![The Rancher Logo: an Open Source Kubernetes Multi Cluster Management Platform](images/rancher_blog_Rancher-Logo-Final-300x180.png) Rancher is a
cloud-agnostic deployment engineering platform for services. It offers a
one-stop shop for all your deployment needs. Rancher provides a handful
of orchestration options including Kubernetes, Swarm, and its own
Cattle, all of which allow you to deploy your application, your way, on
your cloud. With features like multihost spawning via cloud API,
baked-in networking with load-balancing, and terminal-free interaction
with your hosts, Rancher is a compelling platform for managing your
cloud-based project. DigitalOcean is my favorite infrastructure cloud. I
say this wholeheartedly because they provide sensible options for
sensible people who aren’t trying to run their own Netflix on someone
else’s hardware.

In modern development, the only thing that should be
persistent is your database and configurations, where DigitalOcean’s new
[Spaces](https://www.digitalocean.com/community/tutorials/an-introduction-to-digitalocean-spaces)
really shines. Managing and monitoring container hosts through the
dashboard of your DigitalOcean account can be a challenge, however, as
you really don’t know what is consuming resources or what workloads
look like unless you SSH into each of your hosts and check the Docker
stats. While this may be doable for a project running only one or two
containers on a single host, what happens if you want to scale it at
all? How do you handle the monitoring, stratified deployment, and
scaling of your services? Sure, DigitalOcean offers some load-balancing
techniques, but that’s on a machine level, not on a service level.
Running Rancher on top of DigitalOcean sticks the infrastructure behind
a layer of abstraction that you, the developer, don’t need to worry
about. Instead of managing hosts, all you have to worry about are your
services.

### So, why do Rancher and DigitalOcean complement each other so well? Where’s the magic, and why does it matter?

Rancher’s design philosophy is such that no matter how the hardware
configuration changes, you can move services around and they’ll stay
alive as long as one host is available. Rancher aims to allow quick
changes to hardware architecture without compromising on availability.
Provisioning a running host can happen in under three minutes in most
cases. This sounds pretty darn fast but, in reality, bringing up the
host on your cloud provider can take a while if it’s not built to let
you rapidly spin up instances through an API. Thankfully, DigitalOcean
offers SSD-based droplets that you can spin up in under 30 seconds.
Yeah, that’s right. Under 30 seconds. That means you can deploy a new
host and scale your service onto that host in under five minutes, and
you can perform upgrades and infrastructure changes with ease. The
DigitalOcean API is an incredibly powerful tool for DevOps. Not only can
you create an instance from the API, but you can generate and upload
secure SSH keys for each host, configure DNS for the load balancers, and
even reverse the process, destroying droplets and getting rid of DNS
records and SSH keys.

The power of DigitalOcean’s API enables Rancher
to automate all of these tasks for you in a simple interface. When you
want to create a new droplet, all you have to specify is the number,
size, hostnames (which can follow patterns for multi-droplet creations),
and Linux image. All the SSH key distribution, provisioning, networking,
and security is automated by Rancher in the few minutes it takes to spin
up and adopt an instance. Rancher offers a single interface to connect
with all of your clouds, so the process is more or less the same no
matter what infrastructure you’re running.

Essentially, learning
Rancher through an affordable and quick cloud provider like DigitalOcean
enables you to deploy on AWS, Google Cloud Platform, OpenStack, and any
other production infrastructure that industry leaders are running in
their datacenters. For now, though, let’s stick with DigitalOcean. In
an upcoming post, I’ll continue guiding you through the process of
getting started with DigitalOcean on Rancher.

Next, we’ll cover
[Terraforming your
environment](https://rancher.com/terraforming-rancher-deployments-digital-ocean/)
so spin up and spin down are as easy as `terraform < apply|destroy >`.

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)
