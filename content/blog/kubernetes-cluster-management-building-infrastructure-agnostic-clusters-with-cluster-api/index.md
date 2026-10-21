---
title: "Efficient Kubernetes Cluster Management: Building Infrastructure-Agnostic Clusters with Cluster API"
date: 2023-08-14T18:09:29
slug: "kubernetes-cluster-management-building-infrastructure-agnostic-clusters-with-cluster-api"
author: "Hrittik Roy"
image: "images/Kubernetes_logo_without_workmark.svg.png"
products: ["Kubernetes (generic)"]
tags: ["multi-cluster", "installation"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 116204
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-cluster-management-building-infrastructure-agnostic-clusters-with-cluster-api/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "K8s 1.23 and Rancher 2.6 era"
  redirect_target: ""
---

With the widespread adoption of [Kubernetes](https://kubernetes.io/), the [Cloud Native Computing Foundation (CNCF) ecosystem](https://landscape.cncf.io/) has evolved to include projects that address the challenges of using a container orchestrator system. One such challenge is managing and deploying clusters, which can become complex as organizations scale their Kubernetes requirements. Fortunately, [Cluster API (CAPI)](https://cluster-api.sigs.k8s.io/) provides a solution.

CAPI is a declarative solution for managing and deploying clusters across managed clouds and your own unmanaged infrastructure. It's like infrastructure as code (IaC) but for your cluster and its configuration rather than just your infrastructure.

In this tutorial, you'll learn how CAPI works and how to use it to deploy clusters to a managed infrastructure.

## How CAPI works

The Kubernetes Special Interest Group (SIG) for [Cluster Lifecycle](https://github.com/kubernetes/community/tree/master/sig-cluster-lifecycle), responsible for projects such as [kubeadm](https://github.com/kubernetes/kubeadm/blob/main/OWNERS) and [kOps](https://github.com/kubernetes/kops/blob/master/OWNERS), created CAPI to address the challenges related to managing the lifecycle of Kubernetes clusters. The goal of the project is to [simplify the management of Kubernetes clusters](https://www.rancher.com?utm_source=blog&utm_medium=rancher_blog&utm_campaign=building_infrastructure_agnostic_clusters) by abstracting the underlying complexity involved in their deployment. This is facilitated through the use of customer resources that make it easier to manage clusters with CAPI.

The management of clusters using CAPI is facilitated through custom resources. These resources enable users to define the desired state of their clusters, machines, and infrastructure providers and are represented as generated manifests. By utilizing these manifests, users can maintain a central source of truth for their clusters and their configurations. Moreover, these configurations can be version-controlled, tested and audited, as required.

To apply these manifests, you need to provision a [management cluster](images/05a605-concepts.html#management-cluster) where the CAPI components have been installed, providers, such as infrastructure and bootstrap, and resources, such as machines and state data, are stored. The management cluster acts as the control plane for the [workload clusters](images/05a605-concepts.html#workload-cluster) and provides a centralized location for managing and maintaining the cluster's health. In addition, it helps generate the manifest:

![Architecture diagram courtesy of [*The Cluster API Book*](images/05a605-concepts.html)](https://i.imgur.com/LIe0Z7m.png)

Using the providers available through CAPI, you can provision a new workload cluster on your desired infrastructure without interacting with Infrastructure as a Service (IaaS) providers, whether it be on the cloud or in an on-premises data center. Once the workload cluster is provisioned, you can manage and create additional clusters using the management cluster, essentially using Kubernetes to deploy and manage Kubernetes.

## Implementing CAPI

This section explains how to create a workload cluster on the [DigitalOcean](https://www.digitalocean.com/) infrastructure using a locally running management cluster. However, before you begin, there are a few things you need to do to make sure that your machine has the required utilities to create the management cluster, including the following:

- **[kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl):** This is the command line interface (CLI) that helps you create and manage your Kubernetes objects.
- **[clusterctl](https://cluster-api.sigs.k8s.io/user/quick-start.html#install-clusterctl):** This is another CLI that helps you manage the lifecycle of your workload cluster.
- **[Docker](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-requirements/install-docker):** Docker is required for your Kubernetes cluster as a dependency to run and manage containers.
- **Active account with DigitalOcean:** You can use any infrastructure provider for your workload cluster, but this tutorial will use DigitalOcean, so an active account is necessary.
- **DigitalOcean token:** For the cluster configuration and image-building step, you'll need to [generate an API token](https://docs.digitalocean.com/reference/api/create-personal-access-token/) to request an infrastructure resource.
- **[doctl](https://docs.digitalocean.com/reference/doctl/how-to/install/):** This is a command line utility that can help you manage your DigitalOcean resources.
- **[Packer](https://developer.hashicorp.com/packer/tutorials/docker-get-started/get-started-install-cli):** Is required for the image-building part of your clusters.

### Provision your Kubernetes cluster

You can use any cluster for your management cluster, but this tutorial will use [k3d](https://k3d.io/), a lightweight bootstrap engine for K3s that can run in just a few steps. Go ahead and [install it now](https://k3d.io/).

Once k3d is installed, you can use `k3d cluster create management` to run your cluster:

```
hrittik@hrittik:~$ k3d cluster create management 
INFO[0000] Prep: Network                                
INFO[0000] Created network 'k3d-management'             
INFO[0000] Created image volume k3d-management-images   
INFO[0000] Starting new tools node...                   
INFO[0000] Starting Node 'k3d-management-tools'         
INFO[0001] Creating node 'k3d-management-server-0'      
INFO[0001] Creating LoadBalancer 'k3d-management-serverlb' 
INFO[0001] Using the k3d-tools node to gather environment information 
INFO[0001] HostIP: using network gateway 172.21.0.1 address 
INFO[0001] Starting cluster 'management'                
INFO[0001] Starting servers...                          
INFO[0001] Starting Node 'k3d-management-server-0'      
INFO[0005] All agents already running.                  
INFO[0005] Starting helpers...                          
INFO[0005] Starting Node 'k3d-management-serverlb'      
INFO[0012] Injecting records for hostAliases (incl. host.k3d.internal) and for 2 network members into CoreDNS configmap... 
INFO[0014] Cluster 'management' created successfully!   
INFO[0014] You can now use it like this:                
kubectl cluster-info
```

Don't forget to copy your kubeconfig to the path `/.kube/config` or set the environment variables so you can manage the cluster with kubectl. The following command will help you do that and can validate that your cluster is running by checking the nodes:

```
hrittik@hrittik:~$ k3d  kubeconfig get management > ~/.kube/config

hrittik@hrittik:~$ kubectl get nodes
NAME                     STATUS   ROLES                  AGE   VERSION
k3d-managment-server-0   Ready    control-plane,master   39m   v1.25.6+k3s1
```

### Initialize the management cluster

Using the `clusterctl` command that you installed earlier, you can transform the Kubernetes cluster created in the previous stage into a management cluster. You can do this by automatically installing the required components, including `cluster-api`, `cert-manager`, `infrastructure` and control plane components with the help of the CLI.

To do this, you need to initialize `clusterctl` with the desired infrastructure provider, which in this case, is `digitalocean`. However, it's important to note that you must pass the `DIGITALOCEAN_ACCESS_TOKEN`, which you should have acquired before you began this tutorial.

The commands required to initialize `clusterctl` with the DigitalOcean infrastructure provider can be found here:

```
export DIGITALOCEAN_ACCESS_TOKEN=<your-access-token>
export DO_B64ENCODED_CREDENTIALS="$(echo -n "${DIGITALOCEAN_ACCESS_TOKEN}" | base64 | tr -d '\n')"

# Initialize the management cluster
clusterctl init --infrastructure digitalocean
```

If you've initialized it correctly, you should get something that looks like this:

```
hrittik@hrittik:~$ export DIGITALOCEAN_ACCESS_TOKEN="dop_v1_b43fdkfjdkfdjfkdjjf"
hrittik@hrittik:~$ export DO_B64ENCODED_CREDENTIALS="$(echo -n "${DIGITALOCEAN_ACCESS_TOKEN}" | base64 | tr -d '\n')"

hrittik@hrittik:~$ clusterctl init --infrastructure digitalocean
Fetching providers
Installing cert-manager Version="v1.11.0"
Waiting for cert-manager to be available...
Installing Provider="cluster-api" Version="v1.3.3" TargetNamespace="capi-system"
Installing Provider="bootstrap-kubeadm" Version="v1.3.3" TargetNamespace="capi-kubeadm-bootstrap-system"
Installing Provider="control-plane-kubeadm" Version="v1.3.3" TargetNamespace="capi-kubeadm-control-plane-system"
Installing Provider="infrastructure-digitalocean" Version="v1.2.0" TargetNamespace="capdo-system"

Your management cluster has been initialized successfully!

You can now create your first workload cluster by running the following:

clusterctl generate cluster [name] --kubernetes-version [version] | kubectl apply -f -
```

### Prepare the workload cluster configuration

The next step is configuring the context for initializing your workload cluster by setting several environment variables. You can use the following commands to export the environment variables with the appropriate values:

```
export DO_REGION=nyc1
export DO_SSH_KEY_FINGERPRINT=<your-ssh-key-fingerprint>
export DO_CONTROL_PLANE_MACHINE_TYPE=s-2vcpu-2gb
export DO_CONTROL_PLANE_MACHINE_IMAGE=<your-capi-image-id>
export DO_NODE_MACHINE_TYPE=s-2vcpu-2gb
export DO_NODE_MACHINE_IMAGE=<your-capi-image-id>
```

Make sure to replace `<your-ssh-key-fingerprint>` and `<your-capi-image-id>` with the actual values for your SSH key fingerprint and CAPI image ID, respectively. The SSH key fingerprint is used to SSH into your nodes if required. If you don't have an SSH key fingerprint, you can generate one from the following command:

```
ssh-keygen -E md5 -lf ~/.ssh/id_rsa.pub
```

You'll get the key in MD5 format, and it will look similar to this: `72:8b:f8:48:5b:2b:3a:38:59:db:b3:6e:df:4b:82:63`.

If you don't already have an image, the CAPI image ID for the node and control plane acts as the base image for your workload cluster, which can be built and generated using the [image builder](https://github.com/kubernetes-sigs/image-builder). You can find the instructions for building the image with DigitalOcean in [*The Image Builder Book*](https://image-builder.sigs.k8s.io/capi/providers/digitalocean.html).

In summary, to build an image, you start by cloning the [repository](https://github.com/kubernetes-sigs/image-builder), then navigating to your CAPI directory (`image-builder/images/capi`) and using the `make build-do-ubuntu-2004` command. Following is a summary of the commands you can use to build your image:

```
git clone https://github.com/kubernetes-sigs/image-builder

cd image-builder/images/capi

make build-do-ubuntu-2004
```

> It's important to note that building a CAPI image for your workload cluster can be lengthy, as it involves building and configuring a new image on a droplet (a virtual machine) and uploading the snapshot to your internal DigitalOcean registry, a process that has its own prerequisites.

Once the image is built, you can use it multiple times. However, be sure to copy the image ID, which you can do after the build or list using [doctl](https://github.com/digitalocean/doctl), the DigitalOcean command line utility, and pass it as an environment variable:

```
hrittik@hrittik:~$ doctl compute image list

ID           Name                                               Type        Distribution    Slug    Public    Min Disk
126706837    Cluster API Kubernetes v1.23.15 on Ubuntu 20.04    snapshot    Ubuntu                  false     25
```

Once the six values are set, you can set up your workload cluster.

### Set up a workload cluster

After you've set the necessary environment variables for your workload cluster, the next step is to provide instructions to your management cluster using `clusterctl`. While you can generate your workload cluster directly, it's recommended to first generate and store your declarative manifest.

By generating a declarative manifest, you're essentially creating a blueprint of all the resources you want to create for your workload cluster. To generate the declarative manifest, use the following command:

```
clusterctl generate cluster workload-cluster \
    --infrastructure digitalocean \
    --kubernetes-version v1.23.15 \
    --control-plane-machine-count 3 \
    --worker-machine-count=3 \
     > capi-quickstart.yaml
```

Here, `workload-cluster` is the name you give to your workload cluster. `--kubernetes-version` specifies the version of Kubernetes that you want to use. You need to make sure it's the same as the one you generated from the image builder.

`--control-plane-machine-count` specifies the number of control plane nodes you want to create and `--worker-machine-count` specifies the number of worker nodes you want to create.

The command output is a YAML file containing the declarative manifest for your workload cluster. You can modify this file as needed to include additional custom resources or to modify existing ones:

```
hrittik@hrittik:~$ ls 
capi-quickstart.yaml
```

Once you've modified and gone through the declarative manifest, you can apply it to your management cluster using the following command:

```
kubectl apply -f capi-quickstart.yaml
```

If successful, you'll see a lot of custom resources being created:

```
hrittik@hrittik:~$ kubectl apply -f capi-quickstart.yaml
cluster.cluster.x-k8s.io/workload-cluster created
docluster.infrastructure.cluster.x-k8s.io/workload-cluster created
kubeadmcontrolplane.controlplane.cluster.x-k8s.io/workload-cluster-control-plane created
domachinetemplate.infrastructure.cluster.x-k8s.io/workload-cluster-control-plane created
machinedeployment.cluster.x-k8s.io/workload-cluster-md-0 created
domachinetemplate.infrastructure.cluster.x-k8s.io/workload-cluster-md-0 created
kubeadmconfigtemplate.bootstrap.cluster.x-k8s.io/workload-cluster-md-0 created
```

### Provision the workload cluster with a CNI

The workload cluster requires some Container Network Interface (CNI) plugins to enable your cluster nodes to work together. Once your control plane is initialized, you should install them to configure the cluster. For that, you need to watch the objects and the status of your objects using the kubectl commands.

For example, to see your cluster object, use the following command:

```
hrittik@hrittik:~$ kubectl get cluster
NAME               PHASE         AGE    VERSION
workload-cluster   Provisioned   175m
```

The control plane can be listed by querying the control plane object, as shown here:

```
hrittik@hrittik:~$ kubectl get kubeadmcontrolplane
NAME                             CLUSTER            INITIALIZED   API SERVER AVAILABLE   REPLICAS   READY   UPDATED   UNAVAILABLE   AGE    VERSION
workload-cluster-control-plane   workload-cluster   true                                 2                  2         2             176m   v1.23.15
```

After about 5 to 10 minutes, you should observe that the **INITIALIZED** status has turned to **true** for your control plane but nodes are still unavailable, and here, the CNI comes into the picture. To deploy your CNI, you need the kubeconfig of your workload cluster, which you can obtain using this command:

```
 clusterctl get kubeconfig workload-cluster > capi-quickstart.kubeconfig
```

Now, with the new kubeconfig, you can deploy your CNI. Here, you'll use [Calico](https://www.tigera.io/project-calico/)::

```
kubectl --kubeconfig=./capi-quickstart.kubeconfig apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.24.1/manifests/calico.yaml
```

With successful execution, the output should look something like this:

```
hrittik@hrittik:~$ kubectl --kubeconfig=./capi-quickstart.kubeconfig apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.24.1/manifests/calico.yaml
poddisruptionbudget.policy/calico-kube-controllers created
serviceaccount/calico-kube-controllers created
serviceaccount/calico-node created
configmap/calico-config created
customresourcedefinition.apiextensions.k8s.io/bgpconfigurations.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/bgppeers.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/blockaffinities.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/caliconodestatuses.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/clusterinformations.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/felixconfigurations.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/globalnetworkpolicies.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/globalnetworksets.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/hostendpoints.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/ipamblocks.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/ipamconfigs.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/ipamhandles.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/ippools.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/ipreservations.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/kubecontrollersconfigurations.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/networkpolicies.crd.projectcalico.org created
customresourcedefinition.apiextensions.k8s.io/networksets.crd.projectcalico.org created
clusterrole.rbac.authorization.k8s.io/calico-kube-controllers created
clusterrole.rbac.authorization.k8s.io/calico-node created
clusterrolebinding.rbac.authorization.k8s.io/calico-kube-controllers created
clusterrolebinding.rbac.authorization.k8s.io/calico-node created
daemonset.apps/calico-node created
deployment.apps/calico-kube-controllers created
```

### Test the workload cluster

The installation of CNI can take a while, but you can monitor the progress of your cluster and nodes by using the kubeconfig that you used to install Calico. To check the nodes, use the `get nodes` command while passing the `kubeconfig` flag:

```
hrittik@hrittik:~$ kubectl --kubeconfig=./capi-quickstart.kubeconfig get nodes
NAME                                   STATUS   ROLES                  AGE    VERSION
workload-cluster-control-plane-485xr   Ready    control-plane,master   174m   v1.23.15
workload-cluster-control-plane-lmsrd   Ready    control-plane,master   179m   v1.23.15
workload-cluster-md-0-9xcnv            Ready    <none>                 173m   v1.23.15
workload-cluster-md-0-s9zp9            Ready    <none>                 173m   v1.23.15
workload-cluster-md-0-w28pg            Ready    <none>                 173m   v1.23.15
```

At this point, your cluster is ready, but before you can run any workload, you need to install `digitalocean-cloud-controller-manager`, a [cloud controller manager (CCM)](https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/) that helps install components that are responsible for finishing the node bootstrapping process and eventually removing the taint. You can follow the step described on the [DigitalOcean GitHub page](https://github.com/digitalocean/digitalocean-cloud-controller-manager/blob/master/docs/getting-started.md#deployment) to complete the installation.

Once the installation is complete, you can run your containers like a simple Nginx container on your workload cluster:

```
hrittik@hrittik:~$ kubectl --kubeconfig=./capi-quickstart.kubeconfig run nginx --image=nginx
pod/nginx created
hrittik@hrittik:~$ kubectl --kubeconfig=./capi-quickstart.kubeconfig get pods
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          5s
```

With a successful deployment, your workload cluster is now ready to manage your containers, and you're ready to manage it with the help of CAPI.

## Conclusion

In this article, you learned about the benefits of using CAPI to build Kubernetes clusters in an infrastructure-agnostic way, and you created a workload cluster with a declarative approach that is consistent and efficient in producing repeatable results.

However, it's important to remember that CAPI offers a wide range of features beyond creation, including the ability to easily scale clusters (up or down), upgrade to new Kubernetes releases, and even tear down clusters and their underlying infrastructure when they're no longer needed.

To efficiently manage your clusters and related objects, it's recommended to use something like [Rancher](https://www.rancher.com), a top [Kubernetes-management platform](https://www.suse.com/c/should-your-business-be-using-a-kubernetes-management-platform/) from SUSE. Rancher 2.6 and 2.7 utilize Cluster API to deploy [RKE2](https://www.rancher.com/products/rke) and [K3s](https://www.suse.com/products/k3s/) clusters, making it easier for you to fully utilize CAPI's potential and provide a **robust and efficient management solution** for your Kubernetes clusters, regardless of your infrastructure provider.

For more free community training for Kubernetes & Rancher, check out the [Rancher Academy.](https://www.rancher.academy)
