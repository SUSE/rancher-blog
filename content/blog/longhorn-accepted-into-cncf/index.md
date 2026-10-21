---
title: "Longhorn Accepted into CNCF"
date: 2019-10-29T09:07:00
slug: "longhorn-accepted-into-cncf"
authors: ["Sheng Yang"]
image: "images/rancher_blog_longhorn-how-it-works.png"
products: ["Longhorn"]
tags: ["storage"]
content_type: "release"
draft: false
migration:
  wp_id: 85884
  original_url: "https://www.suse.com/c/rancher_blog/longhorn-accepted-into-cncf/"
  disposition: migrate
  commercial: false
  outdated_reason: "CNCF sandbox announcement, 2019"
  redirect_target: ""
---

Today I am very excited to announce that Rancher Labs’ Project Longhorn has been accepted by the Cloud Native Computing Foundation as a sandbox project.

Many Kubernetes users still find it challenging to run stateful workloads and manage persistent storage. Longhorn aims to help you manage stateful workloads in Kubernetes by providing a solution for persistent storage that you can easily deploy, use, and manage.

Longhorn provides the following major features (current for v0.6.2):

- Enterprise-grade distributed block storage software for Kubernetes
- Volume snapshots
- Built-in backup and restore
- Live upgrade without impacting running volumes
- Cross-cluster disaster recovery volume with defined RTO and RPO
- Intuitive UI
- One click installation

We’re actively developing more features, and if you’re interested, you can [follow our progress](https://github.com/longhorn/longhorn/milestones).

There is a tremendous amount of innovation in the Kubernetes storage ecosystem today. Longhorn is unique because it offers the following three benefits:

1. **Simplicity.** We designed Longhorn to be much simpler than traditional storage software. Longhorn implements its enterprise-grade storage features with only 40,000 lines of Go code, including both the data plane (Longhorn engine) and the management plane (Longhorn manager). Longhorn is lightweight because we build on storage technologies that already exist in the Linux operating system. The speed and capacity of modern storage hardware like SSD and NVMe also led to a greatly simplified design.
2. **Easy-to-use.** Most users interact with Longhorn through the UI, and it exposes a storage class for easy provisioning of volumes. Longhorn can be installed and upgraded with a couple of clicks, without needing to first read all of the documentation to understand every nuance. The Longhorn UI not only offers visibility into storage volumes, but it also helps you understand the Kubernetes workload that created and used the volume.
3. **Built-in multi-cluster backup and disaster recovery.** Longhorn protects data at multiple levels. As enterprise-grade distributed storage, Longhorn replicates data synchronously across multiple nodes. You can create snapshots directly in primary storage and revert to previous snapshots. You can also make backups of snapshots to secondary storage and recover the volume to the same cluster or a different one. You can even create an asynchronous replicated standby volume in a different cluster, making it possible to quickly recover data and the application in case of a cluster failure.

We have been working on Longhorn for many years. Thousands of users have experimented with the technology and provided valuable feedback. Becoming a CNCF project will greatly increase the interest in Longhorn and will accelerate its development velocity. We are actively working toward a GA release of Longhorn in the near future, and we’re looking forward to more contributions from the community!

You can find more information about Longhorn at [longhorn.io](https://longhorn.io) or the [project page on Github](https://github.com/longhorn/longhorn). If you’re using Rancher 2.x, you can find Longhorn in the Rancher App Catalog, and it only takes a couple of clicks to install it from there. For other platforms, [the project page on Github](https://github.com/longhorn/longhorn) includes instructions to install Longhorn via Helm or through direct YAML manifests.

Enjoy Longhorn!
