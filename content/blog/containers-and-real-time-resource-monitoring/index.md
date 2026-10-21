---
title: "Containers and Real-Time Resource Monitoring"
date: 2017-05-30T10:17:00
slug: "containers-and-real-time-resource-monitoring"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["observability"]
content_type: "explainer"
draft: false
migration:
  wp_id: 86609
  original_url: "https://www.suse.com/c/rancher_blog/containers-and-real-time-resource-monitoring/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Are you monitoring your containers’ resources in real time? If not,
then you’re probably not monitoring as effectively as possible. In a
fast-moving, dynamic microservices environment, monitoring data that is
even seconds old may no longer be actionable. To prevent disruptions,
you need real-time monitoring. In this post, I explain why real-time
monitoring of container resources is important, and which types of
container metrics you should focus on monitoring in real time. And just
to be clear up front, this isn’t a post endorsing any particular
monitoring vendor’s toolset. While there are now plenty of
container-ready monitoring platforms out there that can support
real-time monitoring, I think it’s better to understand the underlying
essentials of container monitoring, rather than focusing on the feature
set of a particular product. If you know what to monitor in real time in
order to keep your containerized infrastructure running healthily,
you’ll be well-positioned to choose the best toolset to meet your
real-time monitoring needs.

##### Take a deep dive into Best Practices in Kubernetes Networking

![]()
From overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options.

[Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/)

### The Challenges of Real-Time Container Monitoring

Before discussing how to perform real-time monitoring for containers, it’s worth pointing out the special challenges that arise from monitoring containers in real time.

The most obvious is that, in a containerized environment, components disappear
all the time by design. In a legacy environment, you focused on
monitoring servers and apps that were relatively static. But containers
spin up and down constantly. As a result, there is a lot more monitoring
in a containerized environment. By extension, there is a lot more noise.
Separating meaningful data from noise is therefore more difficult,
especially when you need instant monitoring insights and can’t waste
time identifying noise. Real-time monitoring can also be harder in a
containerized environment because of the way Docker abstract containers
away from the host. When you’re dealing with containers, you can’t
simply run monitoring commands like top or ps from the host and get an
accurate picture of what’s happening inside the containers. Since
logging into containers to peer inside in real time for monitoring
purposes is not feasible at scale, the answer to this challenge is to
use agents or another clever type of monitoring solution that provides
real-time visibility into containers and the services they support.

### What Can You Monitor?

Let’s now take a look at which real-time container metrics you can
monitor. Taking Docker as the most obvious example (although much of the
following applies to other container systems, including the Linux-native
LXD), we can break real-time container metrics into four basic
categories:

**Memory**

Docker can monitor the total memory used by an individual container,
along with the amount of cache and swap memory, and the resident set
size, or RSS, which represents memory used by processes and not cached
or stored on disk, such as anonymous memory maps and stacks.

Both RSS and cache memory can be broken down into active and inactive
memory. Minor (duplication or allocation) and major (full read from
disk) page faults are also included in Docker’s memory statistics.

**CPU**

Docker monitors both user CPU time (CPU use by the processes
themselves), and system CPU time (system calls by processes). If CPU
throttling (limiting the time available for a given container) is being
enforced, the throttling count and time for the container will also be
reported.

**I/O**

For I/O, Docker monitors both the number of I/O operations and the
volume of I/O in bytes. In both cases, it counts synchronous /
asynchronous and read / write separately. Docker also provides a count
of sectors (512-byte) read and written (reads/writes are counted
together), and a count of operations currently in the queue.

**Network Resources**

Docker also reports overall network metrics for individual containers,
including packet count, traffic volume in bytes, dropped packets, and
transmit and receive errors.

**And more...** Other metrics to consider are those involving storage
(and storage-related performance metrics), as well as the total number
of containers in use. In addition to container-specific metrics, it is,
of course, important to monitor such traditional factors as overall
system performance, traffic, patterns of user behavior, and application
performance, all of which may directly or indirectly impact container
activity.

### The Best Ways to Monitor

Methods of monitoring and monitoring services are of course important as
well. Docker’s native monitoring tools have a bare-bones interface, but
many of the services which are built on or incorporate those tools have
considerably greater capabilities, which may include non-Docker resource
monitoring, dashboards, analytics at both the container and aggregate
levels, and an API for alerts and other automated responses. Many of
these tools are easily integrated with
[Rancher](https://rancher.com), and can be used to monitor (and
analyze) Rancher-specific resources, as well as those common to
containers in general.

### Why Is Container Monitoring Important?

Why is it important to monitor metrics such as these? Not surprisingly,
the main reasons for monitoring containers closely parallel the main
reasons for monitoring other applications: performance, error detection,
and detection of anomalous behavior. In the case of containers,
monitoring may help you detect problems at the system, container, and
application levels. This doesn’t mean, by the way, that the approach you
take to container monitoring is identical to the one you use in
traditional environments. As noted above, container monitoring presents
particular challenges. But the benefits of container monitoring are the
same in either case.

### Real-Time Container Monitoring and Performance Optimization

Perhaps the most obvious metrics for monitoring container performance
are those involving CPU and memory use. Is a specific container (or more
typically, many or most instances of a container which compose a
specific microservice) taking up too much CPU time, or too much memory?
If so, then you have an opportunity to optimize performance by finding
and fixing the problem. The following are some specific strategies you
can adopt to address performance issues that you can identify through
real-time monitoring.

**Throttling CPU**

You may be able to solve some problems with excessive CPU use simply by
enforcing CPU throttling. In other cases, however, such performance
issues may be an indication of problems in design (at either the overall
application or microservices level), or coding errors. Such
performance-related problems may also show up in I/O or even network
metrics.

Throttling can serve a function similar to that of traditional
load-balancing, but it is important when confronted with CPU-related
performance problems not to simply throttle and assume that will solve
the problem. If a crucial service is using excessive CPU time,
throttling it may simply degrade performance in other ways.

When faced with chronic CPU or memory problems or similar performance
issues, it is important to look for bottlenecks at the design level, and
application errors which may result in inefficient or incorrect use of
memory, CPU services, or other resources.

**Provisioning Resources**

Performance problems may also result from inadequate provisioning of
resources at the system level. You may need to provision more memory,
more storage, more CPU access, or switch to a cloud service contract
which gives you higher priority in accessing resources.

**But Provisioning isn’t a Cure-All** As is the case with throttling,
however, it is important not to simply provision more resources and hope
that it will solve performance problems. You should first look at
application architecture, microservice design, and possible functional
problems at the coding level. You can’t fix design problems or bugs by
throwing resources at them. You may be able to overcome the obvious and
immediate inefficiencies that way, but other effects of the basic
problem may continue undetected, resulting in even greater trouble at
some point.

### Container Monitoring: Bugs and Anomalous Behavior

Performance problems aren’t the only thing that real-time monitoring can
help you find and address. The following are other types of issues (ones
related to cost-optimization, security and user experience) that you
should also keep in mind when performing real-time container monitoring.

**Under-utilized Resources**

A container that uses resources at a lower-than-expected level may be as
serious an indication of trouble as overuse of resources. A credit-card
authorization microservice which makes almost no use of I/O or network
resources, for example, could be a sign of major problems—either with
the authorization microservice itself, with one or more of the
microservices which are supposed to use it, or with some other part of
the application which may be only indirectly involved with credit
authorization.

**Suspicious Traffic**

Container monitoring may uncover other forms of anomalous behavior as
well. If containers are accessing (or simply requesting) resources which
they would not ordinarily use, or if they show an unusual pattern of I/O
or network traffic, it may indicate security problems.

**Unmet needs**

Anomalous container behavior may also be an indication of less alarming
(but still important) problems, such as unexpected patterns of user
activity. If users are (for legitimate reasons) accessing specific
services at a much greater level than originally anticipated, for
example, you may need to look at overall architecture, at patterns of
deployment, or at the possibility of adding new services to meet
currently unmet (or under-met) user needs.

So, while individual, here-one-millisecond-gone-the-next containers may
not be persistent, everything else about your container ecosystem
(infrastructure, stored data, user interactions, resource availability)
does have an ongoing life, one which is strongly impacted by container
behavior, and which may in turn have a major impact on your
application’s performance, and on your organization’s bottom line.
Real-time container monitoring isn’t just important. It’s a necessity.
