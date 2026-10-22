---
title: "Kubernetes: Securing API Access From the Outside Via Role-Based Access and Strong Authentication"
date: 2019-02-21T09:07:00
slug: "kubernetes-securing-api-access-from-the-outside-via-role-based-access-and-strong-authentication"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images-role-access-and-auth.svg"
products: ["Kubernetes (generic)"]
tags: ["security"]
content_type: "explainer"
draft: true
migration:
  wp_id: 85882
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-securing-api-access-from-the-outside-via-role-based-access-and-strong-authentication/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Kubernetes 1.8 and 1.11 details"
  redirect_target: "https://www.rancher.com/blog/understanding-kubernetes-rbac/"
---

Continue your education with Kubernetes Master ClassesLearn to navigate the modern development landscape with confidence and get started without leaving home.[Learn More](https://rancher.com/kubernetes-master-class/)

This is the first of a series of three articles focusing on Kubernetes security: the outside attack, the inside attack, and dealing with resource consumption or noisy neighbors.

[Kubernetes](https://rancher.com/kubernetes "Why is Kubernetes popular and what is it?") has become a popular cloud container orchestration system, providing a “platform for automating deployment, scaling and operations of application containers across clusters of hosts,” according to the Cloud Native Computing Foundation (CNCF). However, the general lack of awareness of security issues related to the Kubernetes environment can expose various components to attacks from both inside and outside the network clusters.

“Outside attacks presume that the attacker doesn’t already have access to the cluster, so they’re looking for ways to get in before trying to escalate privileges,” noted Adrian Goins, a Senior Solutions Architect with Rancher Labs, the company that makes Rancher, a complete container management platform for Kubernetes. “Internal attacks presume that the attacker already has some access to the cluster, so it’s important to make sure they don’t have the ability to easily do more than what they should be allowed to do,” he said.

## Locking Down the API Server, Kubelets

There are various components in a Kubernetes environment that are accessible to external access, including the application programming interface (API) server, kubelet and the data store. If not locked down or secured properly, these components can open the door to data breaches and system compromises.

Kubernetes provides an API interface for development, operations and security teams to interact with applications and the Kubernetes platform. Kubelet is a service that runs on nodes and reads the container manifests to ensure the defined containers are started and running. Kubernetes leverages the etcd distributed key-value store to save and replicate data used by Kubernetes across the entire cluster.
Basically, the Kubernetes systems that are most frequently compromised are those with no access controls in place at all. Kubernetes is easy to deploy and by default doesn’t have a lot of security built into it, Goins noted. For example, the container orchestration system did not have role-based access control capabilities until mid-2017.

One of the highlights of the Kubernetes 1.8 release was Role-Based Access Control (RBAC), an authorization mechanism for managing permissions around Kubernetes resources. RBAC allows configuration of flexible authorization policies that can be updated without cluster restarts.

“In a lot of Kubernetes deployments, once a compromise happens, a person can install and run whatever [software] they want using root level access,” Goins said. “Hackers and cyber criminals are looking to get into a system to escalate their privileges, pivot to other systems and start to collect information such as credit card and personal identification data.”

A security hole in Kubernetes, discovered in December 2018, known as the privilege escalation flaw (CVE-2018-1002105), illustrated how users could establish a connection through the Kubernetes API sever to a backend server. After establishing the connection, an attacker could send arbitrary requests over the network connection directly to backend cluster services, such as kubelets. The flaw allowed any user to gain full administrator privileges on any compute node in the cluster. Patches have been released to fix the security flaw in all supported versions of Kubernetes and are available in versions 1.10.11, 1.11.5 and 1.12.3.

## How Can Organizations Protect Kubernetes Clusters From Outside Attacks?

The first thing Kubernetes users need to do is secure external API access by shutting it down completely or wrapping it in some sort of strong authentication, Goins advises. To alleviate the threat of external attacks, information technology/security administrators must ensure that only the necessary Kubernetes services are exposed. Additionally, they must enforce authentication and configure the right network security policies for any exposed services.

“Unless you specify some flags on kubelet, its default mode of operation is to accept unauthenticated API requests,” Alexander Uricoli of Handy Technologies, [wrote in a blog](https://medium.com/handy-tech/analysis-of-a-kubernetes-hack-backdooring-through-kubelet-823be5c3d67c "Medium blog on Kubernetes Security") analyzing how a hacker infiltrated a Kubernetes cluster on a coworker’s personal server.

“It appears someone found a way to drop some crypto mining software on a running container and execute the process,” Uricoli said. The Kubernetes API server was publicly exposed to the internet but protected with certificate authentication.

As it turned out, the coworker’s server was publicly exposing the kubelet ports (tcp 10250 and tcp 10255). Although the problem was obvious, Uricoli noted, the infiltration should raise some questions about Kubernetes deployment. “If your users have network access to your nodes, then the kubelet API is a full-featured unauthenticated API backdoor to your cluster.” If users have gone through the trouble of enabling authentication and authorization via webhook, RBAC, or some other method, then they should also ensure kubelet is properly locked down.

The Center for Internet Security (CIS) advises users to deploy HTTPS for kubelet connections. “Connections from the API server to kubelets could potentially carry sensitive data such as secrets and keys. It is thus important to use in-transit encryption for any communication between the API server and kubelets,” according to the CIS [guide](https://www.cisecurity.org/benchmark/kubernetes/ "Center for Internet Security Guide") for establishing a secure configuration posture for Kubernetes 1.11.

Kubernetes users should disable anonymous requests to the API server. When enabled, requests that are not rejected by other configured authentication methods are treated as anonymous requests. Those requests are then processed by the API server. Kubernetes users should rely on authentication to authorize access and disallow anonymous requests, while organizations should implement controlled access based on the need to know, according to CIS.

Security controls to strengthen defenses for internal cluster users – RBAC, isolation and privilege limits – are just as important for protecting Kubernetes from outside attacks, Goins noted.

“If someone was to gain access to the cluster from outside using any internal user account, they’d instantly have full access,” he said. “So, it’s not to say that you need internal controls to protect from outside attack. It’s more that if you don’t have them and you get attacked, you’re done.”

*Next Blog:* Three ways to protect Kubernetes from inside attacks: role-based access, Kubernetes features such as logical isolation (Namespaces) and Rancher resources such as Projects.

Continue your education with Kubernetes Master ClassesLearn to navigate the modern development landscape with confidence and get started without leaving home.[Learn More](https://rancher.com/kubernetes-master-class/)
