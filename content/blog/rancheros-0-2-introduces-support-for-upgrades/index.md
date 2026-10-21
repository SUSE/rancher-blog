---
title: "RancherOS 0.2 introduces support for upgrades"
date: 2015-03-24T11:17:00
slug: "rancheros-0-2-introduces-support-for-upgrades"
author: "Rancher Admin"
products: ["RancherOS"]
tags: ["upgrades"]
content_type: "release"
draft: true
migration:
  wp_id: 86955
  original_url: "https://www.suse.com/c/rancher_blog/rancheros-0-2-introduces-support-for-upgrades/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RancherOS discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

[![RancherOS v0.2
Upgrade](images/rancher_blog_RancherOS-v0.2-Upgrade-300x134.png)](https://cdn.rancher.com/wp-content/uploads/2015/03/24153502/RancherOS-v0.2-Upgrade.png)This
week we released RancherOS 0.2, which introduces support for upgrades.
RancherOS is a tiny Linux distribution designed specifically to run
Docker, using containers to isolate user and system processes. Given
that RancherOS does just about everything with containers, it shouldn’t
be a surprise that upgrading a RancherOS node is almost exactly
like upgrading a Docker container. All of the upgrade procedures in
RancherOS are accessed through the “rancherctl” system service. Use
the following command to determine the current version of RancherOS that
you’re using:

```
sudo rancherctl -v
```

Use “os list” to see the other RancherOS versions currently available
to download:

```
sudo rancherctl os list
```

The output should display a list of both remote and local OS versions
similar to the following:

```
rancher/os:v0.1.2 remote
rancher/os:v0.2.0 remote
rancher/os:v0.2.0 local
rancher/os:v0.2.1 remote
rancher/os:v0.2.2 remote
```

To upgrade to the latest version, just issue an “os upgrade” command.

```
sudo rancherctl os upgrade
```

All of the versions of RancherOS are packaged in Docker images
on DockerHub, so once you’ve directed RancherOS to upgrade, it will
automatically pull the images down to your machine, and finally confirm
that you want to upgrade and reboot the host. Once you have rebooted,
you can confirm the upgrade using the “rancherctl -v” command. If at
any point you want to roll back, or upgrade to a specific version
“upgrade -i” allows you to specify the exact version you want to
upgrade to. For example:

```
sudo rancherctl os upgrade -i rancher/os:v0.2.0
```

Darren Shepherd provides a quick demonstration of how to install and
then upgrade a RancherOS 0.2 environment below. RancherOS 0.2 also
includes a number of bug fixes, more
[configurability](https://github.com/rancher/os/blob/master/docs/config.md),
hyper-v support, and greatly improved vagrant support. If you’re
interested in learning more, please register for our first RancherOS
online meetup on March 31st.
