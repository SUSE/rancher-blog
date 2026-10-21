---
title: "Why we're building a container infrastructure platform at Rancher Labs"
date: 2015-06-09T11:30:00
slug: "why-were-building-a-container-infrastructure-platform-at-rancher-labs"
authors: ["Sheng Liang"]
products: ["Company/community"]
tags: ["history", "docker"]
content_type: "company-news"
draft: false
migration:
  wp_id: 87291
  original_url: "https://www.suse.com/c/rancher_blog/why-were-building-a-container-infrastructure-platform-at-rancher-labs/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Today we [announced
Series A
funding](https://rancher.com/press-release-rancher-labs-secures-10m-in-series-a-funding-for-managing-container-infrastructure/)
and officially launched our company Rancher Labs. We started Rancher
Labs because we saw the benefits of running Docker containers in
production and wanted to build tools to help make it happen. We are
building two open source software products: Rancher and RancherOS.
Rancher is a container infrastructure platform designed to make it
simple to operate Docker in production. RancherOS is a minimal Linux
distribution designed specifically for running Docker. While we believe
combining Rancher and RancherOS can result in a uniquely capable
production platform, Rancher and RancherOS are not tightly coupled.
Rancher can manage Ubuntu, RHEL/CentOS, or CoreOS just as well as it
manages RancherOS.

### **Why we decided to build Rancher and RancherOS**

The motivations for both products, Rancher and RancherOS, are rooted in
our belief that Docker is much more than a packaging format, and that it
will become the predominant application runtime platform in the future.
We form this belief based on our learnings from many Docker, Rancher,
and RancherOS users. Three trends have started to appear:

**First, users
are gravitating towards the native Docker experience.** Despite the
numerous orchestration platforms that wrap Docker runtime and provide
high-level abstractions for Docker management, most users choose to
stick with the Docker CLI (e.g, docker run) and the standard Docker API.
This is not a surprise since Docker’s native CLI and API are
exceptionally well built and well designed. We have spoken with many
organizations who are foregoing complex docker container orchestration
solutions and instead use configuration management tools such as Chef,
Puppet, Ansible, and SaltStack to orchestrate Docker native CLI in
production. As Docker continues to develop, the scope of native Docker
experience will broaden to include Docker native orchestration and
scheduling, enabled by Docker Machine, Docker Compose, and Docker Swarm.

**Second, Docker containers are transforming application management.**
By introducing a common application packaging, distribution, and runtime
format, Docker transforms application management. Reusable application
blueprints become a reality and can be deployed independent of the
programming language and target cloud platform. Application
provisioning, scaling, and upgrades can be separated from the
application logic itself. Application management can finally be
practiced by the devops team independent of the application developers.
Docker-built tools such as Docker Compose and third-party tools such as
Kubernetes are both promising developments in Docker application
management.

**Third, containerized applications have created
requirements for a new set of infrastructure services for containers.**
Docker as a new way of consuming infrastructure has defined a new set of
requirements on infrastructure.

Whether you are running a traditional
multi-tier app or cutting-edge microservices app using containers, you
will likely require the following infrastructure services:

1. A number of Linux hosts capable of running Docker containers. These
   hosts may be virtual machines or physical machines in your data
   center, or they may be cloud-hosted instances. A networked Linux
   host is the standard unit of computing resources for Docker.
   Regardless where it comes from, each Linux host provides largely
   consistent CPU, memory, storage, and network connectivity.
2. A network that enables containers on different hosts to communicate
   with each other. This can be achieved using coordinated port
   mappings or software defined network (SDN) technologies running on
   the Linux hosts.
3. Load balancer, DNS, and health check support. Load balancers are
   required to expose services to the Internet. DNS is commonly used to
   implement service discovery. Integrated health check ensures only
   healthy containers are used to serve requests.
4. A way to perform actions triggered by certain events, such as
   restarting new containers on host failure, ensuring a fixed number
   of healthy containers are available, or ensuring new hosts and
   containers are created in response to increased load.
5. A way to clone services by creating new containers from existing
   containers. This is required, for example, when we upgrade a service
   by creating containers running a new version of the Docker image.
   After we make sure the newly cloned service works, we can complete
   the upgrade by redirecting the load balancer and DNS from the
   existing containers to the cloned containers.
6. Storage snapshot and backup. This is required, for example, when we
   want to backup a stateful container for disaster recovery purposes.

We have talked to many organizations who have had to make a sizable
development effort and to integrate a number of open source technologies
in container SDN, service discovery, load balancing, DNS, and
distributed storage management. A product that delivers a powerful set
of infrastructure services out of the box will make it easier for
organizations to run Docker in production.

### **How we built Rancher and RancherOS**

We designed Rancher to address all of the above three use cases. Rancher
is not another orchestration or management layer that shields users from
the native Docker experience. As Docker platform grows over time, a
wrapper layer will likely be superseded by native Docker features.
Rancher instead works in the background so that users can continue to
use native Docker CLI and Docker Compose templates. Rancher uses Docker
labels –a Docker 1.6 feature contributed by Rancher Labs– to pass
additional information through the native Docker CLI. Because Rancher
supports native Docker CLI and API, third-party tools like Kubernetes
work on Rancher automatically. Rancher implements a set of
infrastructure services including multi-host networking, load balancer,
DNS, health checks, event triggers, service cloning, and storage
management. Rancher implements all the infrastructure services as
software, and does not depend on any underlying cloud or virtualization
platform API. Rancher requires just Linux hosts running Docker with CPU,
memory, local disks, and network connectivity. Rancher includes user,
project, and environment management so multiple users can collaborate
over multiple projects and across dev, QA, staging, and production
environments.

Recognizing the fundamental unit of computing for Docker
is a Linux host, we designed RancherOS to be the best Linux platform for
running Docker containers. By using Docker daemon itself as PID 1 and
running all system services as containers, RancherOS offers the smallest
(at around 20MB), easiest-to-manage, and the most robust Linux
distribution for running Docker in production. Many organizations have
already started to work with Rancher and RancherOS. A major SaaS
provider is orchestrating their Docker containers using Puppet scripts
and Rancher, leveraging Rancher’s abilities to work with the native
Docker CLI. A web company has gone a step further and is deploying a
full-stack Docker production platform using Rancher and RancherOS. In a
more traditional IT setting, a major bank is evaluating using Rancher to
manage container workload running on their existing vSphere cluster,
leveraging Rancher’s abilities to manage multiple users, projects, and
environments.

If you have not done so, check out our product pages for
[Rancher](https://rancher.com/)and [RancherOS](https://rancher.com/os/) or our open source
[GitHub](https://github.com/rancher/rancher)repositories. It is easy
to get Rancher and RancherOS up and running. All you need is the ability
to create a couple of Linux instances on your laptop or in the cloud. We
are putting the finishing touches on Rancher and RancherOS products and
are getting ready to launch official Beta programs on both products.

Stay tuned for further announcements, and to learn more please join us
for our June 16th online meetup to see a demo of Rancher and meet some
of our team. You can register by following the link below:
