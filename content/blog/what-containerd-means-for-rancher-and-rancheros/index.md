---
title: "What containerd means for Rancher and RancherOS"
date: 2017-06-20T10:16:00
slug: "what-containerd-means-for-rancher-and-rancheros"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["installation"]
content_type: "opinion"
draft: true
migration:
  wp_id: 86597
  original_url: "https://www.suse.com/c/rancher_blog/what-containerd-means-for-rancher-and-rancheros/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RancherOS and Rancher 1.x containerd plans"
  redirect_target: "https://rancher.com/blog (hub)"
---

containerd is an industry-standard core container runtime that
was [initially
released](https://blog.docker.com/2015/12/containerd-daemon-to-control-runc/)
by Docker Inc. in December 2015 and [contributed to
CNCF](https://blog.docker.com/2017/03/containerd-joins-cncf/) in March
2017. We’ve received a number of questions about the project, so I
thought I would provide you my perspective as well as some preliminary
thoughts on how how Rancher Labs will leverage it.

## Docker, Kubernetes, and containerd

The containerd project represents an important step in the evolution of
the Docker platform. In the beginning, the Docker engine was quite
simple. It merely consisted of the minimum support required to run
Docker images on a single host. Over the last few years, however, the
Docker Engine has evolved significantly. The Docker engine now includes
sophisticated support for cluster management, multi-host networking, and
scheduling. Today, Docker is actually closer to a platform like
Kubernetes, even though Kubernetes was created to manage Docker.
containerd is a simple container runtime built for the sole purpose of
running Docker images on a single host. It is designed to be embedded in
larger systems like Docker and Kubernetes, which add higher-level
capabilities such as scheduling and orchestration.

## Rancher and containerd

[Rancher](https://rancher.com/rancher/) manages Docker and
[Kubernetes](https://rancher.com/kubernetes/). It is a complete container
management platform, which:

1. Enables users to create multiple Docker Swarm and Kubernetes
   clusters (called “environments”)
2. Ensures users can create environments on any infrastructure,
   including public cloud, private cloud, or data centers
3. Includes a [certified Kubernetes
   distribution](https://rancher.com/kubernetes/), and automatically
   manages the install, upgrade, and on-going operation of Kubernetes
   clusters
4. Implements a powerful set of management capabilities such as user
   authentication, RBAC, and security credentials and certificates
5. Integrates with a wide variety of CI/CD, monitoring, and log
   aggregation systems
6. Enables users to easily deploy and upgrade pre-packaged applications
   from a catalog

As the following figure shows, the Rancher platform’s role will not
change when Docker and Kubernetes integrate with containerd. Rancher
will continue to manage Docker and Kubernetes as it does today.
![containerd and
Rancher](images/rancher_blog_containerd1-1024x398.png)

## RancherOS and containerd

RancherOS is a small footprint Linux distribution built for the sole
purpose of running Docker containers. It contains two Docker daemons:
system Docker and user Docker. System Docker plays the role of the init
system (like `systemd`) and runs system services such as udev and DHCP.
User Docker runs application containers. In the future, containerd will
take over as system Docker. containerd provides sufficient capabilities
to function as an init program. A smaller system Docker will result in
an even slimmer RancherOS distro and a more robust system.
![containerd
RancherOS](images/rancher_blog_containerd2-1024x531.png)

## Product Roadmap

Work is underway to build containerd 1.0 and the Kubernetes CRI
(Container Runtime Interface) plug-in for containerd. Rancher and
RancherOS will take advantage of containerd as it becomes ready for
production. Stay tuned for product announcements.
