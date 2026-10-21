---
title: "Rancher now supports Docker logs"
date: 2015-02-26T11:16:00
slug: "rancher-now-supports-docker-logs"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["observability"]
content_type: "release"
draft: true
migration:
  wp_id: 86940
  original_url: "https://www.suse.com/c/rancher_blog/rancher-now-supports-docker-logs/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x Docker logs feature"
  redirect_target: "rancher.com/blog (hub)"
---

Hi, I’m James Harris,
([@sir\_yogi\_bear](https://twitter.com/Sir_Yogi_Bear)) one of the
engineers here [@Rancher\_Labs](https://twitter.com/Rancher_labs), and
I am excited to announce we added support this week for pulling and
viewing Docker logs in Rancher. The addition of the feature allows users
to easily work with their containers from the web UI in a much more
involved way. Previously, there was no way to track the output of a
container through Rancher. Now you can easily follow both the Std out
and Std error of a container. This is the first step in adding more
advanced log management capabilities to Rancher. ![Container
UI](https://i.imgur.com/KnPtuZg.png "Container UI") You can see the new
feature when you look at any container in Rancher. In the top left of
the container screen you will see several icons for taking actions on a
container. ![Container
Actions](https://i.imgur.com/kT9cnBp.png "Container Actions")
![Container Actions Stopping
State](https://i.imgur.com/GVEqVoh.png "Container Actions Stopping State")
![Container Actions
Stopped](https://i.imgur.com/vYvWrk5.png "Container Actions Stopped")
Clicking on the: ![Logs
Icon](https://i.imgur.com/LNyv18C.png "Logs Icon") will allow you to
view the container logs screen. We have two ways of displaying
container’s logs. One where the logs are combined: ![Container Logs
Screen With
TTY](https://i.imgur.com/vWTrMqJ.png "Container Logs Screen With TTY")
And another where logs are separated between standard error and standard
out. This is available when a container is created without the tty flah
selected. Combined:![Container Logs Screen Without
TTY](https://i.imgur.com/G1FEANG.png "Container Logs Screen Without TTY")
Just Std Out:![Container Logs Screen Without Just Std
Out](https://i.imgur.com/KNG1nHU.png "Container Logs Screen Without Just Std Out")
Just Std Error:![Container Logs Screen Without Just Std
Error](https://i.imgur.com/UdDdggy.png "Container Logs Screen Without Just Std Error")
I hope that this new functionality in Rancher enables better management
of your containers, and please stay tuned, we’re going to be adding a
number of other capabilities around log management in the future. If
you’d like to see this or any other Rancher functionality. Please
don’t hesitate to schedule a one on one demo, where we can walk you
through the current features, and some of the capabilities we’re still
working on. James Harris
[@sir\_yogi\_bear](https://twitter.com/Sir_Yogi_Bear)
