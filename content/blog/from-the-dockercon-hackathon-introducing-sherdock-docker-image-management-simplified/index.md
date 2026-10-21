---
title: "From the DockerCon Hackathon - Introducing SherDock: Docker Image Management Simplified"
date: 2015-06-21T11:20:00
slug: "from-the-dockercon-hackathon-introducing-sherdock-docker-image-management-simplified"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["ci-cd", "developer-experience"]
content_type: "community"
draft: true
migration:
  wp_id: 87084
  original_url: "https://www.suse.com/c/rancher_blog/from-the-dockercon-hackathon-introducing-sherdock-docker-image-management-simplified/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Past hackathon tool for Docker 1.x era"
  redirect_target: "rancher.com/blog (hub)"
---

![SherDock-Logo](images/rancher_blog_SherDock-Logo-300x220.png)This year we sponsored the
[DockerCon](https://github.com/rancherio/sherdock)Hackathon, and had an
amazing 24 hours working with people hacking on Docker, Rancher,
RancherOS and more. Two of our team, [Darren
Shepherd](http://twitter.com/@ibuildthecloud) and [Alena
Prokharchyk](http://twitter.com/@lemonjet) were judges, so we didn’t
think it would be fair to enter the contest. That said, we wanted to be
involved in the hacking anyway so we built a little tool called
[SherDock](https://github.com/rancher/sherdock), a simple image
management tool for garbage collection, identifying orphaned volumes and
more. The idea was to help de-clutter your Docker environment, and at
the same time ensure images you do want are always available, with the
latest versions pulled if so desired. Specifically, SherDock runs on a
single Docker host and does the following: - Discovers images,
their sizes, and whether they are in use. - Shows volumes and reads on
disk meta data to determine orphaned volumes. - Graphs image layers
and relationships - Garbage collect unused images on a configurable
interval - Defines an exception list from garbage collection -
Automatically pulls and caches images on a timed interval to ensure
latest versions of a Rancher is available Everything is managed through
the SherDock web interface, which can be exposed when you deploy the
rancherio/sherdock container. You can see all the source code, and find
installation instructions for SherDock on
[github](https://github.com/rancher/sherdock). Special thanks to the
big help from [Josh Curl](http://twitter.com/joshwget) and [Ankush
Agarwal](https://twitter.com/ankushio) who joined our team and were
incredibly helpful in building the garbage collection and backend
systems! **Volume Management in SherDock:** [![sherdock screenshot
volumes](images/rancher_blog_sherdock-screenshot-volumes-1024x593.png)](https://cdn.rancher.com/wp-content/uploads/2015/06/21185811/sherdock-screenshot-config.png)**SherDock
Configuration Management** [![sherdock screenshot
config](images/rancher_blog_sherdock-screenshot-config-1024x586.png)](https://cdn.rancher.com/wp-content/uploads/2015/06/21185811/sherdock-screenshot-config.png)[](https://cdn.rancher.com/wp-content/uploads/2015/06/21185811/sherdock-screenshot-volumes1.png)
