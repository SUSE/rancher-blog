---
title: "Rancher Desktop: K3s on the Desktop (with GUI)"
date: 2021-07-14T16:57:15
slug: "rancher-desktop-k3s-on-the-desktop-with-gui"
authors: ["Nuno Do Carmo"]
products: ["Rancher Desktop"]
tags: ["windows", "developer-experience"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 94197
  original_url: "https://www.suse.com/c/rancher_blog/rancher-desktop-k3s-on-the-desktop-with-gui/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Early Rancher Desktop 0.x GUI walkthrough"
  redirect_target: "/rancher-desktop"
---

# **Introduction**

![](https://media1-production-mightynetworks.imgix.net/asset/26330299/Rancher_Desktop.jpeg?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

K3s is probably the hottest Kubernetes distro right now. Everyone talks about it – whether compared with other Kubernetes distributions or in getting started guides. Still, as a normal Kubernetes distribution, the `control plane` needs to be hosted in a Linux OS. So what about Windows?

Well, it’s actually all about choices! As many guides have already been written for different options, this blog post will concentrate on a brand new option: Rancher Desktop for Windows.

So, are you ready for another rodeo?

## **It’s all about Docs**

Before we look at Rancher Desktop for Windows, here is a list of resources that will help you assess the different options:

- [K3s on WSL2](https://boxofcables.dev/deploying-rancher-on-k3s-on-wsl2/) by Hayden Barnes
- [Introduction to k3d](https://www.suse.com/c/introduction-k3d-run-k3s-docker-src/) by Thorsten Klein
- [k3d with a high availability setup](https://wsl.dev/wsl2-k3d-arkade/) by Nuno do Carmo
- [K3s on Civo cloud with K3sup](https://www.civo.com/learn/kubernetes-on-civo-in-5-minutes-flat) by Alex Ellis

First, WSL2 will be required in some sort. It can **host** K3s directly or act as the **client** for the configuration and management of a local cluster inside Docker (read: k3d). A more advanced use is to install K3s in a remote cluster hosted at a cloud provider with a tool that automates the K3s cluster creation.

Here is a small comparison of the current options for Windows:

![](https://media1-production-mightynetworks.imgix.net/asset/25210999/Screen_Shot_2021-06-17_at_4.52.08_AM.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)
> \*: K3s can be used in a multi-node setup. It’s even possible to do this in WSL2, but the work needed adds complexity from the out-of-the-box experience of K3s, which is to keep it fast and simple to install and use.
> \*\*: K3s can be hosted in a remote location, such as a cloud provider. However, from the point of view of using the binary directly, we must connect to the hosting server(s) before installing it. This constraint is removed with K3sup.
> \*\*\*: k3d runs on Docker, which in Windows will require the use of a VM (legacy) or WSL2 in order to run Linux based containers.

As said, this is a short comparison to provide a glimpse into the main requirements and constraints for each option with Windows.

## **Prerequisites**

Before we discover the brand new Rancher Desktop, there are a few prerequisites that we will need to have:

- Windows 10 version 21H1
- [WSL2 feature installed](https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-1---enable-the-windows-subsystem-for-linux)
- [Optional] [Winget: the Windows package manager](https://github.com/microsoft/winget-cli)

![](https://media1-production-mightynetworks.imgix.net/asset/25258600/winget-install.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

- [Optional] Windows Terminal

  ```
  winget install Microsoft.WindowsTerminal
  ```

![](https://media1-production-mightynetworks.imgix.net/asset/25211382/window-terminal-install.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

## **Install Rancher Desktop**

With the prerequisites installed, we can install Rancher Desktop.

The first step is to get the latest version from the [GitHub repo](https://github.com/rancher-sandbox/rancher-desktop). Once the installer downloads, we can install Rancher Desktop:

![](https://media1-production-mightynetworks.imgix.net/asset/25211393/rancher-desktop-install.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

Once installed, it will request a reboot. Finally, once rebooted, we can launch Rancher Desktop:

![](https://media1-production-mightynetworks.imgix.net/asset/25211502/rancher-desktop-launch.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

**Important note:** Rancher Desktop installation will enable the WSL2 features if not done already, and it will install and add to the Windows path the commands `kubectl.exe` and `kim.exe`:

```
# Check the information about kubectl and kim binaries
get-command kubectl.exe

get-command kim.exe
```

![](https://media1-production-mightynetworks.imgix.net/asset/25211553/kubectl-kim-install.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

## **Connect to Rancher Desktop**

Now that Rancher Desktop is installed, we can connect to it using the `kubectl` command, as we would do with any other Kubernetes cluster or in another OS, like Linux:

```
# Check kubectl and K3s cluster versions
kubectl version

# Get the K3s cluster information
kubectl cluster-info

# [Optional] Check the WSL K3s distribution information
wsl -l -v
```

![](https://media1-production-mightynetworks.imgix.net/asset/25211587/k3s-cluster-check.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

## **Conclusion**

In this blog, we looked at a new way of getting K3s on Windows. With all the current options, Windows is on par with any other OS regarding Kubernetes. No, it cannot run the `control plane` natively, but with WSL2, it definitively has the second-best option.

## **Bonus 1: Changing K3s versions**

Kubernetes development is fast – **very** fast. And sometimes, our application might not be ready for the brand new version, especially if there are breaking changes.

Rancher knows that, so to make it easy on us, Rancher Desktop has the capability to switch versions. And the best part, it’s easy to use:

![](https://media1-production-mightynetworks.imgix.net/asset/25211654/rancher-desktop-switch-version.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)
