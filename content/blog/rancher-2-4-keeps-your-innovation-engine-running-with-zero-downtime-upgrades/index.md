---
title: "Rancher 2.4 Keeps Your Innovation Engine Running with Zero Downtime Upgrades"
date: 2020-04-06T10:13:00
slug: "rancher-2-4-keeps-your-innovation-engine-running-with-zero-downtime-upgrades"
author: "Bill Maxwell"
image: "images/rancher_blog_zero-downtime-featured.png"
products: ["Rancher Manager"]
tags: ["upgrades"]
content_type: "release"
draft: false
migration:
  wp_id: 86481
  original_url: "https://www.suse.com/c/rancher_blog/rancher-2-4-keeps-your-innovation-engine-running-with-zero-downtime-upgrades/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.4 release news"
  redirect_target: ""
---

Delivering rapid innovation to your users is critical in the fast-moving world of technology. Kubernetes is an amazing engine to drive that innovation in the cloud, on-premise and at the edge. All that said, Kubernetes and the entire ecosystem itself changes quickly. Keeping Kubernetes up to date for security and new functionality is critical to any deployment.

## Introducing Zero Downtime Cluster Upgrades

In Rancher 2.4, we’re introducing zero downtime cluster upgrades. That means you can change the engine on the plane mid-flight. Developers keep deploying applications to the cluster and customers continue to consume services without disruption. Meanwhile, cluster operators safely roll out security and maintenance updates within hours of published releases when combined with Rancher’s out of band Kubernetes updates.

In previous versions of Rancher, RKE upgraded etcd nodes first, taking care not to break quorum. Then Rancher quickly upgraded all control plane nodes at once and then, last, the worker nodes were upgraded all at once. This resulted in momentary hiccups in API and workload availability. Also, Rancher saw the cluster as “active” once the control plane was updated, leaving the operator possibly unaware that worker nodes were still being upgraded.

![Cluster updating process in earlier versions of Rancher](images/rancher_blog_zero-downtime-diagram-1.2.png)
Cluster updating process in earlier versions of Rancher

In [Rancher. 2.4](https://rancher.com/products/rancher/2.4), we’ve improved the entire upgrade process to keep CI/CD pipelines delivering and workloads serving traffic. Throughout the process, Rancher views the cluster in an updating state. This allows an operator to quickly see that something is happening in the cluster.

Rancher still starts with upgrades of the etcd nodes, one at a time, and is careful not to break quorum. As an extra precaution, operators can now take a snapshot of both etcd and the Kubernetes configuration before upgrading. And if you need to roll back, the whole cluster can revert to the pre-upgrade state.

Deploying applications to a cluster requires the Kubernetes API to be available. In Rancher 2.4, Kubernetes control plane nodes are now upgraded one at a time. The first server is taken offline, upgraded and then put back into the cluster. The next control plane node upgrade starts only after the previous node reports in healthy. This behavior keeps the API responding to requests during the upgrade process.

![Cluster updating process in Rancher 2.4](images/rancher_blog_zero-downtime-diagram-2.2.png)
Cluster updating process in Rancher 2.4

## Node Upgrade Changes in Rancher 2.4

The majority of activity on a cluster happens in the worker nodes. In Rancher 2.4, there are two big changes to the way the nodes are upgraded. The first is the ability to set the number of worker nodes to upgrade at once. For a conservative approach or on smaller clusters, the operator can opt for a single node at a time. For operators of larger clusters, the setting can be tuned to upgrade larger batch sizes. This option provides the most flexibility in balancing between risk and time. The second change is that operators can opt to drain workloads before the worker node is updated. Draining the nodes first minimizes the impact of pod restarts on Kubernetes minor version upgrades.

The add-on services like CoreDNS, NGINX Ingress and CNI drivers are updated in parallel with the worker nodes. Rancher 2.4 exposes the upgrade strategy settings for each of the add-on deployment types. This allows the add-on upgrades to use the native Kubernetes availability constructs.

For more information on how to leverage the new functionality in Rancher 2.4, [check out our docs](https://rancher.com/products/rancher/2.4).
