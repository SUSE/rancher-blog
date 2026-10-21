---
title: "Load Balancing Traffic on Kubernetes with Rancher"
date: 2018-06-08T09:02:00
slug: "load-balancing-traffic-on-kubernetes-with-rancher"
author: "Rancher Admin"
products: ["Rancher Manager"]
tags: ["networking"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 85818
  original_url: "https://www.suse.com/c/rancher_blog/load-balancing-traffic-on-kubernetes-with-rancher/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Rancher 2.0 UI and ingress steps"
  redirect_target: ""
---

Build a CI/CD Pipeline with Kubernetes and RancherRecorded Online Meetup of best practices and tools for building pipelines with containers and kubernetes.[Watch the training](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/)

When it comes to containerizing user applications and deploying them on Kubernetes, incremental design is beneficial. First you figure out how to package your application into a container. Then, decide on a deployment model – do you want one container or multiple ones – any other scheduling rules, and configuring liveness and readines probes so that if the application goes down, Kubernetes can safely restore it.

The next step would be to expose the workload internally and/or externally, so that the workload can be reached by microservices in the same Kubernetes cluster, or - if it’s a user facing app - from the internet.

And as your application gets bigger, providing it with Load Balanced access becomes essential. This article focuses on various use cases requiring Load Balancers, and fun and easy ways to achieve load balancing with Kubernetes and Rancher.

## Services - The building block of Kubernetes Load Balancing

Once you have your application running in Kubernetes, its’ scheduler makes sure that you have the number of desired pods always running. This means that application pods are created and deleted unexpectedly and you should not rely on a particular pod. However, you do need to be able to access your application in a predictable manner. And to do that, Kubernetes provides the simplest form of load balancing traffic, namely a **Service**.

A Kubernetes Service is an abstraction which defines a logical set of Pods and a policy by which to access them - sometimes called a micro-service. The set of Pods targeted by a Service is (usually) determined by a Label Selector.

For example if you have a backend application with 3 Pods, those pods are fungible, frontends do not care which backend they use. While the actual Pods that compose the backend set may change, the frontend clients should not need to be aware of that or keep track of the list of backends themselves. The Service abstraction enables this decoupling.

In all of the following examples, the first thing created behind the scenes is the Service. Meaning that the logical set of Pods, that represents an application, is exposed with an IP address via a Service. Only after a Service is created internally in Kubernetes, the cloud provider creates an external facing Load Balancer and it is instructed to forward the traffic to the newly created Service.

## L4 Load Balancing

Lets imagine you have an nginx webserver running as a Kubernetes workload on every node in the cluster. It was well tested locally, and the decision was made to go in production by exposing the service to the internet, and make sure the traffic is evenly distributed between the nodes the workload resides on. The easiest way to achieve this set up is by picking the L4 Load Balancer option when you open the port for the workload in the Rancher UI:

![]()

As a result, the workload would get updated with a publicly available endpoint, and, if you click on it, the nginx application page would load:

![]()

### What happens behind the scenes

Smooth user experience implies some heavy lifting done on the backend. When a user creates a workload with Load Balancer port exposed via Rancher UI/API, two Kuberntes objects get created on the backend: the actual workload in the form of the Kubernetes deployment/daemonset/statefulset (depending on the workload type chosen) and the Service of type Load Balancer. The Load Balancer service in Kubernetes is a way to configure L4 TCP Load Balancer that would forward and balance traffic from the internet to your backend application. The actual Load Balancer gets configured by the cloud provider where your cluster resides:

![]()

### Limitations

- Load Balancer Service is enabled on only certain Kubernetes Cluster Providers in Rancher; first of all on those supporting Kubernetes as a service:

![]()

…and on the EC2 cloud provider where Rancher RKE acts as a Kubernetes cluster provisioner, under condition of the Cloud Provider being explicitly set to Amazon during the cluster creation:

![]()

![]()

- Each Load Balancer Service gets its own LB IP Address, so it’s recommended to check your Cloud Provider’s pricing model given thats the use can be excessive.
- L4 balancing only, no HTTP based routing.

## L7 Load Balancing

### Host and path based routing

The typical use case for host/path based routing is using a single IP (or the same set of IPs) to distribute traffic to multiple services. For example, a company needs to host two different applications - a website and chat - on the same set of public IP addresses. First they setup two separate applications to deliver these functions: Nginx for the website and LetsChat for the chat platform. Then by configuring the ingress resource via the Rancher UI, the traffic can be split between these two workloads based on the request coming in. If the request is coming for userdomain.com/chat, it will be directed to the LetsChat servers; if the request is for userdomain.com/website - it will be directed to the web servers:

![]()

Rancher uses native Kubernetes capabilities when it comes to ingress configuration, as well as providing some nice extra features on top of it. One of them is an ability to point the ingress to the workload directly, saving users from creating a service - the only resource that can act as a target for an ingress resource.

### Ingress controller

Ingress resource in Kubernetes is just a Load Balancer spec - a set of rules that have to be configured on an actual load balancer. The load balancer can be any system supporting reverse proxying, and it can be deployed as a standalone entity outside of kubernetes cluster, or run as a native Kubernetes application inside kubernetes pod(s). Below, we’ll provide example of both models.

#### Ingress Load Balancer outside of Kubernetes cluster

If a Kubernetes cluster is deployed on a public cloud having Load Balancing services, it can be used to backup the ingress resouce. For example, for Kubernetes clusters on Amazon, an ALB ingress controller can program ALB with ingress traffic routing rules:

![]()

The controller itself would be deployed as a native Kubernetes app that would listen to ingress resource events, and program ALB accordingly. ALB ingress controller code can be found here: [Core OS ALB ingress controller](https://github.com/coreos/alb-ingress-controller "Core OS ALB ingress controller")

When users hit the url userdomain.com/website, ALB would redirect the traffic to the corresponding Kubernetes Node Port service. Given the Load Balancer is external to the cluster, the service has to be of a NodePort type. A similar restriction applies to Ingress programming on GCE clusters.

#### Ingress Load Balancer as a native Kubernetes app

Let’s look at another model, where the ingress controller acts both as a resource programming Load Balancer records, and as a Load Balancer itself. A good example is the [Nginx ingress controller](https://github.com/kubernetes/ingress-nginx) – a controller that you get installed by default by [RKE](https://rancher.com/announcing-rke-lightweight-kubernetes-installer/ "RKE Announcement") – Rancher’s native tool used to provision k8s clusters on clouds like Digital Ocean and vSphere.

The diagram below shows the deployment details of the nginx ingress controller:

![]()

RKE deploys nginx ingress controller as a daemonset, which means every node in the cluster will get one nginx instance deployed as a Kubernetes pod. You can allocate limited sets of nodes for deployment using scheduling labels. Nginx acts like an ingress controller and the load balancer, meaning it programs itself with the ingress rules. Then, nginx gets exposed via NodePort service, so when a user’s request comes to snodeip/nodePort, it gets redirected to nginx ingress controller, and the controller would route the request based on hostname routing rules to the backend workload.

### Programming ingress LB address to public DNS

By this point we’ve got some undestanding as to how path/hostname routing is implemented by an ingress controller. In the case where the LB is outside of the Kubernetes cluster, the user hits the URL, and based on URL contents, the Load Balancer redirects traffic to one of the Kubernetes nodes where the user application workload is exposed via NodePort service. In the case where the LB is running as a Kubernetes app, the Load Balancer exposes itself to the outside using Node Port service, and then balances traffic between the workloads’ pods internal IPs. In both cases, ingress would get updated with the **address** that the user has to hit in order to get to the Load Balancer:

![]()

There is one question left unasnwered – who is actually responsible for mapping that address to the **userdomain.com** hostname from the URL the user would hit? You’d need to have some tool that would program a DNS service with these mappings. Here is one example of such a tool, from kubernetes-incubator project: [external-dns](https://github.com/kubernetes-incubator/external-dns). External-dns gets deployed as a kubernetes native application that runs in the pod, listens to an ingress, creates/updates events, and programs the DNS of your choice. The tool supports providers like AWS Route53, Google Cloud DNS, etc. It doesn’t come by default with a Kubernetes cluster, and has to be deployed on demand.

In Rancher, we wanted to make things easy for users who are just getting familiar with Kubernetes, and who simply want to deploy their first workload and try to balance traffic to it. The Requirement to setup DNS plugin in this case can be a bit excessive. By using xip.io integration, we make DNS programming automatic for simple use cases:

![]()

Let’s check how it works with Rancher. When you create the ingress, pick `Automatically generate .xip.io hostname...` option:

![]()

The hostname would get automatically generated, used as a hostname routing rule in ingress, and programmed as xip.io publicly available DNS record. So all you have to do is – use the generated hostname in your url:

![]()

### If you want to learn more about Kubernetes load balancing…

Watch our Kubernetes Master Class: [“Load Balancing with Kubernetes”](https://info.rancher.com/load-balancing-kubernetes-concepts-use-cases).

Build a CI/CD Pipeline with Kubernetes and RancherRecorded Online Meetup of best practices and tools for building pipelines with containers and kubernetes.[Watch the training](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/)
