---
title: "MPAC Cuts Cloud Costs by 40 Percent with Rancher"
date: 2020-07-13T09:55:00
slug: "mpac-cuts-cloud-costs-by-40-percent-with-rancher"
author: ""
image: "images/rancher_blog_mpac-featured.png"
products: ["Rancher Manager"]
tags: ["cloud"]
content_type: "case-study"
draft: true
migration:
  wp_id: 86263
  original_url: "https://www.suse.com/c/rancher_blog/mpac-cuts-cloud-costs-by-40-percent-with-rancher/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "Customer case study, buyer-oriented"
  redirect_target: "suse.com (new URL pending)"
---

“Rancher has solved a host of issues facing us as a publicly funded organization – driving predictability, easing cluster management and upholding the right security profile. Rancher was the obvious choice to meet these goals.” Chruz Cruz, Senior Infrastructure Architect, MPAC

Every day, thousands of property owners in Ontario access an online application to view their property profiles, assessment information and comparable properties. Managed by the Municipal Property Assessment Corporation (MPAC), the application is used in the organization’s work of assessing more than five million properties in Ontario. These assessments are the foundation of Ontario’s property tax system, which generates $30 billion annually for municipalities to provide local services.

As custodians of public data, MPAC needs to ensure that its technical infrastructure is secure, modern, robust and cost effective. These priorities hastened MPAC’s journey to the cloud, Kubernetes and Rancher.

## Migrating to AWS and Kubernetes

In 2017, the MPAC team decided to migrate its on-premise data center infrastructure to Amazon Web Services (AWS). This migration involved lifting and shifting Spring Boot and Java applications from on-premise to the cloud, running on standalone compute instances. However, the team realized that their processes were time consuming and expensive due to the need for lots of manual intervention for scaling and analytics. With costs spiraling, they explored containers to streamline workloads and reduce costs.

MPAC moved its applications into containers, then into Kubernetes. Once they realized how agile and self-aware Kubernetes was, there was no looking back. In need of a management tool, MPAC considered several options and landed on Kubernetes Operation (kops). At that time, kops was the standard management tool for AWS-related Kubernetes clusters and allowed MPAC to keep its data management systems in Canada – where Amazon Elastic Kubernetes Service (EKS) didn’t yet have a presence.

## Leaving kops for Rancher

While kops performed well, the team found gaps. Upgrades and maintenance took three to five days, while security patches depended on kops’ release cycle. Kops realized that Rancher 2.3 would resolve these issues and ran a successful POC in February 2020.

In production, Rancher brought a level of operational visibility into MPAC’s AWS-based Kubernetes containers that allowed the team to identify inefficiencies and take action. With Rancher, the team reduced their monthly AWS bill by 40 percent.

[Read our case study](/customers/mpac) to hear how Rancher brings a central, unified, intuitive Kubernetes management methodology to MPAC while reducing update and patch management times by 80 percent and cluster deployment time by 85 percent.
