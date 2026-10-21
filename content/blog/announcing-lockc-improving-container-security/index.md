---
title: "Announcing lockc: Improving Container Security"
date: 2022-01-18T21:46:50
slug: "announcing-lockc-improving-container-security"
author: "Michal Rostecki"
image: "images/icon-lockc-1.png"
products: ["Other"]
tags: ["security"]
content_type: "release"
draft: true
migration:
  wp_id: 89599
  original_url: "https://www.suse.com/c/rancher_blog/announcing-lockc-improving-container-security/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "lockc 2022 project announcement"
  redirect_target: "rancher.com/blog (hub)"
---

*Michal Jura co-authored this post*

The lockc project provides mandatory access controls (MAC) for container workloads. Its goal is to improve the current state of container/host isolation. The lockc team believes that container engines and runtimes do not provide enough isolation from the host, which I describe later in the "Why do we need it?" Section.

In this blog post, I’ll provide an introduction to lockc, discuss why you need it and show you how to try it out for yourself.

## What is lockc?

Lockc uses LSM eBPF - a feature in the kernel that allows you to write eBPF programs that act like traditional security modules.

Lockc provides integration with

- Kubernetes with cri-containerd

- Docker (as a local runtime, without Kubernetes)

 

To try out lockc today, you can simply follow our installation instructions. There are separate sections for [*Kubernetes*](https://rancher-sandbox.github.io/lockc/install/kubernetes.html) and [*Docker*](https://rancher-sandbox.github.io/lockc/install/docker.html).

 

![lockc for container security](images/icon-lockc.png)

## **Introducing eBPF and LSM**

eBPF is a technology (with origins in the Linux kernel) that allows you to run sandboxed programs in an operating system kernel. It can be used to extend or trace the kernel capabilities without changing the kernel source or loading any modules. eBPF is event-driven, which means that it is triggered by various hooks in the kernel. So far, the most popular use cases of eBPF are:

-network packet tracing and filtering

-both on TC hook (after the packet gets parsed by the Linux kernel) and on closer to the raw network packet - XDP

-tracing kernel functions

To learn more about eBPF, check [*the official website of its community*](https://ebpf.io/).

Linux Security Modules (LSM) is a framework that allows the Linux kernel to build security models on top of it. It consists of hooks placed all over the Linux kernel codebase which allow LSM developers to receive events and decide whether to allow a particular event to happen or not. Those events are usually related to:

-program execution operations.

-filesystem mounts

-filesystem operations (mounts, inode operations, opening/creating/deleting/renaming file)

-task operations (scheduling or deleting a process/task)

-netlink messaging

-Unix domain networking

-socket operations

-Key Management operations (keyrings)

-System V IPC operations (in message queues, semaphored)

-using the eBPF maps and programs functionalities through eBPF syscalls.

-perf events

 

[*You can find the full list of LSM hooks here*](https://elixir.bootlin.com/linux/latest/source/include/linux/lsm_hooks.h).

[*Here is the full list of their function signatures*](https://elixir.bootlin.com/linux/latest/source/include/linux/lsm_hook_defs.h).

Security systems like AppArmor, SELinux, Smack and TOMOYO are built on LSM.

Since kernel 5.7, it’s possibile to write eBPF programs attaching to LSM hooks. That means that you can build your LSM as a set of eBPF programs rather than a kernel module. That is the feature that lockc makes use of.

Lockc tracks all the runc processes and their children. So lockc has the potential to integrate with all container engines that make use of runc. For now we are supporting Docker (for local usage) and cri-containerd (as a Kubernetes runtime).

## **Why Do We Need lockc? (Containers Do Not Contain)**

The main reason lockc exists is that "**containers do not contain."** Containers are not as secure and isolated as VMs. By default, they expose a lot of information about host OS and provide ways to "break out" from the container. lockc aims to provide more isolation for containers and to make them more secure.

Many people assume that containers:

-provide the same or similar isolation to virtual machines

-protect the host system

-sandbox applications

While all the points except the first one are partially true, some parts of the host filesystems are still exposed to containers by default and there are ways to gain full access.

One problem is that most filesystems inside /sys are not namespaced and their content is identical with the host filesystem. This means we can look at the metadata of the host’s btrfs filesystem from inside the container:

```
❯ docker run --rm -it opensuse/tumbleweed:latest bash

0d35122d08f9:~ # ls /sys/fs/btrfs/a8222a26-d11e-4276-9c38-9df2812cead2/

allocation  bdi  bg_reclaim_threshold  checksum  clone_alignment  devices  devinfo  exclusive_operation  features  generation  label  metadata_uuid  nodesize  qgroups  quota_override  read_policy  sectorsize
```

Or we can "escape" the container’s filesystem namespace by mounting the host's rootfs:

```
❯ docker run --rm -it -v /:/rootfs opensuse/tumbleweed:latest bash abb67212044d:/
 # chroot /rootfs
 sh-4.4#

 Or by mounting the docker socket:
```

```
❯ docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock docker sh

/ # docker ps

CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES

066811b60d69   docker    "docker-entrypoint.s…"   5 seconds ago   Up 5 seconds             suspicious_liskov

/ # docker run --rm --privileged -it opensuse/tumbleweed:latest bash

fcb94c1d3af6:/ # exit

/ # docker run --rm --privileged -it -v /:/rootfs opensuse/tumbleweed:latest bash

54b08e30fd9e:/ # chroot /rootfs

sh-4.4#
```

The goal of lockc is to eventually prevent all those examples for regular users. Following some examples as root, by explicitly choosing the *privileged* policy level in lockc, is still going to be allowed. However, using the *privileged* level for containers that are not part of Kubernetes infra (CNI plugins, operators, network meshes etc.) is discouraged.

## **Meet the Developer Team**

Join our free webinar, **Understanding Mandatory Access Control for Containers with lockc**, on Thursday, February 3 at 17:00 CET / 8AM PT. You will get a chance to meet the developer team, get details about lockc, see it in action in a demo and ask questions. [Register here for the webinar](https://www.crowdcast.io/e/lockc_webinar?utm_source=post&utm_medium=blog&utm_id=lockc).
