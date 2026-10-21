---
title: "RancherOS v0.8.0 released!"
date: 2017-02-22T11:17:00
slug: "rancheros-v0-8-0-released"
author: "Rancher Admin"
products: ["RancherOS"]
tags: ["installation"]
content_type: "release"
draft: true
migration:
  wp_id: 86964
  original_url: "https://www.suse.com/c/rancher_blog/rancheros-v0-8-0-released/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RancherOS discontinued"
  redirect_target: "docs.rancher.com"
---

![Rancher OS Logo with Black Background](images/rancher_blog_rancheros-logo-01-e1487784829352-300x154.png)RancherOS v0.8.0 is

[now available](https://github.com/rancher/os/releases)! This release

has taken a bit more time than prior versions, as we’ve been laying

more groundwork to allow us to do much faster updates, and to release

more often.

### Release Highlights

**Using the Linux 4.9.9 mainline kernel** Using the mainline stable

Linux kernel should allow us to give container users access to new

features faster - and will mean that RancherOS will have a simpler debug

and update path for other software too.

**Placing the installer container image in the ISO** This change allows

users to install RancherOS without internet access, and simplifies

automated testability of changes. This adds about 13MB to the ISO, but

means that you can do a basic install of RancherOS without pulling an

image from the Docker Hub.

**Running cloud-init earlier in the boot process** Previously, the

cloud-init service ran late in the RancherOS boot process, which made it

impossible to customize system services that ran before cloud-init. As

of v0.8.0, the cloud-init service runs while RancherOS is still running

from memory and before System Docker starts.

By running earlier in the boot process, we’ve enabled a wider range of

different customizations to RancherOS. For example, now you can set HTTP

proxy settings on System Docker or replace configuration files for

services such as NTP. Having cloud-init run earlier also opens the

ability to use other cloud-config keys that are only applicable early in

the boot sequence, such as operations around disk formatting and running

arbitrary commands and systems services while RancherOS is still running

from memory.

**Cloud-config validation** Producing a valid cloud-config file is often

frustrating due to the oddities and edge cases around YAML. A new

command (`ros config validate`) has been created to help solve these

issues. This command allows users to verify whether their cloud-config

is valid for RancherOS. For each invalid component, a detailed error is

provided to help users correct their cloud-config. Once the cloud-config

passes our validation, users can confidently use it in RancherOS without

the fear of a missing space or missing dash causing their cloud-config

to be ignored.

**Syslinux bootloader everywhere** To simplify the installation code, we

went from a mixture of GRUB and Syslinux, to using Syslinux only. For

now, the Syslinux boot prompt is only visible for one second - to

interrupt, you’ll need to type a character quickly - and then to add

boot parameters, replace that with

`rancheros-v0.8.0 rancher.autologin=tty1`, or whatever you want to add.

We are discussing changing the default boot process to autologin on the

physical console (see the discussion on

[GitHub](https://github.com/rancher/os/issues/1563)).

**New ZFS service** We moved away from using an Ubuntu kernel, so using

ZFS via an Ubuntu persistent console no longer works. In v0.8.0, the new

ZFS service installs the kernel-header service, downloads

the [OpenZFS](http://www.open-zfs.org/wiki/Main_Page) source code,

compiles it, and then creates and starts a new zfs-tools service which

proves the zfs tools to the console. It takes a bit longer to install

because it compiles from source, but we’ll work on adding pre-built

modules as we work on our build systems which should consequently speed

things up.

**Boot time and error logging to dmesg** To help debug issues in the

installer and early cloud-init, we added more boot time diagnostics. At

least for a few releases, we’ll be throwing a lot more logging both at

the boot console, and at /dev/kmsg. Please tell us if these changes are

causing you issues! The best ways to let us know are via

[GitHub](https://github.com/rancher/os) or our

[forums](https://forums.rancher.com/c/rancher-os).

**Other minor fixes** We’ve made a few additional small, but notable

changes:

- Fixed issues with VMware open-vm-tools and Virtualbox
- Rewritten the installer and other scripts in Go
- System console image and service definitions move some RancherOS

  customization out of the Dockerfile

### **RancherOS now available in AWS GovCloud region**

RancherOS Linux is now available on the [GovCloud](http://aws.amazon.com/govcloud-us/) isolated AWS Region for US government agencies and organizations. Combining RancherOS with GovCloud provides users with a safe way to build systems for sensitive and regulated data or workflows, and we’re pleased to make this combined solution available for our customers.

### **Next release**

Across Rancher Labs, we’ve committed to smaller and more regular

releases – which means RancherOS v0.9.0 should be out in about a month

with a much more digestible change list. Until then, expect to see

regular point releases with fixes and updated kernels (v0.8.1 is shaping

up to have Linux 4.9.11). As a new member of the Rancher team, this

version of RancherOS is the first one for which I’ve been the release

manager, and we welcome your feedback online – you can follow me

[@SvenDowideit](http://twitter.com/sven_dowideit) or let us know how

you like these changes

[@Rancher\_Labs](http://twitter.com/rancher_labs).
