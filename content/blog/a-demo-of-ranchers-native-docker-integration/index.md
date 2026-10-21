---
title: "A Demo of Rancher's Native Docker Integration"
date: 2015-06-25T09:00:00
slug: "a-demo-of-ranchers-native-docker-integration"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["developer-experience"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 85786
  original_url: "https://www.suse.com/c/rancher_blog/a-demo-of-ranchers-native-docker-integration/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x native Docker demo"
  redirect_target: "rancher.com/blog (hub)"
---

[![Docker Native
Provisioning](images/rancher_blog_Docker-Native-Provisioning-300x163.png)](https://cdn.rancher.com/wp-content/uploads/2015/06/25210421/Docker-Native-Provisioning.png)Hi,
I’m Craig Jellick, an engineer here at Rancher Labs, and I wanted to
walk you through a new set of features that we recently added to Rancher
as we prepared for beta. Internally, we call it our “Native Docker
Management” functionality, and it is incredibly core to our mission
here at Rancher. When we built Rancher, we explicitly didn’t want
to wrap Docker’s APIs with a new management layer. A number of existing
tools already take that approach, and while it is an effective way of
building a controlled system, we really loved the experience using the
Docker CLI and API, and were sure that it would just keep getting better
over time. Because of that we’ve developed Rancher so that it can work
behind the scene as you use Docker directly, or with your favorite
scripting tool. I wrote a few months ago about how we were working
with [Docker events](https://rancher.com/working-with-docker-events/) to
understand what happens on a host, and Darren Shepherd talked about the
importance of [Docker Labels](https://rancher.com/docker-labels/), which
were added to Docker in 1.6. Now, I want to show you how these pieces
fit together to allow users to configure Rancher services directly from
the Docker CLI on any host running our agent containers. I’ve created a
video that demonstrates this approach, and welcome any feedback or
questions you might have in the comments section. You’re
also welcome to ping us on [Twitter](http://twitter.com/guerillanerd) or
#Rancher on IRC if you have any questions.

If you’d like to learn more about Rancher, join our [beta
program](https://info.rancher.com/beta).
