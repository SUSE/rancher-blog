---
title: "Three Ways to Secure Kubernetes From Inside Threats"
date: 2019-02-27T09:43:00
slug: "three-ways-to-secure-kubernetes-from-inside-threats"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images-resource-consumption.png"
products: ["Kubernetes (generic)"]
tags: ["security"]
content_type: "explainer"
draft: false
migration:
  wp_id: 85924
  original_url: "https://www.suse.com/c/rancher_blog/three-ways-to-secure-kubernetes-from-inside-threats/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "PodSecurityPolicy likely covered"
  redirect_target: ""
---

Continue your education with Kubernetes Master ClassesLearn to navigate the modern development landscape with confidence and get started without leaving home. [Learn More](https://rancher.com/kubernetes-master-class/) *This is the second of a series of three articles focusing on Kubernetes security: [the outside attack](/blog/understanding-kubernetes-rbac/), the inside attack, and dealing with resource consumption or noisy neighbors.*

Inherently, Kubernetes clusters are multi-user. As a result, organizations want to ensure that cross-communication is protected via role-based access control, logical isolation and network policies.

A container orchestration system such as Kubernetes brings information technology operations and developers (DevOps) closer together, making it easier for teams to collaborate effectively and efficiently with each other. Most members of DevOps teams do not have malicious intent; however, there is still a need to ensure that if there is cross communication between applications, and if somebody happens to write bad code, the blast radius of an event is automatically contained.

## 1: Role-Based Access Control

The strategies for mitigating malicious threats to containers differ from securing physical servers. However, role-based access control ([RBAC](https://rancher.com/tags/rbac/)) is a vital security procedure, whether systems administrators are deploying multiple servers inside a data center or deploying virtual clusters within Kubernetes.

“Internally, you want to have some type of role-based access control in place that follows the rule of least privilege,” said Adrian Goins, a Senior Solutions Architect with Rancher Labs, the company that makes Rancher, a complete container management platform for Kubernetes.

“You’re giving users and service accounts access to only the resources they need to access, and only with the level of access appropriate for whatever it is that they need to do.” This access control extends down to not running container processes with root privileges.

[Rancher](https://rancher.com/what-is-rancher/what-rancher-adds-to-kubernetes/) interfaces with multiple backend providers for RBAC, simplifying the process for Kubernetes users. For example, a system administrator can deploy Rancher and go to the authentication tab to bring their organization’s Microsoft Active Directory data into Kubernetes. Immediately, Rancher pulls in all users and groups from Active Directory, and those groups are now available for use in roles that are then applied across all of the clusters that Rancher manages.

Typically, an administrator would have to manually configure those roles and duplicate them across every cluster. The effort might not be a problem for an organization with one or two clusters, but if a company has tens, hundreds, or more clusters, the likelihood for human error is very high. Something will invariably be missed, and the consequences can be dire.

Administrators can centralize roles across clusters, drilling down to give users access to particular clusters where they can only perform specific tasks. If someone leaves the organization, it’s as simple as deactivating their accounts inside of Active Directory. Once that is done, the account immediately loses privileges to every single cluster where they previously had access. Because Rancher acts as an authentication proxy for every cluster, administrators no longer need to provision or manage accounts in every provider where they deploy clusters.

## 2: Logical Isolation with Namespaces

In addition, applications deployed to clusters should make use of Namespaces, the logical isolation of resources to which admins can attach security policies. Namespaces segment cluster resources and can include quotas and default resource limits for the Pods that they contain. Although originally intended for use in environments with many users spread across multiple teams, or projects, the use of Namespaces is now recognized as a standard best practice within clusters.

By default, within Kubernetes, there is nothing that prevents two different teams with containers from talking with each other. However, it is possible within the Kubernetes role-based access control feature to restrict that communication.

“We can say containers in my Namespace are only allowed to talk to containers in my Namespace, but not another,” Goins said. Additionally, “we can say that I as a user am only allowed to talk to my Namespace, and you as a user are only allowed to talk to your Namespace.” That is security at the workload level and security at the user level. If done correctly, a user cannot even see that another workload exists.

This is multi-tenancy within a single cluster, a capability provided by Kubernetes. However, Rancher goes beyond Namespaces, incorporating a “Project” resource to help ease the administrative burden of clusters.

Within Rancher, Projects allow administrators to collect multiple Namespaces under a single entity. In the base version of Kubernetes, features such as RBAC or cluster resources are assigned to individual Namespaces. In clusters where multiple Namespaces require the same set of access rights, assigning these rights to each individual Namespace can become a tedious task. Even though all Namespaces require the same rights, there’s no way to apply those rights to all Namespaces in a single action. Administrators would have to repetitively assign these rights to each Namespace, Goins noted.

Rancher Projects solve this issue by allowing administrators to apply resources and access rights at the Project level. Each Namespace in the Project then inherits these resources and policies, so an administrator only assigns them to the Project once, rather than assigning them to each Namespace.

With Projects, administrators can perform actions such as assign users access to a group of Namespaces, assign users specific roles in a Project, assign resources to the Project and assign Pod Security Policies.

## 3: The NetworkPolicy Resource

NetworkPolicy is a Kubernetes resource that configures how Pods – a logical group of one or more containers with shared storage and network resources – can communicate with each other and other network endpoints.

By default, Pods are non-isolated, meaning they accept traffic from any source. “A NetworkPolicy acts like a software-based firewall between Pods running on a Kubernetes cluster,” Goins explained. “Administrators can create a ‘default’ isolation policy for a Namespace by creating a NetworkPolicy that selects all Pods, but doesn’t allow any incoming or outgoing traffic to those Pods.”

Additionally, administrators can configure which Pods can connect to each other. These policies can be detailed, allowing administrators to specify which Namespaces can communicate or choose port numbers to enforce each policy.

The NetworkPolicy resource requires a networking backend that supports the configuration, such as Calico, Canal, Romana or Weave. Simply creating the resource without a controller to implement it will have no effect, according to the Kubernetes documentation.

## Stopping the Inside Threat

Although there are some default tools available for deploying security within Kubernetes, many of them seem designed to prevent outside threats from reaching clusters. And even then, they can be difficult to scale. There are fewer defenses when looking to protect clusters from insider threats, whether from actual malicious insiders or simply preventing mistakes or bad coding from propagating.

Thankfully, solutions exist that have an eye toward keeping clusters safe from unauthorized inside access. Some of them, like Namespaces, exist within the Kubernetes framework, while others like Rancher’s Projects go beyond default settings for more precise management and control over the entire enterprise environment.

The point is not to give up or become discouraged regarding cybersecurity for internal resources. By following these three steps, it’s possible to gain all of the efficiency of using Kubernetes clusters alongside of tightly controlled insider access protection.

For further resources on [Kubernetes security](https://www.suse.com/c/best-practices-for-keeping-kubernetes-secure/), [watch](https://info.rancher.com/preventive-security-kubernetes-enterprise-deployments "Preventative Kubernetes Security Video and Demo") the training video on preventative security for Kubernetes deployments.

*Next up: Dealing with resource limitations. How to stop users from consuming too much in your Kubernetes environment.*Continue your education with Kubernetes Master ClassesLearn to navigate the modern development landscape with confidence and get started without leaving home. [Learn More](https://rancher.com/kubernetes-master-class/)
