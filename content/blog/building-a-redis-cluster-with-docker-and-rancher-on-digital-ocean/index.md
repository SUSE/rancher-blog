---
title: "Building a Redis Cluster with Docker and Rancher on Digital Ocean"
date: 2015-01-29T10:18:00
slug: "building-a-redis-cluster-with-docker-and-rancher-on-digital-ocean"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["storage"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86682
  original_url: "https://www.suse.com/c/rancher_blog/building-a-redis-cluster-with-docker-and-rancher-on-digital-ocean/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Docker and Rancher 1.x Redis tutorial"
  redirect_target: "rancher.com/blog (hub)"
---

*Hussein Galal is a Linux System Administrator, with experience in
Linux, Unix, Networking, and open source technologies like Nginx,
Apache, PHP-FPM, Passenger, MySQL, LXC, and Docker. You can follow
Hussein
on Twitter [@galal\_hussein](http://twitter.com/galal_hussein).*

I recently used Docker and Rancher to set up a Redis
cluster on Digital Ocean. Redis clustering provides a
way to share data across multiple Redis instances, keys are distributed
equally across instances using hash slots.
Redis clusters provide a number of nice features, such as data
resharding and availability between instances.

Availability is provided using Redis replication, where
each master instance has a slave instance which replicate its data, for
more information about redis cluster, see [Redis cluster official
documentation.](https://redis.io/topics/cluster-tutorial)

In this post, I will setup and configure a Redis cluster on the same
host, and I will setup and configure a Redis cluster on Docker instances
on different hosts using Rancher. I’ll explain the limitations of
using a single host to setup the Redis cluster without using
Rancher.

### Why Rancher?

First, Rancher provides me a set of features to help manage
docker containers beyond a single host. Second, and more importantly,
it provides an overlay network that would allow my Docker containers to
more easily communicate across hosts. In essence, Rancher provides a
virtual private network for the registered hosts and will allow Docker
containers to communicate under the same subnet:

Without Rancher, hosts running Docker containers will be isolated from
each other, therefore Docker containers can only communicate with each
other through the public ip’s of the hosts of different cloud service
providers.

### []Prerequisites Of The Setup

1. Digital Ocean Account: To create the instances which we
   will register with Rancher.
2. Docker installed: To be able to create and manage Docker
   instances.
3. Docker Hub Account: To be able to push your Redis image,
   as we will see later in the post.

That is all you need to begin the setup, I will create 7
Digital Ocean instances (with
Docker 1.4 installed), each Digital Ocean instance will
contain one Docker instance, of course you can create the
whole cluster inside one or two Digital Ocean virtual
machines, but I am using multiple machines to
ensure the highest availability possible between Redis instances.

Redis clustering can not be started unless 6 Redis instances join the
cluster. The 7th machine is for the installing
Rancher.

### []Installing Rancher

First create a Digital Ocean machine to install Rancher on, login to
your Digital Ocean account and click create droplet.

After that make sure to select Docker 1.4 under
Applications:

To install Rancher, ssh login to the machine and run this command:

```
$ssh root@104.236.253.116
root@Rancher-io-Mngmt:~#docker run -d --name rancher-server -p 8080:8080 rancher/server
```

This command will create a Docker instance
with a Rancher server that listens on port
8080 and proxy that port to port 8080 on the host. After
running that command wait a few minutes
until the server is ready, To make sure that the
server is running type this command:

```
root@Rancher-io-Mngmt:~# docker logs rancher-server
```

You should see something like the following
output:

```
 20:02:41.943 [main] INFO  ConsoleStatus - [DONE ] [68461ms] Startup Succeeded, Listening on port 8080
```

Now access this machine on port 8080:
http://104.236.253.116:8080

### Register Digital Ocean’s instances With Rancher

Once Rancher is up and running, create 6 Digital Ocean
Instances, and then ssh login to each instance and run
this command:

```
 root@Rancher-Test-Instance-X# docker run -it --privileged -v /var/run/docker.sock:/var/run/docker.sock rancher/agent http://104.236.253.116:8080
```

where 104.236.253.116 is the ip address of the
managment instance.

This will register the 6 machines on Rancher. Once this is finished,
you will see the following when you access the Rancher management
instance:

### Creating Redis Docker Image

Now for the Redis cluster part, I created a Docker image of the Redis
cluster container, here is the Dockerfile of the
image:

```
From ubuntu:14.04
MAINTAINER hussein-galal hussein.galal.ahmed.11@gmail.com
ENV CACHE_FLAG 0
# Install and Upgrade the System
RUN apt-get update
RUN apt-get upgrade -yqq
# Install the dependencies
RUN apt-get install -yqq build-essential gcc g++ openssl wget curl git-core libssl-dev libc6-dev ruby
# Clone the Unstable Version of redis that contains redis-cluster
RUN git clone -b 3.0 https://github.com/antirez/redis.git
# Install Redis and its Tools
WORKDIR /redis
RUN make
RUN gem install redis
# Add the Configuration of the cluster
ADD conf/redis.conf redis.conf
ADD run.sh /run.sh
ENV REDIS_NODE_PORT=7000
ENTRYPOINT ["/bin/bash","/run.sh"]
```

Lets go through this Dockerfile line by line:

- The first 3 lines say that we will going to use Ubuntu 14.04 as our
  base image, the name of the maintainer of this Docker file, and
  finally the cached flag which we will change if we want to rebuild
  the image and not use the cached one.

- The following two lines are used to update the apt cache, and
  upgrade the system by installing the latest updates.

```
RUN apt-get update
RUN apt-get upgrade -yqq
```

- This line will install the packages we will need to compile Redis
  and install its tools.

```
RUN apt-get install -yqq build-essential gcc g++ openssl wget curl git-core libssl-dev libc6-dev ruby
```

- The following line will download the Redis source code from the
  official GitHub repo, note that we installed the 3.0 version which
  is the unstable version but it is the version that implements the
  Redis cluster.

```
RUN git clone -b 3.0 https://github.com/antirez/redis.git
```

- The following 3 lines will change the current directory
  to redis/ directory, then compile the Redis
  source code, and finally will install the Redis client gem which
  contains the Redis cluster tools that we will use.

```
WORKDIR /redis
RUN make
RUN gem install redis
```

- The following 4 lines will copy the configuration file and the
  running script to the Docker image, then assign
  REDIS\_NODE\_PORT variable to 7000, and finally
  execute the script as the entrypoint of the image.

```
ADD conf/redis.conf redis.conf
ADD run.sh /run.sh
ENV REDIS_NODE_PORT=7000
ENTRYPOINT ["/bin/bash","/run.sh"]
```

Now lets take a look at the configuration file and the running
script:

```
redis.config
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
```

This simple configuration file will do the following:

- Enable the cluster mode for the Redis image.
- Define the configuration file of Redis cluster.
- Set the timeout for each Redis server to 5000.

```
/run.sh
#Running Redis Cluster Node
./src/redis-server /redis/redis.conf --port $REDIS_NODE_PORT
```

This line will start the Redis server with the custom configuration we
just made, and bind it to the port we defined in the Dockerfile.

Now you can build this image and then push it to the Docker Hub to be
able to use it with Rancher:

```
~/redis_cluster_node# docker build -t husseingalal/redis_cl_node
~/redis_cluster_node# docker push husseingalal/redis_cl_node
```

Now you will be asked to login to your Docker Hub account, after login,
the Docker image will be pushed successfully.

### Create The Redis Cluster With Rancher

Now I can create a Docker container on each of the Digital Ocean
machine’s we registered early on Rancher, by clicking create
container in the Rancher UI:

Rancher will open a dialog window where you can choose the
options for the Docker containers you will
create.

As you can see, I named the container to be Redis\_node1, at set the Source Image to pull the image we
just created (husseingalal/redis\_cl\_node).

At Network, choose “Manage Network on
docker0”, this will enable one of the unique features of
Rancher which allows the Docker containers to communicate with each
other as if they are in the same network, I will explain this feature
later in the post.

Make sure to choose no at the Console option.

Now on the left bar, choose Ports:

This panel will let us export and proxy any port on
the Docker machine to the host dynamically, and since we use a Docker
instance on each Digital Ocean machine, we can export the port 7000 on
each Docker instance we create.

After that click Create.

I repeated the previous step for
each machine we registered with Rancher, now you should see
something like this:

You can see that on each Digital Ocean instance a Network
Agent container was created automatically by Rancher, that
was the result of choosing to manage the network on docker0.

Rancher implements IPsec tunneling through registered hosts to create a
virtual private network between the hosts.

Another nice feature is using the shell, if you click
on the terminal icon besides each container it will open a shell to the
container, you can use this shell to debug and tweak any configuration
on each container.

### Start The Cluster

Now all the cluster nodes are up and running, but we need to start the
cluster. To start the cluster we will use the
./redis-trib.rb to start the cluster.

Now open a shell at any redis instance, run the following command:

```
root@607b1c92d2b3:/redis# cd src
root@607b1c92d2b3:/redis#./redis-trib.rb create --replicas 1 10.42.251.230:7000 10.42.27.151:7000 10.42.27.160:7000 10.42.138.181:7000 10.42.11.78:7000 10.42.151.100:7000
```

Those ips are the ips of the Redis Docker instances we just created,
note that all the ips in the same local network, due to the
IPsec tunneling that Rancher created.

Now you should see that output which indicates that the cluster up and
running:

```
>>> Creating cluster
Connecting to node 10.42.251.230:7000: OK
Connecting to node 10.42.27.151:7000: OK
Connecting to node 10.42.27.160:7000: OK
Connecting to node 10.42.138.181:7000: OK
Connecting to node 10.42.11.78:7000: OK
Connecting to node 10.42.151.100:7000: OK
>>> Performing hash slots allocation on 6 nodes...
Using 3 masters:
10.42.251.230:7000
10.42.27.151:7000
10.42.27.160:7000
Adding replica 10.42.138.181:7000 to 10.42.251.230:7000
Adding replica 10.42.11.78:7000 to 10.42.27.151:7000
Adding replica 10.42.151.100:7000 to 10.42.27.160:7000
M: 14de36d31c2e40f4d5419690e18b7c529d254071 10.42.251.230:7000
   slots:0-5460 (5461 slots) master
M: 9f33e772ccb4163b56ffa1bb92a51b60bc4b3744 10.42.27.151:7000
   slots:5461-10922 (5462 slots) master
M: dffd80171644a3d510d879ec6f988329774defef 10.42.27.160:7000
   slots:10923-16383 (5461 slots) master
S: 0047ea05b59c7b47cc77ac3a6b7356776e104fb8 10.42.138.181:7000
S: e7cf1d84e72a0dc42677abe618a2c0bf3fafc927 10.42.11.78:7000
   replicates 9f33e772ccb4163b56ffa1bb92a51b60bc4b3744
S: d91c05946fd96abd3f1784b9447c7db71100fecf 10.42.151.100:7000
   replicates dffd80171644a3d510d879ec6f988329774defef
Can I set the above configuration? (type 'yes' to accept): yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join........
>>> Performing Cluster Check (using node 10.42.251.230:7000)
M: 14de36d31c2e40f4d5419690e18b7c529d254071 10.42.251.230:7000
   slots:0-5460 (5461 slots) master
M: 9f33e772ccb4163b56ffa1bb92a51b60bc4b3744 10.42.27.151:7000
   slots:5461-10922 (5462 slots) master
M: dffd80171644a3d510d879ec6f988329774defef 10.42.27.160:7000
   slots:10923-16383 (5461 slots) master
M: 0047ea05b59c7b47cc77ac3a6b7356776e104fb8 10.42.138.181:7000
   slots: (0 slots) master
   replicates 14de36d31c2e40f4d5419690e18b7c529d254071
M: e7cf1d84e72a0dc42677abe618a2c0bf3fafc927 10.42.11.78:7000
   slots: (0 slots) master
   replicates 9f33e772ccb4163b56ffa1bb92a51b60bc4b3744
M: d91c05946fd96abd3f1784b9447c7db71100fecf 10.42.151.100:7000
   slots: (0 slots) master
replicates dffd80171644a3d510d879ec6f988329774defef
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
```

And voila, the cluster is up and running.

### []Seting up Redis Cluster Using Single Host

Using single host to hold the redis cluster will expose some of
the limitations that Rancher resolves.

To set up a redis cluster on a single host, create a Digital Ocean
machine with Docker 1.4 installed, and execute the following
commands:

```
# docker pull husseingalal/redis_cl_node
# docker run -d --name redis_node_1 -p 7000:7000 husseingalal/redis_cl_node
# docker run -d --name redis_node_2 -p 7001:7000 husseingalal/redis_cl_node
# docker run -d --name redis_node_3 -p 7002:7000 husseingalal/redis_cl_node
# docker run -d --name redis_node_4 -p 7003:7000 husseingalal/redis_cl_node
# docker run -d --name redis_node_5 -p 7004:7000 husseingalal/redis_cl_node
# docker run -d --name redis_node_6 -p 7005:7000 husseingalal/redis_cl_node
```

To know the private ips of the redis nodes, you
should use Docker inspect:

```
#docker inspect redis_node_X | grep "IPAddress"
```

Where X is the number of the node, then to
start the cluster, we should install Redis tools and use
the redis-trib.rb script under the
src directory of the source code:

```
# git clone -b 3.0 https://github.com/antirez/redis.git
# apt-get update && apt-get install ruby
# gem install redis
# cd redis/src
# ./redis-trib.rb create --replicas 1 172.17.0.2:7000 172.17.0.4:7000 172.17.0.5:7000 172.17.0.6:7000 172.17.0.7:7000 172.17.0.8:7000
```

Now we should see the same output we saw earlier using Rancher, but now
we will be exposed to several limitations:

- High Availability feature is now missing, and if the Digital Ocean
  machine goes down all of our cluster will go down and fail.

- We can’t use the private ips of the Docker containers to setup a
  full stack application, we can only use the public ip of the Digital
  Ocean machine with the different ports of the Redis
  containers.

That’s why Rancher’s cross container networking is so useful. It
allows me to launch the Redis instances spread across multiple hosts,
ultimately providing HA capability for the Redis cluster.

### Conclusion

In this post we installed Rancher to create a Redis cluster, we
registered 6 machines with Rancher, and on each machine we created a
custom Redis Docker container, and finally we ran the cluster using the
redis-trib.rb command. Using Rancher, we were able
to create a private network for communication between the clustered
Redis machines.

If you’re interested in learning more, please schedule a demo of
Rancher.

*Hussein Galal is a Linux System Administrator, with experience in
Linux, Unix, Networking, and open source technologies like Nginx,
Apache, PHP-FPM, Passenger, MySQL, LXC, and Docker. You can follow
Hussein
on Twitter [@galal\_hussein](http://twitter.com/galal_hussein).*
