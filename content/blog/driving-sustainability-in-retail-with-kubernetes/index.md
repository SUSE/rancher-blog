---
title: "Driving Sustainability in Retail with Kubernetes"
date: 2020-04-28T09:55:00
slug: "driving-sustainability-in-retail-with-kubernetes"
author: ""
image: "images/rancher_blog_optoro-featured.png"
products: ["Rancher Manager"]
tags: ["case-study"]
content_type: "case-study"
draft: true
migration:
  wp_id: 86269
  original_url: "https://www.suse.com/c/rancher_blog/driving-sustainability-in-retail-with-kubernetes/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "Customer case study aimed at buyers"
  redirect_target: "suse.com (new URL pending)"
---

*“With sustainability our primary focus, our technology strategy has to mirror our overall approach. With Rancher we’re driving real transformation to prime us for long-term growth.”*

– Zach Dunn, Senior Director of Platform Operations and CSO, Optoro

Have you ever considered what happens to items you return to etailers? In retail, especially ecommerce, nearly 25 percent of all goods are returned or don’t sell. And in the US alone, the value of these goods is a staggering $500 billion – usually written off as losses by etailers. Beyond the economic impact, there are environmental consequences: many goods ending up in landfills.

Optoro aims to break this cycle. As the world’s leading returns optimization platform, Optoro has pioneered a reverse logistics model to solve this excess goods problem. Using machine learning and predictive analytics, they route returned and excess goods to their next best home, whether it’s an end consumer, charity or recycler – anywhere in the world. Optoro operates a consumer resale site,  www.blinq.com, and a wholesale site, www.BULQ.com. The company estimates that they have diverted 3.9 million pounds of waste from landfills, prevented 22.7 million pounds of carbon emissions, and donated 2.7 million items to charities.

Soon after joining the company, Senior Director of Platform Operations and CSO Zack Dunn decided to move the company from a cloud-based infrastructure to on premises. Optoro had a steady state in terms of costs; APIs and databases were never powered down and so costs would increase or decrease with cloud expansion and contraction. Transitioning into a data center, Dunn could level-set his costs – driving greater predictability into financial management.

After converting their estate of VMs into Docker containers, Dunn and his team started experimenting with Kubernetes. While a move Kubernetes made sense, they didn’t want to absorb additional costs – and could not find a business case for OpenShift, GKE or EKS. They wanted a platform that allowed their developers to consolidate role-based access control and other backend processes and directly manage their clusters through an intuitive UI. Rancher checked all the boxes.

Following a successful proof of concept, the team started to migrate its services into containers and into Rancher. Currently it runs 12 of its 42 services in production, with plans to migrate the entire infrastructure.

[Watch our video case study](/customers/optoro) and hear directly from Dunn about Optoro’s journey from the cloud to the data center and the benefits of adopting Kubernetes and Rancher.
