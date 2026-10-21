---
title: "My First Impressions with SUSE Rancher Kubernetes Projects"
date: 2022-01-24T16:29:10
slug: "my-first-impressions-with-suse-rancher-kubernetes-projects"
author: "Andrés Valero"
image: "images/rancher_blog_kubernetes-everywhere-featured.png"
products: ["Other"]
tags: ["developer-experience"]
content_type: "opinion"
draft: false
migration:
  wp_id: 89692
  original_url: "https://www.suse.com/c/rancher_blog/my-first-impressions-with-suse-rancher-kubernetes-projects/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

I recently started working at SUSE. Before joining SUSE, my Kubernetes experience included vanilla Kubernetes, AKS and EKS but mostly OpenShift and Red Hat Advanced Cluster Management. I worked in technical pre-sales, so I knew about Rancher, K3s and RKE and their key features but I never spent time with them. When I joined SUSE, I started testing Rancher, Rancher Desktop, K3s, k3d and RKE2 and I had a great time with them. First things first, I will introduce you to these projects – from my perspective -- in case you are new to Kubernetes or if you do not know much about them.

## Our Kubernetes Lineup

**Rancher** is a platform for Kubernetes management that provides many features out of the box like cluster configuration at scale, a single pane of glass for managing your clusters, cluster lifecycle, RBAC, monitoring and more. It is lightweight, is easy to use and you can run it in a container if you want to test it. Deploying a cluster or importing one on Rancher and managing it from there is ridiculously easy. You can learn more and try it for yourself at <https://rancher.com/>.

**K3s** is a lightweight Kubernetes distribution perfect for edge and IoT that can run on x86 platforms and Arm. You can start using it in almost any Linux OS. It is also perfect for testing purposes, uses a variety of databases, from SQLite to ETCD, and can run as a single node cluster or in HA. Beyond edge and IoT use cases, K3s is also great for development and testing purposes. It is so light that can run on a Raspberry Pi and so easy that you can start using it by running “curl -sfL https://get.k3s.io | sh -”. To make it even better, there are some cool open source projects around it like [k3sup](https://github.com/alexellis/k3sup) that will make your life easier. More information can be found on <https://k3s.io>.

**k3d** is K3s containerized, and it is simply amazing. It can run almost anywhere -- you just need Docker running on the system where you want to run it. For instance, if you are using a Mac with an M1 processor, it is not easy to find a local testing Kubernetes distribution that works for you. However, k3d solves this and other challenges. To start testing your software locally, install the binary and run “k3d cluster create test-cluster” and k3d will start a single node cluster for you. k3d can be used in Linux, Windows and macOS. k3d can easily add more nodes to your cluster or even start a private registry locally for you; its simplicity is incredible. The good things you can get using k3d do not stop in k3d: there are other projects and tools around k3d like the VSCode extension [vscode-k3d](https://github.com/inercia/vscode-k3d/) or [AutoK3s](https://github.com/cnrancher/autok3s), which improves your experience with k3d. Do yourself a favor and check <https://k3d.io>. I´m serious -- do not wait any longer.

**Rancher Desktop** is yet another cool project. Rancher Desktop is an open source application for Linux, Windows or macOS. It provides Kubernetes and container management in a local environment and is perfect for development. You can use it with Moby (dockerd) or containerd. It supports the same operations as Docker Desktop, so you can build, push, pull and run containers. But it also can build a container image and push it to Kubernetes without a registry. It does not stop here. Rancher Desktop can be used in combination with developer tools like [Skaffold](https://skaffold.dev/), [VSCode](https://code.visualstudio.com/) or [Epinio](https://epinio.io/), turning your computer into an amazing development station. You may not know it yet, but you need to test it! Go to <https://rancherdesktop.io> and try it.

**RKE2** (also known as RKE Government) is a Kubernetes distribution based on K3s. It has all the good stuff coming from Kubernetes and the simplicity of use and low resource consumption of K3s but is focused on security and compliance

Since it is based on K3s, it is extremely easy to deploy and can run in any almost Linux distribution or in Windows (experimental state) -- so you can decide where to run it. You can use a script to deploy it, use rpm packages or just install the binary for the installation and the configuration. Visit  <https://github.com/rancher/rke2> or <https://docs.rke2.io> to check it out.

## Common Traits Make These Projects Great

During my tests, I found some common traits that, in my opinion, make them fantastic projects.

First, they can be used for testing or development purposes to production without surprises. This means that the very same code that you find in the git repo when you test them is the same code that you will use if you purchase a subscription, which provides support but not different code or features.

All of them are simple by design. Simple may sound bad, but in this case, it is not. behind each project has done an incredible job of focusing on usability and making their software incredibly easy to use.

All the projects we have discussed are incredibly low on resource consumption. For instance, K3s can run in Arm devices with 512 MB of RAM and 1as minimum requirements. In the case of RKE2, you can deploy it on hardware with 4CPU and 8 GB of RAM. It´s an enterprise Kubernetes distribution with a tiny blueprint!

We cannot forget about the openness; these projects are not only open because they are open source software but because they provide you with the freedom to use them in many different Operating Systems and processor architectures. Everything in SUSE is coded to be open and flexible; it’s all about making your life easier.

Finally, the community. For SUSE, community is key. We are aware that without a community using our software, we would be failing at our mission. There are a lot of events, training and content available for the community and around our open source projects. . It is easy to find information and other projects that will help you to deploy and consume the SUSE software. But most importantly, you will never be locked in. With a big community supporting the projects – all of which are CNCF compliant -- you are free to use the solutions that work best for you.

In conclusion, I had a lot of fun testing the SUSE Kubernetes stack. I learned that there are plenty of different options for different use cases that these projects can cover. You have the freedom and flexibility to use the combination that works for you since we will not push you to use a certain OS or hardware. I hope you will take the time to take some of these projects for a spin.

### I would love to invite you to join me in the [SUSE & Rancher Community](https://community.suse.com/) – a meetingplace for cloud native enthusiasts. Come and say hello and check out our upcoming events and classes (always free).
