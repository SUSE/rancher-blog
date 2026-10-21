---
title: "Rancher 1.2 Is Now Available!"
date: 2016-12-01T11:14:00
slug: "rancher-1-2-is-now-available"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["networking", "storage"]
content_type: "release"
draft: true
migration:
  wp_id: 86877
  original_url: "https://www.suse.com/c/rancher_blog/rancher-1-2-is-now-available/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x release"
  redirect_target: "rancher.com/blog (hub)"
---

[![1-2](images/rancher_blog_1-2-300x123.png)](https://cdn.rancher.com/wp-content/uploads/2016/11/22172220/1-2.png)

\*Note: since this article has posted, we’ve released Rancher 1.2.1,

which addresses much of the feedback we have received on the initial

release. You can [read more about the v1.2.1 release on Github](https://github.com/rancher/rancher/releases/tag/v1.2.1). \* I am

very excited to announce the release of Rancher 1.2! This release goes

beyond the requisite support for the latest versions of Kubernetes,

Docker, and Docker Compose, and includes major enhancements to the

Rancher container management platform itself Rancher 1.2 fully supports

the latest storage and networking plugin frameworks (more on this

later), and introduces a new and simplified HA setup, a more flexible

configuration of Rancher’s HAProxy load balancer, and a new Rancher CLI.

We’ve also added SAML 2.0 support, resource scheduling, and numerous

improvements for performance and scale. This is a relatively large

release, with many more features outlined in the [release notes](https://github.com/rancher/rancher/releases/tag/v1.2.0). Out of

all these enhancements, there’s a few things that we’d like to

highlight:

####

#### Full support for container networking and storage plugin frameworks

Last year, Docker introduced Docker Volume plugins and libnetwork, while

Kubernetes opted for the Container Network Interface (CNI) and

FlexVolume frameworks. Since then, we’ve seen the container ecosystem

explode with implementations of all these plugin frameworks to allow

users to take advantage of the vast storage and network solutions out

there today. One of Rancher’s superpowers is enabling users to leverage

their tooling of choice across diverse infrastructure. With the release

of v1.2, Rancher supports CNI and is fully capable of leveraging any

vendor CNI network plugins, along with our own newly-rewritten IPSec and

VXLAN solutions for cross-host networking. Users can also create volumes

with any Docker Volume plugins scoped to the container, stack, or

environment. Plugins included with Rancher 1.2 are our newly-rewritten

support for NFS (which replaces ConvoyNFS), AWS EFS, and AWS EBS, with

more to come.

####

#### Modular, push-button, container-ready environments

While Rancher 1.2 provides users with the ability to distribute and

provide lifecycle management for storage and networking plugins, we are

also introducing the concept of custom environment templates. Networking

and storage plugins can now be incorporated as options in a customizable

template, which also includes options for orchestration engines,

external DNS, and health checks. This allows users to better organize

and manage services, and provides a straightforward, consistent, and

repeatable deployment of your infrastructure services. In the future, we

expect to expand the scope of environment templates to include

additional infrastructure services such as logging, monitoring, and

databases.

####

#### Faster, more frequent releases

Finally, when Rancher became generally available with v1.0 earlier this

year, our goal was to provide stable releases each quarter, with

bi-weekly pre-release snapshots for our open source community eager to

play with our latest enhancements. However, key components in Docker and

Kubernetes adhere to different release schedules, and our open source

community requires stable releases more frequently than each quarter. We

have decided that starting with v1.3, we will ship monthly stable

releases of Rancher. This means we will no longer ship pre-release

builds as we have in the past, though release candidates will be

available for download and test. We hope with this new release schedule,

we will be able to increase our agility to ship new features, remain

up-to-date with Docker and Kubernetes, and shorten the time between

stable releases for Rancher users that want to quickly take advantage of

new features and major fixes. We really could not have released Rancher

1.2 without the support of our customers and open source community so a

very BIG thank you for helping us with this release. We also have big

plans for 2017 and can’t wait to share that with you as soon as we can.

Stay tuned!

\*\*To see Rancher 1.2 in action, check out the recording of our December 2016 meetup
