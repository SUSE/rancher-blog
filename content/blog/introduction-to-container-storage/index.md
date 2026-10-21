---
title: "Introduction to Container Storage"
date: 2019-09-10T18:54:02
slug: "introduction-to-container-storage"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["storage"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 87330
  original_url: "https://www.suse.com/c/rancher_blog/introduction-to-container-storage/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

*Editor’s note: Additional writing by Arsh Sharma, who is pursuing a Bachelor’s Degree from the Indian Institute of Technology (BHU), Varanasi.*

## Introduction

Docker’s process-based virtualization has many advantages, especially when combined with the benefits of image layers. It allows for incredibly fast container spawning and lightweight resource utilization. However, one of the side effects of Docker’s ephemeral process model is that you have to be certain to plan when you want to save persistent data. In this guide, we’ll introduce you to Docker’s native solution to this problem: volumes.

## Where Does Data Go When Written in a Container?

Let’s engage in a hypothetical. Suppose we drop into a shell inside of a `busybox` container:

```
docker run -it --rm registry.suse.com/bci/bci-busybox
```

Then, let’s write some data to a location, say, `/tmp`:

```
echo "Data!" > /tmp/data
cat /tmp/data
```

```
Data!
```

We can see that the data definitely get written. But where do the data actually go?

As we learned earlier, Docker images consist of layers stacked on top of each other to result in a final image. Each of these layers contains data changed in an operation such as installing a tool, adding source code, etc. Each one of these layers becomes read-only after its creation.

When a container is created from an image, a thin R/W layer is added on top of the previous image layers. This layer handles all write calls from the container that would otherwise be directed at the read-only layers beneath.

Remember that containers are ephemeral by nature. They are meant to have a specific lifetime and to die at some point like any process. The thin read/write layer is also ephemeral — it disappears along with the container.

So, any writes that we perform in the container are limited to that container’s lifetime. They will disappear when the container is destroyed. This is an obvious limitation that is not conducive to storing stateful information. So, how do developers and administrators work around this?

They use Docker volumes.

## Docker Volumes

Docker volumes are a way to create persistent storage for Docker containers. Docker volumes are not tied to the container lifetime, so any writes to them will not disappear when the container does. They also can be re-mounted to one or more containers so you can share data and connect new containers to existing storage.

Docker volumes work by creating a directory on the host machine and then mounting that directory into a container (or multiple containers). This directory exists outside of the layered image that normally comprises a Docker container, so it’s not subject to the same rules (read-only, etc).

Let’s create a Docker volume and see this in action:

```
docker volume create
```

```
1d358c3fc3750f98345713eee5c294dee52...
```

A simple call to `docker volume create` will create a new volume. If we inspect this volume, we can see where it lives on the host filesystem:

```
docker volume inspect 1d358c3fc3750f98345713eee5c294dee526a3f5d0bd41a0ff4d117218c4af73
```

```
[
    {
        "CreatedAt": "2019-07-01T16:25:30Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/1d358c3fc3750f98345713eee5c294dee526a3f5d0bd41a0ff4d117218c4af73/_data",
        "Name": "1d358c3fc3750f98345713eee5c294dee526a3f5d0bd41a0ff4d117218c4af73",
        "Options": {},
        "Scope": "local"
    }
]
```

There’s a lot of information that comes with this `inspect` call, but all we’re really concerned with right now is the `Mountpoint`. Notice that is lists a path starting with `/var/lib/docker...`. If you were to open that path on your machine running Docker, you could view the data stored inside of this volume.

The method we just used to create a volume isn’t the only way. When running a container, you can specify `-v` to create a new volume on the fly:

```
docker run -it --rm -v testdata:/data registry.suse.com/bci/bci-busybox
```

As you can see, we have added a new argument to our `docker run` command: `-v`. There is a special syntax for this argument, with fields being separated by colons. The first field is the name of the volume, so in this case, `testdata`. The second field is the path on the container where the volume should be mounted, so in this case, `/data`. Let’s write data to the volume from within the container:

```
docker run -it --rm -v testdata:/data registry.suse.com/bci/bci-busybox /bin/sh
```

```
echo "Hello!" > /data/hello
exit
```

That the data is visible from outside of the container, in the volume path on the host:

```
cat /var/lib/docker/volumes/testdata/_data/hello 
Hello!
```

Something you may have also noticed is that the path is no longer a randomized

string — it is now the name of the volume we specified when we used the `-v` argument.

Docker volumes can have either randomized names initialized by the Docker

Engine, or the user can specify a name for the volume. Names must be unique per

host system.

Our created-at-runtime Docker volume also now becomes available in the `docker volume ls` command:

```
docker volume ls
```

```
DRIVER              VOLUME NAME
local               1d358c3fc3750...
local               c63a0af5c8282...
local               testdata
```

That means we can use this volume again with another container, or even multiple containers. Let’s test this out now.

First, connect the volume to a `busybox` container:

```
docker run -it --rm -v testdata:/data registry.suse.com/bci/bci-busybox /bin/sh
```

Inside the container, let’s print the system information and then write to the volume:

```
uname -a
echo "Hello 2" > /data/hello
```

```
Linux 7e299450b997 4.9.125-linuxkit #1 SMP Fri Sep 7 08:20:28 UTC 2018 x86_64 GNU/Linux
```

Now, start up a second `busybox` container running at the same time:

```
docker run -it --rm -v testdata:/data registry.suse.com/bci/bci-busybox /bin/sh
```

We can see the data that was written in the first container:

```
uname -a
cat /data/hello
```

```
Linux c5bf9ca04d3a 4.9.125-linuxkit #1 SMP Fri Sep 7 08:20:28 UTC 2018 x86_64 GNU/Linux
Hello 2
```

This highlights another strength of Docker volumes: sharing data between containers.

### Types Of Docker Volumes

Docker provides us with two types of volumes: **named volumes** and **anonymous volumes**. When you use either of these volumes, Docker manages the path on your machine where the data is stored. The difference between them is that, as their *name* suggests, we can refer to named volumes by specific names. This is useful when we want to share data between different containers as we can use the same **named volume** when launching the containers. In contrast, you will have a hard time doing the same with anonymous volumes since you can’t refer to them by name.

Named volumes, as you saw above, can be created using this command:

```
docker run -v volume-name:/path/in/container image_name
```

Anonymous volumes, on the other hand, are created using:

```
docker run -v /path/in/container image_name
```

Note that anonymous volumes are removed if the container they are attached to gets removed. This means that you should make sure to not use the `--rm` flag when working with anonymous volumes if you want your data to persist after container shutdown.

For most cases, named volumes are a better choice than anonymous volumes. However, anonymous volumes come in handy when you want to test something, as they are easier to manage since they get automatically removed when the container is removed.

## Docker Volume Use Cases

There are many valid use cases for Docker containers, but we will cover the two most common ones here.

For each of these examples, let’s pretend that we have a simple application that runs and collects data from some weather sensors. We want to gather a bunch of weather metrics, store them, and then use them again in the future. Let’s call our sample application `WeatherMon`.

### Persisting Data Beyond the Lifetime of a Container

If we run `WeatherMon` without using Docker volumes, any data that we collect will be destroyed when the container disappears. That’s not very helpful if our goal is to collect data and have it available for future use.

Docker volumes are handy because we can persist our data to the volume and have it remain outside of the container’s lifetime. Perhaps we create our container by calling `docker run` with the argument `-v weathermon:/opt/weathermon`. Then our application can store its weather metrics in the `/opt/weathermon` directory inside of directly on the ephemeral read/write layer provided by the container.

We could alternatively set up a remote database to store this information, but volumes provide an alternative for persisting local-only data.

### Sharing Data Between Containers

Let’s say we’ve been running our `WeatherMon` application for a while now and have collected quite a bit of data. We wish to run some analytics against this data to determine information such as the average temperature per day, or which week in a month had the highest average humidity.

Using Docker volumes, we can mount this existing volume into a new container, `WeatherMon-Analytics`. This new container can read in the data without interrupting collection from `WeatherMon`. It can then perform the analytics we desire, and store that information into the same volume or to a different volume if desired.

This also overlaps with a third use-case: pulling in large amounts of data to a container.

If we didn’t use Docker volumes, we may have to copy all of the required data into the container at runtime. That could be very expensive and slow, especially if we’re working with data like gigabytes of weather metrics.

By using Docker volumes we can simply mount the data volume to the container and start our application. No data loading is required.

## Other Mount Types

There are two other types of Docker volumes that we haven’t discussed yet: bind mounts and tempfs mounts.

### Bind Mounts

Bind mounts are used to mount an existing path on the host machine into a container.

This is very handy when presenting configuration information, such as directories from within `/etc`. It is also useful when you have information that you want a container to use, such as existing data sets or static website files.

Bind mounts also have a particular use case that can significantly ease your development workflow. In order to see a code change reflected in the running containerized instance of your app, you’d have to rebuild the image. This is because when an image is built, it uses the code that’s present. It does **not** get updated when you make changes to your code.

Manually rebuilding the image each time can be a cumbersome process. You can avoid this with bind mounts. You can specify the path on your host machine where the code is and mount it to the path in the container where you copy the code. This way the container will always have the latest code and you’ll see your changes reflected immediately.

You can set up a bind mount using the following command:

```
docker run -v /path/on/host/machine:/path/in/container image_name
```

Use this command to specify existing directories to be mounted into a container.

### Tempfs Mount

The job of the `tempfs` mount is to provide a writable location that specifically does **not** persist information after the lifetime of the container. You may be thinking, “why would that be necessary?”

In a container that does not have a volume mounted, any writes go into the thin R/W layer inserted at runtime. Any writes directed to that layer impact the filesystem as those writes are executed on the underlying host.

This normally is not a problem unless you are writing significant amounts of disposable data (such as logs). In that case, you may witness performance degradation as the filesystem needs to handle all of those write calls.

The `tempfs` mount was created to provide containers a disposable write path that does not impact filesystem operations. Specifically, the `tempfs` mount is an ephemeral mount that writes directly to memory. You can create this volume by using the `--tempfs` argument.

### Volume Drivers

By default, volumes store information on the underlying host system. Docker also has a concept called *volume drivers* that allow you to specify how and where to store volumes. For instance, you could store a Docker volume inside of an Amazon S3 bucket. This can be handy if you wish information to persist not only outside of the container’s lifetime, but outside of the host’s lifetime as well.

## Conclusion

All of the concepts discussed here are broken down in much more detail in [Docker’s documentation about storage](https://docs.docker.com/storage/). Examples of how to use each type of mount and a more in-depth introduction to the concept of volume drivers are available at that link.
