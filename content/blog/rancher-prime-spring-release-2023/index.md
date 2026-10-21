---
title: "Project Snow Cow: A hat-tip to Apple’s MacOS Snow Leopard release that drove the inspiration for Stability, Reliability & Extensibility in Rancher  "
date: 2023-04-18T00:27:52
slug: "rancher-prime-spring-release-2023"
author: "Utsav Sanghani"
image: "images/rancher-prime-logo-vert-color-652x720-8d2bf12c-6089-454c-b915-8cbd92b1bff5.jpg"
products: ["Rancher Manager"]
tags: ["upgrades"]
content_type: "company-news"
draft: true
migration:
  wp_id: 104125
  original_url: "https://www.suse.com/c/rancher_blog/rancher-prime-spring-release-2023/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "Product strategy PR for 2.7 release"
  redirect_target: "suse.com (new URL pending)"
---

Kubernetes has reached an interesting point in its lifecycle where it is now the default choice to run business-critical applications across varied infrastructures, from virtual machines to bare metal and in the cloud. This, combined with the evolving need for a single pane of glass to centralize and manage infrastructure and application deployments, has required IT teams to focus on a stable, reliable and extensible platform that can scale on demand.   

At SUSE, our product direction and strategy are driven by deepening our understanding of our users and customer needs. In a post-Covid-19 world, achieving Kubernetes nirvana became the primary goal for IT teams, focusing on stability, reliability and extensibility driving usage and purchase behavior. To help understand how we solve this problem most effectively, we got back to the basics.   

With the support of our users and our customers, we kicked off ‘Project Snow Cow’ - our hat-tip to the mythological status of Snow Leopard in the Apple community as the catch-all referring to stable software from "the good old days” of Mac and moved forward with building a prioritized delivery plan to make Rancher more stable, reliable, extensible and scalable on demand.   

Project Snow Cow became the bedrock of our v2.7.x releases. Starting with Rancher v2.7.0, we fixed 132 bugs and made over 40+ product changes over the week of Thanksgiving 2022. Rancher v2.7.1 came in next in January 2023 with dedicated security fixes to improve our overall security posture.   

And now Rancher v2.7.2, released in April 2023, took the crown with 204 total resolved issues involving 140+ bugs and 40+ product enhancements, including production-grade GA support for Kubernetes 1.25, AKS 1.25 & GKE 1.25. To facilitate effective usage of K8s 1.25, Rancher v2.7.2 also adds a new [custom resource definition (CRD): PSA configuration templates](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/authentication-permissions-and-global-configuration/psa-config-templates). These templates are pre-defined security configurations that you can apply to RKE and RKE2/K3s clusters out of the box. A lot of goodness is packed into one!  

Building on the success of ‘Project Snow Cow,’ which focused on stability and reliability, our feature teams started adding the desired levels of extensibility with the [introduction of UI extensions](https://www.suse.com/c/rancher_blog/utilizing-rancher-ui-extensions/) that can layer independently on top and allow you to scale up and have a single pane of glass management view across all your cloud native tools, from container application development to container security and deployment.   

These UI extensions were first introduced in v2.7.0 and now allow for a true plug-and-play model into the Rancher platform to accommodate policy management, security and audit compliance use cases, among other things. Alongside v2.7.2, we now offer a Kubewarden extension for Rancher that makes it easy to install Kubewarden into a downstream cluster and manage Kubewarden and its OPA-based policies right from within the Rancher Cluster Explorer user interface. You can see how we build extensions in the upcoming [Global Online Meetup](https://more.suse.com/FY23Q1_CY_ECM_SR_ECMC_WEB_Global_Online_Meetup_Rancher_Extensions_RG_GLB_RegistrationPage-NEW.html) on May 3, 2023, at 11 am EST. 

**Evolving the Rancher Prime Subscription**

![](images/rancher-prime-logo-color-300x121.png)

In line with Rancher v2.7.2, I am excited to also announce the next iteration of the [Rancher Prime Subscription](http://www.rancher.com/products/rancher); Rancher Prime 1.1. The subscription allows customers to extend the benefits of the Rancher Platform to now get a trusted, private registry download mechanism for their entire Kubernetes Management stack. This trusted delivery mechanism and our SLA-backed support model ensures upstream changes and disruptions can be insulated for production environments ensuring changes like the recent deprecation of PSPs in Kubernetes 1.25 and the move to PSA can be minimized dramatically. It also allows customers to extend their SLA-backed support confidence to cover ancillary cloud-native tools like Kubewarden (OPA Policy Management) & Elemental (OS Management) UI extensions in Rancher.   

Customers also now get access to the [Rancher Prime Knowledgebase](https://www.suse.com/c/rancher_blog/suse-launches-dedicated-rancher-prime-knowledgebase), a curated, contextually relevant set of self-service material through the SUSE Collective that gives you direct access to Kubernetes cheat sheets, scalability documentation and white-glove onboarding guidance. Through the Collective, you can also request Product Roadmaps and engage in peer discussions to help accelerate your cloud native journey.   

**What’s next?**

If you haven't already, we encourage you to join the party and test-drive Rancher v2.7.2. Project Snow Cow has a few more releases coming up and that will ensure Rancher at scale is performant. On the Rancher Prime side, customers can expect to see more supported extensions and LTSS options coming in the next iteration. If you are seeking to get more value from your Rancher deployment, get in touch with our team to learn more.   

Remember to stay tuned for updates via our [Slack](https://slack.rancher.io/) and our [GitHub](https://github.com/rancher/) page.
