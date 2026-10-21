---
title: "SUSE Rancher Prime Meets Cluster API: What You Need to Know"
date: 2025-03-19T11:38:43
slug: "suse-rancher-prime-meets-cluster-api-what-you-need-to-know"
authors: ["Nuno Do Carmo"]
products: ["Rancher Prime"]
tags: ["multi-cluster", "gitops"]
content_type: "explainer"
draft: true
migration:
  wp_id: 149890
  original_url: "https://www.suse.com/c/rancher_blog/suse-rancher-prime-meets-cluster-api-what-you-need-to-know/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "Prime-branded CAPI overview"
  redirect_target: "suse.com (new URL pending)"
---

Kubernetes has revolutionized how we deploy and manage applications, but juggling clusters across clouds and on-premises environments can quickly become a tangled mess. Different tools, inconsistent configurations‌ and manual processes drain your team's time and energy. What if there was a way to simplify Kubernetes cluster management, bringing order to the chaos? Enter Cluster API (CAPI) and SUSE Rancher Prime.

Cluster API (CAPI) is a Kubernetes subproject that helps make cluster provisioning and lifecycle management easier. It does this by using declarative APIs and a Kubernetes-native approach. 

**SUSE Rancher Prime** offers streamlined cluster deployment, centralized authentication, access control and observability across the entire infrastructure.

With its seamless integration into SUSE Rancher Prime, CAPI provides a powerful yet user-friendly way to provision, scale and manage clusters.

## What is Cluster API?

Cluster API makes it easier to set up, update and run Kubernetes clusters. It also makes it easier to work with different cloud providers and environments. CAPI abstracts the underlying infrastructure, allowing users to manage clusters declaratively with standardized configurations.

- **Declarative API:** Cluster API provides a declarative API for creating and managing Kubernetes clusters. This means that you can specify the desired state of your cluster, and Cluster API will take care of creating and managing the cluster for you.

- **Kubernetes-based and Extensible:** As a Kubernetes-based project, it is easy to connect to other Kubernetes tools and technologies. You can even add your own custom functions to the Cluster API and change it to meet your company's custom needs.

- **Provider Ecosystem:** The upstream Cluster API community is very active and providers for all the relevant infrastructure (e.g. AWS, Azure, GCP) and cloud vendors are available. You can even create your own provider that follows the CAPI contract. This contract has rules that a provider must follow to work with Cluster API.

- **Cluster templating:** ClusterClass is a game-changer feature - allowing you to define reusable templates for cluster configurations. By reducing boilerplate, ClusterClass simplifies cluster provisioning while ensuring consistency across environments
- **GitOps-Ready:** The declarative approach of Cluster API makes it ideal for using a GitOps approach to [cluster management](https://www.suse.com/c/understanding-cluster-management-for-kubernetes/).

## How SUSE Rancher Prime Enhances Cluster API

The synergy between Cluster API and SUSE Rancher Prime offers unparalleled flexibility and simplicity in managing Kubernetes clusters. Whether you’re managing clusters in AWS, Azure, GCP or on-premises, this integration is the next step toward operational efficiency.

Cluster API has powerful tools to define clusters as Kubernetes API resources and deploy them to most big infrastructure providers. However, it is a complex project that requires a lot of experience managing clusters. This is why we decided to make much of this complexity easier to understand through SUSE® Rancher Prime. This will let end users enjoy a simpler cluster provisioning and management process and access important Cluster API features without the hard learning curve or the operational burden usually associated with mastering it.

- **Unified Management**: Manage clusters through a graphical user interface (GUI) or command-line interface (CLI).
- **GitOps Integration**: CAPI integrates seamlessly with Fleet (Rancher’s continuous delivery tool) for streamlined deployments.
- **Provider****abstractions**: Install and manage CAPI providers with ease, leveraging existing Rancher cloud credentials.
- **Cluster Importing**: Automatically import and manage CAPI clusters in Rancher using simple labels.
- **Enhanced support for air-gapped and edge** deployments with tools like **Spegel**.

Click through for our guide ‘[Getting Started with Cluster API and SUSE Rancher Prime](https://docs.google.com/document/d/1roFqkciydS6I9YHzeq80jiDeStFX6n2OJXra--4TsbY/edit?tab=t.0#heading=h.1t1d8ptmpb8h)’, where we’ll walk you through the basics of the integration between CAPI and Rancher.

## Learn about CAPI & SUSE Rancher Prime

For those new to CAPI, let's get started by exploring its core components and cluster deployment mechanism. The process begins with configuring a Kubernetes cluster as a **CAPI Management Cluster**, which manages the lifecycle of Workload Clusters. A Management Cluster is also where one or more providers run, and where resources such as machines are stored. A Kubernetes cluster becomes a CAPI Management cluster by running the core CAPI controller and installing the required Custom Resource Definitions (CRDs). CAPI uses the term **Workload Cluster** to describe downstream Kubernetes clusters provisioned and managed through the Cluster API.

When you use Cluster API with SUSE Rancher Prime, you don't have to set up the CAPI Management cluster. This makes it easier to get started. Later, we will demonstrate how a Rancher Manager cluster becomes also a CAPI Management cluster via the SUSE Rancher Primer Cluster API Extension.

Read the official [Cluster API Book](https://cluster-api.sigs.k8s.io/introduction). It's a great resource for people who are new to CAPI and want to learn the basics, as well as for more experienced users.

### Core CAPI concepts: Providers, Cluster Classes, and Why They Matter

At its heart, Cluster API is about turning the complex process of managing Kubernetes clusters into something as straightforward as managing Kubernetes applications themselves. To make this magic happen, CAPI leans on a few key building blocks. Let’s break them down: 

👉 **Providers: The Engine Behind CAPI**

Think of Providers as the gears that make Cluster API tick. They're responsible for translating your declarative configuration (aka your YAML files) into actual infrastructure and clusters. In the CAPI ecosystem, there are three main types of providers:

- **Infrastructure Providers:** These create the raw building blocks for your clusters — think cloud VMs, networks, etc. For example, you’d use the AWS Provider to spin up EC2 instances, VPCs...
- **Bootstrap Providers:** These handle the ‘getting started’ bit. They take the shiny new machines your infrastructure provider has created and turn them into actual Kubernetes nodes.
- **Control Plane Providers:** Once you’ve got your Kubernetes nodes, you need a control plane to manage everything. Control Plane Providers ensure your Kubernetes clusters have a functioning control plane ready to go.

These providers work together like a well-rehearsed team: Infrastructure providers set the stage, Bootstrap Providers add the actors and Control Plane providers ensure the play runs smoothly. 

The providers you use depend on the use case and the infrastructure that will host your cluster. For example, the main cloud providers (AWS, Azure, and GCP) also offer managed Kubernetes services. When using the corresponding CAPI Infrastructure Provider, you won't need to start nodes or set up the control plane, as the cloud vendor will do this for you. This means that a single infrastructure provider, like AWS, supports two cluster provisioning methods: self-managed (EC2-based, requires bootstrap and control plane) and managed (EKS, control plane managed by AWS).

👉**ClusterClass: Templates for Success**

Here’s where things get even cooler. In addition to the standard Cluster API provisioning model, CAPI introduces **ClusterClass**, which essentially lets you create a reusable blueprint for your clusters. Instead of writing out all the details for each new cluster from scratch, you define a ClusterClass once and use it over and over. 

Imagine you need to deploy clusters with a specific configuration or topology (like control-plane, machine deployments and machine pools). With ClusterClass, you define all that in one place, and then just tweak the variables for each new cluster.

It's like having a cluster flavor that you can change for different cluster deployments. One ClusterClass can give you 12 clusters that are tailored to their specific needs while staying the same. This is a huge time-saver, especially for managing fleets of clusters, and reduces cluster definition complexity as most of the configuration happens in the class.

Take, for example, a scenario where you have multiple environments (e.g. development, staging, production) and you’d like to replicate the same cluster/s configuration but tweak some of the parameters, resources, etc. You may want to give more resources to the production environment but want to keep the same setup in the other stages of development, so you can test your changes. Cluster classes are a great way to adapt the specifics of a workload cluster while maintaining the core configuration.

Together, Providers and ClusterClass are part of the backbone of Cluster API, making it possible to manage Kubernetes clusters declaratively, repeatably and at scale. Pair this with SUSE Rancher Prime, which simplifies and abstracts away much of the complexity, and you’ve got a powerful, user-friendly way to manage clusters in any environment.

## Getting Started: Importing Cluster API clusters to SUSE® Rancher Prime

The [SUSE® Rancher Prime Cluster API Extension](https://documentation.suse.com/cloudnative/cluster-api/) makes it easier to work with Cluster API. Once you install it, it runs directly on the Rancher Manager Cluster. It also lets you add Cluster API clusters to SUSE® Rancher Prime. It also provides ways to manage Cluster API and Cluster API Provider versions. This makes it easier to provide clusters.

Installing the extension configures the Rancher Manager cluster as a CAPI Management cluster. This allows you to provision workload clusters using CAPI and choose whether to import them into SUSE® Rancher Prime. 

In order to automatically import clusters into SUSE® Rancher Prime, simply apply the label cluster-api.cattle.io/rancher-auto-import”: “true” and you can do it at the cluster or namespace level:

- **Cluster level**: Only the cluster with the label will be detected and imported by the controller.
- **Namespace level**: All CAPI clusters that exist in the namespace will be detected and imported by the controller.

If you feel ready to get hands-on with Cluster API, we’ll walk you through how to create and import a cluster to Rancher in the [next post in this series](https://www.suse.com/c/rancher_blog/suse-rancher-prime-meets-cluster-api-from-theory-to-practice/).

---

Blog post originally authored by:

![Profile photo for Carlos Salas](https://ca.slack-edge.com/T02863RC2AC-U054JEVD1C3-1260a1c08412-512)

Carlos Salas
