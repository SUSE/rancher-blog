---
title: "Kubernetes: Tackling Resource Consumption"
date: 2019-06-18T09:07:00
slug: "kubernetes-tackling-resource-consumption"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images-role-access-and-auth.svg"
products: ["Kubernetes (generic)"]
tags: ["security", "multi-cluster"]
content_type: "explainer"
draft: false
migration:
  wp_id: 85880
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-tackling-resource-consumption/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

This is the third of a series of three articles focusing on Kubernetes security: the outside attack, the inside attack, and dealing with resource consumption or noisy neighbors.

A concern for many administrators setting up a multi-tenant Kubernetes cluster is how to prevent a co-tenant from becoming a “noisy neighbor,” one who monopolizes CPU, memory, storage and other resources. As a result, this noisy neighbor negatively impacts the performance of other users’ resources that share the infrastructure.

Keeping track of the resource usage of Kubernetes containers and Pods is an important function, not only to keep the container orchestration system running optimally and to reduce operating costs, but also to strengthen the overall security posture of Kubernetes.

Some operations teams might not consider resource consumption a security issue on par with protecting Kubernetes from internal and external cyberattacks, but they should. That’s because skilled hackers can find ways to exploit a poorly functioning infrastructure to access Kubernetes components, experts say.

“Security is not just, ‘don’t break into my house,’ but also, ‘how do I keep my house running nicely all the time,’” said Adrian Goins, a Senior Solutions Architect with Rancher Labs, the company that makes Rancher, a complete container management platform for Kubernetes.

Operations teams need to maximize resources consumed by Kubernetes Pods – a group of one or more containers with shared storage and network resources – to ensure optimal performance for every user and to monitor usage for cost allocations. “Usage equals cost,” Goins says, “because Kubernetes resources run on the underlying compute infrastructure of cloud providers like Amazon Web Services, Google or Microsoft. Even when a cluster runs on bare-metal physical infrastructure in a datacenter, excess usage costs money in hardware, power, and other resources.”

By default, containers are provisioned without any limits on the amount of resources they can consume. If the container does not operate efficiently, the organization deploying the container will pay for the excess. Thankfully, Kubernetes has features that help operations teams manage and optimize Kubernetes resource utilization capabilities.

## Managing Resources in Pods

When administrators define a Pod, they can optionally specify how much CPU and memory (RAM) each container needs. When containers have resource requests specified, the scheduler can make better decisions about which nodes to place Pods on. And when containers have their limits specified, contention for resources on a node can be handled in a specified manner, according to the Kubernetes documentation.

By default, all resources in a Kubernetes cluster are created in a default Namespace. Namespaces are a way to logically group cluster resources and include options for specifying resource quotas.

Administrators can set resource limits or quotas on a Namespace, stating that a workload or application running in the Namespace is allotted a certain amount of CPU, RAM or storage – the three resources within a Kubernetes cluster. “If launching another resource in the Namespace would exceed the quota, then nothing else gets to launch,” Goins noted.

“When you apply a resource quota, you are forcing everything that runs in that Namespace to set a resource limit for itself. There are two types of limits: a reservation and a maximum,” Goins explained. For example, with a reservation, an administrator can have a Kubernetes cluster allocate 128 megabytes of RAM for a WordPress site. For every WordPress Pod deployed, there will be a guaranteed 128 megabytes of RAM from the server itself. Consequently, if an administrator combined a resource request with a resource quota of one gigabyte, then users can only run eight WordPress Pods before they exceed their limit. After that, they won’t be able to tap into anymore RAM.

The second part of resource limitations is a maximum. An administrator can put in a resource request reservation of 128 megabytes and a maximum of 256 megabytes of RAM. “If a Pod exceeds more than 256 megabytes of RAM usage, Kubernetes will kill it and restart it,” Goins said. “Now you’re protected from runaway processes and noisy neighbors.”

## Projects and Resource Quotas

A platform such as Rancher is designed to make the management of Kubernetes easier by providing an intuitive interface and centralized management of tasks like the implementation of role descriptions at the global layer.

As mentioned in the previous article on insider threat protection, Rancher goes beyond Namespaces by including a Project resource that helps ease the administrative burden of clusters. Within Rancher, Projects allow administrators to manage multiple namespaces as a single entity. As a result, Rancher can apply resource quotas to Projects.

In a standard Kubernetes deployment, resource quotas are applied to individual Namespaces. However, administrators cannot apply the quota to namespaces simultaneously with a single action. Instead, the resource quota must be applied multiple times. In Rancher, an administrator applies a resource quota to the Project, and then the quota propagates to each Namespace. Kubernetes then enforces the admin’s limits using the native version of resource quotas. If administrators want to change the quota for a specific Namespace, they can override the previous quota.

## Fortifying and Optimizing Kubernetes

Kubernetes has become the container orchestration standard, prompting most cloud and virtualization vendors to offer it as standard infrastructure. However, the general lack of awareness of security issues related to the Kubernetes environment can expose various components to attacks from both inside and outside the network clusters.

The past two articles have offered some actionable steps organizations can take to strengthen Kubernetes from both external and internal cyber threats by using Kubernetes capabilities and container management solutions such as Rancher. Organizations should secure Kubernetes API access from the outside via role-based access control (RBAC) and strong authentication. And for insider protection, because Kubernetes clusters are multi-user, organizations will need to ensure that cross-communication is protected via RBAC, logical isolation and NetworkPolicies.

To protect against other tenants monopolizing CPU, memory, storage and other resources dragging down the performance of clusters, Kubernetes provides features such as resource limitation and quotas to help operations teams manage and optimize Kubernetes resource utilization capabilities.

Finally, there are some very efficient tools that can help with Kubernetes management and cluster protection beyond the available default settings. A platform like Rancher, a highly optimized container management solution built for organizations that deploy multiple clusters into production environments, makes it easier to manage and run Kubernetes everywhere. It can protect Kubernetes clusters from [outside hackers](https://rancher.com/blog/2019/kubernetes-security-outside-attacks), [insider threats](https://rancher.com/blog/2019/secure-kubernetes-from-inside-threads), and even noisy neighbors.

## Online Training in Kubernetes and Rancher

To see Rancher and Kubernetes in action, [join](https://rancher.com/training) the weekly intro to Rancher and Kubernetes online training sessions. Hosted by a Rancher and Kubernetes expert, these sessions are free to join and provide a great hands-on overview of both Kubernetes and the Kubernetes-management platform, Rancher.
