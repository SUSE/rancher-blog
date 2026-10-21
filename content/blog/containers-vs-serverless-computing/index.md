---
title: "Containers vs. Serverless Computing"
date: 2017-10-09T10:17:00
slug: "containers-vs-serverless-computing"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["developer-experience"]
content_type: "opinion"
draft: false
migration:
  wp_id: 86611
  original_url: "https://www.suse.com/c/rancher_blog/containers-vs-serverless-computing/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)

Serverless computing is a hot topic right now—perhaps even hotter than Docker containers. Is that because serverless computing is a replacement for containers? Or is it just another popular technology that can be used alongside containers? In this post, we will take a look at what you need to know about serverless computing and how it should figure into your IT strategy.

## Serverless Is Not Computing Without Servers

First, let’s clear up one point.

As you may already know, serverless computing does not mean that there are no servers involved. Serverless is a cloud-based computing service, and just like everything else in the cloud, it runs on servers.

Serverless is called serverless because the service provider handles all of the server-side IT and operational requirements. All you need to do is write code and deploy. The serverless computing provider takes care of just about everything else. So your experience is serverless, even if the underlying infrastructure is not.

## How Serverless Works

How does it work?

One of the most popular serverless platforms is AWS Lambda. To use it, you write code (currently C#, Go, Java, Node.js, Powershell, Python, and Ruby are supported), set a few simple configuration parameters, and upload everything (along required dependencies) to Lambda. In Lambda terminology, the package that you’ve uploaded is called a function. You can run the function by calling it from an application running on an AWS service such S3 or EC2. Lambda then deploys your function in a container, which persists until your function has done its job, then disappears.

The key point to keep in mind is that Lambda takes care of provisioning, deploying, and managing the container. All you do is provide the code that runs in the container. Everything else goes on behind the scenes.

## A Serverless World?

Does this mean that we now live in a world where software developers and IT teams no longer need to deal directly with containers, or with nuts-and-bolts backend IT at all? Will you be able to just write code, toss it to Lambda or a similar service, and let the provider take care of everything else?

If that sounds too good to be true, it’s for a very good reason—It is too good to be true. Serverless computing of the type represented by AWS Lambda can be an extremely valuable resource, and if it isn’t already part of your DevOps toolbox, it probably should be. The key word, however, is **part**.

Serverless computing is very well suited to a variety of tasks, but it is far from being an all around substitute for deploying and managing your own containers. Serverless computing is really designed to work with containers, rather than replacing them.

## What Serverless Computing Does Well

What, then, are the advantages of serverless computing? When used for the kinds of services it was designed to host, serverless computing can be:

### Inexpensive

With serverless, you typically pay only for the actual time and volume of traffic used. Lambda, for example, breaks its time-based pricing down into increments of 100 milliseconds. The actual cost is generally quite low as well, in part because serverless functions are small, perform relatively simple tasks, and run in generic containers with very little overhead.

### Low maintenance

The list of things that you don’t need to do when you deploy a function on a serverless platform is much longer than the list of things that you do need to do. Among other things, you don’t need to provision containers, set system policies and availability levels, or handle any backend server tasks, for that matter. You can use automatic scaling, or manually scale use by means of some simple capacity-based settings, if you want to.

### Simple

The standardized programming environment and the lack of server and container-deployment overhead means that you can focus on writing code. From the point of view of your main application, the serverless function is basically an external service which doesn’t need to be tightly integrated into the application’s container life cycle.

## Serverless Use Cases

When would you use serverless computing? Consider these possibilities:

### Backend Tasks for Websites or Mobile Applications

A serverless function can take a request (for information from a user database or an external source, for example) from the site or application frontend, retrieve the information, and hand it back to the frontend. It’s a quick and relatively simple task that can be performed as needed, with very little use of frontend time or resources—billing only for the actual duration of the backend task.

### Real-Time Data Streams and Uploads

A serverless function can clean up, parse, and filter incoming data streams, process uploaded files, manage input from real-time devices, and take care of other workhorse tasks associated with intermittent or high-throughput data streams. Using serverless functions moves resource-intensive real-time processes out of the main application.

### High Volume Background Processes

You can use serverless functions to move data to long-term storage, and to convert, process, and analyze data, and forward metrics to an analytics service. In a point-of-sale system, for example, serverless functions could coordinate inventory, customer, order, and transaction databases, as well as intermittent tasks such as restocking and flagging variances.

![network image](images/rancher_blog_network-2402637_1280-1024x576.jpg)

## The Limits of Serverless Computing

Serverless computing also has some very definite limits.

Lambda, for example, has built-in restrictions on the size, memory use, and time available for a function to run. These, along with the limited list of natively supported programming languages, are not necessarily intrinsic to serverless computing at a fundamental level, but they reflect the practical constraints of the system. It is important, for example, to keep functions small and prevent them from taking up too much of the system’s resources in order to prevent a relatively small number of high-demand users from locking everyone else out, or overloading the system.

There are also some built-in limits that arise out of the basic nature of serverless computing. For instance, it may be difficult or impossible to use most monitoring tools with serverless functions, since you typically have no access to the function’s container or container-management system. Debugging and performance analysis may thus be restricted to fairly primitive or indirect methods. Speed and response time can also be uneven; these limits, along with the constraints on size, memory, and duration, are likely to limit its use in situations where performance is important.

## What Containers Can Do Better

The list of things that containers can do better than serverless functions is probably too long and detailed to present in a single article. What we’ll do here is simply point out some of the main areas where serverless functions cannot and should not be expected to replace container-based applications.

### You Can Go Big

A container-based application can be as large and as complex as you need it to be. You can, for example, refactor a very large and complicated monolithic application into container-based microservices, tailoring the new architecture entirely to the requirements of the redesigned system.

If you tried to refactor the same application to run on a serverless platform, you would encounter multiple bottlenecks based on size and memory constraints. The resulting application would probably be composed of extremely fragmented microservices, with a high degree of uncertainty about availability and latency time for each fragment.

### You Have Full Control

Container-based deployment gives you full control over the individual containers, the overall container system, and the virtualized infrastructure on which it runs. This allows you to set policies, allocate and manage resources, have fine-grained control over security, and make full use of container-management and migration services. With serverless computing, on the other hand, you have no choice but to rely on the kindness of strangers.

### You Have the Power to Debug, Test, and Monitor

With full control over the container environment comes full power to look at what goes on both inside and outside of containers. This allows effective, comprehensive debugging and testing using a full range of resources, as well as in-depth performance monitoring at all levels.

You can identify and analyze performance problems, as well as fine-tune performance on a microservice-by-microservice basis to meet the specific performance needs of your system. Monitoring access at the system, container-management, and container levels also makes it possible to implement full analytics at all of these levels, with drill-down.

## Working Together

The truth is that serverless computing and containers work best when they work together, with each platform doing what it does well.

A container-based application, combined with a full-featured system for managing and deploying containers, is by far the best choice for large-scale, complex applications and application suites, particularly in an enterprise or internet environment. Serverless computing, on the other hand, is often best for individual tasks that can easily be run in the background or accessed as outside services.

Container-based systems can hand off such tasks to serverless applications without tying up the resources of the main program. Serverless applications, for their part, can provide services to multiple clients, and can be updated, upgraded, or switched out with other serverless applications entirely independently of the container systems that use their services.

## Conclusion

Are serverless computing services and containers competing platforms? Hardly. Container-based and serverless computing are mutually supporting parts of the ever-evolving world of contemporary cloud and continuous delivery based software.

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)
