---
title: "Automate DNS Configuration with ExternalDNS"
date: 2018-06-18T09:02:00
slug: "automate-dns-configuration-with-externaldns"
author: "Rancher Admin"
image: "images/rancher_blog_external-dns_site-feature.png"
products: ["Kubernetes (generic)"]
tags: ["networking"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 85820
  original_url: "https://www.suse.com/c/rancher_blog/automate-dns-configuration-with-externaldns/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "2018 ExternalDNS versions"
  redirect_target: ""
---

Take a deep dive into Best Practices in Kubernetes NetworkingFrom overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options.[Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/)

One of the awesome things about being in the Kubernetes community is the
constant evolution of technologies in the space. There’s so much
purposeful technical innovation that it’s nearly impossible to keep an
eye on every useful project. One such project that recently escaped my
notice is the ExternalDNS subproject. During a recent POC, a member of
the organization to whom we were speaking asked about it. I promised to
give the subproject a go and I was really impressed.

## The ExternalDNS subproject

This subproject (the incubator process has been deprecated), sponsored
by sig-network and championed by [Tim
Hockin](https://twitter.com/thockin), is designed to automatically
configure cloud DNS providers. This is important because it further
enables infrastructure automation allowing DNS configuration to be
accomplished directly alongside application deployment.

Unlike a traditional enterprise deployment model where multiple siloed
business units handle different parts of the deployment process,
Kubernetes with ExternalDNS automates this part of the process. This
removes the potentially aggravating process of having a piece of
software ready to go while waiting for another business unit to
hand-configure DNS. The collaboration via automation and shared
responsibility that can happen with this technology prevents manual
configuration errors and enables all parties to more efficiently get
their products to market.

## ExternalDNS Configuration and Deployment on AKS

Those of you who know me, know that I spent many years as a software
developer in the .NET space. I have a special place in my heart for the
Microsoft developer community and as such I have spent much of the last
couple of years sharing Kubernetes on Azure via Azure Container Service
and Azure Kubernetes Service with the user groups and meetups in the
Philadelphia region. It just so happens the persons asking me about
ExternalDNS are leveraging Azure as an IaaS offering. So, I decided to
spin up ExternalDNS on an AKS cluster. For step by step instructions and
helper code check out [this
repository](https://github.com/JasonvanBrackel/kubernetes-external-dns-in-rancher).
If you’re using a different provider, you may still find these
instructions useful. Check out the [ExternalDNS
repository](https://github.com/kubernetes-incubator/external-dns) for
more information.

Take a deep dive into Best Practices in Kubernetes NetworkingFrom overlay networking and SSL to ingress controllers and network security policies, we've seen many users get hung up on Kubernetes networking challenges. In this video recording, we dive into Kubernetes networking, and discuss best practices for a wide variety of deployment options.[Watch the video](https://rancher.com/events/2018/kubernetes-networking-masterclass-june-online-meetup/)
