---
title: "Why Kubernetes is Changing Storage"
date: 2020-06-02T09:52:00
slug: "why-kubernetes-is-changing-storage"
authors: ["Wendie Cheung"]
image: "images/rancher_blog_longhorn-storage-featured.png"
products: ["Longhorn"]
tags: ["storage"]
content_type: "opinion"
draft: false
migration:
  wp_id: 86180
  original_url: "https://www.suse.com/c/rancher_blog/why-kubernetes-is-changing-storage/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Learn more about Longhorn, an enterprise-grade, cloud-native container storage solution.[Learn More](https://rancher.com/products/longhorn)

By 2025, IDC expects [worldwide data to grow](https://www.networkworld.com/article/3325397/idc-expect-175-zettabytes-of-data-worldwide-by-2025.html) by 61 percent to 175 zettabytes. This increase in data consumption has contributed to a massive shift within the technology landscape in the last decade, where organizations have been forced to adapt to a digital-dependant world.

Infrastructure-as-a-service (IaaS) providers such as Amazon Web Services, Google Cloud Platform and Microsoft Azure have also accelerated digital adoption by breaking down barriers of entry to the cloud and providing organizations with an alternative to on-premise storage and a scalable platform to host their applications.

With the creation of more data, the need for storage has also increased exponentially. However, the changing technology landscape has also had impacts on the storage industry. Here’s why. As organizations become hyper-focused on delivering exceptional customer experiences, they are adopting newer technologies like Kubernetes to equip them with the agility and ability to consistently deliver a reliable service at scale. This increase in data creation and consumption is generating widespread disruption across the storage industry.

Though Kubernetes is only five years old, by 2022, Gartner predicts that 75 percent of global organizations will be running containerized applications in production.[[1]](#anchor1) This rapid uptake of containerized ecosystems has exposed a gap in the storage industry, where traditional storage providers are unable to provide functionality and support.

## Storage in a Cloud-Native Container World

Kubernetes has fundamentally changed how organizations use their container workloads. Early deployments of containers were primarily for stateless applications.[[2]](#anchor2) However, as the ecosystem matured and more applications were deployed on or migrated to Kubernetes, a clear need for stateful persistent storage solutions emerged.

Although adoption of containers and Kubernetes is growing, the ecosystem is still immature, with an influx of multiple storage solutions from numerous vendors.[[3]](#anchor3) This array of options poses a challenge for IT operations and developers working within a container environment. Finding a suitable storage solution that is sophisticated enough to address an organization’s specific needs – including ease of use, integration with infrastructure, professional support and promoting innovation – is often difficult, if not impossible to find.

## The Role of Cloud-Native Persistent Storage Solutions

Open source storage solutions such as [Longhorn](/blog/2020/longhorn-container-storage) provide organizations with an option to bridge some of these technical gaps when working in a Kubernetes environment. With no barrier to entry, Longhorn delivers a reliable, lightweight and easy-to-use platform that integrates with existing Kubernetes management platforms such as Rancher.

[Longhorn with Rancher](/blog/2020/longhorn-journey-to-ga) gives autonomy and control back to engineers without additional operational overlay. For teams working within enterprise organizations, storage solutions must often fit three criteria:

- Increased reliability, backed by professional support
- Cost-effective yet scalable
- Easy to use and deploy

Proprietary solutions often provide the technical capabilities and assurance enterprise organizations immediately look for. However, as convenient as they are, they inevitably become costly and lock users to their environments. As enterprise organizations adopt agile solutions like Kubernetes, a diversified technology stack that includes open source solutions will eventually play a crucial part of their technology strategy.

Ultimately open source solutions like Longhorn have the opportunity to grow with the community’s needs by continually adapting and developing into a product that addresses critical market requirements that aren’t driven by vendors’ road maps.

At Rancher, Longhorn plays a critical role in how we are driving Kubernetes adoption. As a lightweight, easy-to-use alternative to other cloud-native storage, Longhorn builds on Rancher’s ethos to continually deliver simple and accessible Kubernetes for everyone.

[1] Arun Chandrasekaran, ‘Best Practices for Running Containers and Kubernetes in Production’, February 2019
[2] Julie Palmer & Arun Chandrasekaran, ‘An I&O Leader’s Guide to Storage for Containerized Workloads’, January 2019
[3] Arun Chandrasekaran, ‘Best Practices for Running Containers and Kubernetes in Production’, February 2019

Learn more about Longhorn, an enterprise-grade, cloud-native container storage solution.[Learn More](https://rancher.com/products/longhorn)
