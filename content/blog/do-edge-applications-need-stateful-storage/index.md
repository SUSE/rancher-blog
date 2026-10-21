---
title: "Do Edge Applications Need Stateful Storage?"
date: 2021-02-09T10:14:00
slug: "do-edge-applications-need-stateful-storage"
author: "Rancher Admin"
image: "images/rancher_blog_longhorn-featured.png"
products: ["Longhorn"]
tags: ["storage", "edge"]
content_type: "opinion"
draft: false
migration:
  wp_id: 86501
  original_url: "https://www.suse.com/c/rancher_blog/do-edge-applications-need-stateful-storage/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Kubernetes applications are increasingly making their way to the edge and embedded computing. Storage will quickly follow as the applications that rely on this edge infrastructure become more advanced and naturally carry more state. [According to a study](https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/whats-driving-the-connected-car) by McKinsey and Company, a “connected car” processes up to 25GB of data per hour. Granted not all the data needs to persist, but as engineers add more analytics and processing systems to our cars, the amount of data that we want to retain will only increase. And that’s just one example.

And the cars of tomorrow aren’t the only thing driving new demand (see what I did there?). Gartner predicts that by 2024, at least 40 percent of enterprises will have plans to adopt secure access Edge services. And IDC forecasts worldwide growth of the edge computing market to $250.6 billion by that same year, with edge products and services powering the next wave of digital transformation. There is an obvious demand shift toward edge and IoT that will require technology to adapt, and we’re just at the beginning.

How can we address the storage needs of an embedded, IoT or edge device? Are we going to put a 4U rackmount in the trunk of a car? Install a pizza-box server from the data center into an airplane? Probably not. Even if we could fit it, powering and cooling would require a lot of overhead and resources – both luxuries that resource-constrained devices unfortunately cannot afford compared to data centers. In fact, we might end up investing considerable effort in sourcing hardware that is more electrically and thermally efficient than anything we might have used in a traditional application of storage.

## Longhorn: Cloud Native Persistent Storage

Longhorn is a cloud native persistent storage technology that has been quickly evolving as stateful applications in Kubernetes increase. An enhancement in its latest version 1.1 is quite applicable to this topic: native ARM64 support.

This new Longhorn feature opens up the possibilities for several things. First, Longhorn can operate in all sorts of specialized computing environments. Second, Longhorn now has an advantage in operating in resource-constrained environments compared to any cloud native storage technology. Longhorn’s intrinsic qualities excel in environments where memory and CPU resources are at a premium. Again, if we think about embedding compute in a vehicle, where voltage comes at a premium and heat is difficult to deal with, the unique tradeoffs of an ARM processor are much more appropriate. Finally, even though edge is one of the most obvious applications of ARM chipsets, the traditional data center is also seeing some usage of this platform. AWS has recently developed a new line of ARM based processors (Graviton2), and [customers are already seeing the benefits of this approach](https://thenewstack.io/aws-graviton-marks-the-emergence-of-arm-for-cloud-native-workloads/). Microsoft is also offering ARM in their Azure portfolio, [and appears to be working on their own silicon](https://www.theverge.com/2020/12/18/22189450/microsoft-arm-processors-chips-servers-surface-report) in a similar vein to Amazon.

Because Longhorn is entirely container based, its dependencies and runtime requirements are self contained. This decouples dependency of storage software on the operating system – which will be valuable for a technology that needs to be deployed into a variety of lesser-known operating system versions that are built for embedded or specialty hardware. We like to think this is in the spirit of immutable infrastructure, which we know from data center computing offers more scale and reliability than dynamic configuration of the server and operating system.

With these and other technology advancements, the future – especially in edge computing – is quite bright. If you are considering an edge solution and want to start thinking about how storage can come into play, check out the [README section on Github](https://github.com/longhorn/longhorn/blob/master/README.md) for Longhorn, and more importantly send your feedback to the maintainers in the community slack channel.

[Join the next community meetup on February 17](https://more.suse.com/fy21-global-event-rancher-online-meetup-february2021) where we will explore how Rancher users can leverage the new Longhorn features across their edge environments.
