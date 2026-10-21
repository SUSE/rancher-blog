---
title: "Introduction to Using Docker"
date: 2019-09-10T18:13:46
slug: "introduction-to-using-docker"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["installation"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 87333
  original_url: "https://www.suse.com/c/rancher_blog/introduction-to-using-docker/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "apt-key and Docker 20.10 install steps"
  redirect_target: ""
---

## Introduction

A growing number of companies and individuals have become interested in deploying applications in containers. This article will walk those interested in Docker through the basic steps required to install the software and build containers. To make understanding the instructions a bit easier, we’re going to focus on just one of the many available Docker variants: Docker Community Edition (CE) on Ubuntu and CentOS Linux. We’ll also provide links to the installation page on the Docker website if you are running Windows, macOS, or other platforms.

The reasons for focusing on these versions are straightforward: first, they represent a large base of the systems used by those coming into the world of Docker.

Next, the community edition is designed for those who are getting started and experimenting with Docker. It doesn’t have many of the container management aspects of Docker Enterprise Edition (EE), but in losing those capabilities CE gains simplicity and a reduced set of opportunities for complication and confusion.

Finally, CentOS and Ubuntu are popular Linux distributions and the instructions for installation can be readily adapted to many of the other distributions you might be using.

By the end of the article, you should have the confidence to begin experimenting with Docker on your own.

## Installing Docker

### Installing on Windows, macOS, and Other Platforms

If you are running on Windows, macOS, or another operating system, you can follow the updated instructions associated with your platform on [the Docker website](https://docs.docker.com/install/#supported-platforms). Clicking on the appropriate link will take you to a page where you can download and install the application, just as you would with any other piece of software.

On Linux platforms, the easiest way to install is to use one of Rancher's Docker installation scripts, which are available for most recent versions of Docker.

For example, this command could be used to install Docker 20.10 on  CentOS, openSUSE or Ubuntu:

```
curl https://releases.rancher.com/install-docker/20.10.sh | sh
```

To find out whether a script is available for installing a certain Docker version, refer to this [GitHub repository](https://github.com/rancher/install-docker), which contains all of Rancher's Docker installation scripts.

## Running Docker

For Windows and macOS, the Docker daemon should be automatically up and running.

On Linux, you can check whether the Docker daemon is started and configured to automatically run on boot by typing the following:

```
sudo systemctl is-active docker
sudo systemctl is-enabled docker
```

If either of the above two commands indicates that Docker is not running and configured to run, type:

```
sudo systemctl enable --now docker
```

This will enable the daemon to automatically start at boot. The `--now` flag also starts the daemon immediately if it isn’t already up and running.

You can run a quick test to make sure everything’s functioning correctly by typing:

```
sudo docker run hello-world
```

This will download an image and run a very simple container that displays a welcome message and version number. Congratulations — you’re now the proud administrator of a functioning Docker environment.

## The Next Container

Once you’ve established the environment, what are you going to do with it? Assuming you want to do more than run “hello world” on an endless loop, how do you create images that will become containers and actually do useful things? Before we go any farther, it will be useful to understand two terms that you’ll see quite a lot when you live in the Docker world:

An **image** is a file that contains code for an application and its dependent files. It’s a static asset that you can search for, download, and place in a repository, ready for use.

A **container** is an isolated, running process that has been deployed from an image. A container is an executing application. In the context of this article, Docker is the system that deploys and manages containers from container images.

There are a number of things that you’ll need to do in order to begin using containers. You want to be able to start and stop container execution, look at and clean up local images and containers, interact with remote image registries, and inspect containers to find out more information.

One of the very useful things about Docker as a community is that you don’t always have to write your own images. If you want to start running containers but want to ease into developing them, you can go to an image repository like the official [Docker Hub](https://hub.docker.com/) to find thousands of images that have been contributed and are ready for use. The `docker` command itself is configured to check for local images first and, if the image cannot be found, reach out to a remote registry to automatically pull down the image. As an example, the “hello-world” image that we downloaded and ran earlier was pulled from Docker Hub.

## Start and Stop Containers

You can start containers by typing:

```
sudo docker run <container>
```

As mentioned before, the `docker` command will search the local environment for the image first and use that if found. If it cannot find the image, it will look for an image with the given namespace and name on a remote image registry, configured by default to be [Docker Hub](https://hub.docker.com/).

Depending on the container’s purpose and your own intentions for running it, you might need to provide some additional arguments to the `docker run` command. For example, to publish all of the container’s ports, allowing access to all listening services, you can include the `-P` flag. This will map all of the container’s ports with running services to random ports on the host to allow access.

Later, when you need more control over precisely how your container runs, you can do it through additional options given to the **run** command when you’re starting the container. For now, though, the simple command listed above will do the job.

When it’s time to stop the app, simply type the following for a graceful app shutdown:

```
sudo docker container stop <container>
```

If your app does not respond as expected, you can kill the container to put an end to its operation immediately:

```
sudo docker container kill <container>
```

## Managing Docker Images

Once you have worked with a number of images, you’ll want to be able to see the images along with the basic information about them.

To list the images your instance has locally, type:

```
docker image ls
```

To get detailed information about any specific image you see, you can inspect it by typing:

```
docker image inspect <image>
```

This provides you with the image’s ID number, date of its creation, the path where it is stored, and other essential information.

To remove a local image, you can type:

```
docker image rm <image>
```

This is the command that will take an unwanted image and remove it from the system. If your image was pulled from a remote registry, you can easily pull it back down and use it for as long as it’s available. Keep in mind, however, that if the image was developed locally and wasn’t uploaded elsewhere, it will be gone forever.

The `docker image` subcommand is the basis for just about everything you do with Docker images. Almost all Docker commands related to images can be found by starting with these two words.

## Managing Containers

We’ve seen how to look at the images you’ve stored. But what do you do when you want to manage running containers? There are commands that can help you do that, too.

To get a detailed overview of the state of your system, including how many containers are running, how many are paused, and how many have been stopped, the `docker info` command can be helpful:

```
docker info
```

The output from this command will show you the container information as well as a lot of other useful details about your system.

To view the currently running containers on your system, type:

```
docker ps
```

This will list each of your currently executing containers along with the image they were spawned from, their ID, and information about the command they’re running and their networking information.

Since the basic `docker ps` command only outputs information about currently running containers, we need to add an additional flag to get information about containers that are on the system but not currently running. These containers may have been stopped or exited on their own:

```
docker ps -a
```

This command can help you identify containers that you no longer need. To remove them, you can use the `docker rm` command, passing in either the container’s name or ID:

```
docker rm [<container-name-or-id>
```

To clean up the system more generally, you can instead use:

```
docker system prune
```

This will remove all containers, images, and cache items that are not related to currently running processes.

## Working with a Remote Registry

The `docker` command has built in functionality for working with remote container image registries. By default, the tool is configured to target the registry at [Docker Hub](https://hub.docker.com), which is free to use for public repositories.

To begin publishing your container images to a repository on Docker Hub, you’ll need to [create an account](https://hub.docker.com/signup). After signing up, can authenticate to Docker Hub from your computer by typing:

```
docker login
```

You will be prompted for the Docker ID and password you selected.

If you ever need to sign out again or switch accounts, you can type:

```
docker logout
```

Without signing in, you’ll be able to pull down and use any public image in your configured registry. That’s how we were able to pull down and run the `hello-world` image earlier. By signing in, you’ll also have access to any private registries associated with your account. You’ll also be able to *upload* new images to your repository.

To search for an image on in the image registry, you can use the following command:

```
docker search <term>
```

This will show you a list of relevant images that were found on the remote registry.

To pull down an image from a container image registry, type:

```
docker pull <image>
```

This will search for and download the image you request. It will also update the image if there have been any changes uploaded since you last used it. The `docker pull` command is automatically executed by the `docker run` command if a remote image is required.

To upload your own image to your Docker Hub registry, you first need to make sure it follows the expected naming convention. While image names on your local system can be fairly flexible, uploaded images need to follow a specific pattern, which looks like this:

```
<docker_id>/<image_name>:<tag_name>
```

The first component of the name must be your Docker ID. Afterwards, a forward slash is used to divide the ID from the image name. Finally, a colon is used followed by the name of a specific tag. Multiple images with the same name can be uploaded as long as they have unique tags.

To rename your local images to conform with the above naming convention, you can use the `docker tag` command:

```
docker tag <original-image> <new-name>
```

Once you have an image ready to upload with an appropriate name, you can push the image up to the registry by typing:

```
docker push <image>
```

This will upload your image to your account on Docker Hub, which you should be able to see in the web interface.

## Conclusion

At this point, you should have an idea of what is required to begin using Docker, how to find and launch your first image and container, and where to go for more information. With the information in the article, you should have the confidence to take the next step and begin experimenting with Docker yourself.
