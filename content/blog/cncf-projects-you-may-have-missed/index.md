---
title: "CNCF Projects You May Have Missed"
date: 2017-08-23T10:15:00
slug: "cncf-projects-you-may-have-missed"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["observability"]
content_type: "explainer"
draft: true
migration:
  wp_id: 86549
  original_url: "https://www.suse.com/c/rancher_blog/cncf-projects-you-may-have-missed/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2017 CNCF project survey"
  redirect_target: "https://rancher.com/blog (hub)"
---

Since its founding in 2015, the [Cloud Native Computing
Foundation](https://cncf.io/) (CNCF) has become one of the most
important movers and shakers in the open source ecosystem—especially
when it comes to tools that affect containers and other “cloud-native”
technologies. CNCF was established to promote and organize projects
related to large-scale industry trends towards containerization,
orchestration, and microservices architectures. In the time since, 10
open source projects have been added to the foundation. Even if you have
never heard of the CNCF, in all likelihood you have heard of one of its
more popular projects: the Kubernetes container orchestration platform.
But the CNCF is about much more than Kubernetes. Here’s a look at some
other vital projects within the CNCF ecosystem that are worth following
if you want to stay abreast of important developments in the container
and cloud computing world.

### Linkerd

![](images/rancher_blog_Kubernetes-Docker-Swarm-comparison-150x150.jpg) Compare architectures, feature
sets, and usability of Kubernetes and Docker Swarm. [Download
now](https://info.rancher.com/comparing-kubernetes-swarm) The
first is [Linkerd](http://linkerd.io), a solution for meshing
service-based apps that run in the cloud. The idea behind Linkerd is
this: Microservices are great, but only if you have a good way to
connect them in order to form complete apps. If you don’t, your
microservices apps end up as a clunky mess of moving parts that just
don’t fit together well. Linkerd is an open source project that aims to
solve this challenge by providing what the developers call a “service
mesh.” Linkerd’s service mesh provides a convenient and reliable
interface over which different services can interact. In addition to
making progammers’ lives easier by providing a simple way and
consistent abstraction layer for connect services, linkerd is designed
with scalability, high availability and security in mind. The project,
which is overseen by [Buoyant](https://buoyant.io/), joined the CNCF in
early 2017.

### Fluentd

Metrics are only one aspect of the microservices application visibility
puzzle. Centralized logging is another. As the number of applications
and the size of a company grows (especially as more and more services
are containerized), collecting, analyzing, and querying structured logs
in one location is vital. This is where
[Fluentd](http://www.fluentd.org/) comes in. Fluentd is a log collector
(comparable to LogStash) through which logs can be filtered, sanitized,
and routed to a variety of destinations. Like other log collectors,
Fluentd can be used with a variety of core and third-party input and
output plugins (such as the Elasticsearch plugin, S3 plugin, etc).
Fluentd also has some level of in-memory storage, and reliability. A
very simplified example of how Fluentd might be utilized is the routing
of logs from rsyslog from a variety of hosts to Fluentd and then to an
Elasticsearch cluster.

### OpenTracing

The third piece of the observability pie is distributed tracing. As
monolith applications are broken down into a variety of smaller
services, more and more data is being transmitted from frontend to
backend, service to service, and naturally, within services. But what
happens when a public-facing application with a variety of dependencies
experiences sudden latency? This is where distributed tracing comes in.
At its core, tracing refers to propagating metadata through different
request calls, threads, and processes, and ultimately, constructing a
graph based upon this metadata. [OpenTracing](http://opentracing.io/) is
a tracing standard that was created as a response to a long-running
problem in the field of distributed tracing—namely, how can one
reconcile instrumenting tracing when a company’s stack may consist of a
multitude of third-party software, operating systems, and custom
applications, all in different languages? OpenTracing, a standardized
tracing, is the solution. The project provides standardization of
instrumentation APIs for span (i.e. timed operation) management and
inter-process propagation. As a result, users can easily switch out
tracing libraries or centralized tracing systems (such as Zipkin,
Dapper, etc.) with minimal configuration and headache.

### gPRC

Thus far we have discovered how one might deploy, schedule, and gain
insight into microservices in the cloud. But what about the mode of
communication between them? Enter remote procedure calls. The concept of
remote procedure calls has been around for some time now, and refers to
a pattern where functions are called as though they are remote—often
used in systems with a greater focus on actions rather than the CRUD
model of RESTful services. [gRPC](https://grpc.io/), however, refers to
Google’s implementation of remote procedure calls that leverages http/2
and protocol buffers. Compared to JSON-based RPC, gRPC has been proven
to be [orders of magnitude
faster](https://blog.gopheracademy.com/advent-2015/etcd-distributed-key-value-store-with-grpc-http2/),
making it an excellent choice for large-scale distributed platforms. In
fact, both etcd (the popular key-value store from CoreOS) and Google’s
own BigTable leverage gRPC!

### rkt

The last project to be included on this list
is[rkt](https://coreos.com/rkt) (also known as Rocket), a container
runtime. Although Docker’s containerd runtime was arguably the container
runtime that popularized the concept of containers, and Docker remains a
commonly used runtime within the orchestration ecosystem, rkt is
becoming more and more popular as of late. The differences between the
two are quite apparent. While Docker has chosen to package in Swarm and
consists of a daemon and an executable communicating with the daemon via
a REST API, rkt is far simpler. It consists of a simple command line
tool that, when given an image, a specification format, and an image
discovery mechanism, will run a container. With rkt, users avoid issues
like stale containers when configuring their container runtime with
something such as systemd. Furthermore, rkt is able to run not only
images in the [App Container format](https://github.com/appc/spec), but
also standard Docker images.

### Conclusion

As we move further into this brave new world of microservice
architecture, more and more open source projects are being developed for
those who truly wish to go cloud-native. This list covered just some of
the important CNCF projects worth following. I urge you to look into the
[others](https://www.cncf.io/). *Sneha Inguva is an enthusiastic
software engineer currently working on building developer tooling at
DigitalOcean. She has worked at a variety of startups in the last few
years, and has a unique perspective on building and deploying software
in eclectic verticals (education, 3D printing, and casinos, to name a
few). When she isn’t bashing away on a project or reading about the
latest emerging technology, she is busy rescuing animals or practicing
martial arts.*
