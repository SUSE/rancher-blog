---
title: "Kubernetes Authentication in Rancher and RBAC"
date: 2017-09-22T10:20:00
slug: "kubernetes-authentication-in-rancher-and-rbac"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["security"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86762
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-authentication-in-rancher-and-rbac/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.6 RBAC, superseded by 2.0 post"
  redirect_target: "docs.rancher.com"
---

Update: Craig Jellick updated this topic of Kubernetes RBAC for Rancher 2.0 [here](https://rancher.com/blog/2018/2018-05-04-authentication-authorization-rancher2/).

As of version 1.6.3, Rancher introduced the [Role-Based Access Control
(RBAC) feature](https://rancher.com/rbac-kubernetes-rancher/) in
Kubernetes. This feature allows admins to configure different policies
that allow or deny access for users and service accounts to Kubernetes
API resources. To better understand how the RBAC feature works, this
post will shed light on how authentication works with the Kubernetes
API, and how the RBAC authorization module works with authenticated
users.

### Authentication with Kubernetes in Rancher

Rancher uses [Webhook Token
Authentication](https://kubernetes.io/docs/admin/authentication/#webhook-token-authentication)
strategy to authenticate user’s bearer tokens. First, a user
authenticates with Rancher and navigates to the **Kubernetes > CLI**
tab to get the kube configuration file, which contains the bearer token.
Then, **kubectl** uses this token, along with the web hook
authentication remote service, to authenticate users with the Kubernetes
API: ![Diagram of Authentication with Kubernetes in
Rancher](images/rancher_blog_rancher-k8s-auth-1024x741.png) When the user
tries to authenticate with the Kubernetes API using the bearer token,
the authentication webhook communicates with the Rancher Kubernetes auth
service and sends an authentication review object containing the token.
Then, the Rancher Kubernetes auth service sends a review status that
specifies whether or not the user is authenticated. The review status
contains information about the user, including the name, uid, and
groups. The authorization module in the Kubernetes API uses this
information later to determine the access level for this user. Here’s an
example of an authentication request that Kubernetes sends to the
Rancher Kubernetes authentication service. **Authentication Request:**

```
          {
          "kind": "TokenReview",
          "apiVersion": "authentication.k8s.io/v1beta1",
          "Metad ata": {
               "creationTimestamp": null
               },
          "spec": {
          "token": "xxxxxxxxxxxxxxxxx"
                  },
          "status":{
                  "user": {}
                  }
          }
```

This Rancher Kubernetes auth service decides whether or not this user is
authenticated, and sends a response to Kubernetes. **Authentication
Response:**

```
          {
          "apiVersion": "authentication.k8s.io/v1beta1",
          "kind": "TokenReview",
          "status": {
               "authenticated": true,
               "user": {
                    "groups": [
                        ….
                        "system:masters"
                        ],
                    "username": "galal-hussein"
                    }
               }
          }
```

As you can see, because the environment owner sends this request, the
user is defined in the **system:masters** group, which already has
access to all resources in the Kubernetes cluster:

```
          kind: ClusterRoleBinding
          metadata:
           labels:
            kubernetes.io/bootstrapping: rbac-defaults
           name: cluster-admin
          roleRef:
            apiGroup: rbac.authorization.k8s.io
            kind: ClusterRole
            name: cluster-admin
           subjects:
           - apiGroup: rbac.authorization.k8s.io
            kind: Group
            name: system:masters
```

The **ClusterRole** “cluster-admin” resource allows access to all
Kubernetes resources in all API groups:

```
          apiVersion: rbac.authorization.k8s.io/v1beta1
          kind: ClusterRole
          metadata:
           labels:
             kubernetes.io/bootstrapping: rbac-defaults
           name: cluster-admin
          rules:
          - apiGroups:
           - '*'
           resources:
           - '*'
           verbs:
           - '*'
          - nonResourceURLs:
           - '*'
           verbs:
           - '*'
```

### The RBAC Authorization Module

After the request to the Kubernetes API is successfully authenticated,
the request must be authorized. The request to the API contains
information about the username of the requester, the requested action,
and the object the action affects. The RBAC authorization module defines
four top-level objects that control the authorization decisions for
authenticated users:

- [Roles]
- [ClusterRoles]
- [RoleBinding]
- [ClusterRoleBinding]

**Roles** and **ClusterRoles** both identify sets of permissions for
Kubernetes API resources. The only difference between them is that
**Roles** can be defined within the namespaces whereas **ClusterRoles**
are cluster wide. **RoleBindings** and **ClusterRoleBinding** assign the
defined roles to users, groups, or service accounts. Permissions also
can be granted within a namespace using **RoleBinding**, or cluster wide
using **ClusterRoleBinding**. Examples will be discussed in the
following section.

### Enable RBAC with Kubernetes in Rancher

To enable RBAC feature with fresh installation of Kubernetes in Rancher,
you can either edit the default environment or create a new [environment
template](https://rancher.com/docs/rancher/v1.6/en/environments/#what-is-an-environment-template).
In the Kubernetes environment options, you can enable RBAC or, if you’ve
already launched the Kubernetes infrastructure service, you can click
**Up to Date** to update the configuration options for Kubernetes.

### RBAC Examples

These examples assume that you already started Kubernetes with the RBAC
feature enabled, as explained in the previous section. It also assumes
that you enabled GitHub authentication with Rancher. As the owner of the
Kubernetes environment, you have full access over the Kubernetes API, as
we saw before, because the cluster-admin role is assigned by default to
the environment owner. on-admin users will not have access to any API
resources by default. Assuming that you added some GitHub users and
groups as members of the Kubernetes environment, and then tried to
access the Kubernetes API with them, you would get the following
message:

```
          > kubectl get services
          Error from server (Forbidden): the server does not allow access
          to the requested resource (get services)
```

To enable access for a GitHub organization across all Kubernetes
clusters, create the following **ClusterRole**:

```
           kind: ClusterRole
           apiVersion: rbac.authorization.k8s.io/v1beta1
           metadata:
            name: default-reader
           rules:
            - apiGroups: [""]
             resources:
              - services
             verbs: ["get", "watch", "list"]
            - nonResourceURLs: ["*"]
             verbs: ["get", "watch", "list"]
```

This role defines listing and getting access to the services resource.
At this point, the cluster role is not associated with any user or
group, so the following step is creating the **ClusterRoleBinding**:

```
           kind: ClusterRoleBinding
           apiVersion: rbac.authorization.k8s.io/v1beta1
           metadata:
            name: default-reader-role-binding
           subjects:
            - kind: Group
             name: "github_org:"
           roleRef:
            kind: ClusterRole
            name: default-reader
            apiGroup: rbac.authorization.k8s.io
```

The role binding specifies a GitHub organization group: “github\_org:“.
You will notice that when applying the role bindings to groups, Rancher
authentication has special syntax for each authentication type. For more
details, please refer to the [Rancher
documentation](https://rancher.com/docs/rancher/v1.6/en/kubernetes/rbac/#group-name-syntax).
After creating the role binding, you should be able to list only the
services for any user that belongs to this GitHub organization:

```
           > kubectl get pods
           Error from the server (Forbidden): the server does not allow access
           to the requested resource (get pods)

           > kubectl get service
           NAME        CLUSTER-IP  EXTERNAL-IP  PORT(S)  AGE
           kubernetes  10.43.0.1         443/TCP   42m
```
