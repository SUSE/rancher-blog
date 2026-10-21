---
title: "Rancher 2.0 Now Feature Complete, Enters Final Beta Phase"
date: 2018-04-05T11:14:00
slug: "rancher-2-0-now-feature-complete-enters-final-beta-phase"
authors: ["Sheng Liang"]
products: ["Rancher Manager"]
tags: []
content_type: "release"
draft: false
migration:
  wp_id: 86887
  original_url: "https://www.suse.com/c/rancher_blog/rancher-2-0-now-feature-complete-enters-final-beta-phase/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.0 beta milestone"
  redirect_target: ""
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)

I’m excited to announce that today we achieved feature freeze on Rancher 2.0. This is an important milestone in our journey towards a GA release, which we’re targeting for the end of April. We have upstreamed all of the critical features into Rancher 2.0 master branch, and we are ready to enter the final beta phase focused on testing, documentation, and scalability.

We started 2.0 development more than a year ago. Major feature development and code refactoring continued even after we shipped the Tech Preview 1 release. The Rancher community responded very positively to Tech Preview 3, which we shipped in Q1 2018. Today’s release delivers the last major set of features in Rancher 2.0.

Rancher 2.0 is an enterprise Kubernetes platform that allows you to manage all Kubernetes distros, all Kubernetes clusters, on all clouds. It has three major components: Rancher Kubernetes Engine (RKE), Unified Cluster Management, and Workload Management.

Here is a summary of Rancher 2.0 features. You can find a more detailed list on the [Rancher 2.0 GitHub page](https://github.com/rancher/rancher/wiki/Rancher-2.0).

## Rancher Kubernetes Engine (RKE)

1. **Lightweight Kubernetes Installer**. Rancher embeds RKE to install Kubernetes clusters on vSphere clusters, bare metal servers, and cloud providers that do not yet support a managed Kubernetes service.
2. **Simple Kubernetes Operations**. Rancher supports ongoing operations of Kubernetes clusters, including, for example, cluster upgrade and etcd backup.
3. **Powering Rancher Server HA**. Rancher can be installed into an existing Kubernetes cluster, which could be a small RKE cluster created for the sole purpose of running the Rancher server.

## Unified Cluster Management

1. **Clusters and Node Management**. Rancher supports the ability to provision Kubernetes clusters hosted by a cloud provider (GKE, AKS, and shortly, EKS), created using RKE, or imported from an existing cluster you already have.
2. **Authentication**. Rancher supports local auth, Github, and AD/LDAP for all GKE, AKS, EKS, RKE, and imported clusters.
3. **User Management**. Rancher supports two default user types, admin and user, and the ability to define custom user types.
4. **Role Based Access Control (RBAC)**. – Rancher allows you to create your own global cluster roles that can be easily assigned to any users to manage Kubernetes clusters and projects. Rancher includes all out-of-the-box Kubernetes roles and the ability to customize your own roles. Each custom role can be assigned at a global, cluster, or project level.
5. **Project and Namespace Management**. – Users can create namespaces and assign them to projects. Projects are a new Rancher concept that allows you to group a set of namespaces and assign a set of user permissions on those namespaces.
6. **Pod Security Policies**. Rancher 2.0 allows users to create their own pod security policy or policies that can be applied to roles.
7. **Rancher CLI**. CLI supports all major Rancher 2.0 feature sets.

## Workload Management

1. **Workload UI**. Rancher is introducing a new Workload UI that will allow users to leverage the simplicity of the Rancher UI to create and manage their Kubernetes workloads.
2. **Helm Catalog Support**. Rancher 2.0 catalog is built on Helm charts.
3. **Alert Management**. Rancher 2.0 leverages the Prometheus AlertManager to send system and user level alerts to various notifiers (including Slack, Email, PagerDuty, and Webhooks.)
4. **Logging**. Rancher 2.0 installs Fluentd to collect stdout/err output or logs written to specific directories. A variety of log targets, including ElasticSearch, Splunk, Syslog, and Kafka, are supported.
5. **CI/CD Pipelines**. Rancher 2.0 includes a simple integrated pipeline feature that allows users to create pipelines within projects for continuous integration.

## Migration from Rancher 1.6 to Rancher 2.0

We originally planned to support both Rancher Compose files and Kubernetes YAML templates in Rancher 2.0. That would make migration from Rancher 1.6 to Rancher 2.0 easy: you can take your existing compose files and replay them on Rancher 2.0.

Unfortunately, we encountered a significant number of technical challenges in implementing a fully-compatible Rancher Compose experience on Kubernetes. Kubernetes supports many similar concepts as Cattle. There are often, however, important differences between the two that make an exact translation difficult. An earlier release of Rancher 2.0 TP1 resorted to translating Rancher Compose constructs to pods, bypassing Kubernetes orchestration all-together. Based on user feedback, however, we learned that was not the right solution. Instead we found out that a significant number of the Cattle community are interested in the capabilities of Kubernetes and it does not take that much effort to create Kubernetes YAML files from Rancher Compose because of the similarities between Cattle and Kubernetes.

We therefore decided to focus on supporting Kubernetes YAML templates alone in Rancher 2.0, and develop tools and practices to help Cattle community migrate to Kubernetes in the Rancher 2.1 timeframe. We will continue to support Rancher 1.6 for at least another year. We will take care of the needs of the Cattle user community as the nascent container industry continues to develop.

By embarking on the Rancher 2.0 project, we took on the monumental task of rebasing Rancher from Docker to Kubernetes. We rewrote all of the legacy Rancher 1.6 Java modules in Go, and in the process touched just about every other module in the system. Dozens of our core developers worked on the project at a time. The fact that so many developers can collaborate and move so quickly is a testament to the modularity and maturity of the Kubernetes platform. We are more confident than ever that Kubernetes will become the foundational platform for enterprise applications, and Rancher 2.0 will help make Kubernetes a reality in many organizations.

To see Rancher 2.0 in action, join us for our next Online Meetup: “[Managing Workloads on Kubernetes with Rancher 2.0](https://hubs.ly/H0bynv70)“

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)
