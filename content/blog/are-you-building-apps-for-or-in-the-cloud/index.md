---
title: "Are You Building Apps \"For\" or \"In\" the Cloud"
date: 2021-08-26T18:39:20
slug: "are-you-building-apps-for-or-in-the-cloud"
authors: ["Robert Sirchia"]
products: ["Kubernetes (generic)"]
tags: ["cloud"]
content_type: "opinion"
draft: false
migration:
  wp_id: 93726
  original_url: "https://www.suse.com/c/rancher_blog/are-you-building-apps-for-or-in-the-cloud/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

There are a few paths to cloud development. We can even write code to create your own cloud. When we look at what it takes to develop an app in this new cloud world, we should look at the type. We first need to break down what apps we will build: are we building an app *for* the cloud or *in* it? In this short post, I'll break down what it means by apps *for* the cloud and apps *in* the cloud.

[![](images/ffdc4c-shutterstock_1722461929.jpg)](images/ffdc4c-shutterstock_1722461929.jpg)

First, what are apps *in* the cloud? Well, these are apps we write to run within a platform. Those apps are the vast majority of what we'll be writing for most of us. Any area of cloud modernization will be us modernizing apps into the cloud. This development is in languages like .NET, Java, NodeJs, or Python. Since most companies are building apps in the cloud, enablement needs to focus on this. Getting your developers trained on best practices in the cloud. Such concepts are outlined in such things as the 12 or 15 [factors](https://12factor.net/). Managing data in the cloud is another area of enablement that companies should look into.

On the other side of this discussion, we have writing apps *for* the cloud. For most of us, this isn't where we work--unless you are Google or contribute to OSS on the weekends. This is app development for features and functionality around a platform's features -- think of [Helm](https://helm.sh/) or [RabbitMQ](https://www.rabbitmq.com/). There's nothing wrong with developing software for these purposes, but is it at the core of what your company does? If it's not, then why are you building solutions for it? Individuals developing at this level often have a completely different skill set.

In this context, we're looking to develop apps for infrastructure rather than a business. There is little business value when companies offer solutions to fix these problems. If you have those solutions, then chances are good that other companies already do, too. Some of these solutions are open source and free to use, while others are closed solutions. Then there are my personal favorites: productized open source solutions. They're the best of both worlds, and they come with a few extra features.

If you are in the business of developing solutions *for* cloud infrastructure, go for it. However, if this is not your business, then reevaluate your options and consider other solutions. Know that others have had the same issues you are having. Using an open source or closed solution can get you back to focusing on your business.
