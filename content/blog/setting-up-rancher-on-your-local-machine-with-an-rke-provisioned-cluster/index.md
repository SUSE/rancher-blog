---
title: "Setting up Rancher on Your Local Machine with an RKE Provisioned Cluster"
date: 2021-08-31T18:42:35
slug: "setting-up-rancher-on-your-local-machine-with-an-rke-provisioned-cluster"
author: "SUSE"
products: ["RKE1"]
tags: ["installation"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 93715
  original_url: "https://www.suse.com/c/rancher_blog/setting-up-rancher-on-your-local-machine-with-an-rke-provisioned-cluster/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RKE1 end of life"
  redirect_target: "docs.rancher.com"
---

![](https://media1-production-mightynetworks.imgix.net/asset/28016087/Rancher_Logo.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)One fundamental decision when getting hands-on with Kubernetes is whether to use a local cluster or to set things up in the cloud from the start. Production clusters often run in the cloud, but a local setup is often the easier choice if you want to have a cluster for yourself to work with. However, a challenge with local cluster development is the potential configuration drift that may arise from the differences between your local setup and a cloud environment. After all, the latter comes with additional infrastructure complexities that you don’t have to deal with in a local context. If your goal is to install [Rancher](https://rancher.com/) on a managed cluster like EKS, GKE or AKS, this begs the question, “Why bother with a local setup of Rancher to begin with?” Well, local cluster development offers a host of benefits. These include full cluster access, fault isolation, zero operational costs, minimal administration regarding security, and monitoring and tracking of resource usage. 
That being said, you can exploit these same benefits even when you want to localize Rancher's multi-cluster management. Furthermore, Rancher Kubernetes Engine (RKE) is a great way to alleviate the risk of configuration drift. It runs your Kubernetes cluster in containers, making everything portable and less reliant on your underlying infrastructure for things to run as they should. RKE deploys the Kubernetes core components in containers to the respective nodes. Components managed by RKE are etcd, kube-apiserver, kube-controller-manager, kubelet, kube-scheduler and kube-proxy. As a result, RKE is a fitting option if you want to mirror a “real life” or production environment of your Rancher setup because of how it’s designed to provision clusters. In a nutshell, containerizing your cluster locally with RKE can give you a realistic feel of an RKE cluster provisioned in the cloud. 
In this post, we will use RKE to provision a Kubernetes cluster, after which we will deploy Rancher. All the source code demonstrated in this post can be [found here](https://github.com/SUSE-Rancher-Community/local-setup-of-rancher-with-rke).

## **Prerequisites**

To carry out this setup, you will have to ensure that you meet the following requirements:

- [Rancher Kubernetes Engine (RKE)](https://rancher.com/docs/rke/latest/en/installation/) - RKE is a [CNCF-certified](https://www.cncf.io/certification/software-conformance/) Kubernetes distribution that runs entirely within Docker containers.
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - VirtualBox is an open source tool for virtualizing computing architecture and acts as a hypervisor, creating a VM where users can run a separate Operating System (OS).
- [Vagrant](https://www.vagrantup.com/docs/installation) - Vagrant is a tool for building and managing virtual machine environments in a single workflow.
- [kubectl](https://kubernetes.io/docs/tasks/tools/) - kubectl is a CLI tool used to interact with Kubernetes clusters.
- [Helm](https://helm.sh/docs/intro/install/) - Helm is a package manager for K8s that allows for easy packaging, configuration, and deployment of applications and services onto clusters.

## **Bird's Eye View**

The cluster being provisioned will consist of three nodes; each is a Virtual Machine (VM) running [openSUSE Leap](https://get.opensuse.org/leap/) and bootstrapped with the necessary node prerequisites. There are two reasons for using this particular number of nodes:
1) The first is to demonstrate another way of bridging the local and production cluster gap by mimicking a similar node setup to what you plan to have in a remote cloud environment. So you can change the number of nodes to suit your particular requirements.
2) Three nodes is the minimum requirement to set up a [Highly Available cluster](https://rancher.com/docs/rancher/v2.x/en/installation/resources/k8s-tutorials/how-ha-works/) (which is recommended). 
Vagrant will be used to manage the workflow and lifecycle of your VMs. Your machine will fulfill the role of the RKE workstation, which will connect to each of the nodes (VMs) via SSH to establish a tunnel to access the docker socket. When your cluster has been provisioned, the current stable version of Rancher will be installed using Helm. 

![](https://media1-production-mightynetworks.imgix.net/asset/27390776/1628670486083.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

##

## **Create Virtual Machines**

The first step will be to get the cluster VMs up and running. You will declare 3 VMs, each running openSUSE Leap v15.2. Each node will be provisioned with 2(v)CPUs and 4GB of memory. In addition to this, you will need to prepare your nodes for the Kubernetes cluster with the following important steps:

- Docker installation - RKE is built using containers and runs on almost any Linux OS with Docker installed. The SSH user used for node access must be a member of the docker group on the node.
- Disabling swap - The Kubernetes scheduler determines the best available node on which to deploy newly created pods. If memory swapping is allowed on a host system, this can lead to performance and stability issues within Kubernetes. For this reason, Kubernetes requires that you disable swap in the host system for the proper function of the kubelet service on the control plane and worker nodes.
- Modify network bridge settings - Kubernetes requires that packets traversing a network bridge are processed by iptables for filtering and port forwarding. Ensure that net.bridge.bridge-nf-call-iptables are set to 1 in the sysctl configuration file on all nodes.

To accomplish this, create a Vagrant configuration file (*Vagrantfile*) defining each node, its respective IP address, and the provisioning script (*node\_script.sh*) that will bootstrap the node.
**Vagrantfile**

```
Vagrant.configure("2") do |config|
    # This will be applied to every vagrant file that comes after it
    config.vm.box = "opensuse/Leap-15.2.x86_64"
    # K8s Control Plane
    ## Master Node
    config.vm.define "master" do |k8s_master|
      k8s_master.vm.provision "shell", path: "node_script.sh"
      k8s_master.vm.network "private_network", ip: "172.16.129.21" 
      k8s_master.vm.hostname = "master"
      k8s_master.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--audio", "none"]
        v.memory = 4024
        v.cpus = 2
      end
    end
    # K8s Data Plane
    ## Worker Node 1
    config.vm.define "worker1" do |k8s_worker|
      k8s_worker.vm.provision "shell", path: "node_script.sh"
      k8s_worker.vm.network "private_network", ip: "172.16.129.22"
      k8s_worker.vm.hostname = "worker1"
      k8s_worker.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--audio", "none"]
        v.memory = 4024
        v.cpus = 2
      end
    end
    ## Worker Node 2
    config.vm.define "worker2" do |k8s_worker|
      k8s_worker.vm.provision "shell", path: "node_script.sh"
      k8s_worker.vm.network "private_network", ip: "172.16.129.23"
      k8s_worker.vm.hostname = "worker2"
      k8s_worker.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--audio", "none"]
        v.memory = 4024
        v.cpus = 2
      end
    end
  end
```

**node\_script.sh**

```
#!/bin/bash

# Enable ssh password authentication
echo "Enable SSH password authentication:"
sed -i 's/^PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config
echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
systemctl reload sshd

# Set Root password
echo "Set root password:"
echo -e "iamadmin\niamadmin" | passwd root >/dev/null 2>&1

# Commands for all K8s nodes
# Add Docker GPG key, Docker Repo, install Docker and enable services
# Add repo and Install packages
sudo zypper --non-interactive update
sudo zypper --non-interactive install docker

# Start and enable Services
sudo systemctl daemon-reload 
sudo systemctl enable docker
sudo systemctl start docker

#Confirm that docker group has been created on system
sudo groupadd docker

# Add your current system user to the Docker group
sudo gpasswd -a $USER docker
docker --version

# Turn off swap
# The Kubernetes scheduler determines the best available node on 
# which to deploy newly created pods. If memory swapping is allowed 
# to occur on a host system, this can lead to performance and stability 
# issues within Kubernetes. 
# For this reason, Kubernetes requires that you disable swap in the host system.
# If swap is not disabled, kubelet service will not start on the masters and nodes
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
sudo swapoff -a

# Turn off firewall (Optional)
ufw disable

# Modify bridge adapter setting
# Configure sysctl.
sudo modprobe overlay
sudo modprobe br_netfilter

sudo tee /etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF

sudo sysctl --system

# Ensure that the br_netfilter module is loaded
lsmod | grep br_netfilter
```

To provision the virtual machines, run the following command at the root level of the project directory:

```
vagrant up
```

Once the VMs are up and running, you can check their status with `vagrant status` or by connecting to any one of them using `vagrant ssh [hostname]`. Once you've confirmed that all machines are running with no issues, copy over the generated SSH keys from your workstation/host to each guest machine with the following commands:

```
ssh-copy-id root@[relevant ip address]
```

When prompted, enter the root user password configured in the bootstrap node script.

## **Provision Kubernetes Cluster with RKE**

To provision an RKE cluster on the VMs, you can either use a YAML file (*cluster.yml*) with your desired configuration or run the **rke config** command. This post will demonstrate the first approach. If you opt for the latter, you will be presented with a series of questions to which the answers will be used to declare the cluster configuration in a generated *cluster.yml* file upon completion. 
**cluster.yml**

```
# Cluster Nodes
nodes:
  - address: 172.16.129.21
    user: root
    role: 
      - controlplane
      - etcd
      - worker
    docker_socket: /var/run/docker.sock
  - address: 172.16.129.22
    user: root
    role:
      - controlplane
      - etcd
      - worker
    docker_socket: /var/run/docker.sock
  - address: 172.16.129.23
    user: root
    role:
      - controlplane
      - etcd
      - worker
    docker_socket: /var/run/docker.sock

# Name of the K8s Cluster
cluster_name: rancher-cluster

services:
  kube-api:
    # IP range for any services created on Kubernetes
    # This must match the service_cluster_ip_range in kube-controller
    service_cluster_ip_range: 172.16.0.0/16
    # Expose a different port range for NodePort services
    service_node_port_range: 30000-32767    
    pod_security_policy: false

  kube-controller:
    # CIDR pool used to assign IP addresses to pods in the cluster
    cluster_cidr: 172.15.0.0/16
    # IP range for any services created on Kubernetes
    # This must match the service_cluster_ip_range in kube-api
    service_cluster_ip_range: 172.16.0.0/16

  kubelet:
    # Base domain for the cluster
    cluster_domain: cluster.local
    # IP address for the DNS service endpoint
    cluster_dns_server: 172.16.0.10
    # Fail if swap is on
    fail_swap_on: false

network:
  plugin: calico

# Specify DNS provider (coredns or kube-dns)
dns:
  provider: coredns

# Kubernetes Authorization mode
# Enable RBAC
authorization:
  mode: rbac

# Specify monitoring provider (metrics-server)
monitoring:
  provider: metrics-server
```

To create a Highly Available (HA) Kubernetes cluster, you can modify the node configurations in the *cluster.yml* file to each have the role of the control plane and etcd. Once your cluster.yml file is finalized, you can run the following command:

```
rke up
```

When the cluster has been provisioned, the following files will be generated in the root directory:

- cluster.rkestate - the cluster state file
- kube\_config\_cluster.yml- kube config file

To add the cluster to your context, copy the kube config file:

```
cp kube_config_cluster.yml ~/.kube/config
```

If you do not have a `./kube` directory on your machine you will have to create one.
The last step will be to check that you can connect to your cluster:

```
kubectl cluster-info
```

or

```
kubectl config current-context
```

## **Install Rancher on RKE Cluster**

When you have successfully provisioned your cluster, you can install Rancher following the below steps:

##### Install Cert Manager

Rancher relies on [cert-manager](https://cert-manager.io/docs/) to issue certificates from Rancher's own generated CA or to request Let's Encrypt certificates.

```
kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.4.0/cert-manager.yaml
```

##### Create `cattle-system` Namespace

Create the namespace where the Rancher Kubernetes application resources will be deployed.

```
kubectl create namespace cattle-system
```

##### Add Rancher Helm Repository & Install Rancher

```
helm repo add rancher-stable https://releases.rancher.com/server-charts/stable helm install rancher rancher-stable/rancher \
  --namespace cattle-system \
  --set hostname=<hostname>
```

You may need to update the hosts on your local machine to resolve the addresses of the Virtual Machines. To do this, update the configuration in `/etc/hosts` by adding an entry for your hostname like this:

```
172.16.129.21   <hostname>
172.16.129.22   <hostname>
172.16.129.23   <hostname>
```

Lastly, go to your web browser, enter your selected hostname, and get started!

![](https://media1-production-mightynetworks.imgix.net/asset/28012334/rancher-landing-page.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

If you want to watch a walkthrough on how to provision a local K8s cluster with RKE, install Rancher and import an existing Amazon EKS cluster, check out the video below.

Play Video

## **In Closing**

Once you have Rancher running, you can proceed to either launch or import clusters and enjoy a local rendition of centralized Kubernetes multi-cluster management.
