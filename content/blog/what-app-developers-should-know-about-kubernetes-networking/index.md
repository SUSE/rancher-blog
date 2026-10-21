---
title: "What App Developers Should Know About Kubernetes Networking"
date: 2017-07-17T09:01:00
slug: "what-app-developers-should-know-about-kubernetes-networking"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["networking", "security"]
content_type: "explainer"
draft: false
migration:
  wp_id: 85803
  original_url: "https://www.suse.com/c/rancher_blog/what-app-developers-should-know-about-kubernetes-networking/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Alpha NetworkPolicy API sample is obsolete"
  redirect_target: ""
---

In the world of containers, Kubernetes has become the community standard
for container orchestration and management. But there are some basic
elements surrounding networking that need to be considered as
applications are built to ensure that full multi-cloud capabilities can
be leveraged.

### The Basics of Kubernetes Networking: Pods

The basic unit of management inside Kubernetes is not a container—It
is called a pod. A pod is simply one or more containers that are
deployed as a unit. Often, they are a single functional endpoint used as
part of a service offering. Two examples of valid pods are:

- Database pod—a single MySQL container
- Web pod—an instance of Python in one container and Redis in a
  second container

Useful things to know about pods:

- They share resources—including the network stack and namespace.
- A pod is assigned a single IP which clients connect to.
- A pod configuration defines any public ports and what container
  hosts the port.
- All containers within a pod can interact over any port over the
  network. (They are all referenced as localhost, so be sure that all
  the services in the pod have unique ports.)

### Kubernetes Services

A Kubernetes service is where multiple identical pods are managed behind
a load balancer. Clients connect to the IP of the load balancer instead
of the individual IPs of each pod. Defining your application as a
service allows Kubernetes to scale the number of pods based on the rules
defined, and available resources. Defining an application as part of a
service is the only way to make it available to clients outside of the
Kubernetes infrastructure. Even if you never scale past one node,
services is the avenue to have an external IP address assigned.

### Labels

![](images/rancher_blog_Training.png) Want to learn more about
Docker, Kubernetes, and Rancher? Join us for [free online
training](https://info.rancher.com/kubernetes-training)
Labels are key/value pairs which are assigned to objects, like pods,
within Kubernetes. Labels should be meaningful and relevant. In a
standard installation of Kubernetes, labels do not directly impact core
operations with Kubernetes, but are used primarily for grouping and
identification purposes.

### Network Security

Labels were mentioned in the previous section, and there are now network
plugins recommended by Kubernetes that leverage labels to change some
functionality at runtime. Most of the network plugins that can be used
on Kubernetes are based on the [Container Networking
Interface](https://github.com/containernetworking/cni) (CNI)
specification, which is maintained by the Cloud Native Computing
Foundation. The CNI allows for the same network plugins to be used on
multiple container platforms. As part of the [Kubernetes Network Special
Internet
Group](https://github.com/kubernetes/community/wiki/SIG-Network)
(Network SIG), a way to apply network security policies has been created
that leverages labels so the correct network policies are applied at
runtime, instead of the more traditional model of a network or security
team that pre-assigns everything. (The world of containers is too
dynamic to have that level of manual intervention.) There are several
options available today that support network policies applied to
namespaces and pods, including OpenContrail and Project Calico. With
this new approach, Kubernetes administrators import all pre-approved
policies, and developers are responsible for and have the autonomy to
apply the policies as required—with all of this work being done as
part of the pod definition. Sample Network Policy:

```
POST /apis/net.alpha.kubernetes.io/v1alpha1/namespaces/tenant-a/networkpolicys/
{
    "kind": "NetworkPolicy",
    "metadata": {
        "name": "pol1"
    },
    "spec": {
        "allowIncoming": {
            "from": [
                { "pods": { "segment": "frontend" } }
            ],
            "toPorts": [
                { "port": 80, "protocol": "TCP" }
            ]
         },
            "podSelector": { "segment": "backend" }
     }
}
```

Sample Pod Configuration with Network Policy Defined:

```
apiVersion: v1
kind: Pod
metadata:
 name: nginx
 labels:
   app: nginx
   segment: frontend
spec:
 containers:
 - name: nginx
   image: nginx
   ports:
   - containerPort: 80
```

### Conclusion

With the functionality that Kubernetes offers, developers now have the
flexibility they require to fully define the application and its
dependencies, and can use multiple containers in a single pod.
Kubernetes will ensure that if any of the containers fail, those pods
will be decommissioned and a new one will be spun up to replace it
automatically. Developers can also define what port the application or
service listens on, if it is part of a larger service, or just a
standalone instance. With operations “out of the way,” rapid development
and deployment cycles using continuous delivery and deployment
methodologies can and will be the new normal. *Vince Power is a
Contributor at Fixate IO and Solution Architect who has a focus on cloud
adoption and technology implementations using open source-based
technologies. He has extensive experience with core computing and
networking (IaaS), identity and access management (IAM), application
platforms (PaaS), and continuous delivery.*
