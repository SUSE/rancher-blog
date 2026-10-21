---
title: "What’s new in Rancher v1.6.11?"
date: 2017-11-17T11:30:00
slug: "whats-new-in-rancher-v1-6-11"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: []
content_type: "release"
draft: true
migration:
  wp_id: 87285
  original_url: "https://www.suse.com/c/rancher_blog/whats-new-in-rancher-v1-6-11/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher v1.6.11 release notes"
  redirect_target: "rancher.com/blog (hub)"
---

Let’s explore the new software and features in the latest release of

Rancher, which you can use by running

the `rancher/server:v1.6.11`{.markup–code .markup–p-code} image. Check

our documentation on [Installing Rancher Server](https://rancher.com/docs/rancher/v1.6/en/installing-rancher/installing-server/) if you need help running Rancher.

**NOTE:** Keep in mind that Rancher v1.6.11 is tagged as **latest**,

which means it’s not ready for production use. Our current, stable

version recommended for use in production is Rancher v1.6.10.

## Kubernetes

### Kubernetes 1.8.3

We’ve added Kubernetes 1.8.3 to this release. For all the information on

new features and improvements in Kubernetes 1.8, see the [release blog post](http://blog.kubernetes.io/2017/09/kubernetes-18-security-workloads-and.html). This update also allows you to run

**Docker 1.12.6**, **1.13.1**, and **17.03.2**, as Kubernetes 1.8

supports these versions.

### Azure Cloud Provider Support

In our Kubernetes 1.8.3 catalog item, it is possible to [configure Azure as a cloud provider](https://rancher.com/docs/rancher/v1.6/en/kubernetes/providers/#azure) for Kubernetes. This means you can:

- Use Azure Load Balancer by using `type: LoadBalancer`{.markup–code

  .markup–p-code}
- Use Azure Blob/Managed Disks by

  specifying `kind: StorageClass`{.markup–code

  .markup–p-code} and `kind: PersistentVolumeClaim`{.markup–code

  .markup–p-code}
- Mount Azure File share by using `azureFile`{.markup–code

  .markup–p-code} inside a `volumes`{.markup–code

  .markup–p-code} definition.

### Ability to Change Subnet for Kubernetes

In previous configurations, the Kubernetes subnet was hardcoded

to `10.43.0.0/16`{.markup–code .markup–p-code}. Now parameterized, you

can configure all the parameters to your liking.

![](https://cdn-images-1.medium.com/max/1600/1*5J-Pqb9oRf64_eixYVDZ3Q.png)

## Rancher/Cattle

### Docker

The latest stable version, **Docker 17.09**, is supported when using

Cattle orchestration.

### Draining Connections on Load-Balanced Services

Are you getting `HTTP Bad Gateway (502)`{.markup–code

.markup–p-code} errors when upgrading a load-balanced service? Rancher

v1.6.11 comes with a load balancer that can drain connections before

stopping the container. Inside the load-balanced service definition

in `rancher-compose.yml`{.markup–code .markup–p-code}, it is now

possible to specify `drain_timeout_ms`{.markup–code .markup–p-code} as

an amount of milliseconds to wait before stopping the container. [Check out the Rancher Docs](https://rancher.com/docs/rancher/v1.6/en/cattle/adding-load-balancers/#draining-target-connections-for-a-load-balancer) for more information.

### Clustered MySQL Support

We’ve had a large number of requests to be able to use Rancher with a

clustered MySQL setup which requires a primary key on all tables, like

Percona XtraDB

with `pxc_strict_mode = ENFORCING or MASTER`{.markup–code

.markup–p-code} or some cloud solutions. By

adding `--db-strict-enforcing`{.markup–code .markup–p-code} to

the `docker run`{.markup–code .markup–p-code} command, you can now use

those clustered databases as database for Rancher.

### Prune Services No Longer Specified in Rancher CLI

The Rancher CLI v0.6.5 now compares the specified services in the

current stack to those in the new stack. If a service is no longer

specified in the new stack, it will be removed when you

use `rancher up --prune`{.markup–code .markup–p-code}.

### Infrastructure Services Updates & Fixes

Here’s a quick mention of some great improvements to infrastructure

services:

- [GitHub issue 9957](https://github.com/rancher/rancher/issues/9957) — We’ve applied CPU restrictions to the

  metadata container, which should help in the events of scaling up.

  Before, the load on the systems could get really high which could

  impact the services running on it.
- [GitHub issue 9971](https://github.com/rancher/rancher/issues/9971) — This is a huge improvement on the IPsec side.

  Tunnels that were interrupted would not recover after a certain

  period of time, but in this release we included retry logic to

  re-establish those connections.

## Final Note

Hopefully, you all enjoy the new, improved stuff on which the team has

been working hard. This post includes a subset; read the [full release notes](https://forums.rancher.com/t/rancher-release-v1-6-11/7792) to see what else is new and improved. You can also

subscribe to the Rancher Forums announcements so you get a notification

every time there is a new release. For Kubernetes users, be aware of

[this bug](https://github.com/kubernetes/kubernetes/issues/53644) that

will restart all containers when you upgrade to version 1.8. If you run

into any issues, you can ask a question on the [Rancher Forums](https://forums.rancher.com/),

jump on our [Rancher Users Slack](https://slack.rancher.io/) channel, or [file an issue on GitHub](https://github.com/rancher/rancher/issues/new).
