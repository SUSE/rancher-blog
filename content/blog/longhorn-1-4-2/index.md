---
title: "Longhorn 1.4.2"
date: 2023-05-18T03:45:07
slug: "longhorn-1-4-2"
author: "David Ko"
image: "images/longhorn-icon-color.png"
products: ["Longhorn"]
tags: ["storage"]
content_type: "release"
draft: false
migration:
  wp_id: 107139
  original_url: "https://www.suse.com/c/rancher_blog/longhorn-1-4-2/"
  disposition: migrate
  commercial: false
  outdated_reason: "Longhorn 1.4.2 patch release"
  redirect_target: ""
---

We are thrilled to announce the release of **Longhorn v1.4.2**, the latest stable version. This update significantly enhances Longhorn, focusing on bolstering resilience, ensuring stability and delivering an improved Kubernetes upgrade experience.

In this release, the main focus is to address key areas of improvement. Let's delve into the notable achievements:

## Enhanced Resilience

- Prevent unexpected volume expansion after node reboots. Longhorn will clean up replica information from the instance manager resource, ensuring correct downstream replica rebuilding.
- Prevent encountering the upper limit of the snapshot number. Longhorn will allow users to decide if they should clean up the existing snapshots before creating a new snapshot, especially during replica rebuilding.
- Resolve potential stuck replica rebuilding processes. Longhorn will incorporate a timeout mechanism, accounting for network instability between nodes.
- Resolve RWX volumes stuck in the detaching state after node reboots.

## Improved Stability

- Change admission validation enforcement. Longhorn's admission validating webhook will operate under the "failPolicyFail" setting, improving stability and ensuring proper resource change validation.
- Resolve stuck volume engine upgrades due to inactive replicas caused by node reboots.

## Kubernetes Upgrade with Node Drain Policy

Longhorn introduces the "Node Drain Policy" for Kubernetes upgrade and node maintenance. Users can apply an appropriate drain policy during Kubernetes upgrades or maintenance, facilitating seamless cluster maintenance without data loss concerns. Learn more about the details at <https://longhorn.io/docs/1.4.2/references/settings/#node-drain-policy>.

In addition to these noteworthy achievements, we continuously strive to improve other aspects of Longhorn, including backing image, backup, RWX, and more in this release. For a comprehensive overview of the changes and improvements in Longhorn v1.4.2, please refer to the release notes available at <https://github.com/longhorn/longhorn/releases/tag/v1.4.2>.
