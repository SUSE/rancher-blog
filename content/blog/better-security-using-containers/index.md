---
title: "Better Security Using Containers"
date: 2017-04-07T09:01:00
slug: "better-security-using-containers"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["security"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 85807
  original_url: "https://www.suse.com/c/rancher_blog/better-security-using-containers/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Docker 2017 advice, latest tag guidance misleading"
  redirect_target: "https://rancher.com/blog (hub)"
---

As a relatively new technology, Docker containers may seem like a risk
when it comes to security -- and it’s true that, in some ways, Docker
creates new security challenges. But if implemented in a secure way,
containers can actually help to make your entire environment more secure
overall than it would be if you stuck with legacy infrastructure
technologies. This article builds on existing container security
resources, like [Security for your
Container](https://rancher.com/security-container-environment/), to
explain how a secured containerized environment can harden your entire
infrastructure against attack.

### Some Background on Container Security

When you’re thinking about containers and security, it’s always good to
have some history on why containers work the way they do and what that
means for security. [Aqua Security](https://www.aquasec.com/), one of
the firms that specializes in container security, offers [A Brief
History of
Containers](http://blog.aquasec.com/a-brief-history-of-containers-from-1970s-chroot-to-docker-2016) to
provide some context. As is visible in the evolution from chroot to
Docker and the [Open Container
Initiative](https://www.opencontainers.org/), it is obvious that
isolation between services coexisting on shared servers was always the
leading goal—not necessarily well thought-out, hardened security
practices. Isolation is a good counter-measure, but, as shown in this
[Security for your
Container](https://rancher.com/security-container-environment/) article,
there are a lot more things that can and should be done. Here are three
examples of easy first steps that can be taken use containers to make
your environment more secure:

#### Example 1: Only Expose Required Ports

[![](images/rancher_blog_Training.png)](https://attendee.gotowebinar.com/rt/2905734731496917249)
Register now for free online training on deploying containers with
Rancher Using containers, you can minimize the number of
ports that are exposed to the outside world. This way, you have a
minimal attack surface. Here’s an example of limiting port exposure: If
you are running a container with MySQL, then you need only one port
exposed, which defaults to 3306. For more complicated platforms like
Oracle WebLogic, you may need the admin, node manager, and managed
server ports open (8001, 5556, and 7001). There are multiple ways to
specify these ports. Here are the three most common: **Dockerfile**

```
# Private (only accessible to other containers)
EXPOSE=80
# Public / Published
EXPOSE=443:443
```

**Command Line**

```
$ docker run --name docker-nginx -p 80:80 nginx
```

**A docker-compose.yml file**

```
nginx:
    image: nginx:latest
    networks:
      - loadbalance
    ports:
      - "80"
```

####

#### Example 2: Always Pulling the Latest Images

Containers also make it easy to ensure that the software you run is
always up-to-date and originates from a trusted, secure source. The
easiest way to do this is to pull your container images from trusted
public repositories that are maintained by reputable organizations --
or from your own private, secured registry. In addition, unless you need
a specific version of a container image when you pull it, it’s best not
to specify a version in your Dockerfile. That way, you always get the
latest software. Ideally:

```
FROM: ubuntu:latest
```

Not bad:

```
FROM: ubuntu:xenial
```

Less than ideal:

```
FROM: ubuntu:xenial-20170214
```

Being able to download your app images from secure, centralized
repositories -- and having the installation system default to
up-to-date software -- beats having to download and install binaries
from websites or proxies that you may or may not trust, as you would do
with traditional environments.

####

#### Example 3: Enabling a Container with a Host Firewall via iptables

Containers allow you to set up firewall rules in a very granular way in
order to control which traffic will be allowed in and out of your
specific container(s) at the container level. This is possible because
each container can run its own copy of iptables -- which is a really
cool thing, since in traditional environments, firewall rules are
generally shared across the entire operating system (and although you
could configure them on an application-specific basis, doing so tends to
get very messy). This is particularly convenient in environments with
multiple applications and mixed traffic where you only want to accept
traffic from your load balancer or a specific client, not just anyone
who happens to discover the service. There are two steps to enable this:

1. Pass the “--cap-add=NET\_ADMIN” parameter to the “docker run”
   command.
2. Set up a script to run on startup in your container to apply the
   iptables rules.

**How it is set up by default:**

```
root@docker-1gb-tor1-01:~# docker run -ti --rm centos bash
[root@d7badabb70ba /]# yum install -y iptables
...
Complete!
[root@d7badabb70ba /]# iptables -A OUTPUT -d 8.8.8.8 -j DROP
iptables v1.4.21: can't initialize iptables table `filter': Permission denied (you must be root)
Perhaps iptables or your kernel needs to be upgraded.
[root@d7badabb70ba /]# ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=60 time=1.38 ms
```

**With NET\_ADMIN enabled:**

```
root@docker-1gb-tor1-01:~# docker run -ti --rm --cap-add=NET_ADMIN centos bash
[root@2a35eb22654f /]# yum install -y iptables
...
Complete!
[root@2a35eb22654f /]# iptables -A OUTPUT -d 8.8.8.8 -j DROP
[root@2a35eb22654f /]# ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
ping: sendmsg: Operation not permitted
```

For much more detailed examples, there are several enlightening
tutorials online (such as this one from [Rudi
Starcevic](http://rudijs.github.io/2015-07/docker-restricting-container-access-with-iptables/)).

###

### Conclusion

To deploy containers securely, you’ll have to master some new tricks.
But once you understand what it takes to keep your containerized
environment secure, you’ll find that containers offer a finer-tuned,
deeper level of security than what you can achieve with traditional
infrastructure. In this article, we took a look at just a few of the
many ways in which containers help increase the security of your
environment. *Vince Power, a Solution Architect, focuses on cloud
adoption and technology implementations using open source-based
technologies. He has extensive experience with core computing and
networking (IaaS), identity and access management (IAM), application
platforms (PaaS), and continuous delivery.*
