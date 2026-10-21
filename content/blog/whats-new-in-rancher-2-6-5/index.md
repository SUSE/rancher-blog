---
title: "What's New in Rancher 2.6.5?"
date: 2022-05-17T07:55:58
slug: "whats-new-in-rancher-2-6-5"
authors: ["William Jimenez"]
image: "images/rancher-logo-cow-blue-720x321-5532a813-e5d1-49c2-a682-bfc2a544421f-1.jpg"
products: ["Rancher Manager"]
tags: ["security"]
content_type: "release"
draft: false
migration:
  wp_id: 91606
  original_url: "https://www.suse.com/c/rancher_blog/whats-new-in-rancher-2-6-5/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.6.5 release notes"
  redirect_target: ""
---

With KubeCon underway, many of us in the cloud native community are looking forward to learning about the newest innovations from the companies we follow. At SUSE, we’ve been working hard to deliver some new enhancements to Rancher with our 2.6.5 version. I want to briefly take you through the highlights of this release and why we’re excited about these new additions.

## NeuVector integration

Security has always been a core value-add of the Rancher platform. One of the earliest benefits of Rancher was its ability to bridge enterprise authentication such as Active Directory to the Kubernetes RBAC API. And since then, we’ve continued to invest in technologies that add the security and controls that enterprises need to be successful with Kubernetes. And so, with this latest release, we’ve integrated the NeuVector UI with Rancher, allowing you to access it directly from a Rancher session. This is just the first of what I hope are many integrations between the two products. (Learn more about NeuVector 5.0, the latest release of our full lifecycle container security platform, in Glen Kosaka’s [blog post](https://www.suse.com/c/suse-neuvector-5-0-delivers-a-powerful-open-source-security-platform).)

## RKE2 provisioning is GA in Rancher 2.6.5

Rancher Kubernetes Engine 2 (or RKE2 for short) is our modern Kubernetes distro that is optimized for security and leverages the containerd runtime. It’s the close cousin to the original RKE distribution, so it will be familiar to those who started out with RKE yet refreshing in its novel approach. RKE2 has been available for some time now, but now with 2.6.5, provisioning of RKE2 in Rancher is moving from Beta to Generally Available. This is a huge milestone in the RKE2 journey and signals the product is ready for taking on bigger challenges in the Kubernetes ecosystem.

## Windows container support

Windows container support has been an area of special focus for the Rancher team this past year. We’ve increased our engineering investment and fostered collaborative relationships with other key contributors to the Windows k8s ecosystem. One of the products of that work has been RKE2 support for Windows is now GA in this release. A lot of work went into this, from adapting RKE2 to support the operating system differences to integrating and testing the Calico CNI stack. We are also releasing a new vSphere node driver to enable orchestration of Windows nodes running on VMware. Finally, we’re adding experimental Group Managed Service Account (gMSA) tooling to support the many .NET applications that are being containerized.

## Monitoring and observability

Monitoring and observability are a frequent ask from our customers. In particular, they want the ability to isolate metrics between teams using the same Kubernetes cluster. To better support this, we’ve added project-based monitoring with our v2 Monitoring framework. This allows teams to keep their metrics separate while using the latest in Rancher’s monitoring technology. You can find this feature in Rancher’s Apps and Marketplace under “Prometheus Federator.”

Thanks for taking the time to learn more about what we’ve been up to. The team at SUSE has enjoyed building these new features, and so we’d love to hear your feedback and learn more about how you use them. Be sure to let us know in the [Rancher Slack channel](https://slack.rancher.io/). And if you are at KubeCon this year, please stop by and say hi.

## [Want to give Rancher 2.6.5 a try? Get started here](https://github.com/rancher/rancher/releases).
