---
title: "Guest Blog: Sysdig Announces Integrated Docker Monitoring in Rancher"
date: 2015-11-25T11:26:00
slug: "guest-blog-sysdig-announces-integrated-docker-monitoring-in-rancher"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["observability"]
content_type: "company-news"
draft: true
migration:
  wp_id: 87090
  original_url: "https://www.suse.com/c/rancher_blog/guest-blog-sysdig-announces-integrated-docker-monitoring-in-rancher/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Sysdig integration for Rancher 1.x"
  redirect_target: "rancher.com/blog (hub)"
---

[[![Sysdig
Catalog](images/rancher_blog_Sysdig-Catalog.png)](images/rancher_blog_Sysdig-Catalog.png)]
*Chris Crane is VP of Product at Sysdig.* [Here at Sysdig we build
monitoring and visibility tools, specializing in Docker monitoring and
containerized infrastructures. Our open source CLI tool,
][[sysdig]](http://www.sysdig.org/)[,
offers universal system visibility into Linux machines along with native
support for Docker. And based on the same core technology,
][[Sysdig
Cloud]](https://sysdig.com/)[ offers the
first and only comprehensive monitoring solution built from the ground
up for containers and microservices. In a nutshell, Sysdig’s unique
technology let’s you see inside your containers
]*[from the outside
]*[- no instrumentation, no plugins, no
configuration.] [But Docker containers alone
are not enough to build a modern microservices-oriented infrastructure:
you need proper orchestration and management on top. Enter
][[Rancher]](https://rancher.com/)[.
Rancher makes it easy to deploy Docker across your architecture and
realize all the benefits of a containerized application, without any of
the hassle. Not only are we huge fans of Rancher here at Sysdig, but
many of our users are using Rancher as well. That’s why, today, we’re
excited to announce that Sysdig is integrating our products directly
into Rancher!] [With this new integration,
open source sysdig and Sysdig Cloud are now both available in the
][Rancher
Catalog][.
The Rancher Catalog is an awesome service provided with the Rancher
platform that lets you one-click deploy popular applications directly
into your stack. Rancher takes care of all the Docker image management,
deployment, scheduling and orchestration for you! So now, with the power
of Sysdig + Rancher, in just a couple seconds you can have deep,
container-native visibility and monitoring deployed across your entire
infrastructure.] [Let’s take a quick look at
the deployment process..]

### [Deploying sysdig and Sysdig Cloud from the Rancher Catalog]

[First navigate to the Catalog in your Rancher application and search
for “Sysdig”. You should see two options: sysdig and Sysdig
Cloud.] [![Sysdig
Catalog1](images/rancher_blog_Sysdig-Catalog1.png)](images/rancher_blog_Sysdig-Catalog1.png)
[Select the application you want to deploy, and all you have to do is
add some basic configuration data and you’re good to go! If you’re
deploying Sysdig Cloud, you’ll need to add your unique agent key, which
can be retrieved from your Sysdig Cloud application. But to deploy the
open source sysdig CLI, all you have to do is give your new stack a
name:] [![Sysdig Catalog
2](images/rancher_blog_Sysdig-Catalog-2.png)](images/rancher_blog_Sysdig-Catalog-2.png)
[And that’s it! Now we can see sysdig has been successfully deployed
across our entire cluster. Pretty cool
right?] [![Sysdig Catalog
3](images/rancher_blog_Sysdig-Catalog-3.png)](images/rancher_blog_Sysdig-Catalog-3.png)
[You’ll note that Rancher is smart enough to automatically deploy just a
single Sysdig container on each host machine in your environment. From
there, Sysdig is able to monitor every other container on the machine.
We call this patent-pending technology
]*[ContainerVision][TM]*[
- we’re able to automatically detect every container on a machine,
automatically discover the applications running inside each container,
and automatically start pulling the relevant application level metrics
for your environment to deliver world class Docker
monitoring.] [We’re really excited about the
potential for this Sysdig+Rancher integration, and I hope you’ll go
check it out and ][[let us know your
feedback]](https://twitter.com/sysdig)[. If
you’re a Rancher user and want to test out Sysdig Cloud, then come sign
up for a free trial today! And if you end up wanting to make a purchase,
let us know you read this blog post and we can offer you 10% off the
final price.] [Thanks, happy digging!
] [*To learn more about using Rancher with
Sysdig, please view a [replay of our October
2015](https://rancher.com/best-practices-for-docker-monitoring-with-sysdig-and-rancher-october-2015-online-meetup/)
online meetup on container monitoring.* ] You
can also register for our upcoming meetup where we’ll be demonstrating
the new catalog services ind epth
