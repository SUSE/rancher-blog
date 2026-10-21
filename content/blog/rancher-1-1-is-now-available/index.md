---
title: "Rancher 1.1 is Now Available!"
date: 2016-06-28T11:14:00
slug: "rancher-1-1-is-now-available"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["multi-cluster"]
content_type: "release"
draft: true
migration:
  wp_id: 86875
  original_url: "https://www.suse.com/c/rancher_blog/rancher-1-1-is-now-available/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.1 release notes"
  redirect_target: "rancher.com/blog (hub)"
---

[![rancher 1.1
github](images/rancher_blog_rancher-1.1-github-300x152.png)](https://github.com/rancher/rancher/releases/tag/v1.1.0)
View the Rancher 1.1.0 release notes on GitHub After a very
exciting DockerCon last week where the bulk of the engineering team was
able to see all the latest and greatest innovations surrounding the
Docker ecosystem, our team was able to squash the remaining issues for
our Rancher 1.1 stable release. If you have been following our dev
builds, we have been shipping tech preview features with each release
for our open source community members who want to play with the latest
Rancher has to offer. With 1.1.0, most of those features are now in a
stable state to be used in production. Some highlights include:

- **Docker 1.11.x Support:**[ It has always been our intention to
  support the latest Docker Engine as soon as it is released but
  1.11.x support was a much larger effort to add to a patch release
  for 1.0.x. As Docker prepares for 1.12, we hope to quickly add it to
  a subsequent Rancher 1.2.x release. Look for it
  soon!]
- **Mesos Support:**[ Rancher users can now [choose
  Mesos](https://rancher.com/mesos/) as a container orchestration
  framework when creating environments. Similar to our [support for
  Kubernetes](https://rancher.com/kubernetes/) and
  [Docker Swarm](https://rancher.com/swarm/), users can expect Rancher
  to manage the Mesos engine, the underlying infrastructure, user
  access control, and the catalog of frameworks that can be deployed
  on top of Mesos. ]
- **More Kubernetes Features:**[ We love Kubernetes as a container
  orchestration framework and have added additional features that were
  missing when we originally launched it in our 1.0.0 release. These
  include support for persistence storage to EBS and GCE, private
  registries, ingress controllers, and self-signed SSL support so
  plugins such as a Deis, dashboard, heapster, and pod scaling will
  now work. In addition, with 1.1.0, Rancher can now upgrade
  kubernetes within each environment with a click of a button.
  ]
- [**Machine Catalog**:][ We have now
  “catalog-ized” our Docker Machine integration by [leveraging our
  existing catalog
  framework](https://rancher.com/making-machine-drivers-easy-to-use-in-rancher/).
  Users can now add new Docker Machine drivers with any custom UI and
  make them available to all Rancher users via our public catalog or
  publish it to their own private
  catalogs.]

[Please head to [1.1.0
release](https://github.com/rancher/rancher/releases/tag/v1.1.0) for
[more detailed
notes](https://forums.rancher.com/t/rancher-release-v1-1-0/3265), or
join us for our next free [online
training](https://attendee.gotowebinar.com/rt/7313748307005707010) to
learn how to run Rancher.]

### [Release Builds]

[When we released 1.0.0 GA, we wanted to continue to ship our open
source releases in our bi-weekly releases so users can play with the
latest Rancher has to offer. Our current model of having dev builds were
causing some confusion with users that wanted to run Rancher in
production. With your feedback, we are making a few changes to how our
release builds work.] [For stable builds, in
addition to tagging rancher/server:stable, we will also packaged it as
their own Docker image called rancher/enterprise. If you are running
Rancher in production, it is highly recommended you use or upgrade to
this build.] [Our current dev builds will
continue to be shipped as rancher/server with a small change to the
tagging to -preX rather than -devX to denote a pre-release build for the
upcoming stable build. As usual, our pre-release builds will go through
our normal validation tests and QA cycles to ensure no regressions but
will include the newest features we’ve developed as tech previews. For
example, after 1.1.0 ships, the next pre-release build will be
v1.2.0-pre1.]

### [Rancher Project Planning]

As we move to Rancher 1.2.0 and beyond, we want to be more transparent
to our open source community by providing a look into what we
tentatively plan to add with each major release. We have created a new
[Rancher Project Planning
page](https://github.com/rancher/rancher/wiki/Rancher-Project-Plan) to
address this.

### [Docker 1.12 with built-in orchestration]

[[Sheng’s
blog]](https://rancher.com/dockercon-2016-where-docker-native-orchestration-grows-up/)[
already details how committed we are to supporting multiple frameworks.
With the recent announcement of Docker 1.12 and
its ][[built-in
orchestration]](https://blog.docker.com/2016/06/docker-1-12-built-in-orchestration/)[,
our engineering team is already at work incorporating it as another
container orchestration framework. As Docker 1.12.0 is currently
shipped as a release candidate, please look for a tech preview in our
next pre-release build of Rancher 1.2.0 once it has been officially
released. ]
