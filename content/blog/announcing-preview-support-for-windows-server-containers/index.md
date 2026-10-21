---
title: "Announcing Preview Support for Windows Server Containers"
date: 2019-05-14T09:05:00
slug: "announcing-preview-support-for-windows-server-containers"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_containers.svg"
products: ["Rancher Manager"]
tags: ["windows"]
content_type: "release"
draft: false
migration:
  wp_id: 85854
  original_url: "https://www.suse.com/c/rancher_blog/announcing-preview-support-for-windows-server-containers/"
  disposition: migrate
  commercial: false
  outdated_reason: "2019 Windows preview support"
  redirect_target: ""
---

Today we are announcing the support for Windows containers with Kubernetes 1.14 in Preview mode.

As many users may know, Rancher 2.1.0 supported Windows containers in experimental mode. Now that SIG Windows and Microsoft have announced the general availability of containers in Windows Server 2019 with Kubernetes 1.14, we have upgraded Rancher to both support the latest version of Windows containers (and Kubernetes) and after the preview is over, make it generally available.

## The need for Windows Containers

With countless workloads running on its many versions, Windows remains one of the most popular operating systems in datacenters.
With the rise of containers, DevOps teams have been able to simplify and speed up the delivery of their Linux applications. Windows based applications still had to be treated differently.
Whether the requirement is to quickly create and tear down always updated dev/test environments or to lift and shift the legacy applications to the cloud, support for Windows containers has been one of the most desired technologies in recent years.

## How Rancher supports Windows Containers

Users creating “Custom” clusters in Rancher will see an option of adding Windows or Linux nodes to their clusters. The etcd and control plane nodes can only be Linux nodes and our UI will auto-select that option for you. The worker nodes can be either Windows or Linux.
We recommend that the users create separate clusters for their Windows workloads. You may still need to add at least one Linux worker node (to run your Ingress, Rancher cluster agent, metrics server, etc.).
Flannel is available as the preferred network plugin option with both vxlan and host-gateway modes.

Creating and managing Windows Server 2019 containers in Rancher is fairly straightforward. Please refer to our documentation on how to get started.
However there are many requirements and limitations that users should be aware of:

1. You need Windows Server 2019 which comes with Docker EE-basic 18.09. You also need Kubernetes 1.14 and Rancher 2.3.0 Preview 1
2. For Windows nodes the host image must match the container base image. This means that every major upgrade of the host will require you to recreate your container images or the container may not function properly
3. Networking in Windows containers is exposed through CNI plugins. As of now, Flannel is the only supported network plugin
4. Rancher’s inbuilt Prometheus based monitoring won’t work for Windows
5. Etcd and Control plane nodes can be linux only. You also need at least 1 Linux worker for the cluster to function properly

## Conclusion

The general availability of Windows containers is an exciting development. While we acknowledge that there are a number of limitations and challenges in adopting this technology, we also see that our users have been waiting to containerize and modernize their Windows applications.
With Rancher 2.3.0 Preview 1, our goal is make this journey quick and easy. Here are all the links to get you started:
For Release Notes and installation steps, please visit <https://github.com/rancher/rancher/releases/tag/v2.3.0-alpha3>

## Additional Useful Links

- A blog post by Microsoft announcing the general availability can be found [here](https://cloudblogs.microsoft.com/opensource/2019/03/25/windows-server-containers-now-supported-kubernetes/)
- For Kubernetes documentation, please visit [Kubernetes documentation](https://kubernetes.io/docs/setup/windows/intro-windows-in-kubernetes/)
