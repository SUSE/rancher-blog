---
title: "Using New Relic, Splunk, AppDynamics and Netuitive for Container Monitoring"
date: 2016-12-07T11:29:00
slug: "using-new-relic-splunk-appdynamics-and-netuitive-for-container-monitoring"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["observability"]
content_type: "explainer"
draft: true
migration:
  wp_id: 87258
  original_url: "https://www.suse.com/c/rancher_blog/using-new-relic-splunk-appdynamics-and-netuitive-for-container-monitoring/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2016 vendor monitoring comparison"
  redirect_target: "rancher.com/blog (hub)"
---

[![Monitoring
Icons](images/rancher_blog_Blog-icons-300x238.png)](https://cdn.rancher.com/wp-content/uploads/2016/12/06155306/Blog-icons.png)If
you use containers as part of your day-to-day operations, you need to
monitor them -- ideally, by using a docker performance monitoring solution that you
already have in place, rather than implementing an entirely new tool.
Containers are often deployed quickly and at a high volume, and they
frequently consume and release system resources at a rapid rate. You
need to have some way of measuring container performance, and the impact
that container deployment has on your system. In this article, we’ll
take a look at four widely used monitoring
platforms—[Netuitive](http://www.netuitive.com/), [New
Relic](https://newrelic.com/), [Splunk](https://www.splunk.com/), and
[AppDynamics](https://www.appdynamics.com/)—that support containers,
and compare how they measure up when it comes to monitoring containers.
First, though, a question: When you monitor containers, what kind of
metrics do you expect to see? The answer, as we’ll see below, varies
with the monitoring platform. But in general, container metrics fall
into two categories—those that measure overall container impact on the
system, and those that focus on the performance of individual
containers.

### Setting up the Monitoring System

The first step in any kind of software monitoring, of course, is to
install the monitoring service. For all of the platforms covered in this
article, you can expect additional steps for setting up standard
monitoring features. Here we cover only those directly related to
container monitoring. **Setup: New Relic** With New Relic, you start by
installing [New Relic Servers for
Linux](https://docs.newrelic.com/docs/servers/new-relic-servers-linux/getting-started/new-relic-servers-linux),
which includes integrated Docker monitoring. It should be installed on
the Docker server, rather than the Docker container. The Servers for
Linux package is available for most common Linux distributions; Docker
monitoring, however, requires a 64-bit system. After you install New
Relic Servers for Linux, you will need to create a docker group (if it
doesn’t exist), then add the newrelic user to that group. You may need
to do some basic setup after that, including (depending on the Linux
distribution) setting the location of the container data files and
enabling memory metrics. **Setup: Netuitive** Netuitive also requires
you to install its Linux monitoring agent on the Docker server. You then
need to enable Docker metrics collection in the Linux Agent config file,
and optionally limit the metrics and/or containers by creating a
regex-based blacklist or whitelist. As with New Relic, you may wind up
setting a few additional options. Netuitive, however, offers an
additional installation method. If you are unable to install the Linux
Agent on the Docker server, you can install a Linux Agent Docker
container, which will then do the job of monitoring the host and
containers. **Setup: Splunk** Splunk takes a very different approach to
container monitoring. It uses a Docker API logging driver to send
container log data directly to Splunk Enterprise and Splunk Cloud via
its HTTP Event Collector. You specify the splunk driver (and its
associated options) on the Docker command line. Splunk’s monitoring, in
other words, is integrated directly with Docker, rather than with the
host system. The Splunk log driver requires an HTTP Event Collector
token, and the path (plus port) to the user’s Splunk Cloud/Splunk
Enterprise instance. It also takes several optional arguments. **Setup:
AppDynamics** AppDynamics uses a [Docker Monitoring
extension](https://www.appdynamics.com/community/exchange/extension/docker-monitoring-extension/)
to send Docker Remote API metrics to its Machine Agent. In some ways,
this places it in a middle ground between New Relic and Netuitive’s
agent-based monitoring and Splunk’s close interaction with Docker.
AppDynamics’ extension installation, however, is much more hands-on.
The instructions suggest that you can expect to come out of it with
engine grease up to your elbows, and perhaps a few scraped knuckles. You
must first manually bind Docker to the TCP Socket or the Unix Socket.
After that, you need to install the Machine Agent, followed by the
extension. You then need to manually edit several sections of the config
file, including the custom dashboard. You must also set executable
permissions, and AppDynamics asks you to review both the Docker Remote
API and the Docker Monitoring extension’s socket command file. The
AppDynamics instructions also include troubleshooting instructions for
most of the installation steps.

### What You Get

As you might expect, there are some significant differences in the
metrics which each of these platforms monitors and displays. **Output:
New Relic** New Relic displays Docker container metrics as part of its
Application Performance Monitoring (APM) Overview page; containers are
grouped host servers when Servers for Linux is installed, and are
indicated by a container symbol. The overview page includes drill-down
for detailed performance features. The New Relic Servers monitor
includes a Docker page, which shows the impact of Docker containers on
the server’s performance. It displays server-related metrics for
individual Docker images, with drill-down to image details. It does not,
however, display data for individual containers. **Output: Netuitive**
Netuitive’s Docker monitor collects a variety of metrics, including
several related to CPU and network performance, and almost two dozen
involving memory. It also collects computed CPU, memory, and throttling
percentages. With Netuitive, you build a dashboard by assembling
widgets, so the actual data shown (and the manner in which it is
displayed) will depend on your choice of widgets and their
configuration. **Output: Splunk** Splunk is designed to use data from a
wide range of logs and related sources; for containers, it pulls data
from individual container logs, from Docker and cloud APIs, and from
application logs. Since Splunk integrates such a large amount of data at
the cloud and enterprise level, it is up to the user to configure
Splunk’s analysis and monitoring tools to display the required data.
For containers, Splunk recommends looking at CPU and memory use,
downtime/outage-related errors, and specific container and application
logs to identify problem containers. **Output: AppDynamics** AppDynamics
reports basic container and system statistics (individual container
size, container and image count, total memory, memory limit, and swap
limit), along with various ongoing network, CPU, and memory statistics.
It sends these to the dashboard, where they are displayed in a series of
charts.

### Which Service Should You Use?

When it comes to the question of which monitoring service is right for
your container deployment, there’s no single answer. For most
container-based operations, including Rancher-managed operations on a
typical Linux distribution, either New Relic or Netuitive should do
quite well. With reasonably similar setup and monitoring features, the
tradeoff is between New Relic’s preconfigured dashboard pages and the
do-it-yourself customizability of Netuitive’s dashboard system. For
enterprise-level operations concerned with integrated monitoring of
performance at all scales, from system-level down to individual
container and application logs, Splunk is the obvious choice. Since
Splunk works directly with the Docker API, it is also likely to be the
best option for use with minimal-feature RancherOS deployments. If, on
the other hand, you simply want to monitor container performance via the
Docker API in a no-frills, basic way, the AppDynamics approach might
work best for you. So there it is: Look at what kind of container
monitoring you need, and take your pick.
