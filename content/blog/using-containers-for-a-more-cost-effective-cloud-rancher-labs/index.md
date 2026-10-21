---
title: "Using Containers for a More Cost-Effective Cloud | Rancher Labs"
date: 2017-05-22T11:29:00
slug: "using-containers-for-a-more-cost-effective-cloud-rancher-labs"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["cloud", "aws"]
content_type: "explainer"
draft: true
migration:
  wp_id: 87243
  original_url: "https://www.suse.com/c/rancher_blog/using-containers-for-a-more-cost-effective-cloud-rancher-labs/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Spotinst webinar and Rancher 1.x"
  redirect_target: "https://rancher.com/blog (hub)"
---

Even with the almost unimaginable efficiencies achieved by the major
public cloud providers, at any given time they still have excess
capacity that is left idle. And as an incentive to try to get some
return on those resources, both AWS and Google Compute Engine are
willing to sell those resources at a steep discount, usually starting at
around 90%. What’s the catch? Well, the prices are market driven, set
by the highest bidder. It’s a classic marketplace model: demand drives
the value of assets. The challenge for public cloud users, however, is
that at any given time the spot instance you are using can be reclaimed
if someone outbids you. With Amazon, you have two minutes to vacate the
instance before it is terminated; Google Cloud gives you 30 seconds.
This volatility has kept the bulk of companies using public clouds away
from this model. How can I expect to keep my application running if I
can lose a server at any given moment, especially if setting up the
server to be production ready takes significant amount of time? It is
not uncommon for configuration management tools to take 10 or more
minutes to install packages and deploy an application. The time it takes
to set up a server and the narrow window of time to vacate makes it
extremely challenging to make effective use of these discounted instance
types.

#### How containers help optimize cloud costs

Well as you might have guessed, containers can help with this obstacle
by using the spot market. The pre-built nature of containers means
startup times can be drastically smaller than with a dynamic, scripted
or configuration management-driven approach. The required packages,
application code, and various files have all been figured out at build
time, and written to essentially a compressed archive (Docker image).
This means startup times for your application in the sub-minute time
frame are now within reach. Additionally, containers provide you with
the confidence that you can deploy your application to new hosts and it
will work as expected. The self-contained dependency model means
everything the application needs is along for the ride. You don’t need
to worry about your automation tools failing at a step where a required
package is needed and ending up with a broken node.

#### Optimizing cloud costs with Rancher and Spotinst

To further enhance the stability when using spot instances, there are
great products like
[Spotinst Elastigroup](https://spotinst.com/products/workload-management/elastigroup/)
that uses predictive algorithms to help you anticipate market behavior,
and preemptively migrate workloads between different spot types (based
on price and availability) and on-demand equivalents when the market
drives the spot price above list. Spotinst acts as a prediction layer to
ensure you’re getting the best possible compute cost for your needs.
With Spotinst, you simply create a pool of instance types that will work
for your container hosts, and Spotinst will choose which to provision
based on factors such as current price and market stability. All that
you need to do is to define the instance types that you would like to
use as your hosts. Since Spotinst is cloud agnostic, you can define
separate Elastigroups in AWS, GCP, and Azure, and use the Spotinst API
to scale based on your preferences. (To read more on how Elastigroups
score the spot market to help you optimize costs, head
[here](http://blog.spotinst.com/2016/11/09/new-console-feature-spot-market-scoring/)).
[Spotinst has long offered native integration with
Rancher](http://blog.spotinst.com/2015/11/16/when-containers-met-spot-instances/)
to automate adding the replacement nodes to your Rancher cluster so the
containers on nodes slated for replacement can be gradually migrated
off. Spotinst will instruct Rancher to pause each soon-to-be-disrupted
container, and relocate it to another instance. This integration with
Rancher makes it much easier to successfully use the spot market,
without sacrificing application performance.

#### Learn more

If you were unable to make the webinar that Rancher, Spotinst, and
[Packet](http://www.packet.net) held yesterday on this topic, it’s not
too late! The recording is still available online, and we encourage you
to [check it out](https://info.rancher.com/hack-the-cloud-webinar). To
capture all the value of embracing containers, like increased developer
agility, simplified CI/CD workflows, and better scalability, follow
Rancher Labs on Twitter
([@Rancher\_Labs](http://twitter.com/rancher_labs)). *William Jimenez
is a Solutions Architect at Rancher Labs.*
