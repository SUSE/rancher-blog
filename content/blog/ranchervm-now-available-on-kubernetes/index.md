---
title: "RancherVM Now Available on Kubernetes"
date: 2018-04-27T09:02:00
slug: "ranchervm-now-available-on-kubernetes"
author: "Rancher Admin"
products: ["Other"]
tags: ["virtualization"]
content_type: "release"
draft: true
migration:
  wp_id: 85813
  original_url: "https://www.suse.com/c/rancher_blog/ranchervm-now-available-on-kubernetes/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RancherVM project discontinued"
  redirect_target: "/harvester"
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher. [Sign up here](https://rancher.com/training/) Since we launched RancherVM project a couple of years ago, we have received a lot of positive feedback from users. One enhancement many users wanted is VM management on a cluster of nodes. Today we are excited to announce a port of [RancherVM](http://github.com/rancher/vm) to Kubernetes. We’ve added resource scheduling, a browser-based VNC client, IP address discovery, key-based authentication, and an updated user interface.*Watch James Oliver, Rancher’s Tools and Automation Engineer, demo RancherVM.*

## Design

Under the covers, RancherVM makes heavy use of Docker containerization and container registries. Virtual machine base images are packaged as Docker images and published to any Docker registry. RancherVM ships with some of the more popular OS images stored in [Docker Hub](https://hub.docker.com/). As a user, you may choose between a variety of public and private registries, or even [run your own private registry](https://docs.docker.com/registry/deploying/).

Each virtual machine now runs inside a Kubernetes pod, which we call a VM Pod. A Kubernetes controller manages the vm pod’s lifecycle, granting users the ability to boot or shut down a vm, modify CPU and memory allocated to a machine, and more.

### Persistence

The RancherVM system defines its own Custom Resource Definitions (CRDs) and stores all state within them. Consequently, RancherVM does not require a persistent datastore beyond what Kubernetes requires to run. A REST server exposes endpoints for performing CRUD operations on these CRDs. An updated UI consumes the REST server to provide an improved user experience.

### Scheduling

We now take advantage of Kubernetes scheduler to intelligently place vm pods across many nodes. CPU and memory resource limits ensure that vm pods are safely scheduled onto hosts with sufficient resources. Depending on the size of the nodes, 100+ vm pods on a single host is achievable. There is no extra overhead for scheduling virtual machines; scalability limitations should be dictated by Kubernetes itself. In practice, we’ve seen evidence of 1000+ node clusters.

### Networking

RancherVM uses bridged networking to provide connectivity to guest VMs. Every VM pod retains its network identity by persisting its assigned MAC address to its VirtualMachine CRD. An external DHCP server is required for IP address management. A VM pod’s IP may still change if shut down long enough for the DHCP lease to expire.

A controller runs on every node to resolve MAC addresses to external DHCP-assigned IP addresses. Cloud providers don’t typically do this because they perform their own IP Address Management (IPAM) by implementing a DHCP server. This enables us to bridge networks where we don’t control the DHCP server or add instrumentation inside of the virtual machines.

There are some inherent scalability limitations to this design - the network you bridge must be of sufficient size to provide a unique IP address to each VM.

## Usage

RancherVM requires a running Kubernetes cluster with nodes running Debian-based operating systems and [KVM](https://www.linux-kvm.org/page/Main_Page) installed.

Run this one command to deploy RancherVM components into your Kubernetes cluster.

```
kubectl create -f https://raw.githubusercontent.com/rancher/vm/master/hack/deploy.yaml
```

### GUI

After deployment, you can find the UI endpoint by querying for the frontend Kubernetes service:

```
$ kubectl -n ranchervm-system get svc
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
ranchervm-backend    ClusterIP   10.102.148.5    <none>        9500/TCP         5m
ranchervm-frontend   NodePort    10.104.55.231   <none>        8000:30874/TCP   5m
```

Now you can access the UI by navigating to `<node_ip>:30874`.

You will want to add your public key to enable SSH remote access. On the `Credentials` screen, click `Create`. Add your public key and give it a good name. Click `OK`.

![Add Public Key](https://s3-us-west-1.amazonaws.com/ranchervm/temp/add-pubkey.png)

Creating instances is pretty straightforward. On the `Instances` screen, click `Create`. You are presented with a form to fill out. You will either need to add your public key or enable NoVNC webserver. Click `OK`. That’s it!

![Create Instance](https://s3-us-west-1.amazonaws.com/ranchervm/temp/create-instance.png)

After some time, you can see the virtual machines are running and have been assigned an IP address.

![Instance List](https://s3-us-west-1.amazonaws.com/ranchervm/temp/instance-list.png)

You may now connect to the machine via SSH with your private key. The username is specific to the operating system you deployed. Ubuntu user is `ubuntu`, CentOS user is `centos`, Fedora user is `fedora`, etc.

For security reasons, password-based SSH is disabled by default. If you chose to forego adding a public key to your virtual machine specification, you will need to use NoVNC to access the machine. Click the NoVNC button to open an in-browser console. For the images we provide, username `rancher` and password `rancher` should work.

The dashboard provides a summary of the CRDs currently in your system.

![Dashboard](https://s3-us-west-1.amazonaws.com/ranchervm/temp/dashboard.png)

### CLI

For those with `kubectl` experience, the system may be managed from the command line by manipulating CRDs. Provided are some examples for adding credentials and virtual machines to the system from the command line.

Not all modifications will have an immediate effect; stopping and starting your VM may be required to reflect some specification changes such as CPU / memory allocation changes.

## What’s Next

In the coming weeks, we will add support for [live migration](https://en.wikipedia.org/wiki/Live_migration). Whether an existing virtual machine’s resource requirements surpass what is available on the physical host or an operator has scheduled maintenance that requires interrupting host execution, moving a running virtual machine to another host transparent to the end user is of critical importance.

We are also considering integration with replicated block storage systems such as [Longhorn](https://github.com/rancher/longhorn).

RancherVM is open source software and free for anyone to use. Development is ongoing as we find time. Feel free to contact us through [GitHub issues](https://github.com/rancher/vm/issues) with any questions or suggestions. Thank you!

### James Oliver

Tools and Automation Engineer

[Github](https://github.com/LLParse)

![James Oliver](https://s3-us-west-1.amazonaws.com/ranchervm/temp/james-oliver-200x200.jpg)Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher. [Sign up here](https://rancher.com/training/)
