---
title: "Understanding Kubernetes RBAC"
date: 2017-11-22T11:28:00
slug: "understanding-kubernetes-rbac"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["security"]
content_type: "explainer"
draft: false
migration:
  wp_id: 87237
  original_url: "https://www.suse.com/c/rancher_blog/understanding-kubernetes-rbac/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Kubernetes 2017 RBAC examples"
  redirect_target: ""
---

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform. [Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture) Update: This topic was addressed again and updated by Craig Jellick in [“Understanding Authentication & Authorization in Rancher 2.0”](https://rancher.com/blog/2018/2018-05-04-authentication-authorization-rancher2/).

The general availability (GA) release of [Rancher 2.0](https://rancher.com/rancher2-0/) draws closer by the day. In this

post, we’ll explore the fine control you will have over your Rancher 2.0

deployments when you leverage the role-based access control (RBAC) that

Kubernetes brings to the platform. Kubernetes introduced RBAC in 1.6 and

has improved it in both 1.7 and 1.8. The Internet has many articles

about how to activate and configure it, but I believe that we should

know *why* we are doing things before we start doing them. For this

post, I’ll take you back to a core concept of access control known as

AAA (spoken as “triple A”). AAA defines the procedure for granting

access to an application, network, building, or any other system as the

combination of three components: authentication, authorization, and

accounting. It is from these components that it derives its name, and

each component satisfies a different requirement for ensuring that the

requestor is permitted to carry out an action.

## Authentication

It’s important to know *who* is requesting access. We ask requestors to

provide something that proves they are who they say that they are, such

as a username and password, a one-time password from an MFA/2FA token, a

fingerprint or retina scan, or something else that only that person

would know or be able to access. Interestingly, the best type of

multi-factor authentication (MFA) is a combination of something you

*know* with something you *have* or something you *are*. The objective

of MFA is to make it difficult for an attacker to possess both things at

the same time. This means that password managers which combine an MFA

token with the password record are defeating the purpose of MFA –

someone need only compromise the master password to gain access to both

pieces. None of this is designed to withstand [rubber-hose cryptanalysis](https://en.wikipedia.org/wiki/Rubber-hose_cryptanalysis),

but we try.

## Authorization

Once we believe that people are who they say they are, we move on to

defining what they can do. This happens with a policy that matches

individuals to roles. Within a role are permissions that grant or deny

access to other resources. A role can apply to multiple people, and a

single person can exist in multiple roles. Generally, though not a

Universal constant, a role corresponds to a group with access, such as

“Admins,” “Users,” or “Developers.” When constructing policies for

authorization, collecting them into roles makes it easier to maintain

the policies over time. Even if a user is the sole member of a role, you

don’t know that the role won’t have more members in the future. Simplify

your world by always creating roles that apply to groups and then

controlling role membership via group membership. In the case of

Kubernetes RBAC, a role can apply to an individual, a group of

individuals, or service accounts. Groups are defined by the

authentication component, and group membership is set when

authentication completes. Group membership is only a string value, so

the authentication component must set this string correctly. Kubernetes

will only check for the presence of the string; it trusts the

authentication provider.

## Accounting

Accounting is the process of recording who did what on the system. You

can use this component for auditing, forensics, or for chargeback

billing. Kubernetes provides accounting in two forms: Legacy (introduced

in 1.6) and Advanced (the default in 1.8). Even if you’re already using

Legacy auditing, migrating to Advanced will give you better output and

more detail in what you do and don’t record. Auditing is a critical

component of AAA, but it exists independently from RBAC. I encourage you

to [review the documentation](https://kubernetes.io/docs/tasks/debug-application-cluster/audit/)

to activate it within your cluster.

## Kubernetes Resources

Kubernetes defines two resources for roles: `Role` and `ClusterRole`. It

also defines two resources for connecting members (called *subjects*) to

those roles: `RoleBinding` and `ClusterRoleBinding`. The difference

between a resource that starts with *Cluster* and a resource that does

not is the scope of the object. Cluster-prefixed objects apply globally

to all namespaces in the cluster. Those that do not start with *Cluster*

require a namespace key and only apply to that namespace. It is possible

to define a `ClusterRole` as a policy and then apply it to a

`RoleBinding`. Doing this restricts the scope of that role to the

namespace in the `RoleBinding`. Both `Role` and `ClusterRole` define

verbs that act on resources. For example, you might define that an

account for a monitoring system has read-only access to pods in one

namespace. For that you would use a `Role`:

```
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: default
  name: monitor-pods
rules:
- apiGroups: [""] # "" indicates the core API group
  resources: ["pods", “pods/log”]
  verbs: ["get", "list"]
```

You would assign this role to the monitoring account using a

`RoleBinding`:

```
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: monitor-pods
  namespace: default
subjects:
  kind: Group
  name: monitoring
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: monitor-pods
  apiGroup: rbac.authorization.k8s.io
```

If you wished to define this role across all namespaces, you would use a

`ClusterRole` and a `ClusterRoleBinding`, removing the references to the

namespace:

```
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: monitor-pods
rules:
- apiGroups: [""] # "" indicates the core API group
  resources: ["pods", “pods/log”]
  verbs: ["get", "list"]
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: monitor-pods
subjects:
  kind: Group
  name: monitoring
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: monitor-pods
  apiGroup: rbac.authorization.k8s.io
```

The `apiGroups` key defines the location in the API where the resources

are found. If you provide an empty value in this list, it means the

*core* API group. Other resources live outside of the core API group. If

you use `CustomResourceDefinitions` in your environment, you can

reference those here as well. Please read the [API Reference](https://kubernetes.io/docs/reference/) for more information.

## Default Cluster Roles

If you’re concerned about the complexity of roles but still want to

implement RBAC in your cluster, you can start by using default cluster

roles provided automatically by Kubernetes. These are visible in the

output of `kubectl get clusterrole`, and four that you can use right

away are:

- cluster-admin
- admin
- edit
- view

With these roles, you can start to define who can interact with your

cluster and in what way, and if you follow the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege),

you will grant additional privileges as necessary for work to proceed.

Running `kubectl describe clusterrole {name}` will show you information

about the `ClusterRole`, and if you get the information with `-o yaml`,

you can copy it, edit it, and create new `Roles` and `ClusterRoles` for

your users and resources.

### Next Steps

RBAC changes how you approach security in the cluster. You now have the

tools to activate granular security, but as you move into using them,

move slowly, test, and experiment in a safe environment before you

modify the rules that control your production environment. Kubernetes

has [reference documentation](https://kubernetes.io/docs/admin/authorization/rbac/)

available about RBAC and its implementation, but like all things

Kubernetes, you might find the information overwhelming. Two other

articles that give real-world examples are from

[Bitnami](https://docs.bitnami.com/kubernetes/how-to/configure-rbac-in-your-kubernetes-cluster/)

and [Antoine Cotten](https://acotten.com/post/kube17-security). Both

explore use cases in greater depth than the Kubernetes documentation,

and the latter includes a section on auditing. For information on how

Rancher integrates with Kubernetes RBAC, our own Hussein Galal wrote an

[article](https://rancher.com/kubernetes-authentication-in-rancher-and-rbac/)

in September that explains how Rancher environment roles translate to

Kubernetes ClusterRoles. It also covers how to define groups in

Kubernetes that correspond to Rancher external authentication providers,

such as GitHub or AD. You can also join us

on November 30, 2017, when Darren Shepherd and Shannon Williams will be

demonstrating how to manage Kubernetes clusters with [Rancher 2.0](https://rancher.com/rancher2-0/). Our Meetups are always exciting,

with live demos and great feedback, so

[register](https://info.rancher.com/november-2017-meetup) and come learn!

### About the Author

![](images/rancher_blog_IMG_2323-231x300.jpg)Adrian Goins is a

field engineer for Rancher Labs who resides in Chile and likes to put

out fires in his free time. He loves Rancher so much that he can’t

contain himself.A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform. [Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)
