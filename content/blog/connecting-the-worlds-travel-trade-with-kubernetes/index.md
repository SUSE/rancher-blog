---
title: "Connecting the World’s Travel Trade with Kubernetes"
date: 2020-09-21T09:50:00
slug: "connecting-the-worlds-travel-trade-with-kubernetes"
author: ""
image: "images/rancher_blog_hotelbeds-featured.png"
products: ["Rancher Manager"]
tags: ["multi-cluster", "cloud"]
content_type: "case-study"
draft: true
migration:
  wp_id: 86128
  original_url: "https://www.suse.com/c/rancher_blog/connecting-the-worlds-travel-trade-with-kubernetes/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "Customer case study, buyer-oriented"
  redirect_target: "suse.com (new URL pending)"
---

*“We needed the flexibility to run any technologies side-by-side and a way to run clusters in multiple clouds, and a variety of environments – depending on customer needs. Rancher was the only realistic choice.”* Juan Luis Sanfélix Loshuertos, IT Operations Manager - Compute & Storage, Hotelbeds

When you book a hotel online or with a travel agent, you’ve probably got a wish list that has to do with the size of the room, view, location and amenities. It’s likely you’re not thinking about the technology in the background that makes it all happen. That’s where Hotelbeds comes in. The business-to-business travel technology company operates a hotel distribution platform that travel agents, tour operators, airlines and loyalty programs use to book hotel rooms.

As the world’s leading “bedbank”, the Spanish company provides more than 180,000 hotel properties worldwide with access to distribution channels that significantly increase occupation rates. They give hoteliers access to a network of more than 60,000 hard-to-access B2B travel buyers such as tour operators, retail travel agents, airline websites and loyalty programs.

Hotelbeds attributes much of its success to a focus on technology innovation. One of the main roles of its technology teams is to experiment and validate technologies that make the business more competitive. With this innovation strategy and growing use of Kubernetes, the company is healthy, despite challenges in the hospitality industry.

The company’s initial infrastructure was an on-premise, VM-based environment. Moving to a cloud-native, microservices-centric environment was a goal, and by 2017 they began this transition. They started working with Amazon Web Services (AWS) and by 2018, had created a global cloud distribution, handling large local workloads all over the world. The technology transformation continued as they started moving applications into Docker containers to drive management and cost efficiencies.

## Moving to Kubernetes and Finding a Management Tool

Then, with the groundswell behind Kubernetes, the Hotelbeds team knew moving to feature-rich platform was the next logical step. With that came the need for an orchestration solution that could support a mix of technologies both on-premise and in the cloud. With many data centers and a proliferating cloud presence, the company also needed multi-cluster support. After exhaustive market analysis, Rancher emerged as the clear choice, with its ability to support a multi-cluster, multi-cloud and hybrid cloud/on-premise architecture.

After further testing with Rancher in non-critical data apps, Hotelbeds moved into production in 2020, running Kubernetes clusters both on-premise and in Google Cloud Platform and AWS. With Rancher, they reduced cloud migration time by 90 percent and reduced cluster deployment time by 80 percent.

[Read our case study](/pdfs/customers/Rancher_Hotelbeds.pdf) to hear how Rancher gives Hotelbeds the flexibility to manage deployments across AWS regions while scaling on-premise clusters 90 percent faster at 35 percent less cost.
