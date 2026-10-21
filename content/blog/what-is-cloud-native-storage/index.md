---
title: "What is Cloud-Native Storage?"
date: 2020-12-07T10:12:00
slug: "what-is-cloud-native-storage"
author: "Rancher Admin"
image: "images/rancher_blog_cloud-native-featured.png"
products: ["Longhorn"]
tags: ["storage"]
content_type: "explainer"
draft: false
migration:
  wp_id: 86452
  original_url: "https://www.suse.com/c/rancher_blog/what-is-cloud-native-storage/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Learn more about Longhorn, an enterprise-grade, cloud-native container storage solution.[Learn More](https://rancher.com/products/longhorn)

Cloud-native is the ultimate buzzword lately. So, is “cloud-native storage” just an attempt to grab on to this concept, hoping for a little boost? Actually, there is something more to it, and I’ll unpack that here.

The premise of cloud-native storage is simple: its native habitat is a Kubernetes cluster. When we design with the assumption that a technology will exist in Kubernetes, we get to look around and see what functionalities already exist in that system. And then we repurpose whatever functions are useful for our design.

How is this beneficial? Well, it means we don’t need to rewrite code that already exists. Rewriting or reinventing existing functionality typically makes for a lower-quality product. If you’re looking for a good argument for this principle, look no other than Joel Spolsky’s [Things You Should Never Do](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/).

Kubernetes has a plethora of high-quality distributed systems primitives that are extensible and open by design. This is why CNCF Sandbox [Project Longhorn](https://longhorn.io/) engineers used the [Kubernetes controller model](https://kubernetes.io/docs/concepts/architecture/controller/) to orchestrate most of the activities involving creating, attaching and reattaching volumes in Longhorn (among other things). In contrast, a non-cloud-native storage technology would have had to write its own distributed coordination system. If you’ve already adopted cloud native and Kubernetes, this is an inherent advantage since you get more of the things you know in their technology stack.

Longhorn is designed with containers in mind. This is another key attribute of cloud-native storage – it must treat containers as first-class citizens. Everything the engineers did in the driver and manager architecture was with the goal: “how do we present this volume to a container?” Naturally, all of our code base is heavily optimized without unnecessary functions. With a container as the goal, we can incorporate an awareness of the Kubernetes manifest that is interacting with this storage volume we are managing.

For example, a typical storage system is only concerned with backing up the volume or block device itself. It expects an operator or outside party to know what application runtime goes with that volume. Longhorn, on the other hand, is adding support to keep track of the Kubernetes manifest paired with its volume. When it’s time to restore a volume, Longhorn can also command Kubernetes to bring back the application runtime that should accompany the volume to make the volume truly useful to the user. [Check out our roadmap](https://github.com/longhorn/longhorn/wiki/Roadmap) for this and other great features we are planning.

There are many mature and useful storage technologies out there, both hardware integrated and software defined. But there are few cloud-native storage technologies. And many software-defined storage systems have been adapted to Kubernetes after the fact. This is not the same thing as cloud native. While repurposed technology may have merit in cases where there is already significant investment, consider the tradeoffs these decisions entail.

Learn more about Longhorn, an enterprise-grade, cloud-native container storage solution.[Learn More](https://rancher.com/products/longhorn)
