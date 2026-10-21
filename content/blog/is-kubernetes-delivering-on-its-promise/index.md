---
title: "Is Kubernetes Delivering on its Promise?"
date: 2020-09-14T09:52:00
slug: "is-kubernetes-delivering-on-its-promise"
author: "Rancher Admin"
image: "images/rancher_blog_no-lock-blog-featured.png"
products: ["Kubernetes (generic)"]
tags: ["cloud"]
content_type: "opinion"
draft: false
migration:
  wp_id: 86178
  original_url: "https://www.suse.com/c/rancher_blog/is-kubernetes-delivering-on-its-promise/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Don’t miss the Computing on the Edge with Kubernetes conference on October 21. [Register Now](https://www.accelevents.com/e/edgeconference2020) A headline [in a recent Register article](https://www.theregister.com/2020/09/08/kubernetes_app_portability_problems/) jumped off my screen with the claim: “No, Kubernetes doesn’t make applications portable, say analysts. Good luck avoiding lock-in, too.” Well, that certainly got my attention…for a couple of reasons. First, the emphasis on an absolute claim was quite literally shouting at me. In my experience, absolutes are rare occurrences in software engineering. Second, it was nearly impossible to imagine what evidence this conclusion was based on.

The article summarizes a report by Gartner analysts Marco Meinardi, Richard Watson and Alan Waite. I can understand if skepticism drove their conclusions – let’s acknowledge that software vendors often enjoy developing software that creates lock-in. So, if this is a reaction to past experience, I get that.

But when I look carefully at their arguments, I find the stance less compelling. Let’s look at some of their arguments in more detail:

1. ***“Using Kubernetes to minimize provider lock-in is an attractive idea, but such abstraction layer simply becomes an alternative point of lock-in.”***

I can certainly agree with this point. The net product of Kubernetes is that it does create a dependence on the abstraction layer itself. This is inherent to the nature of abstractions, or interfaces in general. The conclusions the authors draw in this next claim is what I think is problematic:

1. ***“Although abstraction layers may be attractive for portability, they do not surface completely identical functionality from the underlying services — they often mask or distort them.”***

This statement misses the point. It’s probably true that abstraction layers do not achieve “completely identical functionality,” but this is not in question.

An abstraction layer’s virtue is not that it is 100 percent accurate or perfect, but that it sufficiently handles the majority of cases identically. I would put this claim in context that perfection is not a requirement for Kubernetes to be beneficial.

Even if Kubernetes provided portability for 80 percent of use cases, that is still far better than the status quo (building with complete dependence on a traditional cloud provider). There you have very little portability. And especially for net-new projects, where you absorb the cost of building for either IaaS or Kubernetes, why not take one that offers you 80 percent more upside? This claim fails to understand Kubernetes’ value position.

1. ***“The more specific to a provider a compute instance is, the less likely it is to be portable in any way. For example, using EKS on [AWS] Fargate is not CNCF-certified and arguably not even standard Kubernetes. The same is true for virtual nodes on Azure as implemented by ACIs.”***

I suspect this claim is used to support the previous one that the abstraction layer is not consistent and therefore fails at providing its intended value. The problem here is that the examples are results of specific approaches to Kubernetes and not inherent to Kubernetes itself. That is, Kubernetes’ design or approach does not produce situations where there are incompatible implementations. Instead, these are the result of specific vendors making implementation choices to break compatibility. And in many cases, innovation sometimes requires trying something new, but it doesn’t mean it is the only option. In fact, there [32 other conforming Kubernetes distributions](https://www.cncf.io/announcements/2017/11/13/cloud-native-computing-foundation-launches-certified-kubernetes-program-32-conformant-distributions-platforms/#:~:text=Search%20CNCF-,Cloud%20Native%20Computing%20Foundation%20launches%20certified%20Kubernetes,32%20Conformant%20distributions%20and%20platforms) to choose from that won’t have compatibility issues. Therefore, the authors selecting a handful of the most extreme examples is not an accurate reflection of the CNCF ecosystem.

Like I said earlier, I can certainly sympathize with there being many examples of “new platforms” that claim to provide freedom but, in fact, do not. Yet we can’t let experiences taint our ability to try new things in technology. Kubernetes isn’t perfect. It’s not the solution to all engineering problems, nor is it a tool everyone should use. But in my career as a Site Reliability Engineer and a consultant, I’ve seen first-hand real improvements over previous technologies that offer measurable value to engineering teams and the businesses that depend on them.

## Avoid Kubernetes Lock-In With Rancher

At Rancher Labs, we base our business model on the idea of avoiding lock-in – and we really preach this doctrine. You might find this statement curious because I just pointed out that vendors often do the opposite. So, the obvious question is: why is Rancher any different? Well, I can answer that, but I suspect you’ll get a better answer by investigating that yourself. Talk to our customers, look at our software – which is all open source and non-proprietary. I suspect you’ll find that Rancher is in business because we continue to provide a valuable experience, not because a customer has no other option. And organizations like the CNCF keep us accountable by measuring both our Kubernetes distributions (K3s and RKE) against a [rigorous conformance test](https://github.com/cncf/k8s-conformance). But most importantly, our customers keep us accountable, because they elect every year to keep us in business or not. It’s not the easiest business to be in, but it certainly is the most rewarding.Don’t miss the Computing on the Edge with Kubernetes conference on October 21. [Register Now](https://www.accelevents.com/e/edgeconference2020)
