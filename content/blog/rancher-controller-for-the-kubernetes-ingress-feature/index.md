---
title: "Rancher Controller for the Kubernetes Ingress Feature"
date: 2016-05-26T11:15:00
slug: "rancher-controller-for-the-kubernetes-ingress-feature"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["networking"]
content_type: "explainer"
draft: true
migration:
  wp_id: 86918
  original_url: "https://www.suse.com/c/rancher_blog/rancher-controller-for-the-kubernetes-ingress-feature/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x ingress controller"
  redirect_target: "rancher.com/blog (hub)"
---

[![Rancher and
Kubernetes](images/rancher_blog_Rancher-and-Kubernetes.png)](images/rancher_blog_Rancher-and-Kubernetes.png)
*Alena is a principal software engineer at Rancher Labs.*
Rancher has supported Kubernetes as one of our orchestration framework
options since March 2016. We’ve incorporated Kubernetes as an essential
element within Rancher. It is integrated with all of the core Rancher
capabilities to achieve the maximum advantage for both platforms.
Writing the Rancher ingress controller to backup the Kubernetes Ingress
feature is a good example of that. In this article, I will give a
high-level design overview of the feature and describe what steps need
to be taken to implement it from a developer’s point of view.

## What is the Ingress Resource in Kubernetes?

When it comes to orchestration for an app that has to perform under
heavy load, the Load Balancer (LB) is a key feature to be considered.
Three key LB functionalities will be of significant interest for a
majority of the apps that would be involved:

- Distributing traffic between backend servers - key feature of the
  LB.
- Providing a single entry point for users accessing the app.
- Ability to pick a particular LB route based on the target domain
  name and/or URL path as it applies to L7 balancers

The L7 LB functionality enables support for routing multiple domains (or
subdomains) to different hosts or clusters. [![Screen Shot 2016-05-13 at
10.07.55
AM](images/rancher_blog_Screen-Shot-2016-05-13-at-10.07.55-AM.png)](images/rancher_blog_Screen-Shot-2016-05-13-at-10.07.55-AM.png)
The Kubernetes Ingress resource allows you to define LB routing rules in
a clear and user friendly way. Ingress for host based routing is shown
below: [![Screen Shot 2016-05-13 at 10.21.31
AM](images/rancher_blog_Screen-Shot-2016-05-13-at-10.21.31-AM.png)](images/rancher_blog_Screen-Shot-2016-05-13-at-10.21.31-AM.png)
The Ingress for path based routing: [![Screen Shot 2016-05-13 at
10.21.39
AM](images/rancher_blog_Screen-Shot-2016-05-13-at-10.21.39-AM.png)](images/rancher_blog_Screen-Shot-2016-05-13-at-10.21.39-AM.png)
Most importantly, Kubernetes Ingress can be backed up by any other Load
Balancer in your configuration. However, the question that remains to be
answered is, how do you bridge the Ingress resource and your LB? You
would have to write something called an Ingress Controller which is an
app that will have to perform the following functions:

- Listen to Kubernetes server events.
- Deploy Load Balancer and program it with the routing rules defined
  in Ingress.
- IMPORTANT: configure Ingress “Address” field with the Public
  Endpoint of your Load Balancer.

Assuming the Ingress controller is up and running, and you are a
Kubernetes user that wants to balance traffic between apps, this is what
you need to do:

- Define an Ingress
- Wait for the Ingress controller to do its magic and fill in the
  Ingress Address field.
- Use the Ingress Address field as an entry point for the LB. Voila!

[![Screen Shot 2016-05-13 at 10.40.54
AM](images/rancher_blog_Screen-Shot-2016-05-13-at-10.40.54-AM.png)](images/rancher_blog_Screen-Shot-2016-05-13-at-10.40.54-AM.png)

## Rancher Ingress Controller

Load Balancer service has always been a key feature in Rancher.
We’ve continued to invest into its feature growth. It has support for
Host name routing, SSL offload and can be horizontally scaled. So,
choosing Rancher LB as a provider for Kubernetes Ingress doesn’t
require any changes to be done on the Rancher side. All that need be
done is to write the Ingress controller. Rancher Ingress controller is
a containerized microservice written in golang. It is deployed as a
part of the Kubernetes system stack in Rancher. That means it will have
access to both the Rancher and Kubernetes API servers: [![Screen Shot
2016-05-13 at 10.56.36
AM](images/rancher_blog_Screen-Shot-2016-05-13-at-10.56.36-AM.png)](images/rancher_blog_Screen-Shot-2016-05-13-at-10.56.36-AM.png)
The diagram below provides high level architecture of the Rancher
Ingress controller: [![Screen Shot 2016-05-13 at 11.15.56
AM](images/rancher_blog_Screen-Shot-2016-05-13-at-11.15.56-AM.png)](images/rancher_blog_Screen-Shot-2016-05-13-at-11.15.56-AM.png)
The **controller** from the diagram above would:

1. Listen for Kubernetes events like:

- Ingress Create/Remove/Update
- Backend service Create/Remove/Update
- Backend services’ endpoints Create/Remove/Update

1. Generate a Load Balancer config based on the information retrieved
   from Kubernetes
2. Pass it to the LB provider

The **provider** would

1. Create Rancher Load Balancer for every newly added Kubernetes Ingres
2. Remove Rancher Load Balancer when corresponding Ingress gets removed
3. Manage Rancher Load Balancer based on changes in the Ingress
   resource:

- Add/Remove/Update Rancher LB host name routing rules when Kubernetes
  Ingress changes
- Add/Remove backends when newKubernetes Services get defined/removed
  in Kubernetes Ingress
- Add/Remove backend servers when Kubernetes Services’ endpoints get
  changed

1. Retrieve Public Endpoint set on Rancher Load Balancer, and pass it
   back to **controller**.

- The **controller** would make an update call to Kubernetes Ingress
  to update it with the end point returned by the **provider:**

![Screen Shot 2016-05-13 at 11.27.47
AM](images/rancher_blog_Screen-Shot-2016-05-13-at-11.27.47-AM.png) The provider would
constantly monitor Rancher Load Balancer, and in case the LB instance
dies and gets recreated on another host by Rancher HA, the Kubernetes
Ingress endpoint will get updated with the new IP address.

## LB Public Endpoint and Backend Services’ Endpoints

I’ve used these terms quite a lot in the previous paragraphs, but need
to elaborate on them a bit more. What is a LB public endpoint? It’s an
IP address by which your LB can being accessed. In the context of this
blog, it is the IP address of the Host where the Rancher LB container is
deployed. However, it can also be multiple IP addresses if your LB is
scaled cross multiple hosts. Public endpoints get translated to the
Kubernetes Ingress **Address** field as shown below. [![Screen Shot
2016-05-13 at 1.25.57
PM](images/rancher_blog_Screen-Shot-2016-05-13-at-1.25.57-PM.png)](images/rancher_blog_Screen-Shot-2016-05-13-at-1.25.57-PM.png)
But, what acts as the real backend Kubernetes service endpoint which
is the backend IP address where LB is supposed to forward traffic to? Is
it the address of the host where the service is deployed? Or is it a
private IP address of the service’s container? The answer is that
it depends on the Load Balancer implementation. If your Ingress
controller uses an external LB provider (like for example [GCE
ingress-controller](https://github.com/kubernetes/contrib/tree/master/ingress/controllers/gce) does),
it would be the IP address of the host, and your backend Kubernetes
service has to have ”**type=NodePort**“. But, if your LB provider is
deployed in the Kubernetes cluster (like [Nginx
ingress-controller](https://github.com/kubernetes/contrib/tree/master/ingress/controllers/nginx) or [Rancher
ingress-controller](https://github.com/rancher/ingress-controller)), it
can be either the service clusterIP, or the set services’ Pod IPs.
Rancher Load Balancer balances between Kubernetes Services podIPs.

## Pluggable Load Balancer Provider Model

The **controller** has no knowledge about provider implementation. All
communications are done using Load Balancer Config, which is pretty
generic. I’ve chosen to use this model, as it makes it easy to re-use
the code base through:

- Re-use of the controller code by choosing a provider of your choice
- Re-use of the provider code by choosing a controller of your choice.

Provider and controller get defined as arguments passed to the
application entry point. Kubernetes is the default LB controller. The
Rancher Load Balancer is the default LB provider.

## Future Release Implementation

We’ve just released the first version of the Rancher
ingress-controller. We are planning to continue actively contributing
into it. Features to cover in the next release include:

- Horizontal scaling of the Rancher LB by defining scale in the
  Kubernetes Ingress metadata
- Non-standard http public port support. Today, we support default
  port 80, but also want the user to be able to decide which public
  port to use.
- TLS support

## Useful Links

[Kubernetes ingress
doc](http://kubernetes.io/docs/user-guide/ingress/) - here you can read
more on the Kubernetes Ingress Resource. rancher[Kubernetes ingress
controllers contrib github
repo](https://github.com/kubernetes/contrib/tree/master/ingress/controllers)
- very helpful for developers who want to contribute to Kubernetes, and
want to know best practices and common solutions. [Rancher ingress
controller github repo](https://github.com/rancher/ingress-controller) -
Rancher ingress controller github repo. [Rancher Ingress Controller
Documentation](https://docs.rancher.com/rancher/latest/en/kubernetes/ingress/)

[![Avatar](images/rancher_blog_Avatar-150x150.png)](https://cdn.rancher.com/wp-content/uploads/2015/04/21135821/Avatar.png)Alena
Prokharchyk If you have any questions or feedback, please contact me on
twitter: @lemonjet https://github.com/alena1108
