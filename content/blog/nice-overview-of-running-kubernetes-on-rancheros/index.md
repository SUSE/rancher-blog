---
title: "Nice Overview of Running Kubernetes on RancherOS"
date: 2015-03-18T10:20:00
slug: "nice-overview-of-running-kubernetes-on-rancheros"
author: "Rancher Admin"
products: ["RancherOS"]
tags: ["installation"]
content_type: "explainer"
draft: true
migration:
  wp_id: 86764
  original_url: "https://www.suse.com/c/rancher_blog/nice-overview-of-running-kubernetes-on-rancheros/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RancherOS discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

[![Kubernetes running as a system service on
RancherOS](images/rancher_blog_Kubernetes-on-RancherOS-300x158.png)](https://medium.com/@imikushin/running-kubernetes-cluster-on-rancheros-b2bd1308eb6d)
Kubernetes running as a system service on RancherOS from Ivan Mikushin
(@imikushin) Yesterday, Ivan Mikushin did an excellent
write up on deploying [Kubernetes on
RancherOS](https://medium.com/@imikushin/running-kubernetes-cluster-on-rancheros-b2bd1308eb6d).
I spent some time with it, and I think it illustrates some of the
things we are most excited about with RancherOS. Specifically, in
RancherOS we have a concept of system services that are deployed on a
separate Docker daemon that we have called System Docker. In Ivan’s
post he uses the System Docker to deploy and manage Kubernetes, Etcd,
and Flannel. Kubernetes will then deploy containers on the User Docker
daemon. I have to hand it to Ivan for figuring out how to get this all
working in RancherOS, very impressive. In the coming v0.2 and v0.3
(scheduled over the next two weeks) we are working on some new features
to make what Ivan has done much, much easier. First, the system and user
Docker will be fully configurable such that you won’t need to replace
the containers to customize Docker. If you need TLS, custom daemon
args, or even something larger like Powerstrip, you will be able to do
this through configuration. Second, system services can be configured
and defined through a simple yaml configuration file. This will make it
as easy to deploy system services as saying
“enabled\_services=[etcd.yml, flannel.yml, kubernetes-minion.yml]” in
your cloud config. We are really excited about this feature and will be
sharing more details over the next couple weeks. Again, thanks Ivan for
the excellent write up. If you are interested in learning more, please
join me for our first online meetup, March 31st at 1:00 pm US Eastern
time. You can register by following the link below:
