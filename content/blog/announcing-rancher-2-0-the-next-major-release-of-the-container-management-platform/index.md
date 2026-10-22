---
title: "Announcing Rancher 2.0: the next major release of the container management platform"
date: 2017-09-26T09:00:00
slug: "announcing-rancher-2-0-the-next-major-release-of-the-container-management-platform"
author: "Rancher Admin"
products: ["Rancher Manager"]
tags: ["multi-cluster"]
content_type: "release"
draft: false
migration:
  wp_id: 85797
  original_url: "https://www.suse.com/c/rancher_blog/announcing-rancher-2-0-the-next-major-release-of-the-container-management-platform/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.0 tech preview announcement"
  redirect_target: ""
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)

Update: Rancher 2.0 Tech Preview has since gone to GA. Read the announcement [here](/blog/announcing-rancher-2-0-ga/).

[[![Rancher 2.0
logo](images/rancher_blog_Pasted-image-at-2017_09_25-07_20-PM-300x136.png)](https://rancher.com/rancher2-0)

We achieved another
significant milestone today at Rancher Labs. After months of hard work,
our engineering team released a technology preview of the [Rancher
2.0](https://rancher.com/rancher2-0) container management
platform.] Rancher 2.0 builds on the
tremendous momentum of market-leading Rancher 1.x container management
software. Since we shipped Rancher 1.0 in March 2016, Rancher server and
Rancher agent have been downloaded over 60 million times. There are now
over ten thousand live deployments of Rancher world-wide, and over 100
paying customers. Almost every day, happy open source users and
customers tell us how Rancher makes it easy for them to run Docker and
Kubernetes in production. I would like to thank our users who motivate
us to make Rancher software better, and I would especially like to thank
our customers who help fund the continuing development of Rancher
software!

Rancher 1.0 included an
easy-to-use container orchestration framework called Cattle and
supported a variety of industry-standard container orchestrators,
including Swarm, Mesos, and Kubernetes. Rancher users loved the idea of
adopting a management platform that gave them the choice of container
orchestration frameworks.

In the last year,
however, the growth of Kubernetes has far outpaced other orchestrators.
Rancher users are increasingly demanding a better user experience and
more functionality on top of Kubernetes. We have, therefore, decided to
reengineer Rancher 2.0 to take advantage of the power of Kubernetes by
rebasing the popular Rancher experience (known as Cattle) on Kubernetes.
With Rancher 2.0:

1. Cattle users retain the same easy-to-use experience and can
   additionally take advantage of the power of Kubernetes orchestration
   engine, with its rich infrastructure plugins, enhanced RBAC, and
   cloud native ecosystem services.
2. Kubernetes users gain access to unique Rancher user experience and
   the Rancher application catalog.

## Our Kubernetes journey

When we initially built Kubernetes support into Rancher in 2015, the
biggest challenge we faced was how to install and setup Kubernetes
clusters. Off-the-shelf Kubernetes scripts and tools were difficult to
use and were unreliable. Rancher made it easy to setup a Kubernetes
cluster with a click of a button. Better yet, Rancher allowed you to set
up Kubernetes clusters on any infrastructure, including public cloud,
vSphere clusters, and bare metal servers. As a result, Rancher quickly
became one of the most popular ways to launch Kubernetes
clusters.

In early 2016, numerous off-the-shelf and third-party installers for Kubernetes became
available. The challenge was no longer how to install and configure
Kubernetes, but how to operate and upgrade Kubernetes clusters on an
ongoing basis. We built a lot of features in Rancher to make it easy to
operate and upgrade Kubernetes clusters and its associated etcd
database.

By the end of 2016, we started to
notice that the value of Kubernetes operations software was rapidly
diminishing. Two factors contributed to this trend. First, open source
tools such as Kubernetes Operations (kops) have reached a level of
maturity that made it easy for many organizations to operate Kubernetes
on AWS. Second, Kubernetes-as-a-Service started to gain popularity. A
Google Cloud customer, for example, no longer wanted to setup and
operate their own clusters. They could rely on Google, the inventor of
the technology, to operate Kubernetes for
them.

### Kubernetes will be everywhere

In early 2016 I met Joe Beda, who founded the Kubernetes project at
Google and would later found the Kubernetes company Heptio. Joe painted
a vision of “Kubernetes Everywhere,” where Kubernetes can potentially
rival the ubiquity of IaaS.

The popularity of Kubernetes continues to rise in 2017. Its momentum is not slowing. We
have little doubt in the not so distant future, Kubernetes-as-a-Service
will be available from all infrastructure providers. When that happens,
Kubernetes will become the universal infrastructure standard. DevOps
team will no longer need to operate Kubernetes clusters themselves. The
only remaining challenge will be how to manage and utilize Kubernetes
clusters available from everywhere.

## Rancher 2.0: built on Kubernetes

Rancher 2.0 is a complete container management platform built on
Kubernetes. The following figure illustrates the capabilities of
Rancher.

![Rancher 2.0
capabilities](images/rancher_blog_Rancher-2.0.png)

Unlike Rancher 1.0, Rancher server 2.0 includes an embedded Kubernetes master. This
means as soon as you start Rancher using, for example, the
command

```
docker run -d -p 8080:8080 rancher/server
```

you immediately have a Kubernetes cluster up and running. You don’t
need to perform further steps to create your first Kubernetes cluster.
From then on, every host you add will automatically have a Kubelet
installed and be part of a Kubernetes
cluster.

You can create additional clusters using the same embedded Kubernetes master. We have built a custom
multi-tenant Kubernetes API server to minimize the resources required
for multiple Kubernetes clusters.

We envision a future where Kubernetes-as-a-service will become the norm,
and it will become increasingly less common to use the embedded
Kubernetes master. Rancher 2.0 allows you to import and manage
Kubernetes clusters powered by cloud providers like Google Container
Engine (GKE) and Kubernetes clusters, which are built using other tools
such as kops.

### A single point of control and visibility across multiple clusters

!Rancher 2.0
Technical
Architecture

Read the technical architecture paper for more details on the Rancher 2.0 enhancements. An IT administrator can create several
Kubernetes clusters using the embedded Kubernetes master or import
several existing Kubernetes clusters, and then use Rancher as a single
point of control and management for multiple
clusters.

Let us use a concrete example to illustrate how an IT administrator can leverage centralized RBAC and
authentication capabilities in Rancher. Imagine an enterprise IT
organization decides to use Google Container Engine (GKE) as the
standard platform to deploy containerized applications. GKE requires
every user to have a Google account, which is not the standard practice
in most enterprise organizations. With Rancher, the IT admin can import
a GKE clusters into Rancher using a single service account. Other users
can then be authenticated using the organization’s existing
ActiveDirectory credentials.

### A redesigned UI

So many users have told us they really enjoyed using Rancher UI, and we
decided to make it even better in 2.0! We love working on the UI and we
love making it better. The 2.0 UI presents a simple container view by
default, making it very easy for anyone with rudimentary understanding
of containers to get started with Kubernetes. Advanced users still have
access to kubectl and Kubernetes dashboard. The application catalog
experience is further enhanced so that you can not only deploy
applications with a single click, you can now easily access and manage
applications after you deploy them. The 2.0 UI scales to many more
containers, services, and hosts. The 2.0 UI is highly responsive. If you
liked 1.x UI, you will like 2.0 UI even
better.

### Product demo

The following demo provides an overview of all the cool new features in
Rancher 2.0:

[![Rancher 2.0 demo
video](images/rancher_blog_Pasted-image-at-2017_09_25-07_36-PM.png)](https://youtu.be/Ma6FsuWI2Nc)

You can find details on how to quickly get started with Rancher 2.0 [here](https://rancher.com/docs/rancher/v2.x/en/quick-start-guide/).

### More to come in the future

What we released today is an early technology preview. There’s still
lots of unfinished work. We are still busy fixing bugs and adding
features like HA deployment, RBAC and authentication, integrated CI/CD,
monitoring, and logging, etc. We will be shipping new releases
frequently. Stay tuned.

If you would like to learn more details about the technologies and features in Rancher
2.0, join us for our October online meetup. You can sign up
[[here](https://info.rancher.com/october-2017-meetup)].

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)
