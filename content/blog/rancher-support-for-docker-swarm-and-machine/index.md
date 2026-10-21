---
title: "Rancher support for Docker Swarm and Machine"
date: 2015-01-13T11:17:00
slug: "rancher-support-for-docker-swarm-and-machine"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["docker"]
content_type: "company-news"
draft: true
migration:
  wp_id: 86949
  original_url: "https://www.suse.com/c/rancher_blog/rancher-support-for-docker-swarm-and-machine/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Docker Swarm support plans, Rancher 1.x era"
  redirect_target: "rancher.com/blog (hub)"
---

Hi Everyone, I’m Will Chan, the new VP of engineering here at Rancher,
and I wanted to post an update about some of the things we’re working on
here at Rancher for release later this quarter. I started at Rancher in
early December, and since then I’ve been thrilled to see how many people
have downloaded Rancher and are using it to manage and implement
networking around Docker. I’m really excited about some of the features
we’re working on, and wanted to give you a sneak peek of what’s coming
over the next two months. Docker Swarm Rancher has always
closely followed Docker, and based on announcements at DockerCon in
Amsterdam, we are excited to announce that we’re working on adding
support for Docker Swarm and Docker Machine. If you haven’t had a chance
to look at these features, please do so as we feel [Docker
Swarm](https://github.com/docker/swarm "Docker Swarm"), a tool that
allows the deployment of Docker containers into multiple hosts, and
[Docker Machine](https://github.com/docker/machine "Docker Machine"), a
tool that allows the creation of Docker-enabled hosts across various
cloud providers, will become core elements of the Docker ecosystem. Here
are some of features we plan on developing in the short term:

- Docker Machine Support: Docker Machine is designed to run locally on
  the machine where it has been installed. We will be integrating this
  functionality with Rancher so that users will be able to create new
  Docker enabled hosts via Rancher’s UI/API and automatically have
  those hosts register with Rancher. This should simplify scaling of
  infrastructure, and will enable Docker Machine to work with all of
  Rancher’s networking and orchestration capabilities. Of course, you
  can always create hosts via machine outside of Rancher and register
  them manually with Rancher, but we think once you start using
  machine within Rancher you’ll find it much easier.
- Docker Swarm Support: Swarm is also currently a tool that is
  intended to run locally on the machine where it was installed. We
  want to help Swarm scale, so we’re adding a few things to the Swarm
  experience:
  - First, if you create a Swarm cluster via the Rancher UI/API, we
    will automatically create and manage a swarm-server that Rancher
    can communicate against. We will also automatically install the
    swarm-agent on any hosts that have been added to Swarm via
    Rancher.
  - Second, we are working with the Docker team to extend Swarm so
    that a cluster can be created outside of Rancher and
    automatically imported into Rancher for management.
- New UI: We are working on an entirely new UI that will debut soon.
  The UI will focus on visualizing containers, swarms and hosts, and
  will incorporate support for many of the new features we’ll talk
  about below.
- Authentication Support: Currently, Rancher supports a single user
  model. We plan to integrate a framework that will allow
  authentication against an external system via LDAP, OAUTH, SAML,
  etc. Our first implementation will be against Github via OAUTH. With
  this feature, users will be able to invite colleagues to join
  Rancher and collaborate.
- Projects: To extend the focus on collaboration, Rancher is adding
  support for projects. Projects will allow users to share hosts and
  containers across multiple accounts. Initially, we’ll be defining
  Project members as Github team members.

As we work on all of this, we’ll be sharing design and implementation
details on [GitHub](https://github.com/rancher/rancher). Please don’t
hesitate to send feedback. Our goal is to create a fantastic operations
platform that will allow users to seamlessly work with existing Docker
environments and preserve the native Docker experience. Happy New Year
and here’s to a successful 2015! Will
