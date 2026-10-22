---
title: "Load-Balancing in Kubernetes"
date: 2017-08-14T11:11:00
slug: "load-balancing-in-kubernetes"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["networking"]
content_type: "explainer"
draft: false
migration:
  wp_id: 86793
  original_url: "https://www.suse.com/c/rancher_blog/load-balancing-in-kubernetes/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Pre 2018 Kubernetes load balancing"
  redirect_target: ""
---

Take a deep dive into Best Practices in Kubernetes NetworkingFrom overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options. [Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/) Update (June 2018): Engineer Alena Prokharchyk revisited this topic and showed useful and easy ways to load balance with Kubernetes in a recent blog post.

Kubernetes is the container orchestration system of choice for many

enterprise deployments. That’s a tribute to its reliability,

flexibility, and broad range of features. In this post, we’re going to

take a closer look at how Kubernetes handles a very common and very

necessary job: load balancing. Load balancing is a relatively

straightforward task in many non-container environments (i.e., balancing

between servers), but it involves a bit of special handling when it

comes to containers.

### Managing Containers

To understand Kubernetes load balancing, you first have to understand

how Kubernetes organizes containers. Since containers typically perform

specific services or sets of services, it makes sense to look at them in

terms of the services they provide, rather than individual instances of

a service (i.e., a single container). In essence, this is what

Kubernetes does.

#### **Placing Them in Pods**

In Kubernetes, the pod serves as a kind of basic, functional unit. A pod

is a set of containers, along with their shared volumes. The containers

are generally closely related in terms of function and services

provided.

Pods that have the same set of functions are abstracted into sets,

called services. It is these services which the client of a

Kubernetes-based application accesses; the service stands in for the

individual pods, which in turn manage access to the containers that make

them up, leaving the client insulated from the containers themselves.

##### Take a deep dive into Best Practices in Kubernetes Networking

![]()

From overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options.

[Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/)

### Managing Pods

Now, let’s take a look at some of the gory details. Pods are routinely

created and destroyed by Kubernetes, and are not designed to be

persistent entities. Every pod has its own IP address (localhost-based),

UID, and port; new pods, whether they are duplicates of current or

previous pods, are assigned new UIDs and IP addresses. Within each pod,

communication between containers is possible, but direct communication

with containers in different pods is not possible.

##### Take a deep dive into Best Practices in Kubernetes Networking

![]()

From overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options.

[Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/)

### Letting Kubernetes Handle Things

Kubernetes uses its own built-in tools to manage communication with

individual pods. This means that under ordinary circumstances, it is

sufficient to rely on Kubernetes to keep track of pods internally,

without worrying about the creation, deletion, or replication of

individual pods. There may be times, however, when it is necessary for

at least some internal elements of an application managed by Kubernetes

to be visible to the underlying network. When this happens, the method

of exposure must take into account the lack of persistent IP addresses.

### Pods and Nodes

In many respects, Kubernetes can be seen as a pod-management system as

much as a container-management system; much of its infrastructure deals

with containers at the pod level, rather than at the container level. In

terms of internal Kubernetes management, the level of organization above

the pod is the node, a virtual machine which serves as the deployment

environment for the pods, and which contains resources for managing and

communicating with them. Nodes can handle the creation, destruction, and

replacement/redeployment of pods internally. Nodes themselves can also

be created, destroyed, and redeployed. At the node and pod levels,

functions such as creation, destruction, redeployment, use, and scaling

are handled by internal processes called controllers.

### Services as Dispatchers

That’s how Kubernetes handles containers and pods at the management

level. But as we mentioned above, it also abstracts functionally

related/identical pods into services, and it is at the service level

that external clients and other elements of the application interact

with pods. Services have IP addresses (used internally by Kubernetes)

which are relatively stable. When a program element needs to make use of

the functions abstracted by the service, it makes a request to the

service, rather than an individual pod. The service then acts as a

dispatcher, assigning a pod to handle the request.

### Dispatching and Load Distribution

If by now, you’re thinking, “Hey, shouldn’t load balancing happen at

the dispatching level?“— You’re right. A service in Kubernetes is a

bit like a heavy-equipment pool, sending functionally identical machines

into the field as needed. And as part of the dispatching process, it

needs to manage availability and prevent resource bottlenecks.

#### **Let kube-proxy Do It**

The most basic type of load balancing in Kubernetes is actually load

distribution, which is easy to implement at the dispatch level.

Kubernetes uses two methods of load distribution, both of them operating

through a feature called kube-proxy, which manages the virtual IPs used

by services.

The default mode for kube-proxy is called iptables, which allows fairly

sophisticated rule-based IP management. The native method for load

distribution in iptables mode is random selection— an incoming request

goes to a randomly chosen pod within a service. The older (and former

default) kube-proxy mode is userspace, which uses round-robin load

distribution, allocating the next available pod on an IP list, then

rotating (or otherwise permuting) the list.

### Genuine Load Balancing: Ingress

As we mentioned above, however, neither of these methods is really load

balancing. For true load balancing, the most popular, and in many ways,

the most flexible method is Ingress, which operates by means of a

controller in a specialized Kubernetes pod. The controller includes an

Ingress resource—a set of rules governing traffic—and a daemon which

applies those rules. The controller has its own built-in features for

load balancing, with some reasonably sophisticated capabilities. You can

also include more complex load-balancing rules in an Ingress resource,

allowing you to take into account load-balancing features and

requirements for specific systems or vendors.

### LoadBalancer as an Alternative

As an alternative to Ingress, you can also use a service of the

LoadBalancer type, which uses a cloud service-based, external load

balancer. LoadBalancer can only be used with specific cloud service

providers, such as AWS, Azure, OpenStack, CloudStack, and Google Compute

Engine, and the capabilities of the balancer are provider-dependent.

Other load-balancing methods may be available from service providers, as

well as third parties.

### In the Balance, It’s Ingress

Currently, however, Ingress is the load-balancing method of choice.

Since it is essentially internal to Kubernetes, operating as a pod-based

controller, it has relatively unencumbered access to Kubernetes

functionality (unlike external load balancers, some of which may not

have good access at the pod level). The configurable rules contained in

an Ingress resource allow very detailed and highly granular load

balancing, which can be customized to suit both the functional

requirements of the application and the conditions under which it

operates.Take a deep dive into Best Practices in Kubernetes NetworkingFrom overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options. [Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/)
