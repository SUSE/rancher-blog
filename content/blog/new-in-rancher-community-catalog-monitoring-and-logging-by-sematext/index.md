---
title: "New in Rancher Community Catalog: Monitoring and Logging by Sematext"
date: 2016-07-20T11:12:00
slug: "new-in-rancher-community-catalog-monitoring-and-logging-by-sematext"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["observability"]
content_type: "company-news"
draft: true
migration:
  wp_id: 86836
  original_url: "https://www.suse.com/c/rancher_blog/new-in-rancher-community-catalog-monitoring-and-logging-by-sematext/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Community catalog v1 entries"
  redirect_target: "rancher.com/blog (hub)"
---

[[![Sematext Docker
Agent](images/rancher_blog_Sematext-Docker-Agent.png)](images/rancher_blog_Sematext-Docker-Agent.png)]
\*by Stefan Thies ([@seti321](https://twitter.com/seti321)), DevOps
evangelist at [Sematext](http://www.sematext.com). \* [The Rancher
Community Catalog just got two new gems - SPM and Logsene - monitoring
and logging tools from
]**[Sematext](https://sematext.com)**[. If
you are familiar with Logstash, Kibana, Prometheus, Grafana, and
friends, this post explains what SPM and Logsene bring to the Rancher
users’ table, and how they are different from other monitoring or
logging solutions.]

### Meet Sematext Docker Agent

[[Sematext Docker
Agent](http://sematext.com/docker/)] **is a
modern, Docker-native monitoring and log collection agent.** It runs as
a tiny container on every Docker host, and collects logs, metrics, and
events for all cluster nodes and their containers. The agent discovers
all containers on all nodes managed by Rancher. **After the deployment
of Sematext Docker Agent, all logs, Docker events, and metrics are
immediately available out of the box.** Why is this valuable? It means
you don’t have to spend the next N hours or days figuring out which
data to collect, or how to chart it. Plus, you don’t need to resources
to maintain your own logging and monitoring infrastructure - your Docker
metrics and events end up getting shipped to
**[SPM](http://sematext.com/spm)** and logs get shipped to
**[Logsene](https://sematext.com/logsene/)** (SPM is an application
performance monitoring service supporting a **[number of
integrations](https://sematext.com/spm/integrations/)**, including
**[Docker](http://sematext.com/docker)**, while Logsene is a log
management service - a hosted ELK stack that works well with both Kibana
and Grafana). [![Sematext metrics
stack](images/rancher_blog_Sematext-metrics-stack.png)](images/rancher_blog_Sematext-metrics-stack.png)

### DevOps Tools Comparison

There are **[several open source tools for Docker logs and
metrics](https://sematext.com/blog/2016/07/19/open-source-docker-monitoring-logging/)**,
such as cAdvisor and Logspout. Unfortunately, none of these is very
comprehensive, so one is often forced to combine a number of these
tools, which leads down a Franken-monitoring path. This later becomes a
costly technical debt that no one enjoys fixing. Thus, while one might
think Sematext Docker Agent is not much more than a combination of
cAdvisor and Logspout, especially in regards to log management, Sematext
Docker Agent has features such as format detection, log parsing, data
enrichment (Geo-IP, tagging with metadata), and log routing.

### Configure Docker Agent in Rancher Catalog

To setup Sematext Docker Agent with Rancher, you can configure it with
the appropriate catalog template (search for “Sematext” in the
community catalog). Let’s have a quick look at a few key Sematext
Docker Agent features, and how to configure them with Rancher.

#### Automatic Log Tagging for Docker Compose and Kubernetes

All logs are automatically tagged with metadata. This includes support
for Docker/Rancher Compose projects and Kubernetes.

**For Docker Containers**

- Container ID
- Container name
- Image name

**For Docker/Rancher Compose:**

- Service Name
- Project Name
- Container number (if you use scale=N)

**For Kubernetes**:

Note that Kubernetes containers’ logs are not much different from those
of Docker container logs. However, Kubernetes users need to access logs
for deployed pods, so it’s very useful to capture Kubernetes-specific
information available for log search, such as:

- Name space
- Pod name
- Container name
- Kubernetes UID

**TIP: to enable Kubernetes tagging, set
[Kubernetes=1]**

### Log Routing

For large deployments, you may want to index logs for different tenants
or applications in separate indices/Logsene apps (this also lets you
separate who can view which logs). We’ve made this easy: simply tag
your containers with a Docker label, or set the LOGSENE\_TOKEN
environment variable (LOGSENE\_TOKEN=your app token) and Sematext Docker
Agent will ship logs to the correct index! This way you don’t need any
central configuration file to map containers and indices/tokens, and log
routing becomes very dynamic and flexible.

### Integrated Log Parser

[Handling of logs is based on the Docker API and a library called
]**[logagent-js](https://github.com/sematext/logagent-js)**[,
open-sourced by Sematext. This parser framework includes patterns for
log format detection and parsing of a number of different log formats
used by official Docker images such as: ]

- [Web servers like Nginx, Apache httpd or anything using common web
  server log format]
- [Search engines like Elasticsearch and
  Solr]
- [Message queues like Apache Kafaka and nsq.io
  ]
- [Databases like MongoDB, HBase, MySQL]
- [Detection of JSON log format, often used by Node.js applications
  e.g., bunyan and winston logging
  frameworks]

**TIP: to create custom patterns add them to the**
[**LOGAGENT\_PATTERNS**] **catalog template
field.**

### Automatic Geo-IP Enrichment for Container Logs

[Getting logs from Docker Containers
]**collected**[,
]**shipped**[ and
]**parsed**[ out of the box is already a big
time saver, but some application logs need additional
]**enrichment**[ with information from other
data sources. A common use case is to enrich web server logs (or really,
any logs with IP addresses) with geographical information derived from
those IP addresses. ] [Sematext Docker Agent
supports ]**[Geo-IP enrichment of docker
logs](https://sematext.com/blog/2016/04/11/automatic-geo-ip-enrichment-for-docker-logs-2/)**[.
It uses Maxmind Geo-IP lite database, which it periodically updates
automatically for you. There is no need to stop the container or mount
new volumes with the Geo-IP database, or any other manual
work.]

**TIP: to enable Geo-IP enrichment set the environment variable**
[**GEOIP\_ENABLED=true**]**.**

### Filter Container Logs

[In some cases it makes sense to collect only logs from your critical
applications and skip less critical and noisy services (e.g. frequently
running cleanup jobs). To do that you can whitelist and blacklist
containers by image name or container name. The settings take regular
expressions, which are matched against the relevant metadata
fields.]

**Whitelist containers**

[MATCH\_BY\_NAME]

[Regular expression to white list container
names]

[MATCH\_BY\_IMAGE]

[Regular expression to white list image
names]

**Blacklist containers**

[SKIP\_BY\_NAME]

[Regular expression to black list container
names]

[SKIP\_BY\_IMAGE]

[Regular expression to black list image names for
logging]

### How to use the Sematext Catalog Entry

When you run the Rancher server user interface, simply search in the
community catalog for “sematext“, “monitoring” or “logs“.
[![Rancher Catalog monitoring
search](images/rancher_blog_Rancher-Catalog-monitoring-search.png)](images/rancher_blog_Rancher-Catalog-monitoring-search.png)
[Choose “View Details”, and in the “Configuration Options” enter the SPM
and Logsene App tokens. You can obtain these from
][**<https://apps.sematext.com>**,][
where you can sign up and create your SPM and Logsene apps. If your
Rancher cluster runs behind a firewall, you might need to specify the
proxy URL in the HTTPS\_PROXY or HTTP\_PROXY environment variable. If
you run Kubernetes on the same cluster, choose KUBERNETES=1.
] [If you’d like to collect all logs, just
press “Launch” without specifying any filter for containers or images.
] [![Sematext catalog
detail](images/rancher_blog_Sematext-catalog-detail.png)](images/rancher_blog_Sematext-catalog-detail.png)
[![Sematext catalog
options](images/rancher_blog_Sematext-catalog-options.png)](images/rancher_blog_Sematext-catalog-options.png)
[![Sematext
stack](images/rancher_blog_Sematext-stack.png)](images/rancher_blog_Sematext-stack.png)

### Summary

[We hope this introduction to Sematext Docker Agent in Rancher Catalog
helps you get started with Docker monitoring and logging, without having
to take the dreaded Franken-monitoring path. A complete list of
configuration parameters is available on
]**[Github](https://github.com/sematext/sematext-agent-docker#configuration-parameters)**[.
We think the new catalog template covers the most relevant options, but
if you see anything important missing feel free to contribute to the
]**[Rancher community
catalog](https://github.com/rancher/community-catalog)**[ by submitting
an issue or pull request. Give ]**[Sematext
Docker Agent](https://sematext.com/docker/)**[ a try with Rancher and
benefit from a managed service and free plans to watch your cattle while
you sleep. Thanks to the great **[Rancher Community
Catalog](https://github.com/rancher/community-catalog)**, it is super
easy to get monitoring and logging set up and working in no time.
]
