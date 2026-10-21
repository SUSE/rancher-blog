---
title: "Rancher High Availability - Simplified"
date: 2016-05-06T11:15:00
slug: "rancher-high-availability-simplified"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["multi-cluster"]
content_type: "explainer"
draft: true
migration:
  wp_id: 86925
  original_url: "https://www.suse.com/c/rancher_blog/rancher-high-availability-simplified/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x HA setup, discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

With the release of Rancher v1.0.1, setting up and running a
highly-available Rancher cluster just got a whole lot easier. Prior to
this release, users were required to create and manage their own
[Zookeeper
Ensemble](https://zookeeper.apache.org/doc/r3.4.6/zookeeperStarted.html),
[Redis Cluster](http://redis.io/topics/quickstart), external relational
database, Rancher servers and external load balancer. Monitoring of
these components was a wholly manual process or required extra
middleware and ramp-up time. Configuring Rancher servers to communicate
with these components was another hurdle, and left more room for error
and frustration. Rancher now orchestrates and manages its own Zookeeper
and Redis cluster on Docker all on its own! The simplified process is
only a few steps:
[![2016.05.09 - HA
v1.0.1](images/rancher_blog_2016.05.09-HA-v1.0.1-1024x576.jpg)](https://cdn.rancher.com/wp-content/uploads/2016/05/06231843/2016.05.09-HA-v1.0.1.jpg)
Figure 1: The new, simplified Rancher HA deployment topology

- Install an external database
- Startup a rancher server and generate an HA deployment script
- Run the deployment script on each host and configure your load
  balancer

### Recovery

Recovering from a node failure is dead simple: either repair or replace
your node, delete old containers if present, and re-run the deployment
script. The new node registers to the System HA environment. Zookeeper,
Redis and all other internal components automatically repair themselves.
If a new node is created, adjust your load balancer accordingly. Rancher
exhibits the characteristics of an active-passive HA deployment, so the
number of host failures that may be tolerated is computed as `ceil(N /
2) - 1`, where N is the number of Rancher nodes. In simpler terms, a
3-node deployment survives 1 host failure, a 5-node deployment survives
2 host failures, and so on.

### Moving Forward

The latest HA iteration brings automatic Zookeeper and Redis
configuration management, but why stop there? Rancher could handle its
own distributed database, further reducing manual deployment and
management efforts. Rancher could even manage itself. Try Rancher HA out
today - we want to hear your opinions on the Rancher forums.

### Contact Us

If you’re interested in finding out more about Rancher, please download
the software from [github](https://github.com/rancher/rancher), and
visit our [forums](https://forums.rancher.com/) to view topics and
ask questions. To learn more about using Rancher, please join our next
online meetup.
