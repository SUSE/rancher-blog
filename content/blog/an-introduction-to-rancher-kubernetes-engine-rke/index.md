---
title: "An Introduction to Rancher Kubernetes Engine (RKE)"
date: 2017-11-29T09:00:00
slug: "an-introduction-to-rancher-kubernetes-engine-rke"
author: "Rancher Admin"
products: ["RKE1"]
tags: ["installation"]
content_type: "explainer"
draft: true
migration:
  wp_id: 85793
  original_url: "https://www.suse.com/c/rancher_blog/an-introduction-to-rancher-kubernetes-engine-rke/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RKE1 end of life"
  redirect_target: "/rke2"
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)

Kubernetes installation is considered one of the toughest problems for
operators and DevOps. Because Kubernetes can run on various platforms
and operating systems, there are so many factors that should be
considered during the installation process. In this post, I am going to
introduce a new, lightweight tool for installing Kubernetes that
supports installation on bare-metal and virtualized servers. Rancher
Kubernetes Engine (RKE) is a Kubernetes installer written in Golang.
It’s easy to use and doesn’t require a lot of preparation from the user
to get started.

## RKE Installation

You can install RKE from the official [GitHub
repository](https://github.com/rancher/rke/releases). You can run RKE
from both Linux and MacOS machines. After installation, run the
following code to make sure that you have the latest version:

```
./rke --version
rke version v0.0.6-dev

./rke --help
NAME:
   rke - Rancher Kubernetes Engine, Running kubernetes cluster in the cloud

USAGE:
   rke [global options] command [command options] [arguments...]

VERSION:
   v0.0.6-dev

AUTHOR(S):
   Rancher Labs, Inc.

COMMANDS:
     up              Bring the cluster up
     remove          Teardown the cluster and clean cluster nodes
     version         Show cluster Kubernetes version
     config, config  Setup cluster configuration
     help, h         Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --debug, -d    Debug logging
   --help, -h     show help
   --version, -v  print the version
```

## RKE Prerequistes

RKE is a container-based installer, which means it requires Docker to be
installed on the remote server, and it currently requires Docker version
1.12 to be installed on the servers. RKE works by connecting to each
server via SSH and setting up a tunnel to the Docker socket on this
server, which means that the SSH user must have access to the Docker
engine on this server. To enable access to the SSH user, you can add
this user to the Docker group:

```
usermod -aG docker
```

These are the only preparations the remote servers require to start the
Kubernetes installation.

## Getting Started

This example assumes that the user provisioned three servers:

```
node-1: 192.168.1.5
node-2: 192.168.1.6
node-3: 192.168.1.7
```

### The Cluster Config File

By default, RKE looks for a file called **cluster.yml**, which contains
information about the remote servers and services that will run on
servers. The minimum file should look like this:

```
---
nodes:
  - address: 192.168.1.5
    user: ubuntu
    role: [controlplane]
  - address: 192.168.1.6
    user: ubuntu
    role: [worker]
  - address: 192.168.1.7
    user: ubuntu
    role: [etcd]

services:
  etcd:
    image: quay.io/coreos/etcd:latest
  kube-api:
    image: rancher/k8s:v1.8.3-rancher2
  kube-controller:
    image: rancher/k8s:v1.8.3-rancher2
  scheduler:
    image: rancher/k8s:v1.8.3-rancher2
  kubelet:
    image: rancher/k8s:v1.8.3-rancher2
  kubeproxy:
    image: rancher/k8s:v1.8.3-rancher2
```

The cluster configuration file contains a nodes list. Each node should
contain at least these values:

- **Address** — The SSH IP/FQDN of the server
- **User** — An SSH user to connect to the server
- **Role** — A list of the host roles: worker, controlplane, or etcd

The other section is Services, which contains information about the
Kubernetes components that will be deployed on the remote servers. There
are three types of roles for which a host can be used:

- **etcd** — These host(s) can be used to hold the data for the
  cluster.
- **controlplane** — These hosts(s) can be used to hold the
  Kubernetes API server and other components that are required to run
  K8s.
- **worker** These are the hosts on which your applications can
  deploy.

### Running RKE

To run RKE, make sure to have **cluster.yml** in the same directory and
run:

```
➜ ./rke up
```

To point to the other configuration file, run:

```
➜ ./rke up --config /tmp/config.yml
```

You should see output like this:

```
➜ ./rke up --config cluster-aws.yml
INFO[0000] Building Kubernetes cluster
INFO[0000] [ssh] Checking private key
INFO[0000] [ssh] Start tunnel for host [192.168.1.5]
INFO[0000] [ssh] Start tunnel for host [192.168.1.6]
INFO[0000] [ssh] Start tunnel for host [192.168.1.7]
INFO[0000] [certificates] Generating kubernetes certificates
INFO[0000] [certificates] Generating CA kubernetes certificates
INFO[0000] [certificates] Generating Kubernetes API server certificates
….

INFO[0075] [addons] User addon deployed successfully..
INFO[0075] Finished building Kubernetes cluster successfully
```

### Connecting to the Cluster

RKE will deploy a local file in the same directory that has the config
file, which contains kube config information to connect to the newly
generated cluster. By default, the kube config file is called
`.kube_config_cluster.yml`. Copy this file to your local
**~/.kube/config** to start using `kubectl` locally. Note that the
deployed local kube config name is relative to the cluster config file.
For example, if you used a config filed called *mycluster.yml*, the
local kube config will be named *.kube\_config\_mycluster.yml*.

```
➜ kubectl get nodes
NAME                   STATUS    ROLES     AGE
192.168.1.5         Ready     master    4m        v1.8.3-rancher1
192.168.1.6         Ready         4m        v1.8.3-rancher1
```

## A Peek Under the Hood

RKE uses the **x509** authentication method by default to set
authentication between Kubernetes components and for users too. RKE
first generates certificates for every component and for the user
components as well.

```
INFO[0000] [certificates] Generating kubernetes certificates
INFO[0000] [certificates] Generating CA kubernetes certificates
INFO[0000] [certificates] Generating Kubernetes API server certificates
INFO[0000] [certificates] Generating Kube Controller certificates
INFO[0000] [certificates] Generating Kube Scheduler certificates
INFO[0000] [certificates] Generating Kube Proxy certificates
INFO[0001] [certificates] Generating Node certificate
INFO[0001] [certificates] Generating admin certificates and kubeconfig
INFO[0001] [certificates] Deploying kubernetes certificates to Cluster nodes
```

After generating certificates, RKE deploys the generated certificates to
**/etc/kubernetes/ssl** to the servers and saves the local kube config
file, which contains the master user certificate and can be used later
with RKE to remove or upgrade the cluster. RKE then deploys each service
component as containers that can communicate with each other. RKE also
saves the cluster state in Kubernetes as a config map for later use. RKE
is an idempotent tool that can run several times, generating the same
output. It can also deploy one of the following network plugins:

- Calico
- Flannel (default)
- Canal

To use different network plugins, you can specify that in the config
file:

```
network:
  plugin: calico
```

## Add-ons

RKE supports pluggable add-ons on cluster bootstrap. Users can specify
the add-on YAML in the **cluster.yml** file. RKE deploys the add-ons
YAML after the cluster starts. RKE first uploads this YAML file as a
config map in the Kubernetes cluster and then runs a Kubernetes job that
mounts this config map and deploys the add-ons.

> Note that RKE doesn’t yet support the removal of add-ons. Once they
> are deployed the first time, you can’t change them using RKE.

To start using add-ons, use the `addons:` option in the cluster config
file. For example:

```
addons: |-
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-nginx
      namespace: default
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80
```

Note that we are using `|-</code because addons` is a multi-line string
option, in which you can specify multiple YAML files and separate them
with `---`.

## High Availability

The RKE tool is HA ready. You can specify more than one control plane
host in the cluster config file, and RKE will deploy master components
on all of them. By default, the kubelets are configured to connect to
127.0.0.1:6443, which is the address of nginx-proxy service that proxies
requests to all master nodes. To start an HA cluster, specify more than
one host with the role `controlplane`, and start the cluster normally.

## Adding/Removing Nodes

RKE supports adding/removing nodes for `worker` and `controlplane`
hosts. To add additional nodes, you need to update only the cluster
config file with additional nodes and run the cluster config with the
same file. To remove nodes, just remove them from the nodes list in the
cluster configuration file, and re-run the `rke up` command.

## The Cluster Remove Command

RKE supports the `rke remove` command. The command does the following:

- Connects to each host and removes the Kubernetes services deployed
  on it.
- Cleans each host from the directories left by the services:
  - /etc/kubernetes/ssl
  - /var/lib/etcd
  - /etc/cni
  - /opt/cni

Note that this command is irreversible and will destroy the Kubernetes
cluster entirely. For more information about RKE,
[register](https://info.rancher.com/november-2017-meetup) for our Online
Meeting tomorrow. We hope you can join us!

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)
