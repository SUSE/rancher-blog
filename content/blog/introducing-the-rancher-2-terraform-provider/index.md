---
title: "Introducing the Rancher 2 Terraform Provider"
date: 2019-05-16T09:42:00
slug: "introducing-the-rancher-2-terraform-provider"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images-resource-consumption.png"
products: ["Rancher Manager"]
tags: ["installation"]
content_type: "release"
draft: false
migration:
  wp_id: 85915
  original_url: "https://www.suse.com/c/rancher_blog/introducing-the-rancher-2-terraform-provider/"
  disposition: migrate
  commercial: false
  outdated_reason: "2019 Terraform provider announcement"
  redirect_target: ""
---

Infrastructure as code is an important methodology for ensuring that your distributed systems are treated as [cattle and not pets](https://devops.stackexchange.com/questions/653/what-is-the-definition-of-cattle-not-pets). Your Kubernetes and Rancher clusters are no different. You should be able to provision your Rancher clusters, your Kubernetes clusters, and all of your apps with automation.

Rancher provides a number of tools to spin up Rancher clusters. [RKE, or Rancher Kubernetes Engine,](https://rancher.com/docs/rke/latest/en/) allows you to spin up Kubernetes clusters via code. That’s why setting up RKE is the first step in [installing a Rancher HA cluster](https://rancher.com/docs/rancher/v2.x/en/installation/ha/). But what happens after installation is just as important.

You cluster will likely include [log aggregation](https://rancher.com/docs/rancher/v2.x/en/cluster-admin/tools/logging/), [RBAC](https://rancher.com/docs/rancher/v2.x/en/admin-settings/rbac/), [projects](https://rancher.com/docs/rancher/v2.x/en/project-admin/), and [monitoring](https://rancher.com/docs/rancher/v2.x/en/cluster-admin/tools/monitoring/). These all represent important configuration for a repeatably provisionable, production-ready cluster.

[Hashicorp’s Terraform](https://www.terraform.io/) is an incredibly useful tool to automate the creation of infrastructure and other system components. It’s syntax is easy to use and it is highly customizable with a plugable provider mode. The original [Terraform Provider for Rancher 1.x](https://www.terraform.io/docs/providers/rancher/index.html) was incredibly popular for automating state in Rancher 1.x. So not long after we released 2.x, we started work on a Terraform provider to go with it.

This week, Hashicorp published the [Rancher2 provider](https://www.terraform.io/docs/providers/rancher2/index.html) and it is now generally available. [The repository used during initial development](https://github.com/rancher/terraform-provider-rancher2) will be archived and all future development will occur in the [terraform-providers repository](https://github.com/terraform-providers/terraform-provider-rancher2).

On Monday afternoon, May 20 around 2pm Eastern Time, on the RanchCast we’ll explore this new tool in detail. Follow [The RanchCast](https://www.twitch.tv/theranchcast) on Twitch or subscribe to [The RanchCast YouTube channel](https://www.youtube.com/channel/UCTfoEBv6XaI1nEfWDewj5vQ) so you don’t miss it!

*Note: this post has been edited as The RanchCast was rescheduled from 1pm to 2pm, because I read the wrong week on my calendar.*
