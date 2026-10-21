---
title: "Rancher 2.0 First Impressions"
date: 2017-09-28T11:14:00
slug: "rancher-2-0-first-impressions"
author: "Rancher Admin"
products: ["Rancher Manager"]
tags: ["multi-cluster"]
content_type: "opinion"
draft: true
migration:
  wp_id: 86886
  original_url: "https://www.suse.com/c/rancher_blog/rancher-2-0-first-impressions/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 2.0 tech preview impressions"
  redirect_target: "rancher.com/blog (hub)"
---

If you’ve followed the container space recently, you’ve likely seen
the influx of Kubernetes-related technologies being announced. So, when
another one comes along, it’s easy to be less than excited about it.

However, in the case of Rancher’s recent [product
announcement](https://rancher.com/announcing-rancher-2-0/), it’s well
worth your time.

The engineering team at Rancher Labs has been working
on some new ideas that I think will have a real influence on the way we
all think about Kubernetes (K8s). Here are the top three aspects that
interest me.

First off, there is the ability to use `docker-compose` to
deploy K8s pods/services/ingress. Docker nailed the user experience with
compose (among others). I love how intuitive and concise it is, which
levels the playing field for people who don’t have time to become
container experts and just need to get their work done. K8s resource
manifests are powerful and scalable. However, there is a substantial
constituent (especially in the enterprise) that doesn’t benefit from
this, and actually find this format difficult to use. So, one of the
great things about 2.0 is it allows people to deploy their applications
using either `docker-compose` for those who are new to K8s, or native
resource manifests for those who prefer that way. With the frenzy of K8s
initiatives everywhere, I think we haven’t yet had the time as an
industry to step back and evaluate if the average engineer (who is not
one of the enthusiasts driving container adoption) within an
organization is actually groking the K8s user experience. Because in my
experience it’s the broad-base adoption that will make or break a
technology. After a while when the hype has died down, if they don’t
latch on to it, then the technology is at risk to become
“shelfware”--especially when the selling point to begin with was
developer productivity! Second, Rancher 2.0 leverages well-established
features from K8s. You’ve heard the maxim, “don’t reinvent the
wheel,” but we all know how often that happens at technology companies.

As tempting as it was, our development team recognized where they can
lean on the K8s API to implement new features instead of building it
themselves. I’m a firm believer that this makes for better software,
because you don’t have to run the risk of repeating mistakes already
made, and you can focus you energies on solving new problems. I take
some of this from my personal experience as well as the experiences of
others, such as [Joel Spolsky’s
thoughts](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/)
on rewriting software.

What are some examples of this in Rancher 2.0?

For one, we’re implementing a multi-tenancy model by extending existing
K8s constructs, such as namespaces and RBAC. Federation is also
something we thought about doing ourselves before deciding to leverage
K8s implementation. Metrics and monitoring also benefit from Heapster
and InfluxDB having lots of integration with K8s. These are just a few
highlights of how we’re using K8s technology in Rancher.

Finally, I’m most excited about the overall focus K8s will have at Rancher Labs.
Since we first started providing solutions in the container ecosystem,
we’ve sought to give customers as much choice as possible among all of
the available schedulers out there. This was not easy though, and I
always wondered what Rancher could be like if we could focus our
energies on one of these technologies. I’m glad that the industry has
spoken, and democratically elected K8s to be the scheduler of choice so
that we can shift our energies in its direction without the risk of
locking our customers in.

I hope all of the above reasons have at least
sparked your interest to [check out Rancher
2.0](https://rancher.com/rancher2-0/). We really value your feedback, so
please don’t hesitate to share your experience with it. You can find us
on [Twitter](https://twitter.com/Rancher_Labs) and our user
[Slack](https://rancher-users.slack.com/) channel,
**#2-0-tech-preview**.
![](images/rancher_blog_wjimenez-photo-300x300.jpeg)William Jimenez
is a curious systems engineer who enjoys solving problems with
computers, software, and just about any complex system he can get his
hands on. He enjoys helping others make sense of difficult problems. In
his free time, he likes to tinker with amateur radio, cycle on the open
road, and spend time with his family (so they don’t think he forgot
about them).
