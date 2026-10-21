---
title: "RancherOS 1.1.0: Updated Docker support, VMware, Syslinux, and more"
date: 2017-09-04T11:17:00
slug: "rancheros-1-1-0-updated-docker-support-vmware-syslinux-and-more"
author: "Rancher Admin"
products: ["RancherOS"]
tags: ["installation", "virtualization"]
content_type: "release"
draft: true
migration:
  wp_id: 86960
  original_url: "https://www.suse.com/c/rancher_blog/rancheros-1-1-0-updated-docker-support-vmware-syslinux-and-more/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RancherOS discontinued"
  redirect_target: "https://rancher.com/blog (hub)"
---

RancherOS v1.1.0 is [[now
available](https://github.com/rancher/os/blob/master/README.md)]!
It includes a number of key enhancements such as: VMWare ESXi support;
improved OS level logging, including boot-time logs; remote Syslog
logging; and built in Logrotate and Cron services. Syslinux support has
improved with the addition of a boot menu, allowing you to select debug,
autologin, and recovery consoles. The reboot command can kexec into the
latest and previous OS versions. With RancherOS v1.1.0 you still select
Docker engines between 1.12 and 17.06. However, support for Docker
v1.10 and v1.11 is no longer available. RancherOS v1.0.x, our Long Term
Support (LTS) version is now at v1.0.4, with bug fixes and stable
improvements continuing until April 2018.

### VMWare ESXi support

RancherOS now officially supports VMWare ESXi 6.5, and if it detects
that its running in a VMWare hypervisor, automatically adds the VMWare
guestinfo cloud-init datasource and enables the open-vm-tools service
(requires internet access). This support has been paired with changes in
docker-machine v0.12.2 to allow you to set the cloud-init.config.url or
cloud-init.config.data guestinfo values using the
--vmwarevsphere-cloudinit argument.

```
docker-machine -D create --driver vmwarevsphere 
        --vmwarevsphere-username root --vmwarevsphere-password ******* 
        --vmwarevsphere-network "VM Network" --vmwarevsphere-vcenter 10.10.10.41 
        --vmwarevsphere-boot2docker-url rancheros.iso 
        --vmwarevsphere-cloudinit https://raw.githubusercontent.com/RoastLink/roastlink.github.io/master/cloud-config.yml 
        cloud-init-url

docker-machine -D create --driver vmwarevsphere 
         --vmwarevsphere-username root --vmwarevsphere-password ******* 
         --vmwarevsphere-network "VM Network" --vmwarevsphere-vcenter 10.10.10.41 
         --vmwarevsphere-boot2docker-url https://releases.rancher.com/os/latest/rancheros.iso 
         --vmwarevsphere-cloudinit cloud-config.yml 
         cloud-init-local-file
```

## Logging improvements

The RancherOS boot and system services logging now allows admins to
examine the debug information output during boot-up and initialization.
The extra files can be found in the /var/log/boot folder of the console.
In addition, you can use the `netconsole` kernel boot parameters to log
both the kernel level and RancherOS debug logs to a remote syslog server
for later analysis. Logrotate and a Cron system container have been
added to run by default.

## Syslinux boot menu

[![RancherOS v1.1.0 Syslinux boot
menu](images/rancher_blog_t110-xeon-2017-08-23-12-31-03-300x167.png)](https://cdn.rancher.com/wp-content/uploads/2017/08/22193132/t110-xeon-2017-08-23-12-31-03.png)
RancherOS now gives you an interactive boot menu from which you can
select common debug and development options such as auto login, debug
logging, and the recovery console as well as temporarily edit the kernel
boot parameters. You can also use the new
`sudo ros config syslinux` command to edit the system’s global.cfg boot
config.

## Direction for RancherOS v1.2.0

Some of the features we’re considering next are:

- Rancher/Strato for 32bit and 64bit ARM
- More work towards simplifying building customised RancherOS builds
  (LinuxKit)
- Rancher Compose and Containerd
- Hyper-V support
- adding more functionality to our cloud-init immutable OS
  configuration.

As always, we appreciate your input on RancherOS. You can provide
feedback by [[filing an
issue](https://github.com/rancher/os/issues)]
or sending me (@svendowideit) a message on the Rancher Users [[Slack
channel]](https://slack.rancher.io).
You can download RancherOS 1.1.1
[[here](https://github.com/rancher/os/blob/master/README.md)].
The [[quick start
guide]](https://rancher.com/docs/os/v1.0/en/quick-start-guide/)
in the RancherOS docs provides guidance on how to get started.
