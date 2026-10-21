---
title: "Longhorn 1.4.1"
date: 2023-03-14T09:25:04
slug: "longhorn-v1-4-1"
authors: ["David Ko"]
image: "images/longhorn-icon-color.png"
products: ["Longhorn"]
tags: ["storage"]
content_type: "release"
draft: false
migration:
  wp_id: 102885
  original_url: "https://www.suse.com/c/rancher_blog/longhorn-v1-4-1/"
  disposition: migrate
  commercial: false
  outdated_reason: "Longhorn 1.4.1 patch release"
  redirect_target: ""
---

**Longhorn v1.4.1** has been released, marking the first stable version since v1.4.0 was launched three months ago. The primary focus of this release is on improving space efficiency, resilience, performance, and stability.

#### Space efficiency

The space usage of volume snapshots is always the main area to improve. In previous versions, Longhorn supported recurring jobs to retain a specific number of volume snapshots for the volume that applied for the job. However, some cases were not achievable, such as deleting all snapshots or system snapshots with removable snapshots, especially for workloads that have their replication capability like distributed databases. In v1.4.1, there are two new job types introduced: *snapshot-delete* and *snapshot-cleanup*. Users can plan different jobs based on their space usage requirements to clean up unnecessary snapshots and optimize space efficiency.

#### Resilience

If a node becomes not ready due to reasons such as kubelet restarts, network partition, etc., the engine or replica of a volume will become unknown, and wait to see if the situation is temporary or durable. If the situation is temporary, it will be recovered without volume restart or replica rebuild. Otherwise, the replica or engine will stay in the right status to recover if needed. For RWX share manager pods, they will still failover immediately to ensure that the service remains available.

#### Stability

Several stability issues have been addressed in this release. For example, temporary network disconnections will no longer cause replica rebuilding, volume backup and restore will function as expected under a proxy, RWX storage upgrades will address potentially rare segments, and the new support bundle mechanism will operate in an air-gap environment. These are just some of the improvements included in this release.

#### Performance

This release has improved the memory consumption of the instance manager for replicas and unlocked stuck unmount processes caused by RWX volumes being unexpectedly detached.

In addition to the above highlights, this new release also includes several bug fixes. To learn more about these fixes, please refer to the release notes (<https://github.com/longhorn/longhorn/releases/tag/v1.4.1>) and the documentation (<https://longhorn.io/docs/1.4.1/>).

Enjoy this release and feel free to provide any feedback at <https://github.com/longhorn/longhorn/issues>.
