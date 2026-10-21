---
title: "Addressing the Kubernetes dashboard and external IP proxying vulnerabilities"
date: 2019-01-04T09:04:00
slug: "addressing-the-kubernetes-dashboard-and-external-ip-proxying-vulnerabilities"
author: "Will Chan"
products: ["Rancher Manager"]
tags: ["security"]
content_type: "release"
draft: false
migration:
  wp_id: 85835
  original_url: "https://www.suse.com/c/rancher_blog/addressing-the-kubernetes-dashboard-and-external-ip-proxying-vulnerabilities/"
  disposition: migrate
  commercial: false
  outdated_reason: "2019 vulnerability advisory"
  redirect_target: ""
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)

Kubernetes announced two patches to address recently discovered security vulnerabilities for both Kubernetes and the Kubernetes dashboard. For more details of the announcements, see the [Security Impact of Kubernetes API server external IP address proxying](https://discuss.kubernetes.io/t/security-impact-of-kubernetes-api-server-external-ip-address-proxying/4072) and [Security release of dashboard v1.10.1 - CVE-2018-18264](https://discuss.kubernetes.io/t/security-release-of-dashboard-v1-10-1-cve-2018-18264/4069). Let’s take a deeper dive into each one and how they can affect your Rancher deployments.

## Accessing custom TLS certs via the kubernetes dashboard

The Kubernetes dashboard vulnerability (CVE-2018-18264) affects dashboard version v1.10.0 or older. It allows users the ability to “skip” the login process, assume the configured service account, and finally gaini access to the custom TLS certificate used by the dashboard. This CVE only applies to you if you have configured the Kubernetes dashboard to require login and configured it to leverage a custom TLS certificate.

### How does the vulnerability work?

This vulnerability can be explained in two parts.

One, the “skip” option that allows any user to bypass the login process, which was always enabled by default in v1.10.0 or older. This allows users to skip the login process altogether and assume the service account configured with the dashboard.

The second is that the service account configured with the dashboard must minimally have access to the custom TLS certificate (stored as a secret) in order to leverage it. The combination of an unauthenticated login and the ability for the dashboard to retrieve those secrets using the configured service account – compromises them.

With the dashboard v1.10.1 patch, the “skip” option is no longer enabled by default, and the ability for the dashboard to retrieve and display it in the UI has been disabled.

### What does it mean for Rancher 1.6.x and 2.x?

In Rancher 2.x, the Kubernetes dashboard is no longer enabled by default, as the Rancher 2.0 user interface is used as an alternative. Neither uses the dashboard code base and is not affected by this CVE. If you have deployed the dashboard on top of any Kubernetes clusters managed by Rancher, please follow  to patch your deployment.

In Rancher 1.6.x, the Kubernetes dashboard was included as part of every Kubernetes cluster environment. However, 1.6.x deployments are not affected, because the Rancher server acted as the authentication authority and proxy to the Kubernetes dashboard. It does not leverage the default Kubernetes dashboard login mechanism. Furthermore, the Rancher deployed Kubernetes dashboard does not use any custom TLS certificate. If you are on Rancher 1.6.x, there is no need to do anything.

## Kubernetes API server external IP address proxying

Now, let’s explore the second vulnerability as described by the announcement.

The Kubernetes API server offers the ability to proxy requests to pods or nodes using the node, pod, or service proxy API. By modifying the podIP or nodeIP directly, one can direct the proxy requests to any IP. This could then be leveraged to access IPs available to the network that the API server was deployed within. Although, Kubernetes has largely added checks since the release of v1.10 to mitigate this issue, it was only recently discovered that one path was not fully address. That path was the ability to direct the proxy to local addresses to the host that the API server was running on.

### How does it work?

By using the Kubernetes API, a user can request a connection to a pod or node using the node proxy, pod proxy, or service proxy API. Kubernetes takes this request, finds the associated IP of the podIP or nodeIP, and ultimately forwards that request to that IP. These are typically automatically assigned by Kubernetes. However, a cluster admin (or a different role with similar “super user” privileges) can update the podIP or nodeIP fields of a resource to point to any arbitrary IP.

This is largely not an issue because a “normal” user can not change the podIP or nodeIP of a resource. The podIP and nodeIP fields are in the status subresource of the pod and node resource. In order to update the status subresource an RBAC rule must be specifically granted. By default, no Kubernetes roles have access to the status subresource, except cluster admins and internal Kubernetes components (e.g. the kubelet, controller-manager, scheduler). In order to exploit this issue, you first must be granted a high level of access to the cluster.

The fix being issued today is that it was decided that an attack vector can exist in a setup where the control plane is managed separately from cluster. In this situation, a cluster admin is not assumed to have access to the host running the api server. Situations where this exist are in hosted kubernetes services you get from a cloud provider. In that situation a cluster admin could access address local to the API server by modifying the podIP/nodeIP to a local address such as 127.0.0.1. The fix issued today will prevent proxying to local addresses.

### What does this mean for Rancher users?

The default permissions for Rancher managed clusters only gives access to change the podIP or nodeIP field to cluster owners and members. When giving that role to a user, you must assume that user is allowed full access to any node in the cluster. All other default roles, such as project owners/members do not have access to these fields. The fix being issued today is largely for Kubernete clusters deployed where the control plane network differs from the network used from your applications. Kubernete clusters created in Rancher 1.6.x or 2.x assumes the default cluster admin has full access to the control plane nodes. If you are using a 2.x deployment and are using a hosted cloud provider (e.g. EKS, GKE, AKS), please check with them to see if this security is a concern as they own the control plane.

At Rancher, we want to make sure you are always updated with the latest security fixes and patches so the updated kubernetes versions v1.10.12, v1.11.6, and v1.12.4 that addresses this issue will be made available in Rancher v2.1.5 and v2.0.10.

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)
