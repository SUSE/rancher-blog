---
title: "Rancher Desktop – An Open Source App for Desktop Kubernetes and Container Management"
date: 2021-06-22T10:14:00
slug: "rancher-desktop-an-open-source-app-for-desktop-kubernetes-and-container-management"
author: "Matt Farina"
image: "images/rancher_blog_rancher-desktop-featured.png"
products: ["Rancher Desktop"]
tags: ["developer-experience"]
content_type: "release"
draft: false
migration:
  wp_id: 86498
  original_url: "https://www.suse.com/c/rancher_blog/rancher-desktop-an-open-source-app-for-desktop-kubernetes-and-container-management/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher Desktop launch announcement"
  redirect_target: ""
---

For those of us who need to get applications running in Kubernetes, having Kubernetes on the desktop is incredibly useful. When we want to focus on our applications, it’s especially useful when Kubernetes is easy to use. This is where [Rancher Desktop](https://rancherdesktop.io/) comes in. Rancher Desktop provides easy-to-use Kubernetes and container management (something we’ll look at in a moment) for Mac and Windows.

Having Kubernetes isn’t enough. Being able to choose your version of Kubernetes and even being able to test upgrading Kubernetes versions is important. That’s because Kubernetes minor versions contain changes that matter. APIs change.

The version of Kubernetes many of us run isn’t the latest, either. Public clouds typically offer a minor version of Kubernetes that’s supported but not the latest version. Some are running versions of Kubernetes in production that are beyond the supported period.

Then there are those differences in the patch version. Have you ever run into a bug in a patch version that you needed to test or work around? I have. Being able to work with my application at a specific patch version helped me catch the issue and figure out how to work around it until Kubernetes released a solution.

Rancher Desktop helps with all of this and more. That includes things like building and testing container images in Kubernetes without the need to push or pull to a registry. This can really speed up testing – especially with large images.

To see what’s available, let’s look at some of the features in Rancher Desktop.

## Choose Your Kubernetes Version

Out of the box, Rancher Desktop is set to use the latest minor version of Kubernetes available in most public cloud environments. This isn’t the latest version as it takes public clouds a while to make a new version of Kubernetes available.

This is just the default version. You can choose any Kubernetes version that you like since v1.16.

![](images/Rancher-Desktop-1-1024x693.jpeg)

 

The screenshot (above) shows the Kubernetes setting screen in Rancher Desktop for Mac. On this screen, you can choose the version of Kubernetes you want to use. After setting a new version, Rancher Desktop will download any needed components for the version and switch your local version over.

## Test Kubernetes Upgrades

You can learn a lot by testing an upgrade of your application running in Kubernetes. Upgrades aren’t always seamless. For example, sometimes API versions go away – especially if you are using a beta version of an API. Some of those have stayed around a long time and have been used as if they are stable APIs.

![](images/Rancher-Desktop-2-1024x693.jpeg)

In the settings, when you change to a newer version of Kubernetes, your version will be upgraded while keeping your workloads around. This is a great way to test upgrading Kubernetes under your application. And, if you want to wipe out your workloads you can click the “Reset Kubernetes” button at any time to start fresh.

Keeping the workloads when changing the version only works for upgrading Kubernetes. Going to an older version of Kubernetes isn’t supported due to the way Kubernetes works. When switching to an older version, you will get a clean Kubernetes environment. Don’t worry if you forget this. A dialog box warns you before any change like this.

## Working With Container Images

Working with container images is an important part of working with Kubernetes or containers in general. Rancher Desktop provides a means to build, push and pull images. You can already run one-off containers using the *kubectl run* command.

[KIM](https://github.com/rancher/kim), the Kubernetes image manager, works with the instance of containerd under Kubernetes to manage building, pushing and pulling images. This has a great benefit. As soon as the image is built or pulled it is available to Kubernetes. Built images don’t need to be pushed to a registry, so Kubernetes can pull them. They are already available to the container runtime.

The next image shows a terminal window and running *kim build* against a local directory with a *Dockerfile*. You can use the *kim* binary in place of other tools. What you see in the terminal output below is running *kim* and then seeing the output of Buildkit as the image is built. [Buildkit](https://github.com/moby/buildkit) is a common building block used by tools to create container images.

![](images/Rancher-Desktop-3-1024x854.jpeg)

Once the image is built it’s immediately available to use. If you refer to the image in a Kubernetes object or using *kubectl run* the image will be used without needing to download it from anywhere.

## Next Steps

Now that you’ve seen the basics of Rancher Desktop, why not give it a try? You can learn to install it on [rancherdesktop.io](https://rancherdesktop.io/). You can also star [the project on GitHub](https://github.com/rancher-sandbox/rancher-desktop). Let us know what you think!
