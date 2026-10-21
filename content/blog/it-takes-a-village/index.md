---
title: "It Takes a Village"
date: 2019-09-12T09:06:00
slug: "it-takes-a-village"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_tools.png"
products: ["Company/community"]
tags: ["developer-experience"]
content_type: "community"
draft: true
migration:
  wp_id: 85868
  original_url: "https://www.suse.com/c/rancher_blog/it-takes-a-village/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rodeo and RanchCast promo"
  redirect_target: "rancher.com/blog (hub)"
---

## The Look

[Rancher Rodeos](https://rancher.com/rodeos) are great events for learning Kubernetes and Rancher beginner-level concepts, with attendees gaining just the right amount of knowledge to get started with provisioning Kubernetes clusters and launching applications.

I present frequently at Rodeos, and the scene typically unfolds like this: together with attendees, we are walking through Rancher features, and usually as we’re experimenting with [Monitoring, Alerting, and Logging](https://rancher.com/docs/rancher/v2.x/en/cluster-admin/tools/), I see the wheels start turning in their heads. It’s at that point that they start to understand the complexities that come with deploying applications at scale. Soon it will be their team who is on the hook to deliver. I see **that** look: the pop quiz has been announced and no one is ready for what’s coming!

## It’s Not Just About Kubernetes

Maybe you’re in that boat. Your team is tasked with implementing Kubernetes, but you’ve realized that your tasks go **beyond** Kubernetes. While Kubernetes and containers are the best things to happen to computing in the past decade, Kubernetes modus operandi is the management of containers and not a whole lot more.

That’s not to undersell the value of Kubernetes. It accomplishes its objectives with elegance and simplicity. Once you conquer the initial learning curve, deploying Kubernetes at scale doesn’t add significant complexity to Kubernetes management itself. But running your applications in Kubernetes, at scale, goes far beyond the orchestration of containers.

## What Did I Get Myself Into?

Let’s say you have Kubernetes. That’s great! You probably already have some software that you’ve containerized, but now you’re faced with challenges that you may not have expected when you started. For example:

- *My system logs to files. How will I aggregate and collect them? How do I analyze them for useful information when I’m running 10, 100 or 1000 copies? How do I use this to troubleshoot issues?*
- *It was easy to monitor a couple servers. But we’re scaling this application to over 50 instances. How do I know if it’s behaving as expected? How do I see behavior changes when developers build new features or pay back technical debt?*
- *Debugging a microservice is easy on the developer’s laptop, but how do we debug a workflow that’s calling a dozen different microservices in the cluster?*
- *How do I know we’re meeting our contractual service level agreements?*

Bottom line, developing and managing software at scale can be challenging. In addition to baseline Kubernetes management, you also have a host of other potential concerns, including:
- Logging
- Monitoring
- Alerting
- Registry focused image scanning
- Run-time focused container scanning
- Disaster recovery
- Run-time distributed firewall
- Content caching
- Persistent storage
- And more!

## Never Fear, The Rancher Community is Here to Help!

If you’re dealing with any of these challenges, you are not alone! The Rancher community is comprised of more than 30,000 like-minded users, contributing ideas and supporting each other on their respective Kubernetes journeys. If you’re not already a member, I encourage you to join us via any of the following platforms:

- Forums - <https://forums.suse.com/>
- GitHub - <https://github.com/rancher>
- Slack - <http://slack.rancher.io/>

Another great resource is Rancher RanchCasts. RanchCasts air every Wednesday. Each week we pick a topic (e.g. logging with Elastic, monitoring with Prometheus) and collaborate real-time to build example code which can be shared with everyone. Its’ a great forum to leverage the collective knowledge of the community and share your own expertise. It’s never too late to join us. [The code](https://github.com/jasonvanbrackel/automate-all-the-things) is designed to be picked up at any point, and past episodes can be found on YouTube.

The time will vary each week to accommodate users world-wide. Follow [@Rancher\_Labs](https://twitter.com/rancher_labs) and [@jasonvanbrackel](https://twitter.com/jasonvanbrackel) to get the scoop on upcoming sessions. You can also subscribe to RanchCasts using any of the following platforms:

- YouTube - [youtube.com/c/theranchcast](https://youtube.com/c/theranchcast)
- Mixer - [mixer.com/theranchcast](https://youtube.com/c/theranchcast)
- Twitch - [twitch.tv/theranchcast](https://youtube.com/c/theranchcast)
- GitHub - [github.com/jasonvanbrackel/automate-all-the-things](https://youtube.com/c/theranchcast)

There’s never been a better time to go all-in with Kubernetes, and together, there’s no challenge we can’t overcome. I look forward to seeing you in the Rancher community and participating in upcoming RanchCasts!
