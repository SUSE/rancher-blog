---
title: "The History of Cloud Native"
date: 2022-04-13T18:01:36
slug: "the-history-of-cloud-native"
author: "SUSE"
image: "images/shutterstock_1686170080.jpg"
products: ["Kubernetes (generic)"]
tags: ["cloud", "developer-experience"]
content_type: "explainer"
draft: false
migration:
  wp_id: 90943
  original_url: "https://www.suse.com/c/rancher_blog/the-history-of-cloud-native/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Cloud native is a term that's been around for many years but really started [gaining traction](https://trends.google.com/trends/explore?date=all&q=cloud%20native) in 2015 and 2016. This could be attributed to the rise of Docker, which was released a few years prior. Still, many organizations started becoming more aware of the benefits of running their workloads in the cloud. Whether because of cost savings or ease of operations, companies were increasingly looking into whether they should be getting on this "cloud native" trend.

Since then, it's only been growing in popularity. In this article, you'll get a brief history of what cloud native means—from running applications directly on hosts before moving to a hybrid approach to how we're now seeing companies born in the cloud. We'll also cover the "cloud native" term itself, as the definition is something often discussed.

# Starting with data centers

In the beginning, people were hosting their applications using their own servers in their own data centers. That might be a bit of an exaggeration in some cases, but what I mean is that specific servers were used for specific applications.

For a long time, running an application meant using an entire host. Today, we're used to virtualization being the basis for pretty much any workload. If you're running [Windows Subsystem for Linux 2](https://docs.microsoft.com/en-us/windows/wsl/), even your Windows installation is virtualized; this hasn't always been the case. Although the principle of virtualization has been around [since the 60s](https://www.ispsystem.com/news/brief-history-of-virtualization), it didn't start taking off in servers before the [mid-2000s](https://trends.google.com/trends/explore?date=all&q=virtualization). 

Launching a new application meant you had to buy a new server or even an entirely new rack for it. In the early 2000s, this started changing as virtualization became more and more popular. Now it is possible to spin up applications *without* buying new hardware.

Applications were still running on-premises, also commonly referred to as "on-prem." That made it hard to scale applications, and it also meant that you couldn't pay for resources as you were using them. You had to buy resources upfront, requiring a big cash deposit in advance.

That was one of the big benefits companies saw when cloud computing became a possibility. Now you could pay only for the resources you were using, rather than having to deposit in advance—something very attractive to many companies.

# Moving to hybrid

At this point, we're still far from [cloud native](https://www.suse.com/suse-defines/definition/cloud-native/) being a term commonly used by close to everyone working with application infrastructure. Although the term was being thrown around from the beginning of AWS launching its first beta service (SQS) in 2004 and making it generally available in 2006, companies were still exploring this new trend.

To start with, cloud computing also mostly meant a replica of what you were running on-prem. Most of the advantages came from buying only the resources you needed and scaling your applications. Within the first year of AWS being live, they launched four important services: SQS, EC2, S3 and SimpleDB.

Elastic Compute Cloud (EC2) was, and still is, primarily a direct replica of the traditional Virtual Machine. It allows engineers to perform what's known as a "lift-and-shift" maneuver. As the name suggests, you lift your existing infrastructure from your data center and shift it to the cloud. This was the case with Simple Storage Service (S3) and SimpleDB, a database platform. At the time, companies could choose between running their applications on-prem or in the cloud, but the advantages weren't as clear as they are today.

That isn't to say that the advantages were negligible. Only paying for resources you use and not having to manage underlying infrastructure yourself are attractive qualities. This led to many shifting their workload to the cloud or launching new applications in the cloud directly, arguably the first instances of "cloud native."

Many companies were now dipping their toes into this hybrid approach of using both hardware on their own premises and cloud resources. Over time, AWS launched more services, making a case for working in the cloud more complex. With the launch of Amazon CloudFront, a Content Delivery Network (CDN) service, AWS provided a service that was certainly possible to run yourself, but where it was much easier to run in the cloud. It wasn't just whether the workload should be running on-prem or in the cloud; it was a matter of whether the cloud could provide previously unavailable possibilities.

In 2008, Google launched the Google Cloud Platform (GCP), and in 2010 Microsoft launched Azure. With more services launching, the market was gaining competition. Over time, all three providers started providing services specialized to the cloud rather than replicas of what was possible on-prem. Nowadays, you can get services like serverless functions, platforms as a service and much more; this is one of the main reasons companies started looking more into being cloud native.

# Being cloud native

Saying that a company is cloud native is tricky because the industry does not have a universal definition. Ask five different engineers what it means to be cloud native, and you'll get five different answers. Although, generally, you can split it into two camps.

A big part of the community believes that being cloud native just means that you are running your workloads in the cloud, with none of them being on-prem. There's also a small subsection of this group who will say that you can be partly cloud native, meaning that you have one full application running in the cloud and another application running on-prem. However, some argue that this is still a [hybrid approach](https://www.ibm.com/cloud/blog/distributed-cloud-vs-hybrid-cloud-vs-multicloud-vs-edge-computing-part-1).

There's another group of people who believe that to be cloud native, you have to be utilizing the cloud to its full potential. That means that you're not just using simple services like EC2 and S3 but taking full advantage of what your cloud provider offers, like serverless functions.

Over time, as the cloud becomes more prominent and mature, a third option appears. Some believe that to be cloud native, your company has to be *born* in the cloud; this is something we see more and more. Companies that have never had a single server running on-prem have launched even their first applications in the cloud.

One of the only things everyone agrees on about cloud native is cloud providers are now so prominent in the industry that anyone working with applications and application infrastructure has to think about it. Every new company has to consider whether they should build their applications using servers hosted on-prem or use services available from a cloud provider.

Even companies that have existed for quite a while are spending a lot of time considering whether it's time to move their workloads to the cloud; this is where we see the problem of tackling cloud native *at scale*.

# Tackling cloud native at scale

Getting your applications running in the cloud doesn't have to be a major issue. You can follow the old lift-and-shift approach and move your applications directly to the cloud with the same infrastructure layout you used when running on-prem.

While that will work for most, it defeats some of the purposes of being in the cloud; after all, a couple of big perks of using the cloud are cost savings and resource optimization. One of the first approaches teams usually think about when they want to implement resource optimizations is converting their [monolith applications](https://www.talend.com/resources/monolithic-architecture/) to [microservices](https://microservices.io/); whether or not that is appropriate for your organization is an entirely different topic.

It can be tough to split an application into multiple pieces, especially if it's something that's been developed for a decade or more. However, the application itself is only one part of why scaling your cloud native journey can become troublesome. You also have to think about deploying and maintaining the new services you are launching.

Suddenly you have to think about scenarios where developers are deploying multiple times a day to many different services, not necessarily hosted on the same types of platforms. On your journey to being cloud native, you'll likely start exploring paradigms like serverless functions and other specialized services by your cloud provider. Now you need to think about those as well.

My intent is not to scare anyone away from cloud native. These are just examples of what some organizations don't think about, whether because of priorities or time, that come back to haunt them once they need to scale a certain application.

## Popular ways of tackling cloud native at scale

Engineers worldwide are still trying to figure out the best way of being cloud native at scale, and it will likely be an ongoing problem for at least a few more years. However, we're already seeing some solutions that could shape the future of cloud native.

From the beginning, virtualization has been the key to creating a good cloud environment. It's mostly been a case of the cloud provider using virtualization and the customer using regular servers as if it were their own hardware. This is changing now that more companies integrate tools like Docker and Kubernetes into their infrastructure.

Now, it's not only a matter of knowing that your cloud provider uses virtualization under the hood. Developers have to understand how to use virtualization *efficiently*. Whether it's with Docker and Kubernetes or something else entirely, it's a safe bet to say that virtualization is a key concept that will continue to play a major role when tackling cloud native.

# Conclusion

In less than two decades, we've gone from people buying new servers for each new application launch to considering how applications can be split and scaled individually.

Cloud native is an exciting territory that provides value for many companies, whether they're born in the cloud or on their way to embracing the idea. It's an entirely different paradigm from what was common 20 years ago and allows for many new possibilities. It's thrilling to see what companies have made possible with the cloud, and I'll be closely watching as companies develop new ideas to scale their cloud workloads.

#### Let’s continue the conversation! [Join the SUSE & Rancher Community](https://community.suse.com/) where you can further your Kubernetes knowledge and share your experience.
