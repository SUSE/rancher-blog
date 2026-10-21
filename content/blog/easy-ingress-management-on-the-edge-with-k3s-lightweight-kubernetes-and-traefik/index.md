---
title: "Easy Ingress Management on the Edge with K3s lightweight Kubernetes and Traefik"
date: 2019-09-17T09:06:00
slug: "easy-ingress-management-on-the-edge-with-k3s-lightweight-kubernetes-and-traefik"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_networking.svg"
products: ["K3s"]
tags: ["networking"]
content_type: "company-news"
draft: true
migration:
  wp_id: 85864
  original_url: "https://www.suse.com/c/rancher_blog/easy-ingress-management-on-the-edge-with-k3s-lightweight-kubernetes-and-traefik/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Master class promo, 2019"
  redirect_target: "/k3s"
---

*K3s and Traefik are partnering to speed up cloud native applications deployment.*

[K3s](https://k3s.io), by Rancher, is the best way to have a lightweight, fully CNCF conformant Kubernetes cluster running on diverse infrastructures, including possible IoT appliances such as Raspberry Pis.

K3s starts in seconds thanks to its light weight nature. As it adds some components to the cluster automatically, k3s is very easy to use and therefore very accessible for new users. One of these components is Traefik, which is deployed in a k3s cluster as the default Ingress Controller.

Traefik is a cloud-native dynamic reverse proxy. Its purpose is to route incoming requests to all your services deployed on your platform. Traefik is able to observe different container technologies such as Docker or Kubernetes to auto-configure itself.

Since a Kubernetes Ingress Controller must have dynamic reconfiguration, Traefik is a perfect fit. In addition to being light weight and simple to use, Traefik comes with many more features built in: HTTP/2 Support, gRP, websockets or a unique automatic Lets Encrypt integration, just to name a few.

K3s and Traefik aim to be simple and offer the best user experience. K3s provides a fully working and easy to use cluster, with important components on board already. Traefik is integrated into K3s by default and preconfigured to use HTTPS as well as add-ons, such as metric collection or support for external-dns. Since these are already done, all you need to do is specify the Kubernetes Ingress Objects when deploying your application.

How K3s archives is very simple: it automatically deployes any manifest that is a Helm Chart. By reusing the popular Helm Chart technology, k3s can easily run the same deployments you would run on a typical Kubernetes cluster. Also, this design allows you to easily customize the integrated Traefik ingress controller for certain scenarios; for example, by activating the Let’s Encrypt integration, which works well together with the pre-configured HTTPS.

Given the focus on simplicity and user-experience, the combination of k3s and Traefik is a match made in heaven for an easy, production-ready Kubernetes environment.

Want to learn more? Register for the upcoming Kubernetes Master Class on Sept 24, [Speed Up Your Cloud Native Applications Deployment Using k3s and Traefik](https://info.rancher.com/speed-up-apps-with-k3s-and-traefik-online-class).
