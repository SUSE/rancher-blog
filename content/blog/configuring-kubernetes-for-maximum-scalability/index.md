---
title: "Configuring Kubernetes for Maximum Scalability"
date: 2017-08-09T10:16:00
slug: "configuring-kubernetes-for-maximum-scalability"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["multi-cluster"]
content_type: "explainer"
draft: false
migration:
  wp_id: 86581
  original_url: "https://www.suse.com/c/rancher_blog/configuring-kubernetes-for-maximum-scalability/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Kubernetes 1.6 limits and scripts"
  redirect_target: ""
---

Kubernetes is designed to address some of the difficulties that are
inherent in managing large-scale containerized environments. However,
this doesn’t mean Kubernetes can scale in all situations all on its own.
There are steps you can and should take to maximize Kubernetes’ ability
to scale—and there are important caveats and limitations to keep in
mind when scaling Kubernetes. I’ll explain them in this article.

### Scale versus Performance

The first thing that must be understood about scaling a Kubernetes
cluster is that there is a tradeoff between scale and performance. For
example, Kubernetes 1.6 is designed for use in clusters with up to 5,000
nodes. But 5,000 nodes is not a hard limit; it is merely the recommended
node maximum. In actuality, it is possible to exceed the 5,000 node
cluster limit substantially, but performance begins to drop off after
doing so. What this means more specifically is this: Kubernetes has
defined two service level objectives. The first of these objectives is
to return 99% of all API calls in less than a second. The second
objective is to be able to start 99% of pods within less than five
seconds. Although these objectives do not act as a comprehensive set of
performance metrics, they do provide a good baseline for evaluating
general cluster performance. According to Kubernetes, clusters with more
than 5,000 nodes may not be able to achieve these service level
objectives. So, keep in mind that beyond a certain point, you may have
to sacrifice performance in order to gain scalability in Kubernetes.
Maybe this sacrifice is worth it to you, and maybe it’s not, depending
on your deployment scenario.

### Quotas

One of the main issues that you are likely to encounter when setting up
a really large Kubernetes cluster is that of quota limitations. This is
especially true for cloud-based nodes since cloud service providers
commonly implement quota limitations. The reason why this is such an
important consideration is because deploying a large-scale Kubernetes
cluster is a deceptively simple process. The config-default.sh file
contains a setting named `NUM_NODES`. On the surface, it would seem that
you can build a large cluster simply by increasing the value that is
associated with this setting. Although this is possible in some cases,
you could end up running into a quota issue. As such, it is important to
talk to your cloud provider about any existing quotas before attempting
to scale your cluster. Not only can a provider let you know about any
quotas that may exist, but at least some providers will allow
subscribers to request an increase in the quota limit. As you evaluate
the limitations, keep in mind that although there may be a quota limit
that directly controls the number of Kubernetes cluster nodes that you
can create, the cluster size limit is more often caused by quotas that
are only indirectly related to Kubernetes. For example, a provider may
limit the number of IP addresses that you are allowed to use, or the
number of virtual machine instances that you are allowed to create. The
good news is that the major cloud providers have experience with
Kubernetes, and should be able to help you navigate these issues.

### Master Node Considerations

Another issue that you will need to consider is the way that the cluster
size impacts the required size and number of master nodes. The
requirements vary depending on how Kubernetes is being implemented, but
the important thing to remember is that the larger the cluster size, the
greater the number of master nodes that will be required, and the more
powerful those master nodes will need to be. If you are building a new
Kubernetes cluster from scratch, then this may be a non-issue. After
all, determining the number of master nodes that will be required is a
normal part of the cluster planning process. The master node requirement
can become a bit more problematic, however, if you are attempting to
scale an existing Kubernetes cluster, because master node sizes are set
when the cluster starts up, and are not dynamically adjusted.

### Scaling Add-ons

Another thing to be aware of is that Kubernetes defines resource limits
for add-on containers. These resource limits prevent add-ons from
consuming excessive CPU and memory resources. The problem with these
limits is that they were defined based on the use of a relatively small
cluster. If you run certain add-ons in a large cluster, then the add-ons
may need more resources than their limit allows. This happens because
the add-ons must service a greater number of nodes, and will therefore
require additional resources. If add-on-related limits start to become
an issue, then you will see the add-ons continuously being killed.

### Conclusion

Kubernetes clusters can be massively scaled, but can encounter growing
pains related to quotas and performance. As such, it is important to
carefully consider the requirements of horizontal scaling prior to
adding a significant number of new nodes to a Kubernetes cluster.
