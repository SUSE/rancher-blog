---
title: "Getting Started with GKE"
date: 2017-10-19T11:15:00
slug: "getting-started-with-gke"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["cloud", "gcp"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86922
  original_url: "https://www.suse.com/c/rancher_blog/getting-started-with-gke/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Google Container Engine 2017 walkthrough"
  redirect_target: "rancher.com/blog (hub)"
---

Google Container Engine, or GKE for short (the K stands for Kubernetes),
is Google’s offering in the space of Kubernetes runtime deployments.
When used in conjunction with a couple of other components from the
Google Cloud Platform, GKE provides a one-stop shop for creating your
own Kubernetes environment, on which you can deploy all of the
containers and pods that you wish without having to worry about managing
Kubernetes masters and capacity. This article outlines how GKE works and
how to get up and running with GKE.

## Background: Google and Kubernetes

Google founded the Kubernetes open source project based on some existing
code from its infrastructure, which has been built and refined using
Google’s lessons learned from running their entire platform on
containers well before Docker standardized the format, which sparked
mass adoption. With everything from ads and search to mail running in
containers, Google rightly predicted that management and orchestration
would be key to containers’ success in the marketplace.

## Key Benefits of Google Container Engine

GKE has a number of features that take advantage not only of Kubernetes,
but also the rest of the Google Cloud Platform.

### Its key features include:

- Security is handled by the Google security team.
- Compliance with HIPAA and PCI DSS is already managed.
- Kubernetes instances are fully clustered, and will auto scale.
- It’s based on the upstream Kubernetes project, which enables
  workload portability to other Kubernetes instances, whether they are
  another cloud provider or on-premises.

## Getting Started with GKE

Following is a primer for getting up and running with GKE.

1. Log in to the [Google Container
   Engine](https://console.cloud.google.com/projectselector/kubernetes?_ga=2.186405225.-1718754877.1506355235)
   page inside the [Google Cloud Platform](https://cloud.google.com/)
   console.
2. Create a project.
3. Enable billing.
4. Wait for the services to be set up. Once set up, you can create
   clusters to host applications and services.
5. On the **Create a container cluster** screen, you can specify which
   one of Google’s data centers is hosting deployed artifacts.
6. And you can enable other features, like authorization and automatic
   updates.
7. GKE now has a functioning Kubernetes cluster you can connect to and
   use as you wish.

## GKE Caveats

The single biggest drawback of using GKE for your Kubernetes runtime is
that you are tied to Google’s Cloud Platform. If you wish to use GKE,
but also want to be able to support multiple clouds, an option like
[Rancher](https://rancher.com/rancher/) can be a help. Rancher provides a
unified front end for multiple container orchestration frameworks and
environments, giving you a “single pane of glass” for deploying
containers wherever you need.

## Conclusion

If you want to try Kubernetes, or currently use it and want to be able
to scale without needing all the expertise in-house, GKE is a fantastic
single-cloud solution for running Kubernetes. Many companies never get
to the point of having a single cloud provider as a feasible option, but
using a product like Rancher allows a company to leverage existing
investment and expand to other cloud providers according to the dictates
of customer demand.

### About the Author

![](images/rancher_blog_vincent-powers-300x300.jpg)Vince Power is a
Solution Architect who has a focus on cloud adoption and technology
implementations using open source-based technologies. He has extensive
experience with core computing and networking (IaaS), identity and
access management (IAM), application platforms (PaaS), and continuous
delivery.
