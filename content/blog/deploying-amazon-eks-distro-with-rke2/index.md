---
title: "Deploying Amazon EKS Distro with RKE2"
date: 2020-12-01T09:58:00
slug: "deploying-amazon-eks-distro-with-rke2"
author: "Bill Maxwell"
image: "images/rancher_blog_eksd-featured.png"
products: ["RKE2"]
tags: ["cloud", "aws", "installation"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86322
  original_url: "https://www.suse.com/c/rancher_blog/deploying-amazon-eks-distro-with-rke2/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RKE2 v1.18 and EKS-D 2020"
  redirect_target: "/rke2"
---

Today Amazon announced [Amazon EKS Distro (EKS-D)](https://aws.amazon.com/blogs/opensource/introducing-amazon-eks-distro/), a Kubernetes distribution based on and used by Amazon EKS. Amazon EKS Distro enables you to create reliable and secure Kubernetes clusters using the same versions of Kubernetes and its dependencies deployed by Amazon EKS. Each Amazon EKS Distro release follows the EKS process, verifying new Kubernetes versions for compatibility. The Amazon EKS Distro source code, open source tooling, binaries and container images as well as configuration are provided for reproducible builds via public Git and S3 storage locations. With Amazon EKS Distro, Amazon provides extended support for Kubernetes versions after community support expires, providing updated builds of previous versions including the latest security patches.

As an Amazon EKS Distro launch partner, Rancher Labs has added experimental support in Rancher’s [RKE2](https://github.com/rancher/rke2) Kubernetes distribution to allow users to leverage 3rd party Kubernetes components. The new experimental functionality to override the built-in components allows users to take advantage of optimized components for use-case specific workloads and binary compatibility. RKE2 is Rancher’s next-generation Kubernetes distribution that serves as the foundation for our RKE Government solution. RKE2 will be the eventual successor to RKE once full integration into Rancher occurs. The new design leverages the simplified operations experience from K3s and upstream installation paradigms. RKE2 and Amazon EKS Distro both follow community standards allowing the components to easily swap in.

Amazon EKS Distro replaces the kubelet, kube-apiserver, etcd, CoreDNS and kube-controller-manager in RKE2 with the same binaries used by EKS. RKE2 completes the Kubernetes cluster functionality with an ingress controller and the Canal CNI plugin to enable full cluster capabilities. Alternatively, users can leverage their own solutions for CNI and ingress functionality.

## Test out Amazon EKS Distro with RKE2

**Requirements:**

- RKE2 v1.18.12-beta1+rke2r3 or newer
- Python 3 (To use convenience scripts)
- Credentials to access AWS ECR (If needed images are stored in ECR)

These instructions are being run on Ubuntu 20.04. If you use another RKE2 supported OS you will need to adapt.

**Installing:**

First install our beta version of RKE2 to allow using custom Kubernetes components

```
# As root user
curl –sfL https://get.rke2.io | INSTALL_RKE2_VERSION=v1.18.12-beta1+rke2r2 sh -
```

Install dependencies for the helper script to simplify generating the RKE2 configs for use with Amazon EKS Distro.

```
sudo apt-get update

sudo apt-get install –y python3-venv python3-wheel python3-pip

python3 –m venv ~/python3

. ~/python3/bin/activate

git clone https://github.com/rancher/rke2.git

cd rke2/contrib/custom-image-kubelet

pip install -r requirements.txt
```

**Running:**

```
# Configure AWS Keys or Credentials to work in your shell environment

sudo ~/python3/bin/python genconfig.py --release-url https://distro.eks.amazonaws.com/kubernetes-1-18/kubernetes-1-18-eks-1.yaml

# Optionally you can generate these files with `--prefix ./rke2-config` argument to generate the files to copy to remote hosts.

systemctl enable rke2-server

systemctl start rke2-server
```

**Use:**

```
export KUBECONFIG=/etc/rancher/rke2/rke2.yaml PATH=$PATH:/var/lib/rancher/rke2/bin

kubectl version
```

![Image 01](images/rancher_blog_image-01.jpg)

```
kubectl get pods –A
```

![Image 02](images/rancher_blog_image-02.jpg)

We are excited about the new experimental capabilities added to the RKE2 distro to provide users the flexibility of leveraging components of their choice. Users can import their RKE2 clusters with Amazon EKS Distro components into [Rancher](https://rancher.com/products/rancher/) to streamline their management experience. Users can leverage Rancher’s monitoring, logging and continuous delivery capabilities across all Kubernetes clusters. Rancher provides a consistent single pane of glass management across AWS EKS, Amazon EKS Distro, Rancher RKE/K3s and any CNCF compliant Kubernetes cluster.

## About Rancher Labs

Rancher Labs delivers open source software that enables organizations to deploy and manage Kubernetes at scale, on any infrastructure across the data center, cloud, branch offices, and the network edge. With 37,000 active users and greater than 100 million downloads, its flagship product, Rancher, is the industry’s most widely adopted Kubernetes management platform. For additional information, visit www.rancher.com and follow [@Rancher\_Labs](https://twitter.com/Rancher_Labs) on Twitter. All product and company names herein may be trademarks of their registered owners.

Check out RKE2 [here](https://docs.rke2.io/).
