---
title: "Understanding Cattle, Swarm and Kubernetes in Rancher"
date: 2016-06-02T11:40:00
slug: "understanding-cattle-swarm-and-kubernetes-in-rancher"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["multi-cluster"]
content_type: "explainer"
draft: true
migration:
  wp_id: 87340
  original_url: "https://www.suse.com/c/rancher_blog/understanding-cattle-swarm-and-kubernetes-in-rancher/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Cattle and Swarm discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

How to Manage Workloads on Kubernetes with Rancher 2.0 Online MeetupLearn how to deploy Kubernetes applications in Rancher 2.0, and use the monitoring, logging and pipeline features.[Watch the video](https://rancher.com/events/2018/april-online-meetup-managing-workloads-on-kubernetes-with-rancher-2-0/)

[![swarm small
intro](images/rancher_blog_swarm-small-intro.png)](images/rancher_blog_swarm-small-intro.png)
\*Note: Since publishing this post, we’ve created a guide comparing
Kubernetes with Docker Swarm. You can read the details in the blog post
[here](https://rancher.com/comparing-kubernetes-and-docker-swarm/).**.**\*
Over the last six months, Rancher has grown very quickly, and now
includes support for multiple orchestration frameworks in addition to
Cattle, Rancher’s native orchestrator. The first framework to arrive
was [Kubernetes](https://rancher.com/kubernetes), and not long
after, [Docker Swarm](https://rancher.com/swarm/) was added. This week,
the team at Rancher added support
for [Mesos](https://rancher.com/announcing-mesos-support-in-rancher/).
For this article, I’m going to focus on Cattle, Swarm, and Kubernetes,
and as I gain experience with Mesos, I’ll share my thoughts in another
post. Rancher’s support for these different orchestration platforms is
delivered by creating isolated “environments.” When a user or admin
creates an environment, they select the orchestration platform he or
she wants to use, and which users will have access to the new cluster.
Rancher works with Active Directory, LDAP and GitHub, so you can grant
different access privileges to teams or individual on a per cluster
basis. Once you’ve created the environment, Rancher prompts you to add
“hosts,” which are just Linux physical or virtual machines that
running Docker and Rancher’s agent, which is a container. As soon as
the first hosts are added, Rancher begins deploying the orchestration
framework you’ve chosen, and you can start using your new environment.
Each of these orchestration platforms has a different set of
capabilities. For this article, I won’t try to provide a list pros and
cons for each, or a long table comparing features. They are all changing
very quickly, so anything I write would be out of date within a month or
two. Instead, I’ll share some of my personal experiences with all
three, and the scenarios in which I use each of the three frameworks.
Rancher makes it so easy to deploy each of these that I highly recommend
you try them out for yourself and determine which fits your project
best.

## Three Frameworks

First, it is important to note that while deploying a new host with
Cattle is almost immediate, doing it with Swarm and Kubernetes can
take 5-10 minutes as servers are added and each orchestration framework
is implemented. From a user perspective, it isn’t any more complex to
deploy the different platforms, as Rancher automates all the deployment
and configuration of the orchestration platforms. The Kubernetes
framework typically takes the longest to launch, as it is built as a set
of microservices such as etcd (a distributed key-value store for the
cluster), the kubernetes master, kubernetes scheduler, and a handful of
other Kubernetes-native services.

### Cattle

Cattle was the first orchestration framework available when Rancher
started its beta last June. Because of this, it feels quite mature and
stable, and the user experience is very good. At its core, Cattle
should feel very familiar to anyone familiar with Docker. It is based on
Docker commands and leverages docker-compose to define application
blueprints. Application deployments are organized into “stacks,” which
can be launched directly from an application catalog, automatically
provisioned from a docker-compose.yml file and extended with a
rancher-compose.yml file, or created directly within the UI. Each stack
is a made up of “services,” which are primarily a docker image, along
with scaling information, health checks, service discovery links, and a
host of other configurables. You can also include load balancing
services and externals services into a cattle stack. Because it has been
around for so long, Cattle has developed a very large application
catalog, the vast majority of which has been developed by users and
contributed to
the [rancher/community-catalog](http://github.com/rancher/community-catalog)
github repo. You can now choose from more than 50 different apps, all
of which are defined using a docker-compose file and a rancher-compose
file, and deploy them with a single click. This is the kind of
capability that we like most here
at [FricolaB](https://fricolab.github.io/). You can even build a
private catalog from your own git repo, and expose it within your
environment from the settings tab within Rancher. In the example
illustrated in the screenshot, we have created a stack for Gogs, an
application that provides similar functionality to Github, based on the
Go language. In this stack, we have added a load balancer service to
make the external http port that provides access to the graphical Gogs
interface available in a custom subdomain of our server. Thus, our final
deployment will consist simply of three containers; a container with the
database, another with the application, and a third container with a
load balancer. [![The Cattle community app
catalog](images/rancher_blog_lareo3-1024x576.png)](https://cdn.rancher.com/wp-content/uploads/2016/05/16205924/lareo3.png)
The Cattle community app catalog

### Swarm

Docker Swarm is the native Docker clustering system, and important for
anyone who will be working heavily in the Docker ecosystem. I think it
is important for any container management platform to support Swarm, as
it will probably be the most familiar platform for many users. Because
it uses the native Docker API, orchestrating a cluster with Docker
Swarm allows us to keep compatibility with other standard tools. For
example, EduCaaS, a project that [FricolaB](https://fricolab.github.io/)
is developing with [MTA](http://mondragonteamacademy.com/), provides
users with a simple graphical interface based on Docker Swarm to manage
their applications but platform administrators still have perfect
control of all applications being deployed on the platform from within
Rancher GUI. [![Adding hosts and services for Swarm within
Rancher](images/rancher_blog_swarm-features.png)](images/rancher_blog_swarm-features.png)
Adding hosts and services for Swarm within Rancher Swarm
initial deployment, as already mentioned, is a bit more complex than
Cattle. It uses two extra containers in addition to the Rancher agent:
one acts as Swarm master node and the other one a first client node. We
can check it out inside the System section, which now appears inside of
the new menu item, Swarm, which replaces the Application menu once we
have chosen Swarm as our orchestrator. System submenu is equivalent to
the one we had before with Cattle called “Stacks”. In fact, there we can
still control the stacks that had been created before using Cattle. Now
in this new menu we have three elements. One of them provides us access
to our server via terminal, allowing us to download the configuration
file, connect to the remote Docker socket, and manage our server from
the PC using Docker or Docker Compose. The other two tabs, Projects and
Services, show the containers we are deploying inside Swarm. From
Projects, we can add stacks from the internal catalog or attach a custom
docker-compose.yml file. The Services tab will show individual services
already deployed, indicating the number of containers available for each
service. Every time we deploy a project on our cluster Swarm, a
container will be included within each cluster node, so if we have a
cluster consisting of 4 nodes each service will have 4 containers
associated. This is similar to the way Docker Swarm deployments work
without Rancher.

### Kubernetes

[![Managing Kubernetes services within
Rancher](images/rancher_blog_kubernetes-services_expanded_edited-1024x657.jpg)](https://cdn.rancher.com/wp-content/uploads/2016/06/01185359/kubernetes-services_expanded_edited.jpg)
Managing Kubernetes services within Rancher For users
familiar with Docker, Kubernetes can have the biggest learning curve of
all these scheduling options. Many of the concepts are quite different
in Kubernetes from Swarm or Cattle, which both will feel very familiar
to anyone who knows Docker. For example, in Kubernetes, the initial
deployment is not a container, but instead a “pod,” which can include
multiple containers. These pods are then assigned to services and
scaling is managed by replication controllers. All of this is pretty
easy to understand once you’ve spun up a Kubernetes environment in
Rancher. The initial deployment of Kubernetes takes a few minutes,
since [as previously described], it is built using a number of
microservices, and with kubelets and proxy services on each hosts.
However, Rancher makes using Kubernetes quite easy by automating the
deployment and scaling of the cluster, and creating an initial namespace
as soon as you add your first host. One thing to note, it probably makes
sense to deploy Kubernetes on multiple VMs. I tried to deploy it once
on a single 4GB RAM server, and spinning everything up took more than 15
minutes, and sometimes failed due to lack of memory. Once you have the
cluster running, you can access it through the Rancher UI, and directly
log into kubectl. You can also manage manage all deployed services, pods
and replication controllers from the UI, and deploy applications from
the Kubernetes catalog.

## Closing Note

Although it is not the purpose of this post to make a value judgment
about the three orchestrators, it would be unfair not to mention that
the first two are my favorites. I use Cattle in almost all the
environments I manage with Rancher, but I opt for Swarm when it comes to
servers in which I have delegated certain management functions to users,
since Docker ecosystem provides numerous tools that are worth using in
parallel. Obviously, this is just my point of view: the right solution
is always what meets your needs! \*David Lareo is a Rancher user and the
founder of [FricolaB](http://www.fricolab.com). He designs products and
services that respect the fundamental values of the hacker ethic, such
as social awareness, accessibility. \*

How to Manage Workloads on Kubernetes with Rancher 2.0 Online MeetupLearn how to deploy Kubernetes applications in Rancher 2.0, and use the monitoring, logging and pipeline features.[Watch the video](https://rancher.com/events/2018/april-online-meetup-managing-workloads-on-kubernetes-with-rancher-2-0/)
