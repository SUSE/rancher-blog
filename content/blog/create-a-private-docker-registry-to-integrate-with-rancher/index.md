---
title: "Create a Private Docker Registry to Integrate with Rancher"
date: 2016-06-07T10:17:00
slug: "create-a-private-docker-registry-to-integrate-with-rancher"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["installation"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86640
  original_url: "https://www.suse.com/c/rancher_blog/create-a-private-docker-registry-to-integrate-with-rancher/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x private registry setup"
  redirect_target: "rancher.com/blog (hub)"
---

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)

In my last [blog
post](https://rancher.com/preparing-a-micro-service-release-using-rancher/),
I detailed how we can quickly and easily get the Rancher Server up and
running with Github authentication and persistent storage to facilitate
easy upgrades. In this post, I will step through the creation of a
private Docker registry that is password protected and how to integrate
this private registry into Rancher. We will then tag and push an image
to this registry. Finally, we will use the Rancher Server to deploy this
image onto a server. The Docker image that we will be using is
**registry:2** and although I would recommend that you use a storage
driver like AWS S3 for this purpose, I will be storing everything we
need as host level persistence. Some things that we need to use with
this image are:

- A certificate for your domain. I will be using **regv2.piel.io**
- A .htaccess compatible password

To create the first item, I am going to use
[letsencrypt.org](https://letsencrypt.org/) and a handy Docker script by
fatk to quickly get your certificates.

- Clone
  git@github.com:fatk/docker-letsencrypt-nginx-proxy-companion-examples.git
- Modify
  docker-letsencrypt-nginx-proxy-companion-examples/dockerdocker-run/simple-site/docker-run.sh
  and replace “site.example.com” with a public accessible domain
  pointing to the server you will run this on.
- Run the script

```
$ git clone git@github.com:fatk/docker-letsencrypt-nginx-proxy-companion-examples.git
$ cd docker-letsencrypt-nginx-proxy-companion-examples
# Modify the script and replace site.example.com
$ vi dockerdocker-run/simple-site/docker-run.sh
$ ./docker-run.sh
```

While the script is running, the nginx instance, docker-gen
instance, letsencrypt-nginx-proxy-companion instance, and finally the
nginx instance. Let’s see what containers started after the script has
finished! [![nginx, docker-gen, and letsencrypt-nginx-proxy-companion
instances. Click to
enlarge.](images/rancher_blog_dietz-2-29-1024x95.png)](https://cdn.rancher.com/wp-content/uploads/2016/06/07054528/dietz-2-29.png)
So that seemed to have worked...but where are our freshly created
certificates?

```
$ ls volumes/proxy/certs
dhparam.pem  regv2.piel.io  regv2.piel.io.crt  regv2.piel.io.dhparam.pem  regv2.piel.io.key
```

and

```
$ ls volumes/proxy/certs/regv2.piel.io
account_key.json  cert.pem  fullchain.pem  key.pem
```

Yay! So we can use the regv2.piel.io.key and the fullchain.pem for
docker registry:2. Let’s create some directories and place the certs
where the registry can access them.

```
$ mkdir -p /data/docker-registry-certs
$ cp volumes/proxy/certs/regv2.piel.io.key /data/docker-registry-certs/
$ cp volumes/proxy/certs/regv2.piel.io/fullchain.pem /data/docker-registry-certs/
$ mkdir /data/docker-registry-auth
$ mkdir /data/docker-registry
```

The last step before we can get this registry up and running is to
create our username and password. This will result in minimum security
that is recommended by docker registry:2.

```
$ docker run --entrypoint htpasswd registry:2 -Bbn pieltestuser 
"mkakogalb47" > /data/docker-registry-auth/htpasswd
```

This command requires the registry:2 image to exist on the server and
therefore it has to pull it before running the htpasswd command.
Following this, the new container will exit. Check to see if we have the
htpasswd in the file.

```
$ cat /data/docker-registry-auth/htpasswd
pieltestuser:$2y$05$w3IqOzTdsDbot9ls1JpeTeHYr/2vv.PTx3dObRvT.JkfGaygfTkJy
```

Finally, we can run our registry:2.

```
$ docker run -d -p 5000:5000 --restart=always --name docker-registry 
  -v /data/docker-registry:/var/lib/registry 
  -v /data/docker-registry-auth:/auth 
  -e "REGISTRY_AUTH=htpasswd" 
  -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" 
  -e "REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd" 
  -v /data/docker-registry-certs:/certs 
  -e "REGISTRY_HTTP_TLS_CERTIFICATE=/certs/fullchain.pem" 
  -e "REGISTRY_HTTP_TLS_KEY=/certs/regv2.piel.io.key" 
  registry:2

$ docker run -d -p 5000:5000 --restart=always --name docker-registry 
  -v /data/docker-registry:/var/lib/registry 
  -v /data/docker-registry-auth:/auth 
  -e "REGISTRY_AUTH=htpasswd" 
  -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" 
  -e "REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd" 
  -v /data/docker-registry-certs:/certs 
  -e "REGISTRY_HTTP_TLS_CERTIFICATE=/certs/fullchain.pem" 
  -e "REGISTRY_HTTP_TLS_KEY=/certs/regv2.piel.io.key" registry:2
```

Now let’s see if we can log in.

```
$ docker login -u pieltestuser -p "mkakogalb47" -e wayne@wayneconnolly.com regv2.piel.io:5000
$ docker login -u pieltestuser -p "mkakogalb47" -e wayne@wayneconnolly.com regv2.piel.io:5000
WARNING: login credentials saved in /root/.docker/config.json
Login Succeeded
```

So now let’s see if we can pull, tag and then push a docker image to our
new repo. Jenkins is useful for us so I will pull this
https://hub.docker.com/\_/jenkins/

```
$ docker pull jenkins
$ docker tag jenkins:latest regv2.piel.io:5000/piel-jenkins:latest
```

Validate that it worked [![Validating the Jenkins
pull](images/rancher_blog_dietz-2-30-1024x160.png)](https://cdn.rancher.com/wp-content/uploads/2016/06/07055222/dietz-2-30.png)
Now, let’s push it to our registry.

```
$ docker push regv2.piel.io:5000/piel-jenkins:latest
```

There is no easy way to see what images are in the repo at the time of
writing this except for using curl:

```
$ curl -u pieltestuser:mkakogalb47 https://regv2.piel.io:5000/v2/_catalog
{"repositories":["piel-jenkins"]}
```

We can see our new Jenkins image in our private registry in the JSON
result. Now we can apply our registry to our rancher-test.piel.io
environment. Log into rancher and navigate to INFRASTRUCTURE > HOSTS
and click “Add Host”. You will have to populate the rancher servers IP
then you should have an auto-generated command like below. Run this on
the Rancher host.

```
$ sudo docker run -e CATTLE_AGENT_IP='45.32.190.15'  
  -d --privileged 
  -v /var/run/docker.sock:/var/run/docker.sock 
  -v /var/lib/rancher:/var/lib/rancher 
  rancher/agent:v1.0.1 http://rancher-test.piel.io/v1/scripts/FF42DCE27F7C88BD7733:1461042000000:ryU0BaXJFo6c9zuHgeULdAtbCE

$ sudo docker run -d --privileged 
  -v /var/run/docker.sock:/var/run/docker.sock 
  -v /var/lib/rancher:/var/lib/rancher 
  rancher/agent:v0.11.0http://rancher.piel.io/v1/scripts/BE455B92EA48EA1C1F12:1461042000000:mi433ChYRN9nfQSwB2FIlBnpPk
```

Give it a minute and the host will appear. Due to my not yet configuring
the host name of the server, it will show up as “vultr.guest“. Let’s
change this by clicking the vertical ellipsis (3 vertical dots) menu
button on the host and clicking the Edit item. Enter your custom name
and add a Label. I always add a server location label as the bare
minimum.

Next, let’s add our private registry so we can deploy our piel-jenkins
image to this host. Navigate to INFRASTRUCTURE > REGISTRIES and click
“Add Registry” then “Click “Custom” and add your details. This
takes a couple of minutes, but the end result should be your own
registered private registry available to your Rancher server.

Let’s deploy our Jenkins container to this host. Navigate to
INFRASTRUCTURE > HOSTS and click “+ Add Container“. Complete the
fields and put the custom Jenkins image in the select image field as
“regv2.piel.io:5000/piel-jenkins: latest” and set the port map to
redirect the Jenkins default port 8080 to the host port 8080.

This process will take a couple of minutes to pull the image to the host
if it’s not already there. We can see that the host now has the new
container in it called “my-jenkins“.

Let’s navigate to the Jenkins URL, http://regv2.piel.io:8080, and see
if it worked.

Now for a docker ps double confirmation.

SUCCESS!!! We have now:

- created and secured our own private docker registry
- tagged and added an image to it
- added a host to our Rancher Server
- assigned the private registry to our Rancher Server
- deployed our Jenkins container to our host
- confirmed that the container is deployed

Note: The servers used in this tutorial have been decommissions. Next
will be Part 3 where I will discuss creation and usage of stacks to
provide you with a usable platform to describe, deploy and manage your
product offering.

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)
