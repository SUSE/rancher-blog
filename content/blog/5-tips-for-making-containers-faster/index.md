---
title: "5 Tips for Making Containers Faster"
date: 2017-11-05T08:59:00
slug: "5-tips-for-making-containers-faster"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["developer-experience"]
content_type: "explainer"
draft: false
migration:
  wp_id: 85785
  original_url: "https://www.suse.com/c/rancher_blog/5-tips-for-making-containers-faster/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Take a deep dive into Best Practices in Kubernetes NetworkingFrom overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options.[Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/)

One of the selling points of containers is that containerized
applications are generally faster to deploy than virtual machines.
Containers also usually perform better. But just because containers are
faster by default than alternative infrastructure doesn’t mean that
there are not ways to make them even faster. You can go beyond the
defaults by optimizing Docker container image build time, performance
and resource consumption. This post explains how.

## Defining “Faster”

Before we delve into Docker optimization tips, let me first explain what
I mean when I write about making containers “faster.” Within the context
of a conversation about Docker, the word *faster* can have several
meanings. It can refer to the execution speed of a process or an
application that runs inside a container. It can refer to image build
time. It can refer to the time it takes to deploy an application, or to
push code through the entire delivery pipeline. In this post, I’ll
consider all of these angles by discussing approaches to making Docker
faster in multiple ways.

## Make Docker Faster

The following strategies can help make Docker containers faster.

### Take a Minimalist Approach to Images

The more code you have inside your image, the longer it will take to
build the image, and for users to download the image. In addition,
code-heavy containers may run sub-optimally because they consume more
resources than required. For all of these reasons, you should strive to
keep the code that goes into your container images to the bare minimum
that is required for whatever your image is supposed to do. In some
cases, designing minimalist container images may require you to
rearchitect your application itself. Bloated applications will always
suffer from slow deployment and weak performance, whether you deploy
them in containers or in something else. You should also resist the
temptation, when writing your Dockerfile, to add services or commands
that are not strictly necessary. For example, if your application
doesn’t need an SSH server, don’t include one. For another example,
avoid running `apt-get upgrade` if you don’t need to.

### Use a Minimalist Operating System

One of the greatest benefits of containers as compared to virtual
machines is that containers don’t require you to duplicate an entire
operating system to host an application. To take advantage of this
feature to greatest effect, you should host your images with an
operating system that does everything you need, and nothing more. Your
operating system shouldn’t include extra services or data if they do not
advance the mission of your Docker environment. Anything extra is bloat,
which will undercut the efficiency of your containers. Fortunately, you
don’t have to build your own minimalist operating system for Docker.
Plenty of pre-built Linux distributions with small footprints are
available for hosting Docker, such as
[RancherOS](https://rancher.com/rancher-os/).

### Optimize Build Time

Image build time is often the biggest kink in your continuous delivery
pipeline. When you have to wait a long time for your Docker images to
build, you delay your entire delivery process. One way to speed image
build time is to use registry mirrors. Mirrors make builds faster by
reducing the amount of time required to download components when
building an image. Combining multiple RUN commands into a single command
also improves build time for images because it reduces the number of
layers in your image, which improves build speed, and optimizes the
image size to boot. [Docker’s build cache
feature](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#build-cache)
is another useful way to improve build speed. The cache allows you to
take advantage of existing cached images, rather than building each
image from scratch. Finally, creating minimalist images, as discussed
above, will speed build time, too. The less you have to build, the
faster your builds will be.

### Use a Containers-as-a-Service Platform

For staff at many organizations, the greatest obstacle to deploying
containers quickly and efficiently results from the complexity of
building and managing a containerized environment themselves. This is
why using a Containers-as-a-Service platform, or CaaS, can be handy.
With a CaaS, you get preconfigured environments, as well as deployment
and management tools. A CaaS helps to prevent the bottlenecks that would
otherwise slow down a continuous delivery chain.

### Use Resource Quotas

By default, each container can consume as many resources as it wants.
This may not always be ideal because poorly designed or malfunctioning
containers can eat up resources, thereby making other containers run
slowly. To help prevent this problem, you can [set
quotas](https://docs.docker.com/engine/admin/resource_constraints/) on
each container’s compute, memory and disk I/O allotments. Just keep in
mind, of course, that misconfigured quotas can cause serious performance
problems, too; you therefore need to ensure that your containers are
able to access the resources they require.

## Conclusion

Even if your containers are already fast, you can probably make them
faster. Optimizing what goes into your images, improving image build
time, avoiding operating system bloat, taking advantage of CaaS and
setting resource quotas are all ways to improve the overall speed and
efficiency of your Docker environment.

### About the Author

![](images/rancher_blog_Screen-Shot-2017-10-23-at-10.24.04-AM-300x268.png)Chris Tozzi has
worked as a journalist and Linux systems administrator. He has
particular interests in open source, agile infrastructure and
networking. He is Senior Editor of content and a DevOps Analyst at
Fixate IO.

Take a deep dive into Best Practices in Kubernetes NetworkingFrom overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options.[Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/)
