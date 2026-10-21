---
title: "Manual Rotation of Certificates in Rancher Kubernetes Clusters"
date: 2019-06-14T11:50:00
slug: "manual-rotation-of-certificates-in-rancher-kubernetes-clusters"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_security.png"
products: ["RKE1"]
tags: ["security", "upgrades"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 87343
  original_url: "https://www.suse.com/c/rancher_blog/manual-rotation-of-certificates-in-rancher-kubernetes-clusters/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RKE1 EOL, Rancher 2.2 UI"
  redirect_target: "docs.rancher.com"
---

## Introduction

This blog will cover the certificates rotation issue for RKE clusters. Rancher also can be deployed on RKE2 or K3s clusters. The Rancher UI offers the provisioning of RKE2/K3s/AKS/EKS/GKE, not only RKE.

Kubernetes clusters use multiple certificates to provide both encryption of traffic to the Kubernetes components as well as authentication of these requests. These certificates are auto-generated for [clusters launched by Rancher](https://docs.ranchermanager.rancher.io/pages-for-subheaders/launch-kubernetes-with-rancher) and also [clusters launched by the Rancher Kubernetes Engine (RKE) CLI](https://rancher.com/docs/rke/latest/en/installation/).

In Rancher, the auto-generated certificates for [Rancher-launched Kubernetes clusters](https://docs.ranchermanager.rancher.io/pages-for-subheaders/launch-kubernetes-with-rancher) have a validity period of one year, meaning these certificates will expire one year after the cluster is provisioned. The same applies to Kubernetes clusters provisioned by v0.1.x of the [Rancher Kubernetes Engine (RKE) CLI](https://rancher.com/docs/rke/latest/en/installation/#download-the-rke-binary).

If you created a Rancher-launched or RKE-provisioned Kubernetes cluster about 1 year ago, you need to rotate the certificates. If no action is taken, then when the certificates expire, the cluster will go into an error state and the Kubernetes API for the cluster will become unavailable. Rancher recommends that you rotate the certificates before they expire to avoid an unexpected service interruption. The rotation is a one time operation, and the newly-generated certificates will be valid for the next 10 years.

The instructions below detail how to rotate the certificates in both Rancher-launched and RKE-provisioned clusters, both before expiry when certificates are still valid, and also in the event that the certificates have already expired.

**Rotating Kubernetes certificates may result in your cluster being temporarily unavailable as components are restarted. For production environments, it’s recommended to perform this action during a maintenance window.**

## RKE clusters Launched by Rancher

Rancher provides UI support for certificate rotation (available since Rancher v2.2). If you are unable to upgrade your Rancher v2.0.x or v2.1.x instances to v2.2.x, then you can upgrade them to v2.0.15 and v2.1.10 respectively. These versions contain certificate rotation support via the API, and detailed steps for this can be found in the [documentation](https://rancher.com/docs/rancher/v2.x/en/cluster-admin/certificate-rotation/#certificate-rotation-in-rancher-v2-1-x-and-v2-0-x).

### Working Cluster / Valid Certs

To rotate the certificates on a Rancher-launched cluster for which certificates are still valid, follow these steps:

1. As a preliminary step, update your cluster so it goes through the Rancher Kubernetes Engine (RKE) provisioning process. This refreshes the cluster state and configurations. To do so, you can either upgrade your cluster to a newer Kubernetes version or simply change one of the existing parameters on a cluster to trigger the cluster reconciliation process via RKE.
   - To upgrade the Kubernetes version, browse to the cluster in the Rancher UI, click the vertical ellipses, and click `Edit`. Select the newer `Kubernetes Version` under `Cluster Options` and click `Save`.
   - To trigger reconciliation by changing a parameter with minimal impact, browse to the cluster in the Rancher UI, click the vertical ellipses and click `Edit`. Click `Edit as YAML`, update `change addon_job_timeout` to `50`, and click `Save`.
2. Rotate the certificates:
   - **Rancher v2.2.4+**: If you are running Rancher v2.2.4 or higher, you can rotate certificates from the UI. To do so, browse to the cluster in the Rancher UI, click the vertical ellipses, click `Rotate Certificates`, select `Rotate all service certificates` and click `Save`.
   - **Rancher v2.0.15 or v2.1.10**: If you are running Rancher v2.0.15 or v2.1.10, perform the certificate rotation from the API, per the [documentation](https://docs.ranchermanager.rancher.io/v2.0-v2.4/how-to-guides/advanced-user-guides/manage-clusters/rotate-certificates).

After following these steps, the certificates will be rotated and will have a validity of 10 years.

### Non-working Cluster / Expired Certs

If your Rancher-launched Kubernetes cluster is already in an error state because the certificates have expired, follow these steps to rotate the certificate:

1. [Upgrade Rancher](https://docs.ranchermanager.rancher.io/pages-for-subheaders/install-upgrade-on-a-kubernetes-cluster) to v2.2.4 or greater.
2. Open a shell session to the etcd and control plane nodes for the cluster and check if the directory `/etc/kubernetes/.tmp` contains the file `kube-apiserver-requestheader-ca.pem`. If this file is absent, perform the following manual copy:

   ```
   cp /etc/kubernetes/.tmp/kube-ca.pem /etc/kubernetes/.tmp/kube-apiserver-requestheader-ca.pem
   cp /etc/kubernetes/.tmp/kube-ca-key.pem /etc/kubernetes/.tmp/kube-apiserver-requestheader-ca-key.pem
   cp /etc/kubernetes/.tmp/kube-apiserver.pem /etc/kubernetes/.tmp/kube-apiserver-proxy-client.pem
   cp /etc/kubernetes/.tmp/kube-apiserver-key.pem /etc/kubernetes/.tmp/kube-apiserver-proxy-client-key.pem
   ```
3. To rotate certificates, browse to the cluster in the Rancher UI, click the vertical ellipses, click `Rotate Certificates`, select `Rotate all service certificates` and click `Save`.
4. If the UI shows no activity on the cluster while the rotation is happening, and if the log still reports `Expired cert`, perform the steps described in [Rancher Issue #20822](https://github.com/rancher/rancher/issues/20822).
5. After the rotation is finished, browse to the `Nodes` view for the cluster within the Rancher UI and check the state of `Worker` nodes. If the state is not `Active`, do the following:
   - Copy the following certificates from a Kubernetes control plane node to each worker node, under the same location:

     ```
     /etc/kubernetes/ssl/kube-node.pem
     /etc/kubernetes/ssl/kube-proxy.pem
     ```
   - Restart the `kubelet` and `kube-proxy` containers on each worker:

     ```
     docker restart kubelet
     docker restart kube-proxy
     ```

## Clusters Launched by the RKE CLI

If you are running Rancher in High Availability (HA) mode and used a version of RKE less than v0.2.0 to provision the cluster where the Rancher server has been installed via Helm, the certificates on that management cluster have to be rotated using the RKE CLI.

### Prerequisites

Before conducting the certificate rotation, please verify the presence of the `kube-apiserver-requestheader-ca.pem` file.

To do so, open a shell session to the etcd and control plane nodes for the cluster and check if the directory `/etc/kubernetes/.tmp` contains the file `kube-apiserver-requestheader-ca.pem`. If this file is absent, perform the following manual copy:

```
cp /etc/kubernetes/.tmp/kube-ca.pem /etc/kubernetes/.tmp/kube-apiserver-requestheader-ca.pem
cp /etc/kubernetes/.tmp/kube-ca-key.pem /etc/kubernetes/.tmp/kube-apiserver-requestheader-ca-key.pem
cp /etc/kubernetes/.tmp/kube-apiserver.pem /etc/kubernetes/.tmp/kube-apiserver-proxy-client.pem
cp /etc/kubernetes/.tmp/kube-apiserver-key.pem /etc/kubernetes/.tmp/kube-apiserver-proxy-client-key.pem
```

### Working Cluster / Valid Certs

To rotate the certificates on an RKE v0.1.x provisioned cluster for which certificates are still valid, follow these steps:

1. First ensure you have performed the steps under the Prequisites section above.
2. Upgrade the RKE CLI to the latest version. The RKE releases and downloads can be found [on GitHub](https://github.com/rancher/rke/releases/).
3. Run `rke up --config cluster.yml` to refresh your cluster. **Note: Please ensure that both your `cluster.yml` configuration file and the `kube_config_cluster.yml` file are present in the working directory when invoking `rke`**
4. Rotate the certificate using the following command: `rke cert rotate --config cluster.yml`

### Non-Working Cluster / Expired Certs

If your RKE provisioned cluster is already in an error state because the certificates have expired, follow these steps:

1. First ensure you have performed the steps under the Prequisites section above.
2. Upgrade the RKE CLI to the latest version. The RKE releases and downloads can be found [on GitHub](https://github.com/rancher/rke/releases/).
3. Rotate the certificate using the following command: `rke cert rotate --config cluster.yml`. **Note: Please ensure that both your `cluster.yml` configuration file and the `kube_config_cluster.yml` file are present in the working directory when invoking `rke`**

## ChangeLog

- **2019-06-25**: Updated to reflect additional prerequisites for clusters launched by the RKE CLI
