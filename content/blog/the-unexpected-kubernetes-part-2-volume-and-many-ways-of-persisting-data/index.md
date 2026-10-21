---
title: "The Unexpected Kubernetes: Part 2: Volume and Many Ways of Persisting Data"
date: 2018-10-11T09:03:00
slug: "the-unexpected-kubernetes-part-2-volume-and-many-ways-of-persisting-data"
author: "Sheng Yang"
products: ["Kubernetes (generic)"]
tags: ["storage"]
content_type: "explainer"
draft: false
migration:
  wp_id: 85827
  original_url: "https://www.suse.com/c/rancher_blog/the-unexpected-kubernetes-part-2-volume-and-many-ways-of-persisting-data/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Kubernetes 1.11 era details"
  redirect_target: ""
---

## Recap

[Last time we talked about PV, PVC, Storage Class and Provisioner.](https://rancher.com/blog/2018/2018-09-20-unexpected-kubernetes-part-1/)

To quickly recap:

1. Originally PV was designed to be a piece of storage pre-allocated by administrator. Though after the introduction of Storage Class and Provisioner, users are able to dynamically provision PVs now.
2. PVC is a request for a PV. When used with Storage Class, it will trigger the dynamic provisioning of a matching PV.
3. PV and PVC are always one to one mapping.
4. Provisioner is a plugin used to provision PV for users. It helps to remove the administrator from the critical path of creating a workload that needs persistent storage.
5. Storage Class is a classification of PVs. The PV in the same Storage Class can share some properties. In most cases, while being used with a Provisioner, it can be seen as the Provisioner with predefined properties. So when users request it, it can dynamically provision PVs with those predefined properties.

But those are not the only ways to use persistent storage in Kubernetes.

##### Take a deep dive into Best Practices in Kubernetes Networking

![]()

From overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options.

[Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/)

## Volume

In the previous article, I mentioned that there is also a concept of Volume in Kubernetes. In order to differentiate `Volume` from `Persistent Volume`, people sometimes call it `In-line Volume`, or `Ephemeral Volume`.

Let me quote [the definition of Volume](https://kubernetes.io/docs/concepts/storage/volumes/#background) here:
> A Kubernetes volume … has an explicit lifetime - the same as the Pod that encloses it. Consequently, a volume outlives any Containers that run within the Pod, and data is preserved across Container restarts. Of course, when a Pod ceases to exist, the volume will cease to exist, too. Perhaps more importantly than this, Kubernetes supports many types of volumes, and a Pod can use any number of them simultaneously.  
> At its core, a volume is just a directory, possibly with some data in it, which is accessible to the Containers in a Pod. How that directory comes to be, the medium that backs it, and the contents of it are determined by the particular volume type used.

One important property of Volume is that it has the same lifecycle as the Pod it belongs to. It will be gone if the Pod is gone. That’s different from Persistent Volume, which will continue to exist in the system until users delete it. Volume can also be used to share data between containers inside the same Pod, but this isn’t the primary use case, since users normally only have one container per Pod.

So it’s easier to treat Volume as a property of Pod, instead of as a standalone object. As the definition said, it represents a directory inside the pod, and Volume type defines what’s in the directory. For example, Config Map Volume type will create configuration files from the API server in the Volume directory; PVC Volume type will mount the filesystem from the corresponding PV in the directory, etc. In fact, Volume is almost the only way to use storage natively inside Pod.

It’s easy to get confused between Volume, Persistent Volume and Persistent Volume Claim. So if you can imagine that there is a data flow, it will look like this: **PV -> PVC -> Volume**. PV contains the real data, bound to PVC, which used as Volume in Pod in the end.

However, Volume is also confusing in the sense that besides PVC, it can be backed by pretty much any type of storage supported by Kubernetes directly.

Remember we already have Persistent Volume, which supports different kinds of storage solutions. We also have Provisioner, which supports the similar (but not exactly the same) set of solutions. And we have different types of Volume as well.

So, how are they different? And how to choose between them?

## Many ways of persisting data

Take AWS EBS for example. Let’s start counting the ways of persisting data in Kubernetes.

### Volume Way

`awsElasticBlockStore` is a Volume type.

You can create a Pod, specify a volume as `awsElasticBlockStore`, specify the volumeID, then use your existing EBS volume in the Pod.

The EBS volume must exist before you use it with Volume directly.

### PV way

`AWSElasticBlockStore` is also a PV type.

So you can create a PV that represents an EBS volume (assuming you have the privilege to do that), then create a PVC bound to it. Finally, use it in your Pod by specifying the PVC as a volume.

Similar to Volume Way, EBS volume must exist before you create the PV.

### Provisioner way

`kubernetes.io/aws-ebs` is also a Kubernetes built-in Provisioner for EBS.

You can create a Storage Class with Provisioner `kubernetes.io/aws-ebs`, then create a PVC using the Storage Class. Kubernetes will automatically create the matching PV for you. Then you can use it in your Pod by specifying the PVC as a volume.

In this case, you don’t need to create EBS volume before you use it. The EBS Provisioner will create it for you.

### Third-Party Way

All the options listed above are the built-in options of Kubernetes. There are also some third-party implementations of EBS in the format of Flexvolume driver, to help you hook it up to Kubernetes if you’re not yet satisfied by any options above.

And there are CSI drivers for the same purpose if Flexvolume doesn’t work for you. (Why? More on this later.)

### VolumeClaimTemplate Way

If you’re using StatefulSet, congratulations! You now have one more way to use EBS volume with your workload – VolumeClaimTemplate.

VolumeClaimTemplate is a StatefulSet spec property. It provides a way to create matching PVs and PVCs for the Pod that Statefulset created. Those PVCs will be created using Storage Class so they can be created automatically when StatefulSet is scaling up. When a StatefulSet has been scaled down, the extra PVs/PVCs will be kept in the system. So when the StatefulSet scales up again, they will be used again for the new Pods created by Kubernetes. We will talk more on StatefulSet later.

As an example, let’s say you created a StatefulSet named `www` with replica 3, and a VolumeClaimTemplate named `data` with it. Kubernetes will create 3 Pods, named `www-0`, `www-1`, `www-2` accordingly. Kubernetes will also create PVC `www-data-0` for Pod `www-0`, `www-data-1` for `www-1`, and `www-data-2` for `www-2`. If you scale the StatefulSet to 5, Kubernetes will create `www-3`, `www-data-3`, `www-4` and `www-data-4` accordingly. Then you scale the StatefulSet down to 1, all `www-1` to `www-4` will be deleted, but `www-data-1` to `www-data-4` will remain in the system. So when you decide to scale up to 5 again, Pod `www-1` to `www-4` will be created, and PVC `www-data-1` will still serve Pod `www-1`, `www-data-2` for `www-2`, etc. That’s because the identity of Pod are stable in StatefulSet. The name and relationship are predictable when using StatefulSet.

VolumeClaimTemplate is important for the block storage solutions like EBS and Longhorn. Because those solutions are inherently ReadWriteOnce, you cannot share it between the Pods. Deployment won’t work well with them if you have more than one Pod running with persistent data. So VolumeClaimTemplate provides a way for the block storage solution to scale horizontally for a Kubernetes workload.

## How to choose between Volume, Persistent Volume and Provisioner

As you see, there are built-in Volume types, PV types, Provisioner types, plus external plugins using Flexvolume and/or CSI. The most confusing part is that they just provide largely the same but also slightly different functionality.

I thought, at least, there should be a guideline somewhere on how to choose between them.

But I cannot find it anywhere.

So I’ve plowed through codes and documents, to bring you the comparison matrix, and the guideline that makes the most sense to me.

Comparison of Volume, Persistent Volume and Provisioner

| Name | Volume | Persistent Volume | Provisioner |
| --- | --- | --- | --- |
| AWS EBS | ✓ | ✓ | ✓ |
| Azure Disk | ✓ | ✓ | ✓ |
| Azure File | ✓ | ✓ | ✓ |
| CephFS | ✓ | ✓ |  |
| Cinder | ✓ | ✓ | ✓ |
| Fiber Channel | ✓ | ✓ |  |
| Flexvolume | ✓ | ✓ | ✓ |
| Flocker | ✓ | ✓ | ✓ |
| GCE Persistent Disk | ✓ | ✓ | ✓ |
| Glusterfs | ✓ | ✓ | ✓ |
| HostPath | ✓ | ✓ | ✓ |
| iSCSI | ✓ | ✓ |  |
| NFS | ✓ | ✓ |  |
| Photon PersistentDisk | ✓ | ✓ | ✓ |
| Portworx | ✓ | ✓ | ✓ |
| Quobyte | ✓ | ✓ | ✓ |
| Ceph RBD | ✓ | ✓ | ✓ |
| ScaleIO | ✓ | ✓ | ✓ |
| StorageOS | ✓ | ✓ | ✓ |
| vsphereVolume | ✓ | ✓ | ✓ |
| ConfigMap | ✓ |  |  |
| DownwardAPI | ✓ |  |  |
| EmptyDir | ✓ |  |  |
| Projected | ✓ |  |  |
| Secret | ✓ |  |  |
| Container Storage Interface(CSI) |  | ✓ | ✓ |
| Local |  | ✓ |  |

Here I only covered the in-tree support from Kubernetes. There are some [official out-of-tree Provisioners](https://github.com/kubernetes-incubator/external-storage) you can use as well.

As you see here, Volume, Persistent Volume and Provisioner are different in some nuanced ways.

1. Volume supports most of the volume plugins.
   1. It’s the only way to connect PVC to Pod.
   2. It’s also the only one that supports Config Map, Secret, Downward API, and Projected. All of those are closely related to the Kubernetes API server.
   3. And it’s the only one that supports EmptyDir, which will automatically allocate and clean up a temporary volume for Pod\*.
2. PV’s supported plugins are the superset of what Provisioner supports. Because Provisioner needs to create PV before workloads can use it. However, there are a few plugins supported by PV but not supported by Provisioner, e.g. Local Volume (which is a work-in-progress).
3. There are two types that Volume doesn’t support. These are the two most recent feature, CSI and Local Volume. There are works-in-progress trying to bring them to Volume.

*\* A side note about EmptyDir with PV:*

*Back in 2015, there was [an issue](https://github.com/kubernetes/kubernetes/issues/17354) raised by Clayton Coleman to support EmptyDir with PV. It can be very helpful for the workloads needing persistent storage but only have local volumes available. But it didn’t get much traction. Without scheduler supports, it was too hard to do it at the time. Now, in 2018, scheduler and PV node affinity support have been added for Local Volume in Kubernetes v1.11. But there is still no EmptyDir PV. And [Local Volume](https://kubernetes.io/blog/2018/04/13/local-persistent-volumes-beta/) feature is not exactly what I expected since it doesn’t have the ability to create new volumes with new directories on the node. So I’ve written [Local Path Provisioner](https://github.com/rancher/local-path-provisioner), which utilized the scheduler and PV node affinity changes, to dynamically provision Host Path type PV for the workload.*

## Guideline for choosing between Volume, Persistent Volume and Provisioner

So which way should users choose?

In my opinion, users should stick to one principle:

**Choose Provisioner over Persistent Volume, Persistent Volume over Volume when possible.**

To elaborate:

1. For Config Map, Downward API, Secret or Projected, use Volume since PV doesn’t support those.
2. For EmptyDir, use Volume directly. Or use Host Path instead.
3. For Host Path, use Volume directly in general, since it’s bound to a specific node and normally homogeneous across the node.
   1. If you want to have heterogeneous Host Path volumes, it didn’t work until Kubernetes v1.11 due to lack of node affinity knowledge for PV. With v1.11+, you can create Host Path PV with node affinity using my [Local Path Provisioner](https://github.com/rancher/local-path-provisioner).
4. For all other cases, unless you need to hook up with existing volumes (in which case you should use PV), use Provisioner instead. Some of Provisioners are not made into built-in options, but you should able to find them [here](https://github.com/kubernetes-incubator/external-storage) or at vendor’s official repositories.

The rationale behind this guideline is simple. While operating inside Kubernetes, an object (PV) is easier to manage than a property (Volume), and creating PV automatically (Provisioner) is much easier than creating it manually.

There is an exception: if you prefer to operate storages outside of Kubernetes, it’s better to stick with Volume. Though in this way, you will need to do creation/deletion using another set of API. Also, you will lose the ability to scale storage automatically with StatefulSet due to the lack of VolumeClaimTemplate. I don’t think it will be the choice for most Kubernetes users.

## Why are there so many options to do the same thing?

This question was one of the first things that came to my mind when I started working with Kubernetes storage. The lack of consistent and intuitive design makes Kubernetes storage look like an afterthought. I’ve tried to research the history behind those design decisions, but it’s hard to find anything before 2016.

In the end, I tend to believe those are due to a few initial design decision made very early, which may be combined with the urgent need for vendor support, resulting in Volume gets way more responsibility than it should have. In my opinion, all those built-in volume plugins duplicated with PV shouldn’t be there.

While researching the history, I realized dynamic provisioning was already an alpha feature in Kubernetes v1.2 release in early 2016. It took two release cycles to become beta, another two to become stable, which is very reasonable.

There is also a huge ongoing effort by SIG Storage (which drives Kubernetes storage development) to [move Volume plugins to out of tree using Provisioner and CSI](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/storage/csi-migration.md). I think it will be a big step towards a more consistent and less complex system.

Unfortunately, I don’t think different Volume types will go away. It’s kinda like the flipside of Silicon Valley’s unofficial motto: move fast and break things. Sometimes, it’s just too hard to fix the legacy design left by a fast-moving project. We can only live with them, work around them cautiously, and don’t herald them in a wrong way.

## What’s next

We will talk about the mechanism to extend Kubernetes storage system in the next part of the series, namely Flexvolume and CSI. A hint: as you may have noticed already, I am not a fan of Flexvolume. And it’s not storage subsystem’s fault.

*[To be continued]*

*[You can join the discussion [here](https://medium.com/@yasker/the-unexpected-kubernetes-part-2-volume-and-many-ways-of-persisting-data-6d4d19eb2e2a)]*
