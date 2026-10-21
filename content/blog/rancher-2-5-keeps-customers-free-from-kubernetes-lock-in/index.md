---
title: "Rancher 2.5 Keeps Customers Free from Kubernetes Lock-in"
date: 2020-10-21T09:57:00
slug: "rancher-2-5-keeps-customers-free-from-kubernetes-lock-in"
author: "Rancher Admin"
image: "images/rancher_blog_lsd-featured.png"
products: ["Rancher Manager"]
tags: ["multi-cluster"]
content_type: "release"
draft: false
migration:
  wp_id: 86303
  original_url: "https://www.suse.com/c/rancher_blog/rancher-2-5-keeps-customers-free-from-kubernetes-lock-in/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.5 partner view"
  redirect_target: ""
---

Discover what’s new in Rancher 2.5 [Learn More](/products/rancher/2.5) Rancher Labs has launched its much-anticipated Rancher version 2.5 into the cloud-native space, and we at LSD couldn't be more excited. Before highlighting some of the new features, here is some context as to how we think Rancher is innovating.

Kubernetes has become one of the most important technologies adopted by companies in their quest to modernize. While the container orchestrator, a fundamental piece of the cloud-native journey, has many advantages, it can also be frustratingly complex and challenging to architect, build, manage and maintain. One of the considerations is the deployment architecture, which leads many companies to want to deploy a hybrid cloud solution often due to cost, redundancy and latency reasons. This is often on premises and multi cloud.

All of the cloud providers have created Kubernetes-based solutions — such as EKS on AWS, AKS on Azure and GKE on Google Cloud. Now businesses can adopt Kubernetes at a much faster rate with less effort, compared to their technical teams building Kubernetes internally. This sounds like a great solution — except for perhaps the reasons above: cost, redundancy and latency. Furthermore, we have noticed a trend of no longer being cloud native, but AWS native or Azure native. The tools and capabilities are vastly different from cloud to cloud, and they tend to create their own kind of lock-in.

The cloud has opened so many possibilities, and the ability to add a credit card and within minutes start testing your idea is fantastic. You don't have to submit a request to IT or wait weeks for simple infrastructure. This has led to the rise of shadow IT, with many organizations bypassing the standards set out to protect the business.

We believe the new Rancher 2.5 release addresses both the needs for standards and security across a hybrid environment while enabling efficiency in just getting the job done.

Rancher has also released K3s, a highly available certified Kubernetes distribution designed for the edge. It supports production workloads in unattended, resource-constrained remote locations or inside IoT appliances.

## Enter Rancher 2.5: Manage Kubernetes at Scale

Rancher enables organizations to manage Kubernetes at scale, whether on-premise or in the cloud, through a single pane of glass, providing for a consistent experience regardless of where your operations are happening. It also enables you to import existing Kubernetes clusters and centrally manage. Rancher has taken Kubernetes and beefed it up with the required components to make it a fantastic enterprise-grade container platform. These components include push-button platform upgrades, SDLC pipeline tooling, monitoring and logging, visualizing Kubernetes resources, service mesh, central authorization, RBAC and much more.

As good as that sounds, what is the value in unifying everything under a platform like Rancher? Right off the bat there are three obvious benefits:

- Consistently deliver a high level of reliability on any infrastructure
- Improve DevOps efficiency with standardized automation
- Ensure enforcement of security policies on any infrastructure

Essentially, it means you don't have to manage each Kubernetes cluster independently. You have a central point of visibility across all clusters and an easier time with security policies across the different platforms.

## Get More Value out of Amazon EKS

With the release of Rancher 2.5, enhancements enhanced of the EKS platform support means that you can now derive even more value from your existing EKS clusters, including the following features:

- Enhanced EKS cluster import, keeping your existing cluster intact. Simply import it and let Rancher start managing your clusters, enabling all the benefits of Rancher.
- New enhanced configuration of the underlying infrastructure for Rancher 2.5, making it much simpler to manage.
- New Rancher cluster-level UX explores all available Kubernetes resources
- From an observability perspective, Rancher 2.5 comes with enhanced support for Prometheus (for monitoring) and Fluentd/Fluentbit (for logging)
- Istio is a service mesh that lets you connect, secure, control and observe services. It controls the flow of traffic and API calls between services and adds a layer of security through managed authentication and encryption. Rancher now fully supports Istio.
- A constant risk highlighted with containers is security. Rancher 2.5 now includes CIS Scanning of container images. It also includes an OPA Gatekeeper (open policy agent) to describe and enforce policies. Every organization has policies; some are essential to meet governance and legal requirements, while others help ensure adherence to best practices and institutional conventions. Gatekeeper lets you automate policy enforcement to ensure consistency and allows your developers to operate independently without having to worry about compliance.

## Conclusion

In our opinion, Rancher has done a spectacular job with the new additions in 2.5 by addressing critical areas that are important to customers. They have also shown that you absolutely can get the best of both EKS and fully-supported features.

LSD was founded in 2001 and wants to inspire the world by embracing open philosophy and technology, empowering people to be their authentic best selves, all while having fun. Specializing in containers and cloud native, the company aims to digitally accelerate clients through a framework called the LSDTrip. To learn more about the LSDTrip, [visit us](https://www.lsdopen.io) or [email us](mailto:rancher@lsdopen.io).Discover what’s new in Rancher 2.5 [Learn More](/products/rancher/2.5)
