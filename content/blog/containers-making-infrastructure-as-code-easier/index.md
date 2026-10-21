---
title: "Containers: Making Infrastructure as Code Easier"
date: 2017-01-31T10:17:00
slug: "containers-making-infrastructure-as-code-easier"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["developer-experience"]
content_type: "explainer"
draft: false
migration:
  wp_id: 86608
  original_url: "https://www.suse.com/c/rancher_blog/containers-making-infrastructure-as-code-easier/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

[![Containers and Infrastructure as
Code](images/rancher_blog_infra-e1485893996473-300x158.png)](https://cdn.rancher.com/wp-content/uploads/2017/01/31131858/infra-e1485893996473.png)What
do Docker containers have to do with Infrastructure as Code (IaC)? In a
word, everything. Let me explain. When you compare monolithic
applications to microservices, there are a number of trade-offs. On the
one hand, moving from a monolithic model to a microservices model allows
the processing to be separated into distinct units of work. This lets
developers focus on a single function at a time, and facilitates testing
and scalability. On the other hand, by dividing everything out into
separate services, you have to manage the infrastructure for each
service instead of just managing the infrastructure around a single
deployable unit. Infrastructure as Code was born as a solution to this
challenge. Container technology has been around for some time, and it
has been implemented in various forms and withvarying degrees of
success, starting with chroot in the early 1980s and taking the form of
products such as [Virtuozzo](https://virtuozzo.com/) and Sysjail since
then. It wasn’t until Docker burst onto the scene in 2013 that all the
pieces came together for a revolution affecting how applications can be
developed, tested and deployed in a containerized model. Together with
the practice of Infrastructure as Code, Docker containers represent one
of the most profoundly disruptive and innovative changes to the process
of how we develop and release software today.

### What is Infrastructure as Code?

[![Rancher Free Ebook 'Continuous Integration and Deployment with Docker and Rancher'](images/rancher_blog_CiCd-book-232x300.jpg)](https://info.rancher.com/cicd-with-docker-ebook) Free
eBook: Continuous Integration and Deployment with Docker and
Rancher Before we delve into Infrastructure as Code and how
it relates to containers, let’s first look at exactly what we mean when
we talk about IaC. IaC refers to the practice of scripting the
provisioning of hardware and operating system requirements concurrently
with the development of the application itself. Typically, these scripts
are managed in a similar manner to the software code base, including
version control and automated testing. When properly implemented, the
need for an administrator to log into a new machine and configure it
manually is replaced by scripts which describe the ideal state of the
new machine, and execute the necessary steps in order to configure the
machine to realize that state.

### Key Benefits Realized in Infrastructure as Code

IaC seeks to relieve the most common pain points with system
configuration, especially the fact that configuring a new environment
can take a significant amount of time. Each environment needs to be
configured individually, and when something goes wrong, it can often
require starting the process all over again. IaC eliminates these pain
points, and offers the following additional benefits to developers and
operational staff:

1. Relatively easy reuse of common scripts.
2. Automation of the entire provisioning process, including being able
   to provision hardware as part of a continuous delivery process.
3. Version control, allowing newer configurations to be tested and
   rolled back as necessary.
4. Peer review and hardening of scripts. Rather than manual
   configuration from documentation or memory, scripts can be reviewed,
   updated and continually improved.
5. Documentation is automatic, in that it is essentially the scripts
   themselves.
6. Processes are able to be tested.

### Taking Infrastructure as Code to a Better Place with Containers

As developers, I think we’re all familiar with some variant of, “I don’t
know mate, it works on my machine!” At best, it’s mildly amusing to
utter, and at worst it represents one of the key frustrations we deal
with on a daily basis. Not only does the Docker revolution effectively
eliminate this concern, it also brings IaC into the development process
as a core component. To better illustrate this, let’s consider a
Dockerized web application with a simple UI. The application would have
a Dockerfile similar to the one shown below, specifying the
configuration of the container which will contain the application.

```
FROM ubuntu:12.04

# Install dependencies
RUN apt-get update -y && apt-get install -y git curl apache2 php5 libapache2-mod-php5 php5-mcrypt php5-mysql

# Install app
RUN rm -rf /var/www/*
ADD src /var/www

# Configure apache
RUN a2enmod rewrite
RUN chown -R www-data:www-data /var/www
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 80

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
```

If you’re familiar with Docker, this is a fairly typical and simple
Dockerfile, and you should already know what it does. If you’re not
familiar with the Dockerfile, understand that this file will be used to
create a Docker image, which is essentially a template that will be used
to create a container. When the Docker container is created, the image
will be used to build the container, and a self-contained application
will be created. It will be available for use on whatever machine it is
instantiated on, from developer workstation to high-availability cloud
cluster. Let’s look at a couple of key elements of the file, and explore
what they accomplish in the process.

```
FROM ubuntu:12.04
```

This line pulls in an Ubuntu Docker image from Docker Hub to use as the
base for your new container. Docker Hub is the primary online repository
of Docker images. If you visit Docker Hub and search for this image,
you’ll be taken to the [repository for
Ubuntu](https://hub.docker.com/r/library/ubuntu/). The image is an
official image, which means that it is one of a library of images
managed by a dedicated team sponsored by Docker. The beauty of using
this image is that when something goes wrong with your underlying
technology, there is a good chance that someone has already developed
the fix and implemented it, and all you would need to do is update your
Dockerfile to reference the new version, rebuild your image, and test
and deploy your containers again. The remaining lines in the Dockerfile
install various packages on the base image using apt-get. Add the source
of your application to the /var/www directory, configure Apache, and
then set the exposed port for the container to port 80. Finally, the CMD
command is run when the container is brought up, and this will initiate
the Apache server and open it for http requests. That’s Infrastructure
as Code in its simplest form. That’s all there is to it. At this point,
assuming you have Docker installed and running on your workstation, you
could execute the following command from the directory in which the
Dockerfile resides.

```
$ docker build -t my_demo_application:v0.1
```

Docker will build your image for you, naming it my\_demo\_application
and tagging it with v0.1, which is essentially a version number. With
the image created, you could now take that image and create a container
from it with the following command.

```
$ docker run -d my_demo_application:v0.1
```

And just like that, you’ll have your application running on your local
machine, or on whatever hardware you choose to run it.

### Taking Infrastructure as Code to a Better Place with Docker Containers and Rancher

A single file, checked in with your source code that specifies an
environment, configuration, and access for your application. In its
purest form, that is Docker and Infrastructure as Code. With that basic
building block in place, you can use docker-compose to define composite
applications with multiple services, each containing an individualized
Dockerfile, or an imported image for a Docker repository. For further
reading on this topic, and tips on implementation, check out Rancher’s
documentation on [infrastructure
services](https://docs.rancher.com/rancher/v1.6/en/rancher-services/) and
[environment
templates](https://docs.rancher.com/rancher/v1.6/en/environments/#what-is-an-environment-template).
You can also read up on [Rancher
Compose](https://rancher.com/docs/rancher/v1.6/en/cattle/rancher-compose/),
which lets you define applications for multiple hosts. *Mike Mackrory
is a Global citizen who has settled down in the Pacific Northwest - for
now. By day he works as a Senior Engineer on a Quality Engineering team
and by night he writes, consults on several web based projects and runs
a marginally successful eBay sticker business. When he’s not tapping on
the keys, he can be found hiking, fishing and exploring both the urban
and the rural landscape with his kids.*
