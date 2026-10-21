---
title: "Announcing Rancher 2.0 GA"
date: 2018-05-01T09:02:00
slug: "announcing-rancher-2-0-ga"
authors: ["Sheng Liang"]
products: ["Rancher Manager"]
tags: []
content_type: "release"
draft: false
migration:
  wp_id: 85814
  original_url: "https://www.suse.com/c/rancher_blog/announcing-rancher-2-0-ga/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.0 GA announcement"
  redirect_target: ""
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)

Today we reach an important milestone. Rancher 2.0, a release we worked on in the past year, has achieved GA and is ready for production deployment. I’d like to thank everyone who has worked on this release, and to thank all Rancher customers, users, and partners who have provided so much valuable support and feedback in the development process.

Based on the overwhelming demand from our customers, we know Rancher 2.0 is a unique and timely product. “Kubernetes Everywhere” is becoming a reality. Leading infrastructure software providers like VMware, Canonical, Red Hat, and SUSE are shipping Kubernetes distros. Leading infrastructure cloud providers like Amazon, Google, and Microsoft have all launched managed Kubernetes services. Enterprise customers need a software platform that can realize the benefits of enterprise Kubernetes orchestration in their organization. Rancher 2.0 is the only product that can manage all Kubernetes clusters on all clouds and implemented by any distros.

### Rancher 2.0 contains 3 major components:

1. **Rancher Kubernetes Engine (RKE).** RKE is the easiest way to install and manage Kubernetes clusters on vSphere clusters, bare metal servers, and cloud providers that do not yet support a managed Kubernetes service.
2. **Unified Cluster Management.** In addition to managing RKE clusters, Rancher 2.0 users can manage cloud-managed Kubernetes clusters like GKE, EKS, and AKS, as well as existing Kubernetes clusters built using other tools such as the Canonical Distribution of Kubernetes (CDK), Kops, and Kubespray. Rancher implements uniform authentication and centralized access control and security policies across all Kubernetes clusters.
3. **Application Workload Management.** Rancher 2.0 offers an intuitive user interface that drives the adoption of Kubernetes in your organization. Other features include enhanced Helm catalog support, CI/CD integration, alerts, and centralized logging.

With Rancher 2.0 GA behind us, the Rancher team is already working on the next release. I’m excited about lots of things our team is working on.

### In particular:

1. We are building tools for migrating Rancher 1.6 workloads to Rancher 2.x. The upcoming Rancher 2.1 will ship with tools that convert 1.6-style compose files to Kubernetes templates.
2. We will enrich the overall Rancher experience by bringing many ecosystem partner solutions to Rancher users. Look out for integrated registry, monitoring, security, storage, and networking solutions in the coming months.
3. We will continue to incorporate and build on new and exciting technologies coming out of the CNCF ecosystem. We believe serverless and service mesh can dramatically simplify user experience and drive Kubernetes adoption to the next level in many large organizations.

Thank you again for all your support in our 2.0 development process. We look forward to continuing work with you and making “Kubernetes Everywhere” a reality.

### Get Started with Rancher 2.0 GA

[Deploy](https://rancher.com/quick-start/) Rancher 2.0 or learn [how Rancher 2.0 works](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture) in depth.

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)
