---
title: "Comparison of Container Operating Systems (Container OS)"
date: 2019-04-16T09:05:00
slug: "comparison-of-container-operating-systems-container-os"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_containers.svg"
products: ["Docker/containers (generic)"]
tags: []
content_type: "explainer"
draft: true
migration:
  wp_id: 85857
  original_url: "https://www.suse.com/c/rancher_blog/comparison-of-container-operating-systems-container-os/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2019 OS landscape, RancherOS era"
  redirect_target: "https://www.rancher.com/blog/meet-elemental-cloud-native-os-management-in-kubernetes/"
---

## Introduction

Containers have rapidly become a necessary part of the modern data center. Containers can be built on any of a number of operating system foundations — so how do you choose one container os over another?

In the context of a container deployment, development managers need to know which operating system features and functions are critical to the applications being released and whether there are other factors — like manageability and configuration flexibility — that would lead an organization to choose one operating system over another.

How do the different operating systems compare in features and essential functionality? How do those differences affect the way that they will support applications? Those are the essential questions that we’ll be looking at through representative example of three broad types of OSes:

- Traditional, full-featured operating systems
- General purpose minimal operating systems
- Purpose-built, container-specific operating systems

In each category, we’ve chosen two examples that will represent all the distributions and products in the group.

After reading this article, IT managers should have a much clearer picture of the differences between the types of operating systems. They will have a better idea of why developers might choose one container OS over another for containerized applications, and why they might support or question those choices.

## Full-Featured Operating Systems

What does “full featured operating system” mean? And why, in the context of a container deployment, would full features matter? This section will look at why the same operating system that might be used in a traditional server deployment can be the best answer for a container platform.

The first thing to know is that these operating systems can do it all. If an application needs a feature or function, odds are that one of these will have it. That “be prepared” flexibility comes at a price, though: these operating systems require the most from the system when it comes to storage, memory, and CPU resources. Those features also increase the attack surface of the operating system, providing potential attackers with a great many more nooks and crannies in which to do their work. These are costs that are easily borne if those features are needed by the applications, but the price gets very high, very quickly, if only a small number of the features are required.

These full-featured operating systems may be most appropriate in an environment that sees multiple, diverse applications deployed in containers on top of a single OS instance. In those cases, the breadth of features may be the most economical way to support the fleet of apps.

### Ubuntu

Ubuntu has become the default operating system on server, cloud, and even desktop for many organizations. Well-supported by Canonical, Ubuntu is available in a wide variety of downloadable formats with the utility packages, shells, functions, and feature sets necessary for deployments supporting IoT, containers, servers, or clouds.

Ubuntu has moved into the space once occupied exclusively by Red Hat Linux: it’s a safe choice for enterprise deployments, with the support and reputation to make its selection one that most executive committees will see as “reasonable.” It’s important to remember, though, that reasonable does not translate to best in every circumstance — it’s still a big, full operating system with all that that implies.

### CentOS

Where Ubuntu has become the buttoned-up enterprise choice among full-featured operating systems, CentOS is the open-source, community-driven version of another “safe” choice – Red Hat. CentOS emphasizes community support and contribution to the expanding set of features and functions in the OS while still building on the stability of its Red Hat foundation. That’s not to say that CentOS isn’t used by large organizations — you’ll find it sitting on servers at national laboratories and major cloud providers. But Ubuntu tends to boast more rapid updates than CentOS, which includes packages that tend to be older, yet very well tested.

## Minimal Operating Systems

Containers came into being as collections of minimal functions brought together to create a complete application. What features found in “full” Linux distros are missing from these minimal operating systems — and does it matter to your application? From the other side of the equation, what are the advantages to basing applications on distributions stripped to the bare minimum?

The best answers lie at the intersection of application requirements and OS functionality. Without thoughtful preparation, the size and complexity advantages expected from minimal operating systems can be lost through the addition of individual utilities, functions, and applets required for specific applications.

This section looks at two distros, BusyBox and Alpine Linux, and the advantages they can bring in the right circumstances. The two operating systems are related — Alpine is based on BusyBox — but there are key differences that can lead a team to choose one over the other for particular deployments. Those differences involve not only specific capabilities, but the support community and ecosystem of each.

### BusyBox

BusyBox is useful for container deployments because it wasn’t designed with containers in mind. Dubbed by its developers as “the Swiss Army Knife of Embedded Linux,” BusyBox was intended as a single, small-footprint executable file that contained all the functionality required by most embedded applications. That forced it to take a very container-like approach to deployment before containers existed.

BusyBox can be deployed using Linux or other POSIX operating systems as its foundation and bundles them with many of the common Linux utilities in stripped-down form. The result is a compact, single-file executable that contains much of the functionality of a “full” Linux distro, though many of the functional options available in those full versions have been left out of BusyBox in the name of saved space.

### Alpine Linux

As mentioned, Alpine Linux is based on BusyBox, but it builds on the earlier distribution in both goal and detail. Where BusyBox is designed with a small footprint as its singular focus, Alpine Linux uses a hardened kernel to add security to the compact, simple goals of its predecessor.

Alpine Linux also makes it easier for developers to add functionality than does BusyBox. By basing its distribution on BusyBox and the musl library, Alpine Linux gives developers a head start on adding functionality and building compact distribution packages. This is a minimal OS capable of producing very small container images for deployment, and the hardened kernel makes it suitable for production, as well as development, deployment.

## Container Operating Systems

A container operating system arrives out of the box with automation and container orchestration built in. They are designed and built to be “host” operating systems — the operating system on which container OSes like Alpine and BusyBox are hosted. So why are they not the automatic choice for every container deployment?

Container operating systems are distinguished by not simply being software that supports containers, but software deployed using containers. An architecture that is “containers all the way down” can provide a level of customization for a deployment that is considerably more complex than a traditional OS deployment. On the other hand, for organizations early in their move to containers, or in application deployments pushing the limits of container architectures, an “all-container” architecture may be a bridge too far for management’s comfort.

Rancher OS and Container Linux are two of the principal options for those looking for container operating systems. Understanding what each brings to the table will help developers understand the advantages they possess, and the situations for which they are the only logical choice.

### RancherOS

Each process within RancherOS is run within a separate container managed by Docker. The optimization for and dependence upon Docker allows RancherOS to be very small with a very fast boot time. Beyond the basic performance benefits, though, there are deployment factors that may argue in favor of RancherOS.

RancherOS system services are defined and configured by Docker Compose. This reliance means that only the services needed for the application are loaded and deployed, further speeding and simplifying deployment. Deployment is simplified again through integration with cloud-init, which allows automated configuration and deployment on a wide-spread and high-speed basis.

### Container Linux

CoreOS’s Container Linux is designed for container deployment on a cloud-scale basis. Now part of Red Hat, Container Linux is optimized for cluster deployments across public or private cloud infrastructures.

Container Linux is deployed with the kernel and essential utilities in a single executable with all other utilities and functions deployed in containers.

Container Linux has long been in wide use, with support available for deploying across most public clouds. It’s acquisition by Red Hat has done nothing to slow its adoption and has made some organizations more comfortable with the idea of deployment on the platform. Container Linux is distributed with an open-source license and has an active developer community.

## Conclusion

Given the three broad types of operating systems available for container deployment, which container os should a development team choose? If the only purpose for a particular server is hosting containers, then container operating systems like RancherOS and Container Linux have a great deal to recommend them. Their automation, deployment speed, and consistent container architecture make them a logical choice for those looking to optimize a container hosting environment. Moving one level up to the operating systems for the containers themselves, the choices become more nuanced.

If there are both container and non-container applications to consider, then there’s no question that traditional Linux deployments like Ubuntu and CentOS can be used as a container platform. Their architecture and list of utilities and features will make them slower to boot and will require more system resources, but they can do the job if boot speed and minimal resource consumption aren’t key considerations.

In the middle lie the minimal operating systems like BusyBox and Alpine Linux. These can be solid container choices on their own but truly come into their own if there are resource-constrained non-container applications, such as those for the IoT, that must also be considered as part of the total application environment.

Understanding the difference between the capabilities and limitations of the different types of operating systems is critical for any productive OS platform discussion. With modern operating systems the real conversation shouldn’t then be around which OS will work, but around which will do the job most efficiently and effectively.

## Get started with RancherOS

RancherOS is a simplified Linux distribution built from containers, for containers. [Download the latest release](https://github.com/rancher/os/releases) and get started today.
