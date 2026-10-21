---
title: "Building Rancher Docker Container Catalog Templates from Scratch : Part 1"
date: 2016-07-11T11:15:00
slug: "building-rancher-docker-container-catalog-templates-from-scratch-part-1"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["developer-experience"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86907
  original_url: "https://www.suse.com/c/rancher_blog/building-rancher-docker-container-catalog-templates-from-scratch-part-1/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher catalog v1 discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)

[![Catalog
Icons](images/rancher_blog_catalog-300x284.png)Rancher](https://rancher.com/) ships
with a number of reusable, pre-built application stack templates.
Extending these templates or creating and sharing completely new ones
are great ways to participate in the Rancher user community and to help
your organization effectively leverage container-based
technologies. Although the [Rancher documentation](https://rancher.com/docs/) is
fairly exhaustive, so far documentation on how to get started as a new
Catalog template author has consisted of only a [single high-level blog
post](https://rancher.com/building-rancher-catalog-templates/). This
article is the first in a series aimed at helping the new Catalog
template author ramp-up quickly, with the best available tooling and
techniques. For the first article in this series, we are going to
construct a very simple (and not terribly useful) Cattle Catalog
template. In an upcoming article, we will flesh out this template with
more detail until we have a working multi-container NGINX-based static
website utilizing all of the basics of Rancher Compose, Docker Compose,
and Rancher Cattle.

### [Overview and Terminology]

Before we dive into creating a new Rancher Catalog template, let’s
first get some common terminology out of the way. If you are an
experienced Rancher user, you may be able to scan through this section.
If you are new to the world of [Linux
containers](http://www.google.com/#q=linux+containers), [cluster
managers](http://www.google.com/#q=cluster+managers), and [container
orchestration](http://www.google.com/#q=container+orchestration), now is
a good time to do some Googling. For our purposes, Rancher is Open
Source software enabling deployment and lifecycle management of
container-based application stacks, using most of the commonly available
Open Source container orchestration frameworks. As of this writing,
Rancher has excellent support for Docker containers and the following
orchestration frameworks:

- Kubernetes
  ([1](https://docs.rancher.com/rancher/latest/en/kubernetes/),
  [2](http://www.kubernetes.io/))
- Mesos ([1](https://docs.rancher.com/rancher/latest/zh/mesos/),
  [2](http://mesos.apache.org/))
- Docker Swarm ([1](https://docs.rancher.com/rancher/latest/en/swarm/),
  [2](http://docs.docker.com/swarm))
- Rancher’s own Docker Compose-based Cattle

If your favorite framework isn’t listed rest assured, that support is
probably on the way. Within the context of each of the previously
mentioned orchestration frameworks, Rancher includes a catalog of
pre-built and reusable application templates. These templates may be
composed of a single container image, but many times they stitch
together multiple images. Templates can be fed environment-specific
configuration parameters and instantiated into running application
stacks via the Rancher admin console. The screenshot below shows several
applications stacks as viewed via the Rancher admin console. Note that
the [Wordpress](http://wordpress.org/) and
[Prometheus](http://prometheus.io/) stacks are expanded to show the
multiple containers comprising each stack. [![Screenshot of the
available application Templates in the Rancher Cattle
Catalog](https://nrvale0.github.io/images/Rancher-Cattle-Stacks.png)](https://nrvale0.github.io/images/Rancher-Cattle-Stacks.png)
In this article, we are going to focus on Rancher’s own Cattle
orchestrator. See the image below for examples of some of the many
pre-built Catalog templates which ship for Cattle. [![Screenshot of the
Rancher admin Console with running application
Stacks](https://nrvale0.github.io/images/Rancher-Cattle-Catalog.png)](https://nrvale0.github.io/images/Rancher-Cattle-Catalog.png)

###

### Creating your first Rancher Cattle Catalog template

Many times these pre-built Rancher Catalog templates can be used as
shipped, but sometimes you’ll need to modify a template (and please
then submit your pull request to the upstream!), or even create a new
template from scratch when your desired application stack does not
already have one.

#### Doing it manually

For the purposes of this exercise, I’ll assume you have:

(1) a container host running the rancher/server container (2) at least
one compute node running rancher/agent (for the purposes of the demo,
(1) and (2) can be the same host) (3) a configured Rancher Cattle
environment (available by default with a running rancher/server
instance)

If that is not the case, please check out the one of the Rancher
Overview videos on the [Rancher Labs YouTube
channel](http://youtube.com/RancherLabs).

#### Adding a custom Cattle Catalog template

By default, the Catalog templates listed in the Rancher admin console
are sourced from the [Rancher Community Catalog
repository](http://github.com/rancher/community-catalog). We’ll create
our own git repo as a source for our new ‘demo app’ Cattle Catalog
template. First, we’ll set up our working directory on our local
workstation: [![Screenshot of local workstation setup for 'demo'
Template](https://nrvale0.github.io/images/Rancher-Cattle-Template-workingdir-setup.png)](https://nrvale0.github.io/images/Rancher-Cattle-Template-workingdir-setup.png)
Although there’s no deep magic, let’s step through the above:

1. Create a project working directory named ‘rancher-cattle-demo’
   under ~/workspace. These names and paths are fairly arbitrary
   though you may find it useful to name the working directory and git
   repo according to the following convention: rancher-<orchestration
   framework>-<app name>.
2. Create the git repo locally with ‘git init’ and on
   [GitHub](https://github.com/) via the
   ‘[hub](http://github.com/github/hub)’ utility.
3. Populate the repo with a minimal set of files necessary for a
   Rancher Cattle Catalog template. We’ll cover this in detail in a
   second.

Now let’s do our initial commit and ‘git push’ of the demo template:
[![Screenshot of initial git commit & push of our demo
Template](https://nrvale0.github.io/images/Rancher-Cattle-Template-initial-commit.png)](https://nrvale0.github.io/images/Rancher-Cattle-Template-initial-commit.png)
For sanity’s sake, you might want to check that your push to GitHub was
successful. Here’s my account after the above push: [![Screenshot of
initial push to
GitHub](https://nrvale0.github.io/images/Rancher-Cattle-Template-GH-after-initial-push.png)](https://nrvale0.github.io/images/Rancher-Cattle-Template-GH-after-initial-push.png)
It’s worth noting that in the above screenshot I’m using the
[Octotree](https://chrome.google.com/webstore/detail/octotree/bkhaagjahfmjljalopjnoealnfndnagc?hl=en-US)
Chrome extension to get a full filesystem view of the repo. Now let’s
configure Rancher to pull in our new Catalog template. This is done via
the Rancher admin console under Admin/Settings: [![Screenshot of
Admin/Settings in Rancher admin
console](https://nrvale0.github.io/images/Rancher-admin-console-Admin_Settings.png)](https://nrvale0.github.io/images/Rancher-admin-console-Admin_Settings.png)
Click the “+” next to “Add Catalog” near the middle of the page.
Text boxes will appear where you can enter a name and URI for the new
Catalog repo. In this case, I’ve chosen the name ‘demo app’ for our
new Catalog repo. Note the other custom Catalog settings from previous
custom work. [![Screenshot of adding a new Catalog
repo](https://nrvale0.github.io/images/Rancher-admin-console-Add-Catalog.png)](https://nrvale0.github.io/images/Rancher-admin-console-Add-Catalog.png)
Now we can go to Catalog/demo app in the Rancher admin console and pull
see the listing of container templates. In this case, just our ‘demo
app’ template. But wait there’s something wrong... [![Screenshot of
'demo app' Catalog with incomplete
Template](https://nrvale0.github.io/images/Rancher-Cattle-Template-demo_app.png)](https://nrvale0.github.io/images/Rancher-Cattle-Template-demo_app.png)
We’ve successfully created the scaffolding for a Rancher Cattle
template, but we’ve not populated any of the metadata for our template,
nor the definition or configuration of our container-based app. The
definition of our application via docker-compose.yml and
rancher-compose.yml is worthy or its own blog post (or two!), but for
now we’ll focus on just basic metadata for the template. In other words,
we’ll look at just the contents of config.yml

### Minimal config.yml

The [Rancher documentation](https://rancher.com/docs) contains detailed
information about config.yml. We’re going to do just enough to get
things working, but a thorough read of the docs is highly recommended.

#### config.yml

The config.yml file is the primary source of metadata associated with
the template. Let’s look at a minimal example:

> ```
> ---
> name: Demo App
> description: >
>   A Demo App which does almost nothing of any practical value.
> version: 0.0.1-rancher1
> category: Toy Apps
> maintainer: Nathan Valentine <nathan@rancher.com|nrvale0@gmail.com>
> license: Apache2
> projectURL: https://github.com/nrvale0/rancher-cattle-demo
> ```

In case it wasn’t evident from the filename, the metadata is specified
as YAML. Given the above YAML and the Icon file present in this [git
commit](https://github.com/nrvale0/rancher-cattle-demo/commit/cc324bbbb402da3462251a5c6f9903d951812f41),
let’s look at the new state of our template: [![Screenshot of improved
demo
Template](https://nrvale0.github.io/images/Rancher-Template-demo-version2.png)](https://nrvale0.github.io/images/Rancher-Template-demo-version2.png)
That’s starting to look a lot better, but our Catalog template still
doesn’t do anything useful. In our next post in this series, we’ll cover
how to define our application stack (Hint: it involves populating the
docker-compose.yml and rancher-compose.yml files.)

### A better way to create templates

Before we move on to definition of our application, I need to tell you a
secret... When creating new Catalog templates manually doesn’t require
any deep magic, it’s easy to make a small and silly mistake which
results in an error. It would be excellent to have tooling that allowed
us to create new Catalog templates in a fast, repeatable,
low-probability-of-error way...and in fact there is. The Rancher
community has submitted a [Rancher Catalog Template
‘generator’](https://github.com/Slashgear/generator-rancher-catalog)
to [The Yeoman Project](http://yeoman.io/). Assuming you have a working
Node.js environment, generating a new Cattle Catalog Template with
default scaffolding is as simple as the process shown below: [![Animated
GIF of creating a new Cattle Catalog Template with
Yeoman](https://nrvale0.github.io/images/Rancher-yo_rancher_catalog.gif)](https://nrvale0.github.io/images/Rancher-yo_rancher_catalog.gif)

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)
