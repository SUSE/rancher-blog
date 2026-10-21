---
title: "Securing Financial Transactions with Rancher"
date: 2020-09-28T10:10:00
slug: "securing-financial-transactions-with-rancher"
author: ""
image: "images/rancher_blog_entersekt-featured.png"
products: ["Rancher Manager"]
tags: ["security"]
content_type: "case-study"
draft: true
migration:
  wp_id: 86383
  original_url: "https://www.suse.com/c/rancher_blog/securing-financial-transactions-with-rancher/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "Customer case study, buyer-oriented"
  redirect_target: "suse.com (new URL pending)"
---

*“With Rancher and Kubernetes, we’ve started moving to a microservices architecture. What this means is our teams don’t have to know Kubernetes inside out, just the projects they’re working on. Rancher simplifies Kubernetes for technicians, which results in greater agility and innovation.”* Tertius Wessels, Senior Vice President of Engineering, Entersekt

We’ve all heard about high-profile security hacks and have no doubt been the recipient of phishing emails. So, when it comes to financial services, you want to be sure that your privacy and security are never compromised. Enter Entersekt, a global fintech company that protects more than 50 million enrolled users all over the world and prevents more than one billion security breaches a month.

Based in South Africa, [Entersekt](https://www.entersekt.com/) delivers a patented digital identity system to financial services providers who serve up secure, convenient omnichannel experiences to their customers. The company’s Entersekt Secure Platform (ESP) is the *de facto* market standard in device identity, multi-channel payments security and low-friction strong customer authentication.

## Choosing Rancher over OpenShift and Mesosphere

Like many companies transitioning from startup to global enterprise, Entersekt has spent a lot of time improving processes in pursuit of greater efficiency. This includes modernizing its monolithic legacy infrastructure. With Kubernetes and Rancher, Senior VP of Engineering Tertius Wessels and his team are gaining control over a sprawling estate of microservices and creating a more cloud native and security-centric architecture for their customers.

The team originally adopted Docker Swarm as a platform to improve deployment velocity. However, they found it difficult to debug and decided it was not a long-term solution. Meanwhile, Kubernetes had become the standard for container orchestration, with a huge community behind it. Yet the team knew the complexity of Kubernetes would prove challenging for customers, so they looked for a management solution. After POCs with Rancher, OpenShift and Mesosphere, Rancher emerged as the clear winner, with its ability to simplify the deployment and management of Kubernetes.

## Adopting Microservices and Cloud-Native with Rancher

Entersekt’s monolithic architecture and single codebase created several management challenges for the team. While they had several sub-teams, each one was doing end-to-end development – resulting in duplication of work and code overwrites. Breaking the monolith into microservices was the answer.

By moving to Kubernetes and Rancher, Entersekt segmented its codebase into microservices and adopted development best practices. Now Wessels has nine teams working in parallel – some on the nuts and bolts of the system, others on developing applications as cloud-native microservices. Each team works in its own space, which streamlines development and accelerates deployment.

With a microservices model, Entersekt can release applications when they’re ready, rather than having to wait for a six-month release cycle. That means they’re continuously engaging with customers and providing updates as they are ready.

[Read our case study](/pdfs/customers/Rancher_Entersekt.pdf) to hear how Entersekt has increased release velocity by 80 percent and improved productivity by 70 precent with Rancher.
