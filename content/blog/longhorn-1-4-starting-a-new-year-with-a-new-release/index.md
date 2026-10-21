---
title: "Longhorn 1.4 - Starting A New Year With A New Release"
date: 2023-01-09T07:59:26
slug: "longhorn-1-4-starting-a-new-year-with-a-new-release"
authors: ["William Jimenez"]
image: "images/icon-longhorn.svg"
products: ["Longhorn"]
tags: ["storage"]
content_type: "release"
draft: false
migration:
  wp_id: 98936
  original_url: "https://www.suse.com/c/rancher_blog/longhorn-1-4-starting-a-new-year-with-a-new-release/"
  disposition: migrate
  commercial: false
  outdated_reason: "Longhorn 1.4 release"
  redirect_target: ""
---

The team are excited to start the new year with the latest release for Longhorn 1.4. This latest version is packed with new features and enhancements designed to help make cloud native enterprise storage simpler and more accessible to the cloud native community. For existing users of Longhorn, this latest release is focused on helping you build better value and resiliency across your storage strategy. 

Longhorn 1.4 is a major release and includes 16 entirely new enhancements, 51 improvements for existing features and 96 bug fixes. Here are some of the highlights of this release. 

**ReadWriteMany Support General Availability** 

First off, we have two significant functionalities that are becoming generally available (GA). ReadWriteMany (RWX) support is one of the most sought-after features in Longhorn since its GA in 2019. By combining native support for both Block and File in the same platform, Longhorn can now support the increasingly diverse storage use cases within an organization.  

**ARM64 Support General Availability** 

The GA of ARM64 also supports the growing use cases of ARM within organizations. Both in the datacenter and at the edge, ARM based infrastructure is becoming more important as we’ve heard from our users. And with the growing need for edge computing, ARM excels where hardware is expected to be more sensitive to the power and thermal limitations of the environment.  

In summary Longhorn’s support of ARM as an architecture and design that converges storage and compute together instead of the traditional storage array approach makes it ideal for these next generation use cases 

**Volume Bit-rot Protection** 

Bit-rot and data corruption become an important factor as storage systems grow and age. To combat this, the Longhorn team has introduced a snapshot checksum feature that validates the integrity of different copies of data in the storage system. The Bit-rot protection feature can also schedule periodic calculations of these checksums to confirm if any replica has incurred corruption. If corruption is found, the replica is rebuilt from the known good copies.   

**TRIM Support** 

TRIM enables volumes to be reduced in size after they were previously written to. Traditionally filesystems were designed with the expectation that the physical media backing it would not shrink in size. TRIM was introduced to allow the filesystem to tell the block device that a block is now unused and can be reused. In context for project Longhorn, this means that now Longhorn can reclaim the space that was previously unusable even though the files it represents were deleted.  

For example, if you write 100MB to a Longhorn volume and then delete 98MBs, even though your filesystem would forget about those deleted bytes, underneath the filesystem Longhorn would not know those blocks were “forgotten” and would continue to replicate and maintain them. Now with this new feature, Longhorn can free up those blocks, reducing snapshot sizes and allowing other volumes to use them instead. 

**Online Volume Expansion** 

Related to volume shrinking, another use case users have encountered is how to grow a volume after it was created. The advantage of this feature is now a volume can be expanded while being read from and written to. This makes the operation of volume expansion relatively inexpensive and simple. Longhorn will both grow the size of the virtual block device (volume) and grow the filesystem that manages the blocks inside of it (assuming a supported filesystem) 

**Strict Local Data Volume** 

Finally, the Strict Local volume is an exciting new foray into Longhorn supporting workloads that are already providing their own replication such as a modern cloud native database or distributed data system.  

For example, if a user is running MongoDB, which already maintains the replication of data between each worker/volume, but wants to rely on Longhorn for backup and data management, they can now have the best of both worlds.  

This volume is designed to be very high performance since it does not need to be replicated and will always be collocated with the workloads. Longhorn will use a local UNIX socket to broker the I/O between the container and the disk device instead of the TCP stack as with a typical distributed Longhorn replica set.  

We're excited to deliver more community-focused features for Longhorn in 2023. Stayed tuned and connected with us via [Slack](https://rancher-users.slack.com/archives/CC2UQM49Y)

You can check out the other enhancements in addition to these new highlights we've made for project Longhorn in the release notes and the associated design proposals (LEPs) and documentation [here](https://github.com/longhorn/longhorn/releases/tag/v1.4.0).

If you want to try out Longhorn, you can also deploy it using the Helm chart [here](https://longhorn.io/docs/1.4.0/deploy/install/).
