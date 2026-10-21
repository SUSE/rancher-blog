---
title: "Rancher and the Moby Project"
date: 2017-04-21T11:16:00
slug: "rancher-and-the-moby-project"
author: "Rancher Admin"
products: ["RancherOS"]
tags: ["installation"]
content_type: "opinion"
draft: true
migration:
  wp_id: 86936
  original_url: "https://www.suse.com/c/rancher_blog/rancher-and-the-moby-project/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RancherOS and Moby 2017"
  redirect_target: "https://rancher.com/blog (hub)"
---

This week, [the Moby Project was
introduced](https://blog.docker.com/2017/04/introducing-the-moby-project/)
with the idea of componentizing Docker into a series of assemblies. At
DockerCon, a neat demo was done using the `moby` tool to assemble
various components into customized Linux operating system images. While
very cool, this seemed to have confused people – we’d like to provide
some more background and explanation about the Moby Project and how it
affects Rancher, RancherOS, and our users.

#### **Some background on the Moby Project**

The transition to the Moby Project actually started a couple of months
ago, with a discussion among the Docker Project maintainers, about the
dual nature of Docker as both a *product* and a *project*. This dual
nature served Docker (the project and the company) well in the
beginning, but at the end of the day, Docker, Inc. must make hard
decisions about what their product should and will be. As a group of
maintainers, we agreed that the product and project should be split. The
end goal was to further componentize Docker, building on previous work
to do so. Componentizing Docker is nothing new; this work has been going
on for a long time, starting with runc and containerd, and has long been
a goal of the Docker project. Thanks to over a thousand contributors and
the maintainers, Docker is currently a well-organized set of libraries
and packages. The Moby Project turns the Docker project into a
fully-componentized architecture, and provides a new home to the vast
majority of the Docker code, but not the product itself. Moby allows us,
as members of the community, to innovate, contribute, and steer
container technologies in ways that weren’t possible before. We now have
the ability to address use cases that are quite valid from a technical
perspective, but that would have previously conflicted with the Docker
product. One such use case is RancherOS.

#### **How Moby affects Rancher, RancherOS, and our users**

Now to answer the question: how does this impact Rancher, RancherOS, and
our users? Most users won’t see any change; Docker is still Docker. It
will continue to be the Docker you know and love (with what is hopefully
a better internal architecture). Where you will see a change is in
RancherOS. As an operating system in which all components are
containers, RancherOS is a highly-specialized application of containers.
We’ve needed some really low-level knobs in Docker to make RancherOS
possible, and Docker has been kind enough to give us many of those
knobs, even to the detriment of the Docker UX. For example,
`--uts=host`: I would guess 99% of Docker users have no idea what that
flag is for, but RancherOS requires it so DHCP can dynamically propagate
hostname changes. Going forward, the Moby Project is going to be great
for RancherOS. We can keep the same great Docker user interface, but
with Moby, we can get access to all the fancy low-level Linux knobs we
need. In the end, you will see RancherOS get smaller, faster, and more
secure. The Moby Project is also great for Rancher; Rancher is designed
to manage Docker containers, and in the future, we’ll be able to also
manage customized Linux components assembled from the Moby Project.
**And in closing...** Rancher Labs are very much in favor of the Moby
Project, and we hope the community understands that its introduction is
good for everyone. We’re looking forward to working closely with Docker
users, Rancher users, and everyone else in the container ecosystem.
*Darren Shepherd is Chief Architect of Rancher Labs.*
