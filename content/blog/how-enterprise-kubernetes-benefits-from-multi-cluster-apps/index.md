---
title: "How Enterprise Kubernetes Benefits from Multi-Cluster Apps"
date: 2019-02-20T09:06:00
slug: "how-enterprise-kubernetes-benefits-from-multi-cluster-apps"
author: "Rancher Admin"
image: "images/rancher_blog_online-meetups-site-feature.svg"
products: ["Rancher Manager"]
tags: ["multi-cluster"]
content_type: "opinion"
draft: true
migration:
  wp_id: 85863
  original_url: "https://www.suse.com/c/rancher_blog/how-enterprise-kubernetes-benefits-from-multi-cluster-apps/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 2.2 feature marketing"
  redirect_target: "rancher.com/blog (hub)"
---

Join the February Online MeetupFebruary's online community gathering covers Multi-Cluster Applications, Global DNS, and Multi-Tenant Catalogs[Learn More](https://rancher.com/events/2019/meetup-multi-cluster-apps/)

There is a lot to love about [Kubernetes](https://rancher.com/kubernetes "Why Kubernetes is so popular"). It offers one of the best ways to deploy and run applications on a large pool of resources.

With its easy-to-use UI and out-of-the-box capabilities like RBAC, monitoring, auditing, logging, and more, Rancher makes it easy to stand up and manage enterprise grade Kubernetes.

Using Rancher, IT Operators can point to their cloud provider (AWS, GCP, Azure, etc.) or datacenter and create a cluster with just a few clicks.

As the demand for Kubernetes grows within an enterprise, IT Operators have two options:

- Scale Up: Teams working together on related projects and without any need for isolation scale up the existing cluster by adding more nodes.
- Scale Out: Teams requiring a high degree of isolation due to security concerns, resource chargeback, or other reasons can scale out the

Kubernetes environment by adding more clusters.
Rancher supports both options.

One of our goals is to make sure that whether you scale up or scale out, the effort and cost of enterprise grade Kubernetes management remains low.

Support for multi-cluster applications is a step toward realizing that goal. Though the name implies that this capability is for multiple clusters only, it also works for multiple Projects in the same cluster.

**The “scale up” scenario**: As the requirement for high reliability, high availability or just larger clusters grows, a cluster administrator may add more nodes to the existing cluster. To achieve some degree of isolation, the admin may provide each team their own Project. A Project in Rancher is higher level abstraction than namespaces and can be restricted with RBAC.

Teams using the same cluster can still work within their own Project with no visibility into other Projects. Due to corporate requirements or because different teams may be using same applications, copies of the said application have to be pushed into more than one Project. For example, a project team of in-house developers may have to collaborate with an outsourced team. Since they both have to work on the same apps but need their own separate instances, a copy of the application should be available in both Projects.

**The “scale out” scenario**: As Kubernetes adoption grows within an enterprise, we often find customers building multiple clusters to get the highest level of isolation among different teams.
In such scenarios corporate requirements, such as the need to have a security tool deployed in each cluster, requires cluster admins to push copies of the same application to each cluster.
In edge computing scenarios where the customer may have hundreds (or even thousands) of clusters, the problem is exponentially complex.

In both, scale up and scale out, scenarios deployment of the application copy to multiple targets is the smaller problem. Upgrading and keeping these apps in sync is nearly impossible without sophisticated scripts and a highly skilled support team.

This is where support for the multi-cluster applications becomes so important. Imagine pointing to the Helm chart for the application that needs to go into multiple Projects on the same (or multiple clusters), providing config values, overriding project/cluster specific settings and then clicking one button to get the application deployed.

This “how-to” blog post I wrote a few weeks ago goes into the details of this capability.

The ability to choose your upgrade strategy (rolling or simultaneous update) for these applications further simplifies how your applications will remain up to date.

Multi-cluster applications is a powerful capability for all users - from those supporting enterprise grade Kubernetes with multiple clusters to the ones just experimenting with a single cluster with multiple projects.

## Conclusion

Give it a try. You may find that adopting Kubernetes as your enterprise strategy is not as complex as some people make it out to be!

To test these features in your lab or development environment, install [the latest alpha release](https://rancher.com/docs/rancher/v2.x/en/installation/server-tags/#helm-chart-repositories "Latest Helm Chart of Rancher 2.2 Alpha"). If you have any feedback, please [open an issue on Github](https://github.com/rancher/rancher/issues), or join us [in the forums](https://forums.rancher.com/) or on [Slack](https://slack.rancher.io/).

Join the February Online MeetupFebruary's online community gathering covers Multi-Cluster Applications, Global DNS, and Multi-Tenant Catalogs[Learn More](https://rancher.com/events/2019/meetup-multi-cluster-apps/)
