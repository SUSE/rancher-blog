---
title: "Kubernetes on Azure: Deploy and Manage Your First Cluster in AKS"
date: 2020-04-14T09:52:00
slug: "kubernetes-on-azure-deploy-and-manage-your-first-cluster-in-aks"
author: "Rancher Admin"
image: "images/rancher_blog_kubernetes-azure-featured.png"
products: ["Kubernetes (generic)"]
tags: ["azure", "cloud"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 86191
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-on-azure-deploy-and-manage-your-first-cluster-in-aks/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "2020 AKS portal steps"
  redirect_target: ""
---

Most Kubernetes deployments live on the cloud. [According to the CNCF](https://www.cncf.io/blog/2018/08/29/cncf-survey-use-of-cloud-native-technologies-in-production-has-grown-over-200-percent/), while 63 percent of companies use AWS for Kubernetes, 29 percent are deploying Kubernetes on Azure, and the number is rapidly growing. Microsoft Azure provides mature Kubernetes tools, primarily the Azure Kubernetes Service (AKS).

In this post, we’ll show you how to run your first Kubernetes cluster on AKS, and how to manage enterprise Kubernetes deployments on AKS with Rancher.

In this article, you will learn:

- **What Is Kubernetes?**
- **Why Use Kubernetes in Azure?**
- **What Is Azure Kubernetes Service (AKS)?**
- **Deploy an Azure Kubernetes Service Cluster in AKS**
- **Using Rancher to Manage Containers on AKS**

## What Is Kubernetes?

Kubernetes (K8s) is a container orchestration tool you can use to manage your containerized applications and microservices. It is an open-source tool created by Google.

Kubernetes offers the following features:

- Self-healing and resilient infrastructure
- Zero-downtime deployments
- Rolling updates and rollback functionality
- Scaling and load-balancing

The purpose of Kubernetes is to reduce the complexity of managing container deployments at scale. You can use Kubernetes in almost any environment, including public and private cloud platforms and on-premises.

## Why Use Kubernetes in Azure?

When choosing a container orchestration tool, Kubernetes is an obvious choice. It is the most commonly used platform and is widely supported by many vendors, including Microsoft. If you are planning to deploy Kubernetes in a public cloud, there are a few reasons why Azure may be the best choice for you.

These reasons include:

- **Cloud-native application development**—Azure has a wide range of tools you can use to create and host cloud-native applications. It also includes integrated development environments for easy application deployment.
- **Existing Azure customers**—if you are already using Azure for your workloads, it is easier to add a container deployment to your environment.
- **Managed services and integrations**—Azure provides a [managed Kubernete](https://www.suse.com/c/ensuring-high-availability-with-cloud-managed-kubernetes/)s option you can use to streamline your deployment. It also supports a variety of integrations you can include.

If you are not yet using Azure, or are in the process of migration, Kubernetes can help you make this process easier. With containers, you can more easily lift and shift legacy applications. You can also more easily transfer applications from other cloud providers you may be using.

## What Is Azure Kubernetes Service (AKS)?

AKS is Azure’s managed Kubernetes option. It aims to reduce the operational overhead and expertise needed to deploy k8s to Azure. AKS manages the most basic tasks of Kubernetes for you, including:

- Health monitoring
- Maintenance and upgrades
- Management of masters

With this service, you are only responsible for managing your worker nodes. While the service itself is free you are also responsible for any costs associated with worker nodes, including storage and networking.

To use AKS, you can create clusters in the Azure Portal or with the Azure CLI. Alternatively, you can use templates along with Resource Manager or Terraform to deploy. Regardless of the method you choose, AKS deploys and configures your cluster and nodes for you. You also have the option of configuring additional features, such as Azure Active Directory integration, monitoring specifications, and advanced networking.

## Deploy an Azure Kubernetes Service Cluster in AKS

The following guide shows you how to create a cluster in AKS via the CLI. These steps have been adapted from the [Azure documentation](https://docs.microsoft.com/en-us/cli/azure/aks?view=azure-cli-latest#az-aks-create).

When you follow this process, you need to create an Azure Active Directory service principal to enable your cluster to interact with your Azure resources. This is done automatically if you do not specify a principal.

In the below example, the automatically created principal is granted access to your Azure Container Registry instance. You can customize what resources are attached by changing this value.

```
az aks create

   --resource-group {Resource group name}

   --name {Cluster name}

   --node-count 2

   --generate-ssh-keys

   --attach-acr {ACR name}
```

The creation process takes a few minutes. Once complete, you are provided a JSON file with information about your deployment.

### Install the Kubernetes CLI

Once your cluster is created, you can connect to it from your local machine, using kubectl. kubectl is the built-in CLI for k8s.

This tool is already installed for you if you are working with Azure Cloud Shell. If not, you can install it manually with the following command:

az aks install-cli

### Connect to your cluster using kubectl

Next, you need to configure kubectl. This requires getting AKS credentials. You can obtain these credential with the following command:

```
az aks get-credentials --resource-group {Resource group name} --name {Cluster name}
```

Once credentials are obtained, you need to verify that kubectl can successfully connect to your cluster. You can do this with the following command:

```
$ kubectl get nodes
```

This will result in an output such as the one below:

```
NAME                  STATUS   ROLES   AGE   VERSION

Aks-nodepool-test     Ready    agent   50m   v1.14
```

## Using Rancher to Manage Containers on AKS

Although feature-rich and undeniably convenient, AKS isn’t the best fit for every organization or use case. By running containers in Azure/AKS for all their Kubernetes needs, enterprises are locked into a single vendor ecosystem and for most, an unnegotiable cost.

In fact, 81 percent of respondents in a [Gartner survey of public cloud users](https://www.gartner.com/smarterwithgartner/why-organizations-choose-a-multicloud-strategy/) revealed that they are working with two or more providers. As such, multi-cloud has become the “new normal.” Operating containers on a range of platforms, such as multiple cloud platforms or hybrid environments, makes orchestration and management more complex. If you are planning to use AKS in addition to other deployments, Rancher can help you standardize and centralize your configurations.

By abstracting the management control plan from a particular cloud provider and architecting cloud-native applications to run on any certified Kubernetes distributions, organizations gain application portability. They also gain cycles that would have been wasted on platform-specific configurations, network interfaces and management workflows.

Rancher includes a variety of features to make your deployments simpler, including:

- **Centralized user authentication & RBAC** — integrates with Active Directory, LDAP or SAML-based authentication services. Centralized permissions management makes it easier to ensure regulatory compliance, reduces maintenance time, and enables greater control over your deployments.
- **Intuitive user interface** — centralized UI enables you to quickly and easily manage deployments and launch applications. This supports agile workflows by enabling DevOps teams to focus on application development and deployment rather than k8s specifics.
- **Enhanced cluster security** — you can define security policies and instantly apply policies to your clusters. This provides centralized control over how users and workloads access and interact with your resources.
- **Global catalog & multi-cluster apps** — includes global application catalogs that you can use across your clusters. This helps simplify multi-cloud deployments and eases the workloads on operations teams.
- **Streamlined day-2 operations** — includes built-in integrations for day-2 operations, including Istio service mesh, Prometheus and Grafana for observability, Fluentd for logging, and Longhorn for persistent, highly-available storage.

Rancher does all this without locking you in to yet another vendor. [Learn more](https://rancher.com/products/rancher/) about the Rancher platform.
