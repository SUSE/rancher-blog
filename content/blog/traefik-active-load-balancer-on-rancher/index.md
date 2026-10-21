---
title: "Traefik Active Load Balancer on Rancher"
date: 2016-05-24T11:31:00
slug: "traefik-active-load-balancer-on-rancher"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["networking"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 87316
  original_url: "https://www.suse.com/c/rancher_blog/traefik-active-load-balancer-on-rancher/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x load balancer with Traefik"
  redirect_target: "rancher.com/blog (hub)"
---

Take a deep dive into Best Practices in Kubernetes NetworkingFrom overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options.[Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/)

[![traefik.logo](images/rancher_blog_traefik.logo_.png)](images/rancher_blog_traefik.logo_.png)
*Raul is a DevOps microservices architect specializing in scrum, kanban,
microservices, CI/CD, open source and other new technologies.* *This
post focuses on the Traefik “active mode” load balancer technology
that works in conjunction with Docker labels and Rancher meta-data to
configure itself automatically and provide access to services.* Load
balancers/proxies are software programs that make it possible for you to
access your services backend. In the microservices architectures scope,
they have an additional challenge to manage high dynamism. They have to
be aware of frontend and backend changes in a dynamic and automated way
so as to update and reload their configuration. They also need to talk
with discovery systems. **Rancher-metadata** In Rancher, we have an
excellent built-in discovery system called the rancher-metadata service.
In rancher-metadata, we could get info from self-services or from other
stacks or services. Rancher-metadata information is up to date on what
is running on your system and where it is located. To generate dynamic
configs files for your service, you need to talk with rancher-metadata.
To do it, use **confd** with specifics templates. To get more details, I
recommend reading Bill Maxwell’s article, located in the community
Zookeeper catalog package;
**<https://rancher.com/introducing-rancher-metadata-service-for-docker/>**
**Load Balancers** Rancher provides a built-in load balancer service. It
is a containerized haproxy, and it’s very useful in publishing your
services ports externally. The load balancer can work in two different
modes. That implies that it can act in two different OSI levels,
specifically, layers 4 and 7. But, what does that mean?

- Layer 4 - You can publish and provide access to TCP
  ports. It works in a kind of raw mode that forwards packages to the
  backend of your service, without the possibility of modifying them.
  In this mode, you couldn’t share ports. It means you need to publish
  a different port for every service.

**[![Raul
2-1](images/rancher_blog_Raul-2-1-1024x925.png)](https://cdn.rancher.com/wp-content/uploads/2016/05/18182124/Raul-2-1.png)**

- Layer 7 - You are working at the application level,
  and can only publish HTTP(s) ports. In this mode, the load balancer
  has the possibility to see and modify HTTP packets. You can check,
  add, or change the HTTP header. In this mode, you can share the same
  published port to different services. Obviously, the load balancer
  has to know how to differentiate the incoming packets so it can
  forward them to the right service. To do it, you need to define HTTP
  header filters that are checked with the incoming HTTP packages.
  Once the match is made, the request is sent to the correct service.
- In both modes, load balancers work in “passive mode”. That means
  that once you deploy a new service, you have to edit the load
  balancer config and add your service. Obviously, if you remove a
  service configured in the load balancer, it removes itself from the
  load balancer config.

**[![Raul
2-2](images/rancher_blog_Raul-2-2-996x1024.png)](https://cdn.rancher.com/wp-content/uploads/2016/05/18182057/Raul-2-2.png)**
**Traefik Active Load Balancer** To provide users a better choice, we’ve
created an “active mode” load balancer using Docker labels and
rancher-metadata. The load balancer scans rancher-metadata and is able
to configure itself and provide access to services that have configured
certain labels. To obtain that feature, we use Traefik. Traefik is a
programmatic open source load balancer, written in golang. It can be
integrated with different service discovery systems such as Zookeeper,
etcd, Consul and others. We did an early integration with
rancher-metadata. Traefik has a true zero downtime reload and implements
the possibility of defining circuit breakers rules. To get more info, go
to **<https://traefik.io/>.** To use Traefik, select it from community
catalog and launch it. With default parameters, Traefik will run in all
hosts with label **traefik\_lb=true.** Expose the host port 8080 for
HTTP services and 8000 as the Traefik admin port. It refreshes
configuration every 60 seconds. It is possible to override all
parameters when you deploy the service. **[![Raul
2-3](images/rancher_blog_Raul-2-3-1024x484.png)](https://cdn.rancher.com/wp-content/uploads/2016/05/18182008/Raul-2-3.png)**
**[![Raul
2-4](images/rancher_blog_Raul-2-4-1024x328.png)](https://cdn.rancher.com/wp-content/uploads/2016/05/18181949/Raul-2-4.png)**
Once the service is deployed, you can access the admin interface at
**[http://host-address:9000](http://host-address:9000/)** You need to
define these labels at the service to get services automatically exposed
at Traefik:

- **traefik.enable = <true | false>**
- **traefik.domain = < domainname to route rule >**
- **traefik.port = < port to expose throught traefik >**

It’s mandatory that you define a health check in your service because
only healthy backends are added to Traefik. If you define,
**traefik.enable = true** label in your service, but, the service does
not have a health check then the frontend would be added to Traefik, but
with an empty list of backends. **Testing** We’ve written a basic web
test service to make it possible to check the Traefik service and test
it in a quick way. That service exposes the web service at port 8080.
You will create a new stack importing these docker-compose.yml and
rancher-compose.yml

```
docker-compose.yml
web-test:
  log_driver: ''
  labels:
    traefik.domain: local
    traefik.port: '8080'
    traefik.enable: 'true'
    io.rancher.container.hostname_override: container_name
  tty: true
  log_opt: {}
  image: rawmind/web-test
```

```
rancher-compose.yml
web-test:
  scale: 3
  health_check:
    port: 8080
    interval: 2000
    initializing_timeout: 60000
    unhealthy_threshold: 3
    strategy: recreate
    response_timeout: 2000
    request_line: GET "/" "HTTP/1.0"
    healthy_threshold: 2
```

It has Traefik labels added to its definition. When deployed, its
backend would be in “healthy” state. They would be added automatically
to the Traefik service exposed as
**http://${service\_name}.${stack\_name}.${traefik.domain}:${http\_port}.**
You could verify this at the Traefik admin UI;
**[http://host-address:8000](http://host-address:8000/)** [![Raul
2-5](images/rancher_blog_Raul-2-5-1024x417.png)](https://cdn.rancher.com/wp-content/uploads/2016/05/18181929/Raul-2-5.png)
If you scale the web-test service up or down, you could see in the
Traefik admin UI how the backend server will be added or removed
automatically. However, you have to wait for the refresh interval time
before the configuration is refreshed. To access the web-test service,
add an alias to your DNS, web-test.proxy-test.local pointing to your
host address, and go to **http://web-test.proxy-test.local:8080.** When
you request the web-test service, it shows you all the headers, as
below: **http://web-test.proxy-test.local:8080** [![Raul
2-5a](images/rancher_blog_Raul-2-5a-1024x226.png)](https://cdn.rancher.com/wp-content/uploads/2016/05/18181851/Raul-2-5a.png)
Once you refresh the page, you should see that the Real\_Server is
changing as the load balancer is doing its job. ***TIP: To avoid having
to set the DNS entry, you could test the service with curl, adding a
Host header*** **curl -H Host:web-test.proxy-test.local
[http://host-address:8080](http://host-address:8080/)** **Exposing your
services** To expose your services to Traefik, update them an add the
following labels to them:

- **traefik.enable = true**
- **traefik.domain =** **< yourdomain >**
- **traefik.port = <** **service\_port >**

The service **${traefik.port}** would be exposed externally as:
**http://${service\_name}.${stack\_name}.${traefik.domain}:${http\_port}**
***TIP: If you delete the Traefik stack, when you deploy it again, you
don’t need to reconfigure it, it would be configured by automatically
scanning services labels.*** **Work In Progress** At the moment, only
HTTP services access are available. We are working to integrate ssl
certificates to get HTTPS services access available. Look for my next
post here on the Rancher blog that extends this discussion to ssl
certificate integration. **References**
**<https://github.com/rawmind0/alpine-traefik>**
**<https://github.com/rawmind0/rancher-traefik>**
**<https://github.com/rawmind0/web-test>**

Take a deep dive into Best Practices in Kubernetes NetworkingFrom overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options.[Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/)
