---
title: "Using Rancher-Gen to Dynamically Update Docker Configuration Files"
date: 2016-09-28T11:29:00
slug: "using-rancher-gen-to-dynamically-update-docker-configuration-files"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["developer-experience"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 87274
  original_url: "https://www.suse.com/c/rancher_blog/using-rancher-gen-to-dynamically-update-docker-configuration-files/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x metadata and Rancher-Gen"
  redirect_target: "rancher.com/blog (hub)"
---

*[![pitrho](images/rancher_blog_Pitrho1.png)](images/rancher_blog_Pitrho1.png)This
is a guest post by Alejandro Mesa, Full-Stack Software Engineer and
Chief Architect at [Pit Rho](http://pitrho.com/).* **Introduction**
Docker and [Rancher](https://rancher.com/rancher) have made it far
easier to deploy and manage microservice-based applications. A key
challenge, however, is managing the configuration of services that
depend on other dynamic services. Imagine the following scenario: you
have multiple backend containers that run your web application, and a
few nginx containers that proxy all requests to the backend containers.
Now, there’s a new release of the web application that must be deployed,
which means new backend containers need to be built and deployed. After
they are deployed, the nginx configuration needs to change to point to
the new backend containers. So, what do you do with nginx? Do you change
the its configuration, build a new container and deploy it? What if
there was a way for you to automatically detect the changes on the
backend service and dynamically update nginx? That’s where
[Rancher-Gen](https://github.com/pitrho/rancher-gen) comes into play.
Rancher-Gen is a Python utility that listens for service changes in
Rancher and renders a user-specified [Jinja2](http://jinja.pocoo.org/)
template. This allows a user to generate configuration files for
existing services based on those changes. In addition, it provides a
mechanism to run a notification command after the template has been
rendered. Below is a tutorial that describes how to automatically
generate an nginx configuration file for a backend service running the
[ghost](https://ghost.org/) blogging platform.

### **Tutorial**

All configuration files described below can be found under the
[demo](https://github.com/pitrho/rancher-gen/tree/master/demo) directory
in the [Rancher-Gen](https://github.com/pitrho/rancher-gen) repository.
**Step 1 -  Deploying the ghost service** For simplicity, we’re going
to use the official ghost image from Docker hub. So, create a
docker-compose.yml file and add the ghost service as follows:

```
ghost:
  image: ghost
  expose:
    - "2368"
```

Now, deploy the ghost service using Rancher Compose:

```
$ rancher-compose -p demo up -d ghost
```

**Step 2  -  Create the nginx image with rancher-gen** Here is the
Dockerfile used to build the nginx image:

```
FROM phusion/baseimage:0.9.17
MAINTAINER pitrho

# Step 1 - Install nginx and python
ENV DEBIAN_FRONTEND noninteractive
RUN 
 apt-add-repository -y ppa:nginx/stable && 
 apt-get update && 
 apt-get install -y python-software-properties 
   wget 
   nginx 
   python-dev 
   python-pip 
   libev4 
   libev-dev 
   expect-dev && 
 rm -rf /var/lib/apt/lists/* && 
 chown -R www-data:www-data /var/lib/nginx && 
apt-get clean

# Step 2 - Install rancher-gen
ENV RANCHER_GEN_VERSION 0.1.2
RUN pip install rancher-gen==$RANCHER_GEN_VERSION

# Step 3 - Define services
RUN mkdir /etc/service/nginx /etc/service/rancher_gen /nginxconf
COPY nginx_run /etc/service/nginx/run
COPY rancher-gen_run /etc/service/rancher_gen/run
COPY default.j2 /nginxconf

# Step 4 - Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Step 5 - Expose ports.
EXPOSE 80
EXPOSE 443
```

Let’s break down the Dockerfile step by step. Steps 1 and 2 are
self-explanatory: simply install nginx, python and rancher-gen. Step 3
is where we setup the services that run when the image starts. The first
service is nginx, and it runs using the file at
**/etc/servce/nginx/run**. The contents of this file are:

```
#!/bin/bash
 rancher-gen --host $RANCHER_GEN_HOST 
 --port $RANCHER_GEN_PORT 
 --access-key $RANCHER_GEN_ACCESS_KEY 
 --secret-key $RANCHER_GEN_SECRET_KEY 
 --project-id $RANCHER_GEN_PROJECT_ID 
 $RANCHER_GEN_OPTIONS 
 --notify "service nginx reload" /nginxconf/default.j2 /etc/nginx/sites-available/default
```

Notice how, after the notify step, we pass two paths, namely
**/nginxconf/default.j2** and **/etc/nginx/sites-available/default**.
The former is the Jinja2 template and the latter is the output location
of the rendered template. Below are the contents of the default.j2 file:

```
upstream ghost.backend {
{% for container in containers %}
  {% if container['state'] == "running" %}
    server {{container['primaryIpAddress']}}:2368;
  {% endif %}
  {% endfor %}
}

server {
  listen 80;
  server_name ghost_demo;
  location / {
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header HOST $http_host;
    proxy_set_header X-NginX-Proxy true;
    proxy_pass http://ghost.backend;
    proxy_redirect off;
  }
}
```

Steps 4 and 5 of the Dockerfile set the run command
”[/sbin/my\_init](https://github.com/phusion/baseimage-docker)” in the
image and exposes ports 80 and 443. Now, it’s time to build the image:

```
$ docker build -t="pitrho/nginx-rancher-gen-demo" .
```

**Step 3 — Create the nginx service and deploy it** Now that we have
the nginx image, add the nginx service to the docker-compose.yml file
created in Step 1:

```
ghost:
 image: ghost
 expose:
 - "2368"

nginx:
 image: pitrho/nginx-rancher-gen-demo:latest
 ports:
 - 80:80
 links:
 - ghost
 environment:
 NGINX_RUN_TYPE: rancher-gen
 RANCHER_GEN_HOST: $RANCHER_HOST
 RANCHER_GEN_PORT: $RANCHER_PORT
 RANCHER_GEN_ACCESS_KEY: $RANCHER_ACCESS_KEY
 RANCHER_GEN_SECRET_KEY: $RANCHER_SECRET_KEY
 RANCHER_GEN_PROJECT_ID: $RANCHER_GEN_PROJECT_ID
 RANCHER_GEN_OPTIONS: --stack demo --service ghost
```

The `RANCHER_GEN_OPTIONS` environment variable above is used to pass
additional command-line options to rancher-gen. See the Rancher-Gen
documentation for an explanation of these options. Now run
rancher-compose to start the nginx service:

```
$ rancher-compose -p demo up -d nginx
```

At this point, both the ghost and nginx services should be up and
running. [![ghost nginx
check](images/rancher_blog_ghost-nginx-check-1024x111.jpg)](https://cdn.rancher.com/wp-content/uploads/2016/09/23141307/ghost-nginx-check.jpg)
and ghost can be accessed by pointing your browser to the IP address of
the host running the nginx container: [![ghost
screen](images/rancher_blog_ghost-screen-1024x481.jpg)](https://cdn.rancher.com/wp-content/uploads/2016/09/23141303/ghost-screen.jpg)
If you were to inspect the nginx container using the shell, and open the
rendered file **/etc/nginx/sites-enabled/default**, you will see the
following output:

```
upstream ghost.backend {
   server 10.42.136.216:2368;
 }

server {
     listen 80;
     server_name ghost_demo;

     location / {
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header HOST $http_host;
         proxy_set_header X-NginX-Proxy true;
         proxy_pass http://ghost.backend;
         proxy_redirect off;
     }
  }
```

As expected, this is the rendered output based on the template specified
when running the rancher-gen command. At this point, if you were to
upgrade the ghost service, and again look at the rendered file, you
would notice that the IP address under the upstream section has changed.

### Conclusion

To recap, Rancher-Gen is an automation utility that can be used to
generate files and run notification commands. With the expressiveness of
Jinja2 templates, and its clean command line interface, Rancher-Gen can
be used to generate most configuration files, and automate tasks that
otherwise would be tedious and repetitive for most sysadmins and
software engineers. If you have any questions or suggestion on how to
improve Rancher-Gen, feel free to reach us through the
[github](https://github.com/pitrho/rancher-gen) repository, or contact
us on Twitter [@PitRho](https://twitter.com/pitrho).
