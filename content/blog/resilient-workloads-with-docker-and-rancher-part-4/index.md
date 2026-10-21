---
title: "Resilient Workloads with Docker and Rancher - Part 4"
date: 2017-01-17T11:18:00
slug: "resilient-workloads-with-docker-and-rancher-part-4"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["upgrades", "high-availability"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86996
  original_url: "https://www.suse.com/c/rancher_blog/resilient-workloads-with-docker-and-rancher-part-4/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x rancher-compose upgrades"
  redirect_target: "rancher.com/blog (hub)"
---

*Note: this is Part 4 in a series on building highly resilient
workloads. Parts
[1](https://rancher.com/5-keys-running-workloads-resiliently-rancher-docker-part-1/), [2](https://rancher.com/5-keys-running-workloads-resiliently-rancher-docker-part-2/), and [3](https://rancher.com/5-keys-to-running-workloads-resiliently-with-docker-and-rancher-part-3/) are available already online.*
[![](images/rancher_blog_rancher-logo_square-wht-on-blue.jpg)](images/rancher_blog_rancher-logo_square-wht-on-blue.jpg)
In Part 4 of this series on running resilient workloads with Docker and Rancher, we take a look at service updates. Generally, service updates are where the risk of downtime is the highest. It doesn’t hurt to have a grasp of how deployments work in Rancher and the options available within. For this post, instead of focusing on how to setup a continuous deployment/integration pipeline, we’ll instead focus on experimenting and learning with upgrades using rancher-compose files, and reference the great chain of articles by the awesome bloggers. We will skim over the Rancher [CI/CD ebook](https://info.rancher.com/cicd-with-docker-ebook) for now, and
sprinkle in enough theory to get us start using Rancher upgrades comfortably. [![Rancher Free Ebook 'Continuous Integration and Deployment with Docker and Rancher'](images/rancher_blog_CiCd-book-232x300.jpg)](https://info.rancher.com/cicd-with-docker-ebook) Free eBook: Continuous Integration and Deployment with Docker and Rancher For those newer to CI/CD, a good reading order would be[a great walk through](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-1/) by the guys at This End Out, before diving into the official [CI/CD with Rancher ebook](https://info.rancher.com/cicd-with-docker-ebook). A thorough reading is not required, as we will lay enough groundwork theory to run our experiments; but for those who want to dig a bit deeper, there will be links to specific sections of the articles.

### The Simple Case

Say we want to launch a simple website using one Wordpress container and
One database container (MySQL). Lets assume we have our database outside
of Docker on the same host.

```
docker run -d -p 80:80 -e WORDPRESS_DB_HOST='localhost' -e WORDPRESS_DB_USER='root' -e 0WORDPRESS_DB_PASSWORD='' wordpress
```

[![Single
Host](images/rancher_blog_Codesheppard-4-singlehost.png)](images/rancher_blog_Codesheppard-4-singlehost.png)
If you were to look at the process of updating Docker services in
production, we would SSH into the host, stop the container, pull the
new image down from a registry, then restart the container. Or, if we
were to list it out:

```
# Docker Container stop, Docker Container Pull, Replace Docker Container

$> docker stop
$> docker pull
$> docker start
$> docker rm <old-container>
```

Since we are running our services on Rancher, these steps are automated
and managed on remote hosts by the Rancher agent. ![Resilient Docker
Workloads -
Upgrade](images/rancher_blog_Codesheppard-4-upgrade-300x147.png)Clicking this Upgrade
button on our service will open a dropdown menu that allows various
configurations of the upgrade. Since we know that Rancher will be
re-creating the container, the various options to add links,
environments, and volumes are open again as if we are creating a new
service: [![Resilient Docker Workloads - Upgrade
Form](images/rancher_blog_Codesheppard-4-UpgradeForm-1024x444.png)](https://cdn.rancher.com/wp-content/uploads/2017/01/16141812/Codesheppard-4-UpgradeForm.png)
This is called an in-service or in-place update, and is the exact
mechanism provided by the Rancher upgrade. If we think of the Rancher
agent running these commands for us on one of the child nodes, we can
appreciate the convenience that Rancher provides. The chain of articles
from past blog posts provide a deeper illustration of the rationale
starting with [wrapping manual docker deployment inside
scripts](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-1/),
followed with [encoding the deployment metadata into
docker-compose](https://rancher.com/lessons-learned-building-a-continuous-deployment-pipeline-with-docker-docker-compose-and-rancher-part-2/),
and each discovery in the blog chain leads us to a container
orchestration system like those within Rancher as our use cases advance.

### Update Experiments

To experiment and learn more about Rancher upgrades, I’ve put together
a Vagrant rancher setup with three VMs, using Ansible for provisioning.
You can check out the repositories below and follow along on the
experimentation. **Setup** Checkout the repository for
[rancher-vagrant](https://github.com/codesheppard/rancher-vagrant)); make
sure you have [Vagrant](https://www.vagrantup.com/downloads.html), a
virtualization environment such as
[Virtualbox](https://www.virtualbox.org/), and the provisioning tool
[Ansible](https://www.ansible.com/) installed. This will allow us to
setup a VM for our experimentation. The Vagrant setup will include
various nodes, but we can first start off provisioning Rancher server,
followed by a single node.

```
$> cd rancher-vagrant
$> vagrant up rancher
$> vagrant up node1
```

> **Note:** if you suspend the computer or laptop on which the VMs run,
> you may need to run vagrant reload on the VMs to get the static IPs
> working again.

**In Service (Place) Updates** Once the provisioning of the Vagrant
server is complete, the next step is to play with service upgrades
inside Rancher. So we start using the following **docker-compose.yml**.
Lets wait for our localhost Vagrant setup to complete. Once we have our
host setup we should see the following on our Vagrant server node
on **http://192.168.111.111:8080/:** [![Resilient Docker Workloads -
Vagrant](images/rancher_blog_Codesheppard-4-vagrant1-1024x529.png)](https://cdn.rancher.com/wp-content/uploads/2017/01/16144920/Codesheppard-4-vagrant1.png)
Next up, let’s grab some API keys from Rancher; you can check how to do
this from the Rancher on [how to setup
rancher-compose](https://rancher.com/docs/rancher/v1.6/en/cattle/rancher-compose/#setting-up-rancher-compose-with-rancher-server).
Once we can access our new Rancher environment, we can begin setting up
our first stack:

```
mywordpress:
 tty: true
 image: wordpress
 ports:
 - 80:80
 links:
 - database:mysql
 stdin_open: true
database:
 environment:
 MYSQL_ROOT_PASSWORD: pass1
 tty: true
 image: mysql
 volumes:
 - '/data:/var/lib/mysql'
 stdin_open: true
```

Lets start this stack up, and then upgrade it. We launch the stack
through **rancher-compose** command: **Single Host** The first case
is when we upgrade with a single host:

```
rancher-compose up --upgrade mywordpress
```

At first, this does nothing, due to the fact that our service compose
has not changed. The image is the same, and the **docker-compose** has
not had any changes. Checking the **rancher-compose** help, we take a
look at why this might happen:

```
rancher-compose up --help
Usage: rancher-compose up [OPTIONS]

Bring all services up

Options:
--pull, -p Before doing the upgrade do an image pull on all hosts that have the image already
-d Do not block and log
--upgrade, -u, --recreate Upgrade if service has changed
--force-upgrade, --force-recreate Upgrade regardless if service has changed
--confirm-upgrade, -c Confirm that the upgrade was success and delete old containers
--rollback, -r Rollback to the previous deployed version
--batch-size "2" Number of containers to upgrade at once
--interval "1000" Update interval in milliseconds
```

By default, Rancher Compose will not pull an image if the image already
exists on the host. So be sure to either label your container with
`io.rancher.container.pull_image=always` or specify `--pull` on the
upgrade command. Next, let’s try to force an upgrade, since nothing
about our service has actually changed - Rancher is being smart and
ignoring the no-op update.

```
rancher-compose up --force-upgrade mywordpress
INFO[0000] [0/2] [mywordpress]: Starting
INFO[0000] Updating mywordpress
INFO[0000] Upgrading mywordpress
...
```

Even if we CTRL-C the rancher-compose upgrade, once it starts it will
proceed until completion. You can see the UI react to the request:
[![Resilient Docker Workloads -
Upgrading](images/rancher_blog_CodeSheppard-4-upgrading-1024x223.png)](https://cdn.rancher.com/wp-content/uploads/2017/01/16145745/CodeSheppard-4-upgrading.png)
The containers will then enter into an intermediate state on the host
where one container down and a fresh one crops up: [![Resilient Docker
Workloads - Intermediate
State](images/rancher_blog_Codesheppard-4-upgrade-intermediate-state-1024x348.png)](https://cdn.rancher.com/wp-content/uploads/2017/01/16145852/Codesheppard-4-upgrade-intermediate-state.png)
We then clear this state with an explicit command from
**rancher-compose**, or tap it on the UI. At the end of the process, the
old container is removed, and the new one remains.

```
rancher-compose up --upgrade --confirm-upgrade mywordpress
```

Or if something is wrong with the new software, we can then rollback:

```
rancher-compose up --upgrade --rollback mywordpress
```

Once you have confirmed the upgrade, rolling back to the old version is
no longer possible, since the old container is purged from the host by
Rancher. If you have been testing the Wordpress site, you will realize
that since this is the only container on port 80, we won’t be serving
any traffic during the update process. For test environment or
prototyping capacity, this is acceptable, but as we get closer to
production a more reliable upgrade process is desired. Luckily, Rancher
provides a way to start the new containers first before terminating the
old ones. We will just need to modify our **rancher-compose** with the
following flags.

```
mywordpress:
 scale: 1
 upgrade_strategy:
 start_first: true
```

A quick **rancher-compose** update will get us started on the upgrade
process, though if you pay attention what happens is that the new
container never actually starts up. Why is that? If we browse the
container that failed to start, Rancher will eventually propagate an
error.

```
 Error (500 Server Error: Internal Server Error ("driver failed programming external connectivity on endpoint 9315c003-ffc5-4e96-a299-3b9b962490f3 (1daf9cab9e7fd2eabf5aec4995bec015e4cb9373a256380f4d433eb7c54e8428): Bind for 0.0.0.0:80 failed: port is already allocated"))
```

Here we have a port conflict: if we take a look at our
**docker-compose.yml** we will see that the container is started on port
:80, since this is a single host we have clashes on port 80. The error
is not very obvious at first glance, but deployment issues usually
propagate from the lower level issues such as a host port name conflict.
In this case, the new containers will enter into a constant restart
loop. [![Resilient Docker Workloads -
Upgrading](images/rancher_blog_Codesheppard-4-stuck-in-upgrading-1024x144.png)](https://cdn.rancher.com/wp-content/uploads/2017/01/16150224/Codesheppard-4-stuck-in-upgrading.png)
Clearly, this method of hosting on a single container on port 80
doesn’t scale. Lets replace it with a loadbalancer on port 80, then
restart again!

```
mywordpress:
 tty: true
 image: wordpress
 links:
 - database:mysql
 stdin_open: true
database:
 environment:
 MYSQL_ROOT_PASSWORD: pass1
 tty: true
 image: mysql
 volumes:
 - '/data:/var/lib/mysql'
 stdin_open: true
wordpresslb:
 ports:
 - 80:80
 tty: true
 image: rancher/load-balancer-service
 links:
 - mywordpress:mywordpress
 stdin_open: true
```

If we SSH into our vagrant host, we can also run Docker to view the
containers running inside the VM:

```
$> vagrant ssh node1
$> vagrant@vagrant:$ sudo docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
10ae46afa471 rancher/agent-instance:v0.8.3 "/etc/init.d/agent-in" 33 minutes ago Up 33 minutes 0.0.0.0:80->80/tcp 268c0107-78d2-4e77-8bd4-efef4a151881
b360e6c6e535 wordpress:latest "docker-entrypoint.sh" 33 minutes ago Up 33 minutes 80/tcp 87a7cdb0-2277-4469-8784-4e6adb76897e
f873ab956fc3 wordpress:latest "docker-entrypoint.sh" 33 minutes ago Up 33 minutes 80/tcp b3903acf-462c-4817-be9c-b749f9df5a57
298aa4a36ec2 mysql:latest "docker-entrypoint.sh" 33 minutes ago Up 33 minutes 3306/tcp 861d3664-0db7-4b15-a1a9-9fb5f27f0722
1c6c3f9562e2 rancher/agent-instance:v0.8.3 "/etc/init.d/agent-in" 58 minutes ago Up 58 minutes 0.0.0.0:500->500/udp, 0.0.0.0:4500->4500/udp 543a11ee-7285-44f8-8c7a-462c36fc5fbb
02b4efc61913 rancher/agent:v1.0.2 "/run.sh run" 42 hours ago Up About an hour rancher-agent
```

###

### Rolling Upgrade

There is another type of upgrade that is not supported in the Rancher
UI: the [rolling
upgrade](https://rancher.com/docs/rancher/v1.6/en/cattle/upgrading/#rolling-upgrade).
This method of upgrades allows one service to completely replace
another. We take a look at how it works in Rancher. > The recommended
in-service upgrade allows you to stop the old containers and start new
containers in the same service name. An in-service upgrade is the only
type of upgrade supported in the UI, and it is also supported in Rancher
Compose. The terminology for service is the single unit in the
**docker-compose.yml** file found in Rancher. In this case, it is for
the Wordpress service. We first add the new **mywordpressv2** that we
want to roll towards:

```
...
mywordpressv2:
 tty: true
 image: wordpress
 links:
 - database:mysql
 stdin_open: true
...
```

The command to perform a service replacement is **rancher-compose
upgrade**. Taking a look at the help menu, we can get a brief idea of
the options presented to us:

```
Usage: rancher-compose upgrade [OPTIONS]

Perform rolling upgrade between services

Options:
 --batch-size "2" Number of containers to upgrade at once
 --scale "-1" Final number of running containers
 --interval "2000" Update interval in milliseconds
 --update-links Update inbound links on target service
 --wait, -w Wait for upgrade to complete
 --pull, -p Before doing the upgrade do an image pull on all hosts that have the image already
 --cleanup, -c Remove the original service definition once upgraded, implies --wait
```

Test the upgrade command with one command:

```
$> rancher-compose upgrade mywordpress mywordpressv2
INFO[0000] Upgrading mywordpress to mywordpressv2, scale=2
```

This returns our mywordpressv2 installation from zero containers to 2,
while our mywordpress containers went from 2 to zero. All the while the
links on the loadbalancer are being updated to point to the new service
by default through [inbound link
updates](https://rancher.com/docs/rancher/v1.6/en/cattle/upgrading/#updating-inbound-links).
[![Resilient Docker Workloads - Rolling
upgrades](images/rancher_blog_Codesheppard-4-rollupgrade-1024x159.png)](https://cdn.rancher.com/wp-content/uploads/2017/01/16150947/Codesheppard-4-rollupgrade.png)
If we’d like, we also have the option to go back to the old services
with new scale:

```
$> rancher-compose upgrade mywordpressv2 mywordpress --scale 5
```

Our new service has now been started with five containers. With more
tinkering, we look at what happens when we try to upgrade back to the
new service.

```
$> rancher-compose upgrade mywordpress mywordpressv2 --scale 2
FATA[0000] Action [upgrade] not available on [...]
```

After a bit of digging, it looks like there are certain state
restrictions on services trying to perform an update. From the Rancher
code on Cattle, we can see the various states that a service can be in.
> Rancher-compose will not let you update a service that is awaiting
upgrade confirmation. There are restrictions on what state a service can
be in to perform upgrades. We had to go to the UI to confirm the update
on mywordpress from our first upgrade before we can revert back to the
old service. Lastly, we can automatically opt to clean up the
mywordpressv2 service with the following command. Otherwise the old
service will remain with a scale of 0. If we are sure that we need to
cleanup the services as we perform the rolling upgrade, we can attach
the --cleanup flag to remove the old service.

```
$> rancher-compose upgrade service1 service2 --cleanup
```

### Multiple Hosts

Traditionally, with virtual machines (VMs) we deploy one application per
VM and some supporting software, but we sometimes wonder when using
containers makes sense in an organization. In a summary of an blog post
by Docker on [VMs or
Containers](https://blog.docker.com/2016/05/vm-or-containers/), there’s
three main use cases.

- A new application that the team commits to writing in a microservice
  architecture. The team can share containers so other developers can
  test against the latest services on their development stations.
- Wrap a monolith inside a docker container, then break off components
  into docker containers as the team works to break it up into
  microservices.
- Using containers for their portability, once an application is made
  for containers. It is much easier to run a containers across various
  Cloud Providers than it would be to try to port VM images.

Containers can better utilize a few powerful hosts to run multiple
applications on the same host. From the linked blog:

“Though one can think of the analogy between a house (VM) with
apartments (Containers).

To me, the light bulb moment came when I realized that Docker is not a
virtualization technology, it’s an application delivery technology. In
a VM-centered world, the unit of abstraction is a monolithic VM that
stores not only application code, but often its stateful data. A VM
takes everything that used to sit on a physical server and just packs it
into a single binary so it can be moved around. With containers, the
abstraction is the application; or more accurately, a service that helps
to make up the application.”

To facilitate the concept that Docker is an application delivery
technology, container orchestration frameworks like those within Rancher
(including Mesos and Kubernetes) provide host clustering, scheduling and
network management to manage our containers in support of our
application. They abstract the mechanisms needed, so that multiple
smaller hosts look like one large environment. While containers can act
like VMs that can package an OS as its base layer, they’re generally a
problem to manage once they scales to large numbers; If we launch fifty
containers on a host, every container carries unnecessary bloat.
Containers should just run one process and be kept simple for the best
mileage. Once we have simple containers that run one specific process,
we can more easily know the constraints on its runtime, such as CPU
limit, memory limit, and enforce them as explained in the [Docker Run
manual](https://docs.docker.com/engine/reference/run/#/runtime-constraints-on-resources).
This block of memory, CPU, and data bundle can then be scheduled into
any host in the cluster with available space. Ideally, the
infrastructure won’t need to know what is running in the container, and
the container’s code won’t worry about whether the host can support
it. The Rancher container scheduler will move containers around based on
metrics for CPU, available memory, and other parameters. If your
services are tied to specific ports and host IPs, upgrading requires
more flags on the scheduler. Let’s begin setting up our multiple node
environment by spinning up the second node on our Vagrant Rancher
cluster.

```
$> vagrant up node2
```

### Updates with Multiple Hosts

Running our update script again, we can now see that that the scheduler
has started placing containers on the other host!

```
$> rancher-compose up --upgrade --force-upgrade -d mywordpress
```

[![Resilient Docker workloads - scheduler
experiment](images/rancher_blog_Codesheppard-4-scheduler-experiment-1024x828.png)](https://cdn.rancher.com/wp-content/uploads/2017/01/16151711/Codesheppard-4-scheduler-experiment.png)
Now since we have our stack hooked up to a load-balancer, Rancher routes
the traffic within Rancher’s overlay network. Our load-balancer on
node1 can then proxy request to containers on node2. However, when this
network connection is disrupted, in-place upgrades can display
inconsistent behavior. In our next installment, we’ll pick up next by
common problems encountered with updates. Stay tuned! *Nick Ma is an
Infrastructure Engineer who blogs about Rancher and Open Source. You can
visit Nick’s blog, [CodeSheppard.com](http://codesheppard.com/), to
catch up on practical guides for keeping your services sane and reliable
with open-source solutions.*
