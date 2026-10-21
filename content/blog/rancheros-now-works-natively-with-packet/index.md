---
title: "RancherOS Now Works Natively with Packet"
date: 2016-11-03T11:17:00
slug: "rancheros-now-works-natively-with-packet"
author: "Rancher Admin"
products: ["RancherOS"]
tags: ["cloud"]
content_type: "release"
draft: true
migration:
  wp_id: 86962
  original_url: "https://www.suse.com/c/rancher_blog/rancheros-now-works-natively-with-packet/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RancherOS discontinued"
  redirect_target: "docs.rancher.com"
---

[![rancherpacket](images/rancher_blog_RancherPacket-300x85.png)](https://cdn.rancher.com/wp-content/uploads/2016/11/02105647/RancherPacket.png)We’re
excited to announce that [RancherOS](https://github.com/rancher/os) is
now available as a first-class operating system on
[Packet](https://www.packet.net/) for all instance types. Packet is a
bare metal cloud that combines the speed of physical hardware with the
flexibility and ease of use of virtualized infrastructure. We’ve always
been fans of Packet and we make use of it internally quite often. In
fact, we’ve recently decided to move our entire CI/CD pipeline over to
Packet instances. Prior to native RancherOS support, we’ve been running
it internally by booting another operating system and then running a
custom installation script. Even with this overhead we’ve had an
excellent experience with Packet. After adding support for automated
RAID installs and integrating with Packet’s provisioning system, we were
able to create an official installation process and move away from our
custom script. The first version of RancherOS available on Packet is
v0.7.0. This release brings [many exciting
features](https://rancher.com/whats-new-rancheros-v0-7-0/) such as the
ability to dynamically choose the Docker engine version via a
cloud-config parameter and the ability to easily customize Docker daemon
settings. In addition to these new features, RancherOS brings all of its
traditional features to the table, such as being an order of magnitude
smaller than other operating systems available on Packet. We’d like to
thank Andrew Hodges and the rest of the Packet crew for all of their
help throughout this process.
