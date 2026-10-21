---
title: "Rancher 2.5 Delivers Enhanced Full Lifecycle Management of EKS Clusters"
date: 2020-10-06T09:56:00
slug: "rancher-2-5-delivers-enhanced-full-lifecycle-management-of-eks-clusters"
author: "Bill Maxwell"
image: "images/rancher_blog_rancher-2-5-lifecycle-featured.png"
products: ["Rancher Manager"]
tags: ["cloud", "aws"]
content_type: "release"
draft: false
migration:
  wp_id: 86299
  original_url: "https://www.suse.com/c/rancher_blog/rancher-2-5-delivers-enhanced-full-lifecycle-management-of-eks-clusters/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.5 EKS announcement"
  redirect_target: ""
---

Discover what’s new in Rancher 2.5[Learn More](/products/rancher/2.5)

Amazon EKS is the most popular managed Kubernetes solution. DevOps teams can quickly spin up clusters in the cloud and get started with Kubernetes in a few clicks. As organizations embrace Kubernetes in the cloud, the challenge becomes managing clusters across multiple regions or accounts. At that point, organizations struggle to visualize all of their clusters. Additionally, security and operations teams have difficulty rolling out a consistent set of policies and configurations across the environment. This is where Rancher management can help ease the full lifecycle management of all your Amazon EKS clusters.

## Getting Started with Amazon EKS

In Rancher 2.5, we have made getting started with EKS even easier. You can now provision new EKS Clusters in AWS and configure public and private endpoints, the IP access list to the API, control plane logging, and secrets encryption with AWS Key Management Service (**KMS**). Also, in Rancher 2.5, Rancher provisions managed node groups supporting the latest Amazon Machine Images (AMIs), Auto Scaling group (ASG) parameters, and GPU settings. Operators can configure multiple node groups with different instance types to support multiple workloads on the cluster.

New Rancher users who have lots of EKS clusters can already use a new cluster registration workflow. When you register a cluster into Rancher 2.5, the cluster can be configured and upgraded using Rancher APIs. This allows teams to centralize their management workflows through a single management and provisioning interface going forward. Admins will be able to add, configure and remove managed node groups for the cluster.

## Monitor Your EKS Clusters and Applications with Rancher

Once Rancher manages your EKS clusters, operations and development teams have access to apps to simplify managing Kubernetes. Rancher can monitor your cluster and applications deployed on your EKS clusters. Users can configure their metric endpoints, alerts and Grafana dashboards, making it easy to monitor and visualize their applications. Application logs can be collected to common data stores like Elasticsearch and Splunk using Rancher's built-in logging tools. In addition to centralized authentication through Rancher, DevOps and security teams can perform CIS scans against their EKS clusters using the new [EKS-1.0 CIS Benchmark](https://aws.amazon.com/blogs/containers/introducing-cis-amazon-eks-benchmark/#:~:text=The%20newly%20developed%20CIS%20Amazon%20EKS%20Benchmark%20in%20version%201.0.&text=The%20EKS%20Benchmark%20is%20applicable,security%20configurations%20of%20Kubernetes%20components.). Operators can also leverage OPA Gatekeeper on EKS clusters to enforce policy on their Kubernetes clusters.

## What Rancher 2.5 Adds to Amazon EKS

Also, it is now possible to run the Rancher application on EKS clusters. Before Rancher 2.5, backups of the Rancher application required etcd snapshots of the management cluster. This caused problems for operators looking to run Rancher on hosted Kubernetes solutions like Amazon EKS because there are no etcd backups. In Rancher 2.5, a new backup restore operator can back up the Rancher management server data to S3 or a volume in the Kubernetes cluster. With this new backup utility, you can now safely run the Rancher management server on Amazon EKS clusters.

Amazon EKS out-of-the-box provides a solid Kubernetes foundation that eases the operational burdens of managing a Kubernetes control plane. With the right knowledge and a motivated team willing to deep dive into the CNCF landscape, organizations can create a solution to achieve full lifecycle management. By using Rancher 2.5 as a control plane, you'll have immediate access to the Lifecycle Management (LCM) capabilities and CNCF tools available to users of our popular on-prem distribution, RKE. In the table below, you can get an overview of what Rancher 2.5 brings to EKS.

![CONTINUOUS DELIVERY CHART](images/rancher_blog_rancher-2-5-lifecycle.png)

Discover what’s new in Rancher 2.5[Learn More](/products/rancher/2.5)
