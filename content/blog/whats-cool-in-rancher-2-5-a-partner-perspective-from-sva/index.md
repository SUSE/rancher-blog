---
title: "What’s Cool in Rancher 2.5? A Partner Perspective from SVA"
date: 2020-11-24T09:57:00
slug: "whats-cool-in-rancher-2-5-a-partner-perspective-from-sva"
author: "Rancher Admin"
image: "images/rancher_blog_sva-featured.png"
products: ["Rancher Manager"]
tags: ["multi-cluster"]
content_type: "release"
draft: false
migration:
  wp_id: 86305
  original_url: "https://www.suse.com/c/rancher_blog/whats-cool-in-rancher-2-5-a-partner-perspective-from-sva/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.4 and 2.5 partner view"
  redirect_target: ""
---

Discover what’s new in Rancher 2.5[Learn More](https://www.rancher.com/products)

Since 2014, Rancher Labs has been making it easier for IT professionals to handle containers. Until now, every release of their flagship product, Rancher, brought features that you wouldn’t want to be without. But the latest releases have really taken things up a few notches.

In the 2.4 release, you could already see that something was about to happen. The number of manageable clusters and nodes had multiplied. In addition, you could patch nodes individually, enabling zero-downtime updates. Finally, our IoT colleagues could take their existing K3s clusters with them into Rancher management without major effort. There was also the first implementation of the Open Policy Agent with Gatekeeper. A dashboard button caught my eye, which led to an unfamiliar-looking user interface (UI).

By and large, Rancher 2.4 was a very good release with many new features and improvements. Not only did the developers and the Rancher community do a great job, but marketing didn’t sleep. They established Rancher Academy, a free training program for Rancher and Kubernetes, and also provided tech sales training. They also expanded their Platinum Partner program to EMEA.

These efforts paid off later in the year with Rancher’s announcement of the upcoming acquisition by SUSE. After that, however, the company with the blue cow became a little quiet. But now I know why: [Rancher 2.5](https://rancher.com/products/rancher/2.5) was in the works.

## Rancher Release 2.5

It’s finally here: the long-awaited major release of Rancher 2.5. This release also has many new features. In a comparatively short time, the developers and the community have done a great job.

## Cluster Manager vs. Cluster Explorer

The release has two UIs that can be easily separated and meet functionally different requirements. Rancher 2.5 features a new dashboard called Cluster Explorer. Cluster Manager is still available for doing just that (managing clusters). With this UI update, things are finally taking shape. If you take a closer look at the left sidebar of the new Cluster Explorer, you will find that you can find your Kubernetes cluster resources there, just as you are used to from the console via kubectl. This makes working with this UI pleasant and straightforward, even for those with an affinity for terminals.

![Image 01](images/rancher_blog_image-01.jpg)

Also, monitoring, logging and alert management, CIS scanning, Rancher pipelines and Istio are listed in the release notes as “deprecated features” and have migrated to Cluster Explorer.

These features weren’t just moved from one UI to another. This release fundamentally revises the integration of monitoring and logging. With monitoring, for example, you can now display your dashboards in the Cluster Explorer. For logging, Rancher 2.5 uses Fluent Bit to streamline the delivery of logs to external data stores. Furthermore, users now have the option of setting appropriate log processing and filter rules. The CIS scanning feature can now scan every certified Kubernetes cluster. Of course, this includes the managed Kubernetes systems of the various cloud providers. And Istio version 1.7 is now available. With the Istio Operator, it is now easy to provide several gateways.

Multi-cluster apps won’t move to the Cluster Explorer: now you can roll them out via Rancher Continuous Delivery. For pipelines that were previously made available via Jenkins, Rancher recommends migrating them to Rancher Continuous Delivery. Note that Continuous Delivery is a solution for delivering applications. For the upstream part of Continuous Integration, you should use a preferred CI tool, such as Gitlab CI, Travis CI, Tekton or one of the other numerous solutions.

And what is Rancher Continuous Delivery? Powered by Fleet, a project that Rancher announced in April, Continuous Delivery makes it possible to distribute applications with everything that goes with them to one or more clusters using a classic GitOps approach. The challenge so far has been to provide the necessary capabilities on different clusters and configure them accordingly. With Continuous Delivery, applications from the Git repo and all their policies are distributed over several clusters.

# Push-Button Backups and a New K8s Distro

Rancher 2.5 has even more exciting features.

First, now you can schedule or carry out backups at the push of a button. The Rancher Backup Operator makes it possible to map backups without direct access to the cluster database (etcd). Of course, this works on all Kubernetes certified clusters, including managed Kubernetes platforms in the cloud.

Rancher has also unveiled a new Kubernetes distribution to meet increased security requirements: [RKE Government](https://rancherfederal.com/blog/introducing-rke-government-security-driven-kubernetes-engine/) (or RKE2). It adds FIPS 140-2 Encryption and Security-Enhanced Linux (SELinux) support via containerd (an industry first). This distribution runs in a [hardened mode](https://docs.rke2.io/security/cis_self_assessment/) and is designed to pass the Center for Internet Security’s (CIS’) most-rugged security standards.

Also, you can install RKE Government clusters on RHEL and CentOS 8 machines. With this, Rancher expands the circle of potential users, especially to the public and banking sectors. We should mention that the automatic provisioning of the clusters from the manager is not yet possible with this distribution.

To add more flavor, Rancher includes a few more experimental features.

The version status of the OPA Gatekeeper, which Rancher included in version 2.4, can now be managed directly via Rancher. However, make sure you uninstall the older version of the Gatekeeper before the update.

A new cluster provisioning binary called [RancherD](https://ranchermanager.docs.rancher.com/) comes into play. RancherD is a single binary you can launch on a host to bring up a Kubernetes cluster bundled with a deployment of Rancher itself. This is a welcome solution, especially for installing Rancher Management Servers or single clusters. This has worked pretty well with RKE so far. However, afterwards, you had to install important services such as “cert-manager” and, above all, the Rancher management services using a helm chart or Kubernetes manifests.

## Installation Notes for Rancher 2.5

If you update an existing Rancher version, you should note the following:

- You need Helm version 3.2 or higher to install the current Cert-Manager release
- Run Kubernetes version 1.17
- If Rancher speaks to the Internet via a proxy, you must add the .svc and cluster.local to the Helm variable NO\_PROXY in the values
- You need to remove the add-local = false flag; otherwise, Rancher will not start. To prevent access to the local cluster, you can now use the restricted-admin role
- If Rancher starts in Docker, the container must be started privileged since further containers are started from the container
- Ensure that the installed features are installed via the Cluster Manager or the Cluster Explorer to avoid conflicts with the CRDs.
- If you have installed a feature with the Cluster Explorer, use it to manage this feature (the same applies to features that were rolled out via the Cluster Manager)

Especially when updating, it’s a good idea to look at the [Rancher release](https://github.com/rancher/rancher/releases) notes. Note that as of this writing, version 2.5.2 has been published as a stable release.

## Conclusion

Rancher developers and the community behind them were hard working and did an excellent job on Rancher 2.5. I am curious to see how things will continue and, above all, how much the UI design will develop with Cluster Explorer. As far as the functionality, Rancher leaves nothing to be desired. So, you should all be excited to see what will be sorted out in the current minor release and, above all, what will follow in the next release.

Discover what’s new in Rancher 2.5[Learn More](https://www.rancher.com/products)
