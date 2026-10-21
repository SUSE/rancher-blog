---
title: "Adding Label Support to Docker 1.6"
date: 2015-04-16T11:28:00
slug: "adding-label-support-to-docker-1-6"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["developer-experience"]
content_type: "company-news"
draft: true
migration:
  wp_id: 87216
  original_url: "https://www.suse.com/c/rancher_blog/adding-label-support-to-docker-1-6/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Docker 1.6 labels, 2015 news"
  redirect_target: "rancher.com/blog (hub)"
---

Over the last few months our team, with the help of Daniel Walsh
([@rhatdan](https://twitter.com/rhatdan)) from Red Hat and many other
community members, have worked to add support for [labels in Docker
1.6](https://github.com/docker/docker/pull/9882/). Labels allow users
to attach arbitrary key value metadata to Docker images and containers.
This feature, while very simple in concept, gives us the opportunity to
add many powerful features to Rancher, and will benefit everyone in the
Docker ecosystem. If you understand how environment variables work in
Docker, you will see that container labels function very much the same
way. Labels are similar to environment variables in that they are key
value pairs attached to an image or a container. Labels are different
from environment variable in that they are not visible to the running
application and they can also be used for fast look-up of images and
containers.

## Container and Image Labels

To apply a label to an image just use the LABEL command in your
Dockerfile. For example `FROM busybox LABEL com.example.foo=bar`
`docker build -t test .` Once you have your image with a label, you can
then search for your image using
`docker images -f label=com.example.foo=bar` If you create a container
from that image that label will be applied to the running container.
`docker run --name test test echo hi docker inspect -f '{{.Config.Labels}}' test`
Additionally you can apply more labels when launching a container, and
then search based on those new labels
`docker run --name test2 -l com.example.bar=baz test echo hi docker ps -a -f label=com.example.bar=baz`

## Using Labels with Rancher

At Rancher Labs we plan to use labels extensively. For example, Rancher,
our orchestration system, provides the ability to deploy a
container-based, auto-scaling load balancer. In order to load balance a
workload, you must specify the targets you want to direct traffic
towards. There are many ways to do that, but we wanted to find the
simplest and most flexible way. Also, we’ve made it a priority to
always support a Docker native interface. If we have to come up with our
own Load Balancing API, that is not as desirable as using an approach
based on Docker’s interface. With labels, that is now possible. When a
user starts a container all they have to do is add the label
“io.rancher.service.provides=foo“. There is then an existing load
balancer configured in Rancher that will see that container with that
label and then add it to the existing Load Balancer. This means you can
use various means to add targets to load balancers. For example a
configuration management tool like Puppet or Chef or using Amazon’s
auto scaling services. Through the power of labels we can attach
additional metadata to containers that can be used to add more services
to the container. I hope you’ll find this feature as useful as we think
it will be. If you’d like more information on using Rancher to manage
containers, please join our next online meetup, where we’ll be
demonstrating some of these capabilities
