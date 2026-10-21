---
title: "What's new in Longhorn 1.5"
date: 2023-08-10T12:29:32
slug: "whats-new-in-longhorn-1-5"
authors: ["David Ko"]
image: "images/longhorn-icon-color.png"
products: ["Longhorn"]
tags: ["storage"]
content_type: "release"
draft: false
migration:
  wp_id: 117396
  original_url: "https://www.suse.com/c/rancher_blog/whats-new-in-longhorn-1-5/"
  disposition: migrate
  commercial: false
  outdated_reason: "Longhorn 1.5 release"
  redirect_target: ""
---

Longhorn version 1.5 has been released, along with the latest patch. This release includes a number of new features and improvements that can benefit users. Here are some of the highlights:

## v2 Data Engine based on SPDK (Preview)

In addition to the existing iSCSI stack (v1) data engine, we are introducing the v2 data engine based on SPDK (Storage Performance Development Kit). This release includes the introduction of volume lifecycle management, degraded volume handling, offline replica rebuilding, block device management, and orphaned replica management. For the performance benchmark and comparison with v1, check [the report](https://longhorn.io/docs/1.5.1/spdk/performance-benchmark/).

## Longhorn Volume Attachment

Introducing the new Longhorn VolumeAttachment CR, which ensures exclusive attachment and supports automatic volume attachment and detachment for various headless operations such as volume cloning, backing image export, and recurring jobs.

## Cluster Autoscaler GA

Cluster Autoscaler was initially introduced as an experimental feature in v1.3. After undergoing automatic validation on different public cloud Kubernetes distributions and receiving user feedback, it has now reached general availability.

## Instance Manager Engine & Replica Consolidation

Previously, there were two separate instance manager pods responsible for volume engine and replica process management. However, this setup required high resource usage, especially during live upgrades. In this release, we have merged these pods into a single instance manager, reducing the initial resource requirements.

## Volume Backup Compression Methods

Longhorn supports different compression methods for volume backups, including lz4, gzip, or no compression. This allows users to choose the most suitable method based on their data type and usage requirements.

## Automatic Volume Trim Recurring Job

While volume filesystem trim was introduced in v1.4, users had to perform the operation manually. From this release, users can create a recurring job that automatically runs the trim process, improving space efficiency without requiring human intervention.

## RWX Volume Trim

Longhorn supports filesystem trim for RWX (Read-Write-Many) volumes, expanding the trim functionality beyond RWO (Read-Write-Once) volumes only.

## Upgrade Path Enforcement & Downgrade Prevention

To ensure compatibility after an upgrade, we have implemented upgrade path enforcement. This prevents unintended downgrades and ensures the system and data remain intact.

## Backing Image Management via CSI VolumeSnapshot

Users can now utilize the unified CSI VolumeSnapshot interface to manage Backing Images similar to volume snapshots and backups.

## Snapshot Cleanup & Delete Recurring Job

Introducing two new recurring job types specifically designed for snapshot cleanup and deletion. These jobs allow users to remove unnecessary snapshots for better space efficiency.

## CIFS Backup Store & Azure Backup Store

To enhance users' backup strategies and align with data governance policies, Longhorn now supports additional backup storage protocols, including CIFS and Azure.

## Kubernetes Upgrade Node Drain Policy

The new Node Drain Policy provides flexible strategies to protect volume data during Kubernetes upgrades or node maintenance operations. This ensures the integrity and availability of your volumes.

Longhorn version 1.5 introduces a lengthy list of new features as above, as well as numerous important fixes and improvements to enhance the overall experience. Please see the [release notes](https://github.com/longhorn/longhorn/releases/tag/v1.5.0) for more details.

We encourage you to try out this release and share your feedback with us. Your input is crucial to helping us improve Longhorn and provide an enhanced experience for our users. Here are some resources you can use to join our community and share your feedback:

- Longhorn [Slack](https://rancher-users.slack.com/archives/CC2UQM49Y): Get help from Longhorn experts and chat with other users.
- Longhorn [GitHub](https://github.com/longhorn/longhorn): File bug reports, contribute code, and stay up-to-date on the latest development.

We appreciate your feedback!
