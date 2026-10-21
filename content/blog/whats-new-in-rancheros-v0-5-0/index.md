---
title: "What's New in RancherOS v0.5.0"
date: 2016-08-12T11:30:00
slug: "whats-new-in-rancheros-v0-5-0"
author: "Rancher Admin"
products: ["RancherOS"]
tags: ["installation"]
content_type: "release"
draft: true
migration:
  wp_id: 87287
  original_url: "https://www.suse.com/c/rancher_blog/whats-new-in-rancheros-v0-5-0/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RancherOS discontinued"
  redirect_target: "docs.rancher.com"
---

[![rancheros-logo-01](images/rancher_blog_rancheros-logo-01.png)](images/rancher_blog_rancheros-logo-01.png)We’ve
recently released [v0.5.0](https://github.com/rancher/os) of RancherOS,
the latest major release since v0.4.0. Since then, we’ve moved RancherOS
out of an alpha state and made many changes to improve both stability
and user experience. In addition to various bug fixes and support for
Docker 1.11, v0.5.0 includes the following changes:

### [Official Raspberry Pi Image]

[On our releases page you can now find an [official Raspberry Pi
image](https://github.com/rancher/os/releases/download/v0.5.0/rancheros-raspberry-pi.zip)
which is known to work on both Raspberry Pi 2 and 3. We’re especially
excited about this since it offers users a cheap method of getting
started with Docker and RancherOS. We’d like to thank the
[Hypriot](http://blog.hypriot.com/)][ team
for their assistance on this feature.]

### [Improved Build Process]

[Our build process has been refactored to support multiple
architectures. With a given kernel, RancherOS can now be built for both
ARM and ARM64 devices. In addition, the build process is now faster than
it was previously which makes it easier than ever to create custom
builds of RancherOS.]

### [Console Switching without a Reboot]

[Switching to an alternate console can now be done without a reboot. The
`ros console` subcommand was added to make this an easy process. The
available consoles can be listed with `ros console list`. Ubuntu,
Debian, Fedora, and CentOS consoles are currently available. The `ros
console switch` command can be used to perform the
switch.]

### [Additional Configuration Options]

[Several additional cloud-config options were
added.]

- [`console` - Sets the console container without having to add
  system services]
- [`resize\_device` - Enables partition expanding with relying on a
  system service or network access]
- [`mounts` - Implements the cloud-init `mounts` key, which allows
  a set of mounts to be specified]
- [`sysctl` - Allows specifying sysctl
  settings]
- [`registy\_auths` - Configures private registry and private image
  authentication for system services]

###

### [Demo]

While the best way to check out these new features is to launch
RancherOS, we’ve recorded a new demo that covers the basics of the
operating system:

###

### [Conclusion]

[This is an exciting release for us to bring to our community and users.
It’s great to watch RancherOS as it becomes a more stable operating
system for a variety of uses. As always, we are keeping to the
philosophy that RancherOS should only include the minimum necessary to
get Docker up and running. To get started with RancherOS or learn more
about it, check out our [docs](https://docs.rancher.com/os/). If you have
questions or issues, please head over to our
[Github](https://github.com/rancher/os) page or to the [RancherOS
forums](https://forums.rancher.com/c/rancher-os).]
