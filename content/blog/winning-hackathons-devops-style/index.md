---
title: "Winning Hackathons, DevOps-Style!"
date: 2017-08-03T11:30:00
slug: "winning-hackathons-devops-style"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["ci-cd"]
content_type: "community"
draft: true
migration:
  wp_id: 87292
  original_url: "https://www.suse.com/c/rancher_blog/winning-hackathons-devops-style/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Hackathon story with Cattle and Drone"
  redirect_target: "https://rancher.com/blog (hub)"
---

Recently, I moved to New York City. As a new resident, I decided to take
part in the [NYC DeveloperWeek
hackathon](http://www.developerweek.com/NYC/hackathon/#prizes), where
our team won the NetApp challenge. In this post, I’ll walk through the
product we put together, and share how we built a CI/CD pipeline for
quick, iterative product development under tight constraints.

**The Problem**: Have you ever lived or worked in a building where it’s
a pain to configure the buzzer to forward to multiple roommates or
coworkers? Imagine that a friend arrives and buzzes your number, which
is set to forward to your roommate who is visiting South Africa, and has
no cell service. If you’re running late, your friend is just stuck
outside.

**The Product**: We built a PBX-style application that integrations with
[Zang](http://zang.io/), and forwards a buzzer to multiple numbers, and even
allows your friend to use a PIN on his phone to gain entry.

**The constraint**: For the hackathon, we had to use hardware that had
already been setup and allocated.

### Building our Hackathon CI/CD Pipeline

[![](images/rancher_blog_CICD-cover-150x150.jpg)](https://info.rancher.com/cicd-with-docker-ebook) Our
newly-updated eBook walks you through incorporating containers into your
CI/CD pipeline. [Download
today!](https://info.rancher.com/cicd-with-docker-ebook) For
the competition, we knew that we wanted our builds scalable from the
start, and that each deployment would snapshot our entire data
environment pre-deployment using NetApp ONTAP (a sponsor of the
Hackathon, and a really nice group of folks); if any deployment had an
issue, we could simply and quickly roll back. Fortunately, I am a firm
believer in building stateless, Docker container-ready, rebuildable
architecture; I can’t go back to the world that existed before: no real
CI/CD, lots of SSH-ing into other systems, or SCP-ing data from one
place to another. Thankfully, today we have tools and strategies that
can help us. Here’s what we used:

- **[Rancher](https://rancher.com/rancher):** awesome tool for
  deploying containers with Kubernetes (or Cattle), just about
  anywhere
- **[Drone](https://github.com/drone):** a great, simple CI tool with
  a stateless build mindset built on top of Docker
- **[NetApp
  ONTAP](http://www.netapp.com/us/products/data-management-software/ontap.aspx)**:
  Scalable and resilient data management software

and the basic steps we took:

1. Turn the NetApp server into a Rancher host
2. Create a NetApp snapshot plugin for Drone
3. Create the CI/CD pipeline with snapshots baked in

Now, let’s take a closer look at these steps.

#### Turn a NetApp Server into a Rancher Host

Assuming that you’ve already got Rancher up and running, create a new
environment by going to Infrastructure -> Hosts on the navigation bar.
Using the Custom host option, use the provided command to register the
host with Rancher. It should look something like this:

```
sudo docker run — rm — privileged -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/rancher:/var/lib/rancher rancher/agent:v1.2.2 http://rancher.somedomain.com/v1/scripts/somekeyvalues
```

After a few minutes, you should see the host show up in Rancher, and
you’ll have the freedom to deploy any containers to it.

#### Creating a NetApp snapshot plugin for Drone

Plugins for Drone are just simple Docker containers, with environment
variable injected. This means you can use it in any build system you
have. In this case, running a simple command (as follows) will create a
snapshot of the data volume you just created:

```
docker run --rm                       
  -e PLUGIN_URL=<source>              
  -e PLUGIN_USERNAME=<user_name>      
  -e PLUGIN_USER_NAME=<user_password> 
  -e PLUGIN_STORAGE_VM_KEY=<vm_key>   
  -e PLUGIN_VOLUME_KEY=<volume_key>   
  -e PLUGIN_NAME_PREFIX
=<name_prefix>
  -v $(pwd):$(pwd)                    
  -w $(pwd)                           
  peloton/drone-netapp-snapshot
```

You can see all the code on GitHub
[here](https://github.com/josmo/drone-netapp-snapshot).

#### Create CI/CD pipeline with snapshots baked in

Full Drone pipelines are out of the scope of this post (though we’ll
publish a follow up next week), but by adding the following pipeline
makes it possible to bake in snapshots:

```
  build:
    ...
  docker_publish:
    ...
  snapshot:
    image: peloton/drone-netapp-snapshot
    url: https://netappapiserver:8443/api/2.0/ontap/snapshots
    storage_vm_key: 082eb55c-53b0-11e7-b33e-633e98aa9f79:type=vserver,uuid=6141d5cc-53b0-11e7-b33e-633e98aa9f79
    volume_key: 082eb55c-53b0-11e7-b33e-633e98aa9f79:type=volume,uuid=2b8a5865-8def-4dd1-a7b1-c2fbe52921f1
    name_prefix: mySnapshot
    secrets: [ NETAPP_USER_NAME, NETAPP_USER_PASSWORD ]
  deploy:
    image: peloton/drone-rancher
    url: http://rancher.domainname.com
    access_key: accesskeyvalue
    secrets: [ rancher_secret_key ]
    service: hack/web
    docker_image: classis/dockerimage:${DRONE_BUILD_NUMBER}
```

In this case, you get a full snapshot prior to any deployments. This
then makes rolling back to a prior snapshot pretty quick and easy.
Rancher makes it simple to build these in a mixed environment, and I
can’t imagine living in a world where it’s not around. Drone helps
create simple build and delivery pipelines, and NetApp helps with simple
snapshots. This all translates beautifully to corporate environments,
where things may need to be hosted in a private cloud. At
[Pelo.tech](https://www.pelo.tech/), we’re working on the next versions
of these concepts, which will allow for complete, self-hosted
applications that are highly available, highly scalable, and updated
with simple blue/green deployments. Reach out to us if you’re interested
in learning more about us and what we do! \* \* *Joachim Hill-Grannec
([@lindyblues](https://twitter.com/lindyblues)) is a Partner at
[pelo.tech](https://www.pelo.tech/), which helps organizations improve
their dev practices and culture. These days, you’ll also find him
traveling around the world dancing at West Coast Swing events.*
