---
title: "Rancher Desktop 0.7 - Now with Docker CLI Support, The Ability To Run On Apple Silicon, and More"
date: 2021-12-16T16:32:44
slug: "rancher-desktop-0-7-now-with-docker-cli-support-the-ability-to-run-on-apple-silicon-and-more-2"
author: "Matt Farina"
image: "images/rancher-desktop.jpeg"
products: ["Rancher Desktop"]
tags: ["developer-experience"]
content_type: "release"
draft: false
migration:
  wp_id: 92853
  original_url: "https://www.suse.com/c/rancher_blog/rancher-desktop-0-7-now-with-docker-cli-support-the-ability-to-run-on-apple-silicon-and-more-2/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher Desktop 0.7 release"
  redirect_target: ""
---

The latest release of [Rancher Desktop](https://rancherdesktop.io/) brings two new features along with numerous bug fixes and other changes.

## Docker CLI / Moby / dockerd

Many people are familiar with the [Docker CLI](https://github.com/docker/cli). It has features that other container management CLI tools have not, yet, implemented. We wanted to support these features. Starting with Rancher Desktop 0.7, there is support for the Docker CLI.

![](https://media1-production-mightynetworks.imgix.net/asset/32373418/Screen_Shot_2021-12-14_at_5.19.49_PM.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

You can choose your runtime, which impacts if you can use nerdctl or docker for your CLI, when you start Rancher Desktop for the very first time. If you want to change it later, you can do so in the Kubernetes Settings.

The Docker CLI communicates over a socket to a container runtime other than containerd. This meant that Rancher Desktop needed to support a second container runtime. This happens through the use of [Moby](https://mobyproject.org/) and is similar to the way many popular Linux distributions provide Docker CLI support. Moby provides dockerd (the container runtime). Only one container runtime is in use at a time.

The socket needed for the runtime and CLI to communicate can be used by other tools, such as [k3d](https://k3d.io/). That means you can use k3d to manage multiple k3s environments.

![](https://media1-production-mightynetworks.imgix.net/asset/32443569/Screen_Shot_2021-12-16_at_9.41.37_AM.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

This second image shows the updated *Kubernetes Settings* screen with the new *Container Runtime* toggle. The first screenshot shows the styling in dark mode while this second screenshot shows the settings in light mode.

## Apple Silicon Support

Alongside the most recent round of updates to the Apple Macbook Pro laptops, Apple stopped shipping Intel based Macbook Pros. Apple is well into their transition to Apple Silicon based computers. To support that, Rancher Desktop now ships a build that runs on Apple Silicon.

This is the first version with support so there are some caveats. First, [Rosetta 2](https://en.wikipedia.org/wiki/Rosetta_%28software%29#Rosetta_2) is needed to run this version. There are some components that Rancher Desktop uses that aren't available with Apple Silicon builds. An environment that is completely native is in the roadmap. Second, cross building between amd64 and ARM isn't supported, yet. Running Rancher Desktop on Apple Silicon is an ARM based experience.

## Networking On Mac

There have been requests on Mac to have a routable IP address to the virtual machine where the containers and Kubernetes is running. As of v0.7.0, that is now possible.

## Linux Repositories

When we first released Linux support for Rancher Desktop, the RPMs and Debian packages were attached to the release on GitHub. This didn't provide a good means for installing and managing software using the typical methods on Linux. Starting with v0.7.0, there are now [repositories](https://software.opensuse.org/download.html?project=isv%3ARancher%3Astable&package=rancher-desktop) that you can use to install and update Rancher Desktop from.

There are some Linux Desktop environments that may have trouble with these repositories. In addition to the repositories, an [AppImage](https://download.opensuse.org/repositories/isv:/Rancher:/stable/AppImage/) is available of Rancher Desktop. This version currently has some limitations, such as a lack of a self update feature. We are working on it.

## Other Updates

In addition to these large changes there are a number of other small changes including:

- Helm has been updated to v3.7.2
- nerdctl, which has seen active development to add many new features, has been updated to v0.15
- Many small bugs have been fixed

## Next Steps

There are several next steps:

- Star [Rancher Desktop on GitHub](https://github.com/rancher-sandbox/rancher-desktop) to show that you like it. This is how we know you like it and want to see development continue.
- Install the [v0.7.0 release](https://github.com/rancher-sandbox/rancher-desktop/releases/tag/v0.7.0).
- Provide feedback in the [issue queue](https://github.com/rancher-sandbox/rancher-desktop/issues).
