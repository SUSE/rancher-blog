---
title: "Introduction to Container Security"
date: 2018-10-01T09:03:00
slug: "introduction-to-container-security"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["security"]
content_type: "explainer"
draft: false
migration:
  wp_id: 85824
  original_url: "https://www.suse.com/c/rancher_blog/introduction-to-container-security/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher. [Sign up here](https://rancher.com/training/) Containers are still a relatively new technology, but they have already had a massive impact on software development and delivery. Companies all around the world are starting to migrate towards `microservices`, and containers enable developers to quickly spin up services with minimal effort. In the past it took a fair amount of time to download, install, and configure software, but now you can take advantage of solutions that have already been packaged up for you and only require a single command to run. These packages, known as `images`, are easily extensible and configurable so that teams can customize them to suit their needs and reuse them for many projects. Companies like [Docker](https://docker.com) and [Google](https://google.com) helped to make containers easier to use and deploy, introducing orchestration tools like [Docker Compose](https://docs.docker.com/compose/), [Docker Swarm](https://docs.docker.com/engine/swarm/), and [Kubernetes](https://kubernetes.io).

While the usefulness and power of containers continues to grow, security is still something that prevents containers from receiving wider adoption. In this article, we’re going to take a look at the security mechanisms of containers, some of the big issues with [container security](https://www.suse.com/c/what-is-container-security/), and some of the methods that you can use to address those issues.

## Cgroups and Namespaces

We will begin by talking about two of the Linux kernel features that helped make containers as we know them today possible. The first of these features is called [cgroups](https://en.wikipedia.org/wiki/Cgroups). This feature was developed as a way to group processes and provide more control over the resources that were available to the group, such as `CPU`, `memory`, and `I/O`. This feature also allows for better accounting of the usage, such as when teams need to report the usage for billing purposes. The `cgroups` feature of containers allows them to scale in a controllable way and have a predictable capacity. It is also a good security feature because processes running in containers can not easily consume all the resources on a system - for example, a denial of service attack by starving other processes of required resources.

The other feature is called [namespaces](https://en.wikipedia.org/wiki/Linux_namespaces) which essentially allows a process to have its own dedicated set of resources, such as `files`, `users`, `process ids`, and `hostnames` (there are different namespace types for each of the resource types). In a lot of ways, this can make a container process seem like it is a `virtual machine`, but the process still executes system calls on the main kernel.

`Namespaces` limit what the process running inside a container can see and do. Container processes can only see processes running in the same namespace (in general, containers only have a single process, but it is possible to have more than one). These processes see a filesystem which is a small subset of the real filesystem. The user ids inside the container can be mapped from different ids outside the container (you could make the user root have user id 0 inside the container but actually has user id 1099 outside the container - thus appearing to give administrative control when not actually doing so). This feature allows containers to isolate processes, making them more secure than they would normally be.

## Priviledged Containers

When you are running processes in containers, there is sometimes a need to do things that do require elevated privileges. A good example is running a web server that needs to listen on a `privileged port`, such as 80. Ports under 1024 are privileged and usually assigned to more sensitive network processes such as `mail`, `secure shell access`, `HTTP`, and `network time synchronization`. Opening these ports requires elevated access as a security feature so that rogue processes can’t just open them up and masquerade as legitimate ones. If you wanted to run an Apache server (which is often used as a secure entry point to an application) in a container and listen on port 80, you would need to give that container privileged access.

The problem with giving a container elevated rights is that it makes it less secure in a lot of different ways. Your intent was to give the process the ability to open a privileged port, but now the process has the ability to do other things that require privileged access. The limitations imposed by the `cgroups` controller have been lifted, and the process can do almost anything that is possible to do running outside the container. To avoid this issue, it is possible to map a non-privileged port outside the container to a privileged port inside the container. For example, you map port 8080 on the host to port 80 inside the container. This will allow you to run processes that normally require privileged ports without actually giving them privileged access.

## Seccomp Profiles

[Seccomp](https://en.wikipedia.org/wiki/Seccomp) and `seccomp-bpf` are Linux kernel features that allow you to restrict the system calls that a process can make. Docker allows you to define [seccomp security profiles](https://docs.docker.com/engine/security/seccomp/) to do the same to processes running inside a container. The default seccomp profile for Docker disables around 40 system calls to provide a baseline level of security. These profiles are defined in `JSON` and use `whitelisting` for allowed calls (making any calls not listed prohibited). This whitelisting approach is safer because added system calls don’t immediately become available until added to the whitelist.

The issue with these seccomp profiles is that they must be specified at the start of the container and are difficult to manage. Detailed knowledge of the available Linux system calls is required to create effective profiles, and it can be difficult to find the balance between a policy too restrictive (preventing some applications from running) and a policy too flexible (possibly creating an unnecessary security risk).

## Capabilities

`Capabilities` are another way of specifying privileges that need to be available to a process running in a container. The advantage of capabilities is that groups of permissions are bundled together into meaningful groups which makes it easier to collect the privileges required for doing common tasks.

In Docker, a large number of capabilities are enabled by default and can be dropped, such as the ability to `change owners of files`, `open up raw sockets`, `kill processes`, or `run processes as other users` using `setuid` or `setgid`.

More advanced capabilities can be added, such as `load and unload kernel modules`, `override resource limits`, `set the system clock`, `make socket broadcasts and listen to multicasts`, and `perform various system admin operations`.

Using capabilities is much more secure than simply running a container as privileged, and a lot easier to manage than using seccomp profiles. Next we’ll talk about some system wide security controls that can also apply to containers.

## SELinux and AppArmor

A lot of the security concerns for processes running in containers apply to processes on a host in general, and a couple of different security tools have been written to address the issue of better controlling what processes can do.

[SELinux](https://en.wikipedia.org/wiki/Security-Enhanced_Linux) is a Linux kernel security module that provides a `mandatory access control (MAC)` mechanism for providing stricter security enforcement. `SELinux` defines a set of `users`, `roles`, and `domains` that can be mapped to the actual system users and groups. Processes are mapped to a combination of `user`, `role`, and `domain`, and policies define exactly what can be done based on the combinations used.

[AppArmor](https://wiki.ubuntu.com/AppArmor) is a similar `MAC` mechanism that aims to confine programs to a limited set of resources. AppArmor is more focused on binding access controls to programs rather than users. It also combines capabilities and defining access to resources by path.

These solutions allow for fine grain control over what processes are allowed to do and make it possible to secure processes to the bare minimum set of privileges that will be required to run. The issue with solutions like these is that the policies can take a long time to develop and tune properly.

Policies that are too strict will block a lot of applications that may expect to have more privileges than they really need. Policies that are too loose are effectively lowering the overall level of security on the system. A lot of companies would like to use these solutions, but they are simply too difficult to maintain.

## Some Final Thoughts

Container security controls are an interesting subject that goes back to the beginning of containers with **cgroups** and **namespaces**. Because of a lot of the things that we want to do with containers, extending privileges is often something that we must do. The easiest and least secure approach is simply using `privileged` containers, but we can make that a lot better by using `capabilities`. More advanced techniques like `seccomp profiles`, `SELinux` or `AppArmor` allow more fine grained control but require more effort to manage. The key is to find a balance between giving the process the least amount of privileges possible and the ease by which that can be done.

Containers are, however, a quickly evolving technology, and with security become more and more of an important focus in software engineering, we should see better controls continue to emerge, especially for large organizations which may have hundreds or thousands of containers to manage. The platforms that make managing so many containers possible are likely to guide the way in building the next generation of security controls. Some of those controls will likely be new Linux kernel features, and we may even see a hybrid approach where containers use a virtual kernel instead of the real one to provide even more security. The future of container security is looking promising.Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher. [Sign up here](https://rancher.com/training/)
