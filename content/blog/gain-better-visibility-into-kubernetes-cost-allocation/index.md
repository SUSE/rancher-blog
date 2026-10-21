---
title: "Gain Better Visibility into Kubernetes Cost Allocation"
date: 2020-09-30T09:49:00
slug: "gain-better-visibility-into-kubernetes-cost-allocation"
author: "Rancher Admin"
image: "images/rancher_blog_cost-optimization-featured.png"
products: ["Kubernetes (generic)"]
tags: ["observability", "cloud"]
content_type: "explainer"
draft: false
migration:
  wp_id: 86090
  original_url: "https://www.suse.com/c/rancher_blog/gain-better-visibility-into-kubernetes-cost-allocation/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Master class promo, old tooling"
  redirect_target: ""
---

Join The Master Class: Kubernetes Cost Allocation and Visibility, Tuesday, October 13 at 2pm ET [Register Now](https://info.rancher.com/kubernetes-master-class-oct13-2020)

## The Complexity of Measuring Kubernetes Costs

Adopting Kubernetes and service-based architecture can bring many benefits to organizations – teams move faster and applications scale more easily. However, visibility into cloud costs is made more complicated with this transition. This is because applications and their resource needs are often dynamic, and teams share core resources without transparent prices attached to workloads. Additionally, organizations that realize the full benefit of Kubernetes often run resources on disparate machine types and even multiple cloud providers. In this blog post, we’ll look at best practices and different approaches for implementing cost monitoring in your organization for a showback/chargeback program, and how to empower users to act on this information. We’ll also look at Kubecost, which provides an open source approach for ensuring consistent and accurate visibility across all Kubernetes workloads.

![Image 01](images/rancher_blog_image01.png)

A common Kubernetes setup with team workloads spread across Kubernetes nodes and clusters

Let’s look further into best practices for accurately allocating and monitoring Kubernetes workload costs as well as spend on related managed services.

## Cost Allocation

Accurately allocating resource costs is the first critical step to creating great cost visibility and achieving high cost efficiency within a Kubernetes environment.

To correctly do this, you need to allocate costs at the workload level, by individual container. Once workload allocation is complete, costs can be correctly assigned to teams, departments or even individual developers by aggregating different collections of workloads. One framework for allocating cost at the workload level is as follows:

![Image 02](images/rancher_blog_image02.png)

Let’s break this down a bit.

The average amount of resources consumed is measured by the Kubernetes scheduler or by the amount provisioned from a cloud provider, depending on the particular resource being measured. We recommend measuring memory and CPU allocation by the maximum of request and usage. Using this methodology reflects the amount of resources reserved by the Kubernetes scheduler itself. On the other hand, resources like load balancers and persistent volumes are strictly based on the amount provisioned from a provider.

The Kubernetes API can directly measure the period of time a resource is consumed. This is determined by the amount of time spent in a Running state for resources like memory, CPU and GPU. To have numbers that are accurate enough for cloud chargeback, we recommend that teams reconcile this data with the amount of time a particular cloud resource, such as a node, was provisioned by a cloud provider. More on this in the section below.

Resource prices are determined by observing the cost of each particular resource in your environment. For example, the price of a CPU hour on a m5.xlarge spot instance in us-east-1 AWS zone will be different than the on-demand price for that same instance.

Once costs are appropriately allocated across individual workloads with this framework, they can then be easily aggregated by any Kubernetes concept, such as namespace, label, annotation or controller.

## Kubernetes Cost Monitoring

With costs allocated by Kubernetes concept (pod or controller) you can begin to accurately map spend to any internal business concept, such as team, product, department or cost center. It’s common practice for organizations to segment team workloads by Kubernetes namespace, whereas others may use concepts like Kubernetes labels or annotations to identify which team a workload belongs to.

Another key element for cost monitoring across different applications, teams, etc. is determining who should pay for idle or slack capacity. This specifically refers to unused cluster resources that are still being billed to your company. Often these are either billed to a central infrastructure cost center or distributed proportionally to application teams. Assigning these costs to the team(s) responsible for provisioning decisions has shown to have positive results by aligning the incentive to have an efficiently sized cluster.

## Reconciling to Cloud Bill

Kubernetes provides a wealth of real-time data. This can be used to give developers access to immediate cost metrics. While this real-time data is often precise, it may not perfectly correspond to a cloud provider’s billing data. For example, when determining the hourly rate of an AWS spot node, users need to wait on either the Spot data feed or the Cost & Usage Report to determine exact market rates. For billing and chargeback purposes, you should reconcile data to your actual bill.

![Image 03](images/rancher_blog_image03.png)

## Get Better Visibility & Governance with Kubecost

We’ve looked at how you can directly observe data to calculate the cost of Kubernetes workloads. Another option is to leverage [Kubecost](https://kubecost.com/), a cost and capacity management solution built on open source that provides visibility across Kubernetes environments. Kubecost provides cost visibility and insights across Kubernetes workloads as well as the related managed services they consume, such as S3 or RDS. This product collects real-time data from Kubernetes and also reconciles with your cloud billing data to reflect the actual prices you have paid.

![Image 04](images/rancher_blog_image04.png)

A Kubecost screenshot showing cost by Kubernetes cost by namespace

With a solution like Kubecost in place, you can empower application engineers to make informed real-time decisions and start to implement immediate and long-term practices to optimize and govern cloud spend. This includes adopting cost optimization insights without risking performance, implementing Kubernetes budgets and alerts, showback/chargeback programs or even cost-based automation.

Kubecost community version is available for free with all of these features described – and you can find the Kubecost Helm chart in the Rancher App Catalog. Rancher gives you broad visibility and control; Kubecost gives you direct insight into spend and how to optimize. Together they provide a complete cost management story for teams using Kubernetes. To learn more about how to gain visibility into your Kubernetes costs, [join our Master Class](https://info.rancher.com/kubernetes-master-class-oct13-2020) on Kubernetes Cost Allocation and Visibility, Tuesday, October 13, at 2pm ET.Join The Master Class: Kubernetes Cost Allocation and Visibility, Tuesday, October 13 at 2pm ET [Register Now](https://info.rancher.com/kubernetes-master-class-oct13-2020)
