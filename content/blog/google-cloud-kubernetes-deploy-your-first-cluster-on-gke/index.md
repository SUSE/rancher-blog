---
title: "Google Cloud Kubernetes: Deploy Your First Cluster on GKE"
date: 2020-04-15T09:50:00
slug: "google-cloud-kubernetes-deploy-your-first-cluster-on-gke"
author: "Rancher Admin"
image: "images/rancher_blog_google-gke-featured.png"
products: ["Kubernetes (generic)"]
tags: ["gcp", "cloud"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 86121
  original_url: "https://www.suse.com/c/rancher_blog/google-cloud-kubernetes-deploy-your-first-cluster-on-gke/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "2020 GKE console steps"
  redirect_target: ""
---

Google, the original developer of Kubernetes, also provides the veteran managed Kubernetes service, Google Kubernetes Engine (GKE).

GKE is easy to set up and use, but can get complex for large deployments or when you need to support enterprise requirements like security and compliance. Read on to learn how to take your first steps with GKE, get important tips for daily operations and learn how to simplify enterprise deployments with Rancher.

**In this article you will learn:**

- **What is Google Kubernetes Engine?**
- **How GKE is priced**
- **How to create a Kubernetes cluster on Google Cloud**
- **GKE best practices**
- **How to simplify GKE for enterprise deployments with Rancher**

## What is Google Kubernetes Engine (GKE)?

Kubernetes was created by Google to orchestrate its own containerized applications and workloads. Google was also the first cloud vendor to provide a [managed Kubernetes service](https://www.suse.com/c/ensuring-high-availability-with-cloud-managed-kubernetes/), in the form of GKE.

GKE is a managed, upstream Kubernetes service that you can use to automate many of your deployment, maintenance and management tasks. It integrates with a variety of Google cloud services and can be used with hybrid clouds via the Anthos service.

## Google Cloud Kubernetes Pricing

Part of deciding whether GKE is right for you requires understanding the cost of the service. The easiest way to estimate your costs is with the [Google Cloud pricing calculator](https://cloud.google.com/products/calculator#tab=container).

**Pricing for cluster management**

Beginning in June 2020, Google will charge a cluster management fee of $0.10 per cluster per hour. This fee does not apply to Anthos clusters, however, and you do get one zonal cluster free. Billing is calculated on a per-second basis. At the end of the month, the total is rounded to the nearest cent.

**Pricing for worker nodes**

Your cost for worker nodes depends on which Compute Engine Instances you choose to use. All instances have a one-minute minimum use cost and are billed per second. You are billed for each instance you use and continue to be charged until you delete your nodes.

## Creating a Google Kubernetes Cluster

Creating a cluster in GKE is a relatively straightforward process:

**1. Setup**

To get started you need to first enable API services for your Kubernetes project. You can do this from the Google Cloud Console on the [Kubernetes Engine page](https://console.cloud.google.com/projectselector/kubernetes?_ga=2.139827828.671066939.1584025382-1372532908.1563724267). Select your project and enable the API. While waiting for these services to be enabled, you should also verify that you’ve enabled billing for your project.

**2. Choosing a shell**

When setting up clusters, you can use either your local shell or Google’s Cloud Shell. The Cloud Shell is designed for quick startup and comes preinstalled with the kubectl and gcloud CLI tools. The gcloud tool is used to manage cloud functions and kubectl is used to manage Kubernetes. If you want to use your local shell, just make sure to install these tools first.

**3. Creating a GKE cluster**

Clusters are composed of one or more masters and multiple worker nodes. When creating nodes, you use virtual machine (VM) instances which then host your applications and services.

To create a simple, one-node cluster, you can use the following command. However, note that a single node cluster is not fit for production so you should only use this cluster for testing.

`gcloud container clusters create` {Cluster name} `--num-nodes=1`

**4. Get authentication credentials for the cluster**

Once your cluster is created, you need to set up authentication credentials before you can interact with it. You can do so with the following command, which configures kubectl with your credentials.

`gcloud container clusters get-credentials` {Cluster name}

## Google Cloud Kubernetes Best Practices

Once you’ve gotten familiar with deploying clusters to GKE, there are a few best practices you can implement to optimize your deployment. Below are a few practices to start with.

**Manage resource use**

Kubernetes is highly scalable but this can become an issue if you scale larger than your available resources. To ensure that you are not creating too many replicas or allowing pods to use too many resources, you can enforce, request and limit policies. These policies can help you ensure that your resources are fairly distributed and can prevent issues due to overprovisioning.

**Avoid privileged containers**

Privileged containers enable contained processes to gain unrestricted access to your host. This is because a privileged container’s uid is mapped to that of the host. To avoid the security risk that is created by these privileges, you should avoid operating containers in privileged mode whenever possible. You should also ensure that privilege escalation is not allowed.

**Perform health checks**

Once you reach the production stage, your Kubernetes deployment is likely highly complex and can be difficult to manage. Rather than waiting for something to go wrong and then trying to find it, you should perform periodic health checks.

Health checks are a way of verifying that your components are working as expected. These checks are performed with probes, like the readiness and liveness probes.

**Containers should be stateless and immutable**

While you can use stateful applications in Kubernetes, it is designed for use with stateless processes. Stateless processes do not include persistent memory and contained data only exists while your container does. For data to be retained, containers must be attached to external storage.

Ideally, your containers should be both immutable and stateless. This enables Kubernetes to smoothly take down or replace containers as needed, reattaching to external storage as needed.

The immutable aspect means that a container does not change during its lifetime. If you need to make changes, such as updates or configuration changes, you make the change as needed and then build a new image to deploy. There is an option to get around this for some configuration, however. Using ConfigMaps and Secrets, you can externalize your configuration. From there you can make changes without needing to rebuild your image after each change.

**Use role-based access control (RBAC)**

RBAC is an efficient and effective way to manage permissions within your deployment. In GKE, it is applied as an authorization method that is layered on the Kubernetes API.

With RBAC, all access is denied by default and it is up to you to define granular permissions to individual users. Keep in mind, any user roles you create only apply to one namespace. To work across namespaces, you need to define cluster roles.

**Simplify monitoring**

Monitoring and logging events is a requirement for proper management of your applications. Commonly, monitoring in Kubernetes is done through Prometheus, a built-in integration that enables you to automatically discover services and pods.

Prometheus works by exposing metrics to an HTTP endpoint. These metrics can then be ingested by the monitoring tool of your choice. For example, you can use a tool like Stackdriver, which includes its own Prometheus version.

## Simplifying GKE for Enterprise Deployments with Rancher

Rancher is a Kubernetes management platform that simplifies setup and ongoing operations for Kubernetes clusters at any scale. It can help you run mission critical workloads in production and easily scale up Kubernetes with enterprise-grade capabilities.

Rancher enhances GKE if you also manage Kubernetes clusters on different substrates—including Amazon’s Elastic Kubernetes Service (EKS) or the Azure Kubernetes Service (AKS), on-premises or at the edge. Rancher lets you centrally configure policies on all clusters. It provides the following capabilities beyond what is offered in native GKE:

**Centralized user authentication and role-based access control (RBAC)**

Rancher integrates with Active Directory, LDAP and SAML, letting you define access control policies within GKE. There is no need to maintain user accounts or groups across multiple platforms. This makes compliance easier and promotes self service for Kubernetes administrators — it is possible to delegate permission for clusters or namespaces to specific administrators.

**Consistent, unified experience across cloud providers**

Alongside Google Cloud, Rancher supports AWS, Azure and other cloud computing environments. This allows you to manage Kubernetes clusters on Google Cloud and other environments using one pane of glass. It also enables one-click deployment across all your clusters of [Istio](https://rancher.com/docs/rancher/v2.x/en/cluster-admin/tools/istio/), [Fluentd](https://rancher.com/docs/rancher/v2.x/en/cluster-admin/tools/logging/fluentd/), [Prometheus and Grafana](https://rancher.com/docs/rancher/v2.x/en/cluster-admin/tools/monitoring/), and [Longhorn](https://longhorn.io/).

**Comprehensive control via one intuitive user interface**

Rancher allows you to deploy and troubleshoot workloads consistently, whether they run on Google Cloud or elsewhere, and regardless of the Kubernetes version or distribution you use. This allows DevOps teams to become productive quickly, even when working on Kubernetes distributions or infrastructure providers they are not closely familiar with.

**Enhanced cluster security**

Rancher allows security teams to centrally define user roles and security policies across multiple cloud environments, and instantly assign them to one or more Kubernetes clusters.

**Global app catalog and multi-cluster apps**

Rancher provides an application catalog you can use across numerous clusters, allows you to easily pick an application and deploy it on a Kubernetes cluster. It also allows applications to run on several Kubernetes clusters.

[Learn more](https://rancher.com/products/rancher/) about the Rancher managed Kubernetes platform.
