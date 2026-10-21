---
title: "The Similarities and Differences Between Windows and Linux Containers"
date: 2017-09-20T11:31:00
slug: "the-similarities-and-differences-between-windows-and-linux-containers"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["windows"]
content_type: "explainer"
draft: true
migration:
  wp_id: 87305
  original_url: "https://www.suse.com/c/rancher_blog/the-similarities-and-differences-between-windows-and-linux-containers/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2017 Docker for Windows details"
  redirect_target: "https://rancher.com/blog (hub)"
---

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)

You can run Docker containers on Windows as well as Linux. Although, in
many ways, Docker works similarly on these operating systems, there are
some differences. Below, I walk through the steps of installing and
running Docker on Windows, and point out how they are similar to and
different from running Docker on Linux.

#### Installing Docker on Windows and Linux

Let’s start with installation. The Docker installation process is
different on both operating systems. To install Docker on Windows, just
download the application and install it as you would any Windows
application. You get a user-friendly installation wizard: ![The Windows
installation wizard displays and asks you to select any additional tasks
you'd like to set
up.](images/rancher_blog_Install-Docker-on-Windows.png) To
install Docker on Linux, in contrast, you can either grab the Docker
package from your distribution’s package manager (yum, dnf, or something
similar), or install directly from Docker’s site with the command:

```
sudo sh -c "wget -qO- https://get.docker.io/gpg | apt-key add -"
```

#### Docker Under the Hood: Differences Between Windows and Linux

The Docker method of installation is just one difference between Windows
and Linux. When you install Docker on Linux, you install only the Docker
Engine and management tools. You don’t need to create a virtual machine
or virtual networks, because your containers will handle the setup for
you. Things are different on Windows. At the time of installation,
Docker creates a Linux-based virtual machine called MobyLinuxVM, which
is based on [Alpine Linux](http://alpinelinux.org/). The Docker
application connects to this machine, so that you can create your
container with the necessary apparatus for operation. The Docker
installation also configures a subnet for the virtual machine to
communicate with the local network and NAT for your containers to use in
the application. All of these steps occur behind the scenes and, as the
user, you don’t really have to worry about them. Still, the fact that
Docker on Windows runs a virtual machine in the background is another
major difference between Docker on Windows and Docker on Linux.

#### Docker Commands

Once you install Docker, the commands are the same on both Linux and
Windows. You only have to learn one set of tools, no matter which
operating system you run. The only difference between Windows and Linux
when running Docker commands is where you run them. On Linux, you can
use the terminal emulator of your choice. On Windows, use the PowerShell
CLI. Below are examples of running Docker in PowerShell on Windows. The
first screenshot displays information about the system, while the second
shows some containers running on Windows. ![PowerShell displays
information about the Docker on Windows
system](images/rancher_blog_Docker-PowerShell-system.png) ![Docker
containers running on Windows in
PowerShell](images/rancher_blog_Docker-containers-in-Windows-PowerShell.png)

#### Windows vs. Linux: Which is Better for Docker?

Personally, I find it easier to work with Docker from Linux than from
Windows. Even though there is no functional difference between Docker on
Windows and Linux environments, the installation process on Linux is a
bit faster (an apt-get install is quicker than installing a Windows
package), and the shell is easier to access on Linux. That said, this is
just my personal preference. From a technical standpoint, there is no
real difference between using Docker on Windows and Linux. You can
achieve the same things with Docker on both platforms. I don’t think you
can say that either Windows or Linux is “better” for hosting Docker.

#### Conclusion

The fact that no operating system is better than another for Docker is
what makes Docker so great. No matter where Docker runs (despite some
differences in configuration and what goes on in the background), the
Docker user experience is always the same. A **docker run -d -p 80:80
nginx** command spins up an NGINX container, no matter which operating
system you are working from, which particular shell you’re using,
whether your Docker environment runs in the cloud or on-premises, or
whether it’s sunny or rainy outside. This consistency is what makes
Docker so reliable and pleasant to work with. It saves you from the
configuration hell and environment unpredictability that are part and
parcel of working with virtual machines and other older forms of
infrastructure.

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)
