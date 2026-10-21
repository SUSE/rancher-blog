---
title: "Kubernetes DevOps: A Powerful Pair"
date: 2020-02-10T09:45:00
slug: "kubernetes-devops-a-powerful-pair"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_ci-cd.png"
products: ["Kubernetes (generic)"]
tags: ["ci-cd", "gitops"]
content_type: "explainer"
draft: false
migration:
  wp_id: 85987
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-devops-a-powerful-pair/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Kubernetes has seen an incredible rise over the past few years as organizations leverage containers for complex applications, micro-services and even cloud-native applications. And with the rise of Kubernetes, DevOps has gained more traction. While they may seem very different — one is a tool and the other is a methodology — they work together to help organizations deliver fast. This article explains why Kubernetes is essential to your DevOps strategy.

Google designed Kubernetes and then released it as open source to help alleviate the problems in DevOps processes. The aim was to help with automation, deployment and agile methodologies for software integration and deployment. Kubernetes made it easier for developers to move from dev to production, making applications more portable and leverage orchestration. Developing in one platform and releasing quickly, through pipelines, to another platform showcased a level of portability that was previously difficult and cumbersome. This level of abstraction helped accelerate DevOps and application deployment.

## What is DevOps?

DevOps brings typically siloed teams together – Development and IT Operations. DevOps promises to help teams work collectively and collaboratively to achieve business outcomes faster. Security is also an important part of the mix that should be included as part of the culture. With DevSecOps, three silos come together as “first-class citizens” working collaboratively to achieve the same outcome.

From a technology point of view, DevOps typically focuses on CI/CD (continuous integration and continuous delivery or continuous deployment). Here is a quick explanation:

**Continuous integration:** developers make constant updates to source code within a shared repository, which is then scanned and checked by an automated build, allowing teams to detect problems early.

**Continuous deployment:** once approved, code is released into production, resulting in many production deployments every day.

**Continuous delivery:** software is built and can be released at any time – but by a manual process

## Quick Kubernetes Recap

As noted above, Google created Kubernetes and released a variation as open source to the general public. It is now one of the flagship products looked after by the Cloud Native Computing Foundation (CNCF). Different deployments of Kubernetes are available, including those from managed providers (AWS, Azure and GCP), Rancher RKE and others that can be built from scratch (Kubernetes the Hard Way by Kelsey Hightower).

Kubernetes allows organizations to run applications within containers in a distributed manner. It also handles scaling, resiliency and availability. Additionally, Kubernetes provides:

- Load balancing
- Ability to provide access to storage (persistent and non-persistent)
- Service discovery
- Automated rollouts, upgrades and rollbacks
- Role-based access control (RBAC)
- Security controls for running applications within the platform
- Extensibility to leverage a large and growing ecosystem to support DevOps

## The Kubernetes DevOps Connection

By now we can start to see a correlation between DevOps teams creating applications and running containers and needing an orchestration engine that keeps them running at scale. This is where Kubernetes and DevOps fit together. Kubernetes helps teams respond to customer demands without having to worry about the infrastructure layer – Kubernetes does this for them. The orchestration engine within Kubernetes takes over the once-manual tasks of deploying, scaling and building more resiliency into the applications; instead, it has the controls to manage this on the fly.

Kubernetes is essential for DevOps teams looking to automate, scale and build resiliency into their applications while minimizing the infrastructure burden. Letting Kubernetes manage an application’s scale and resiliency based on metrics, for example, allows developers to focus on new services instead of worrying whether the application can handle the additional requests during peak times. The following are key reasons why Kubernetes is essential to a DevOps team:

**Deploy Everywhere.** As noted previously, Kubernetes handles the ability to deploy an application anywhere without having to worry about the underlying infrastructure. This abstraction layer is one of the biggest advantages to running containers. Wherever deployed, the container will run the same within Kubernetes.

**Infrastructure and Configuration as Code.** Everything within Kubernetes is “as-code,” ensuring that both the infrastructure layer and the application are all declarative, portable and stored in a source repository. By running “as-code,” the environment is automatically maintained and controlled.

**Hybrid.** Kubernetes can run anywhere – whether on-premises, in the cloud, on the edge. It’s your choice. So, you’re not locked in to either an on-premises deployment or a cloud-managed deployment. You can have it all.

**Open Standards.** Kubernetes follows open-source standards, which increases your flexibility to leverage an ever-growing ecosystem of innovative services, tools and products.

**Deployments with No Downtime.** Since applications and services get continuously deployed during the day, Kubernetes leverages different deployment strategies. This reduces the impact on existing users while giving developers the ability to test in production (phased approach or blue-green deployments). Kubernetes also has a rollback capability – should that be necessary.

**Immutability.** This is one of the key characteristics of Kubernetes. The oft-used analogy, “cattle, not pets,” means that containers can (and should) be able to be stopped, redeployed and restarted on the fly with minimal impact (naturally, there will be an impact on the service the container is operating).

## Conclusion: Kubernetes + DevOps = A Good Match

As you can see, the relationship between the culture of DevOps and the container orchestration tool Kubernetes is a powerful one. Kubernetes provides the mechanisms and the ecosystem for organizations to deploy applications and services to customers quickly. It also means that teams don’t have to build resiliency, scale, etc. into the application – they can trust that Kubernetes services will take care of that for them. The next phase is to integrate the large ecosystem surrounding Kubernetes (see the CNCF ecosystem landscape), thus, building a platform that is highly secure, available and flexible to allow organizations to serve their customers faster, more reliably and at greater scale.

## More Resources

Read the white paper: [How to Build an Enterprise Kubernetes Strategy](https://more.suse.com/fy21-global-web-landing-page-how-to-build-enterprise-kubernetes-strategy).
