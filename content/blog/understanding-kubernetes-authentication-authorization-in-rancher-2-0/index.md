---
title: "Understanding Kubernetes Authentication & Authorization in Rancher 2.0"
date: 2018-05-04T09:02:00
slug: "understanding-kubernetes-authentication-authorization-in-rancher-2-0"
author: "Rancher Admin"
products: ["Rancher Manager"]
tags: ["security"]
content_type: "explainer"
draft: false
migration:
  wp_id: 85815
  original_url: "https://www.suse.com/c/rancher_blog/understanding-kubernetes-authentication-authorization-in-rancher-2-0/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Rancher 2.0 era UI and auth providers"
  redirect_target: ""
---

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform. [Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture) As you may already know, Rancher 2.0 [recently](https://rancher.com/blog/2018/2018-05-01-rancher-ga-announcement-sheng-liang/) reached GA. One area we focused heavily on was authentication and authorization. By building on top of Kubernetes’ strong base and focusing on ease of use and simplicity, we’ve built a system that is both robust and user-friendly. It enables administrators to manage multi-cluster environments while also empowering end-users to get up and running quickly. This article will explain what we built and the benefits it provides to organizations, admins, and users.

Before we can dive into what Rancher brings to the table, let’s briefly review the Kubernetes concepts that make it all possible. This is not meant to be an exhaustive review; Much more detail on these concepts can be found [here](https://kubernetes.io/docs/admin/authentication/) and [here](https://kubernetes.io/docs/admin/authorization/rbac/).

## Authentication

To understand authentication in Kubernetes and how Rancher leverages it, one must understand the following key concepts: **authentication strategies**, **users and groups**, and **user impersonation**.

### Authentication Strategies

Kubernetes offers a variety of authentication strategies including: client certificates, OpenID Connect Tokens, Webhook Token Authentication, Authentication Proxy, Service Account Tokens, and several more. Each strategy has its benefits and drawbacks but ultimately, they are all responsible for asserting the identity of the user making an API call so that the Kubernetes RBAC framework can then decide if the caller is authorized to perform the requested action.

While the plethora of strategies available addresses most use cases, its important to note that configuring them requires precise control of the configuration and deployment of the Kubernetes control plane. Cloud providers such as Google with GKE typically lock this down and prevent users from configuring it to their liking. Rancher 2.0 addresses this, but that will be discussed later in the article.

### Users and Groups

Kubernetes has two types of users: service accounts and normal users. Service accounts are managed completely by Kubernetes while “normal” users are not managed by Kubernetes at all. In fact, Kubernetes does not have user or group API resources. Ultimately, normal users and groups manifest as opaque “subjects” in role bindings, against which permissions can be checked, but more on that later.

### User Impersonation

User impersonation in Kubernetes is the ability for one user (or service account) to act as another. A subject must explicitly have the “impersonate” privilege in order to be able to perform impersonation of other users. While this may seem like a fairly obscure and nuanced piece of functionality, it is actually critical to how Rancher has implemented authentication.

## Authorization

To understand authorization in Kubernetes and how Rancher builds on top of it, one must understand these concepts: roles, clusterRoles, roleBindings, and clusterRoleBindings. As their names imply, these concepts are very similar, but apply to different scopes.

A role is scoped to a namespace. That means it was created in a namespace and can only be referenced by a roleBinding inside that namespace. A roleBinding creates an association between a user, group, or service account (known as a subject in kubernetes) and a role in a namespace. It effectively says User X has Role Y in Namespace Z, or to give a concrete example: Sarah is allowed to create, update, and delete deployments in the “dev” namespace.

A clusterRole looks and acts very similar to a role. The only difference is that it is not namespaced. It is defined at the cluster level. Similarly, a clusterRoleBinding is the non-namespaced version of a roleBinding. When you create a clusterRoleBinding, you are giving the specified subject(s) those permissions across the entire cluster, in every namespace.

NOTE: A roleBinding can reference either a role or clusterRole. Regardless of the type of role it references, the permissions only apply to the namespace in which the rolebinding resides.

With this understanding of the underlying Kubernetes concepts in place, we can now discuss how Rancher uses and enhances them to create a robust and easy to use authentication and authorization system.

## Rancher Authentication and Authorization

One of our main goals for Rancher 2.0 is to help system administrators run multiple heterogeneous kubernetes clusters. Those clusters can come from any combination of cloud providers or on-prem solutions. This creates many interesting authentication and authorization challenges. The key ones we identified and have addressed are:

- How do you have a unified authentication experience across different types of clusters?
- How do you manage users and permissions across clusters?
- How do you enable a “self-service” approach to utilizing clusters while still maintaining an appropriate level of control?
- How do you prevent users from gaining too much access to the underlying infrastructure resources in environments of low trust?

Each of these challenges will be discussed below.

### Unified Authentication

To achieve a unified authentication experience that works across clusters, we designed the Rancher server as the central point for all authentication. **Administrators need only configure their authentication provider once in Rancher and it will be applied everywhere.** Rancher then acts as an authentication proxy sitting in front of all requests that go to the Kubernetes clusters.

Because most cloud providers do not expose the necessary hooks to plug into Kubernetes’ various authentication strategies, Rancher’s authentication proxy sits outside and independent of the clusters. It performs the necessary authentication, gathers the user’s identity and any groups, and then forwards the request to the appropriate cluster using user impersonation to act as that user. Standard Kubernetes bearer tokens are used as the means for authentication, so our proxy plugs seamlessly into existing Kubernetes tools such as kubectl.

### User Management

As previously stated, Kubernetes does not have a first-class user concept. Rancher, however, does. Users can be manually created by administrators or created on-demand when an authentication provider like GitHub is turned on and a user logs in for the first time. Applying lessons learned from Rancher 1.x, the local authentication provider is on by default and always on. This makes Rancher secure by default and provides a backup mechanism for accessing Rancher when your authentication provider has an outage.

Creating a first-class user resource that lives in the central Rancher server has many benefits. For example, administrators can now see and manipulate the access any particular user has across all clusters. It also gives Rancher the ability to manage resources specific to each user like system preferences, API tokens, and node templates. Finally, it makes managing permissions for the user simpler, which we’ll discuss next.

### RBAC Authorization

Before we get any deeper into a discussion of authorization, we must first introduce and discuss a key Rancher concept: the **project**. A project is a collection of namespaces that various policies can be applied to. These policies (not all of which made it into our initial GA release) include RBAC, network access, pod security, and quota management. A project “owns” namespaces and any RBAC bindings made for the project apply to all namespaces in the project. This key concept allows for the efficient segmentation and organization of clusters into smaller, more manageable chunks.

Rancher effectively has three tiers of roles or permissions for users: global, cluster, and project level. The global scope defines what you are allowed to do outside of individual clusters. For most, this will boil down to marking a subset of users or groups as “admins” and the rest as “normal” users. In addition to having full access to all clusters, admins are able to do things like configuring authentication providers and managing users. Normal users just have access to the clusters or projects that they own or have been invited to.

Rancher RBAC is built directly on top of Kubernetes RBAC (the role and binding concepts previously discuss). If you understand the Kubernetes concepts, Rancher RBAC is easy to understand. Essentially, we create templates of roles and bindings in the Rancher server and propagate them down to the appropriate clusters. As such, we have the following custom resources in the Rancher API: roleTemplates, clusterRoleTemplateBindings, and projectRoleTemplateBindings. Administrators can manage roleTemplates and cluster and project owners can use them to grant varying degrees of access to their clusters or projects.

### Self-service access

Rancher supports a self-service access model by default to help organizations empower their users to get more out of Kubernetes. A normal user can create their own cluster and become its owner. They are then the admin of that cluster and can grant access to other users and groups by making them cluster members. Once a user is a cluster member, she can create projects in the cluster and become the owner of those projects. As the project owner, she can invite others to become project members or owners. Project members are able to create namespaces and deploy workloads in the projects that they are a part of. You can see how this creates a system of self-service where users are able to get up and running quickly and easily.

A common question to this approach is, “What if I don’t want to let users create clusters or projects?”

There are several answers to that question. First, if they do not have access to infrastructure resources (meaning they cannot create VMs or don’t have keys to your organization’s cloud provider), then they cannot create functional clusters. Secondly, our RBAC system is designed to be configurable so that administrators can explicitly choose what users are able to do by default. Finally, a user can be added directly to a project without being made an explicit cluster member. This means they will not be able to create new projects; they’ll only be able to use the projects they were explicitly added to. In this way, Rancher enables organizations to empower their users while giving administrators the control they need.

### Controlling infrastructure level access

Many use cases require that users be limited in the types of containers that they can deploy and what those containers are allowed to do. To address this use case, Kubernetes has podSecurityPolicies. This is a very important feature, but it is difficult to use properly in its raw form. A full discussion of how it works and what it can do is beyond the scope of this article, but we can sum it up to this: podSecurityPolicies allow administrators to restrict the types of pods that can be deployed in a cluster. The most basic and easily understood example is that it can prevent users from deploying privileged containers, which closes a large security hole for many use cases.

Rancher not only supports podSecurityPolicies, but enhances the feature to greatly improve its usability. With Rancher, administrators can globally define a set of podSecurityPolicy templates that can be used across all clusters. Cluster owners can then assign a default policy to the cluster and manage exceptions to the default on a per-project basis. In other words, a cluster owner can say “all projects have a restricted policy that prevents them from deploying privileged containers except for these few special projects.” This feature allows for safer, more secure multi-tenant clusters.

## Conclusion

In summary, hopefully you can see that we put a lot of focus on authentication and authorization in Rancher 2.0. All of it is built on top of the rock solid foundation of Kubernetes’ underlying concepts. Rancher’s enhancements and extensions bring our signature focus on usability and simplicity to these concepts to create a very powerful combination.A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform. [Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)
