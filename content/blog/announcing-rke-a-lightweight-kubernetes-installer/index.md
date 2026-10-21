---
title: "Announcing RKE, a Lightweight Kubernetes Installer"
date: 2017-11-29T09:01:00
slug: "announcing-rke-a-lightweight-kubernetes-installer"
author: "Rancher Admin"
products: ["RKE1"]
tags: ["installation"]
content_type: "release"
draft: true
migration:
  wp_id: 85802
  original_url: "https://www.suse.com/c/rancher_blog/announcing-rke-a-lightweight-kubernetes-installer/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RKE1 announcement, end of life"
  redirect_target: "/rke2"
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)

Today, we are announcing a new open-source project called the Rancher
Kubernetes Engine (RKE), our new Kubernetes installer. RKE is extremely
simple, lightning fast, and works everywhere.

## Why a new Kubernetes installer?

In the last two years, Rancher has become one of the most popular ways
to stand up and manage Kubernetes clusters. Users love Rancher as a
Kubernetes installer because it is very easy to use. Rancher fully
automates etcd, the Kubernetes master, and worker node operations.
Rancher 1.x, however, also implements container networking. Therefore, a
failure of the Rancher management plane could disrupt the operation of
the Kubernetes cluster. Users who want to stand up Kubernetes clusters
today have many choices of installers. Two of the most popular
installers we have encountered are
[kops](https://github.com/kubernetes/kops) and
[Kubespray](https://github.com/kubernetes-incubator/kubespray):

1. **Kops** is perhaps the most widely used Kubernetes installer. It is
   in fact much more than an installer. Kops prepares all required
   cloud resources, installs Kubernetes, and then wires up cloud
   monitoring services to ensure the continuing operation of the
   Kubernetes cluster. Kops is closely integrated with the underlying
   cloud infrastructure. Kops works the best on AWS. Support for other
   infrastructure platforms like GCE and vSphere is a work in progress.
2. **Kubespray** is a popular standalone Kubernetes installer written
   in Ansible. It can install a Kubernetes cluster on any servers. Even
   though Kubespray has some degree of integration with various cloud
   APIs, it is fundamentally cloud independent and can, therefore, work
   with any cloud, virtualization clusters, or bare-metal servers.
   Kubespray has grown to be a sophisticated project with participation
   from a large community of developers.

[Kubeadm](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/)
is another Kubernetes setup tool that comes with upstream Kubernetes.
Kubeadm, however, does not yet support capabilities like HA clusters.
Even though pieces of kubeadm code are used in projects like kops and
Kubespray, kubeadm is not ready as a production-grade Kubernetes
installer. [Rancher 2.0](https://rancher.com/rancher2-0/) is designed to
work with any Kubernetes clusters. We encourage users to leverage
cloud-hosted Kubernetes services like GKE and AKS. For users who want to
set up their own clusters, we considered incorporating either kops or
Kubespray into our product lineup. Kops does not suit our needs because
it does not work with all cloud providers. Kubespray is in fact very
close to what we want. We especially like how Kubespray can install
Kubernetes anywhere. In the end, we decided not to use Kubespray and
instead build our own lightweight installer for two reasons:

1. We can have a simpler system by starting from scratch and take
   advantage of many advances in Kubernetes itself.
2. We can have a faster installer by going with a container-based
   approach, just like how we installed Kubernetes in Rancher 1.6.

## How RKE Works

RKE is a standalone executable that reads from a cluster configuration
file and brings up, brings down, or upgrades a Kubernetes cluster. Here
is a sample configuration file:

```
---
auth:
  strategy: x509

network:
  plugin: flannel

ssh_key_path: /home/user/.ssh/id_rsa

nodes:
  - address: server1
    user: ubuntu
    role: [controlplane, etcd]
  - address: server2
    user: ubuntu
    role: [worker]

services:
  etcd:
    image: quay.io/coreos/etcd:latest
  kube-api:
    image: rancher/k8s:v1.8.3-rancher2
    service_cluster_ip_range: 10.233.0.0/18
    extra_args:
      v: 4
  kube-controller:
    image: rancher/k8s:v1.8.3-rancher2
    cluster_cidr: 10.233.64.0/18
    service_cluster_ip_range: 10.233.0.0/18
  scheduler:
    image: rancher/k8s:v1.8.3-rancher2
  kubelet:
    image: rancher/k8s:v1.8.3-rancher2
    cluster_domain: cluster.local
    cluster_dns_server: 10.233.0.3
    infra_container_image: gcr.io/google_containers/pause-amd64:3.0
  kubeproxy:
    image: rancher/k8s:v1.8.3-rancher2

addons: |-
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-nginx
      namespace: default
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80
```

We start the file by specifying authentication strategy, network model,
and local SSH key path. The main body of the cluster configuration file
consists of the following three parts:

1. The nodes section describes all the servers that make up the
   Kubernetes cluster. Each node assumes one or more of the three
   roles: controlplane, etcd, and worker. You can add or remove nodes
   in a Kubernetes cluster by changing the nodes section and rerunning
   the RKE command.
2. The services section describes all the system services that run on
   the Kubernetes cluster. RKE packages all system services as
   containers.
3. The add-ons section describes the user-level programs that run on
   the Kubernetes cluster. An RKE user, therefore, can specify the
   Kubernetes cluster configuration and application configuration in
   the same file.

RKE is not a long-running service that can monitor and operate the
Kubernetes cluster. RKE is designed to work in conjunction with a
full-fledged container management system like Rancher 2.0 or with a
stand-alone monitoring system like AWS CloudWatch, Datadog, or Sysdig.
You can then construct your own scripts to monitor the health of RKE
clusters.

## RKE as an Embedded Kubernetes Installer

People who build distributed applications have to deal with backend
databases, data access layers, clustering, and scaling. Instead of using
a traditional application server, developers are beginning to use
Kubernetes as a distributed application platform:

- They use etcd as the backend database.
- They use Kubernetes Custom Resource Definition (CRD) to as the data
  access layer, and they use `kubectl` to perform basic CRUD
  operations on their data model.
- They package their applications as containers and use Kubernetes for
  clustering and scaling.

Applications built this way are shipped to customers as Kubernetes YAML
files. Customers can run these applications easily if they already have
Kubernetes clusters running or have access to a cloud-hosted Kubernetes
service like GKE or AKS. But what happens to the customers who want to
install the applications on virtualized or bare-metal servers? An
application developer can address this need by bundling RKE into the
application as an embedded Kubernetes installer. The application install
can start by invoking RKE and create a Kubernetes cluster for the
customer. We are seeing a tremendous amount of interest to embed a
lightweight installer like RKE into distributed applications.

## Next Steps

You can download RKE
from [GitHub](https://github.com/rancher/rke/releases). I encourage you
to read the [blog post](https://rancher.com/an-introduction-to-rke/) by
Hussein Galal, who wrote a significant portion of RKE code, for a more
in-depth introduction to RKE. Join us
tomorrow for an Online Meetup where we’ll give a demo of RKE. Please
[sign up](https://info.rancher.com/november-2017-meetup) today.

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)
