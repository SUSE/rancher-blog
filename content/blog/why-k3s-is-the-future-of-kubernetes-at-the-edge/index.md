---
title: "Why K3s Is the Future of Kubernetes at the Edge"
date: 2019-11-19T09:43:00
slug: "why-k3s-is-the-future-of-kubernetes-at-the-edge"
authors: ["Caroline Tarbett"]
image: "images/rancher_blog_header.png"
products: ["K3s"]
tags: ["edge"]
content_type: "opinion"
draft: true
migration:
  wp_id: 85927
  original_url: "https://www.suse.com/c/rancher_blog/why-k3s-is-the-future-of-kubernetes-at-the-edge/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2019 Arm interview, dated claims"
  redirect_target: "/k3s"
---

An interview with [Bhumik Patel](https://www.linkedin.com/in/bhumikpatel/), Director, Software Ecosystem at Arm

**Rancher was among the first to use Amazon EC2 A1 instances powered by Arm Neoverse; why is such a unique development environment required?**

By next year the number of connected devices will exceed 20 billion. The vast majority of these devices run on Arm architecture, increasingly at the infrastructure edge. With this growth in mind, the need for an agile, Arm-based development methodology has become increasingly urgent. Arm Neoverse provides the required IP for building the next gen of edge to cloud infrastructure to support the data explosion we are seeing, primarily caused by IoT. Amazon EC2 A1 instances, powered by 64-bit Arm Neoverse cores, provide a cost-effective way to build scale-out and Arm-based applications. This includes native development of applications to be deployed on Arm platforms, eliminating the complexities of using cross-compilers and emulators.

Now, containers are transforming the way edge and IoT platforms have been operated and managed in the past. Providing scalability, manageability and the ability to deploy general and multi-purpose applications on these devices drives a cloud-like flexibility into the IoT world. At first glance, Kubernetes appears too large and complex for edge and IoT devices, which typically have a smaller resource footprint than in the data center or cloud. Rancher’s K3s, however, is a lightweight, easy to install Kubernetes distribution geared toward resource-constrained environments and low touch operations - particularly edge and IoT environments.

During the development of K3s, Rancher ran its CI infrastructure on Arm servers. A1 instances enabled Rancher to build an Arm-native CI pipeline for K3s that improves developer productivity, increases reliability and lowers the overall development and test infrastructure spend. This made a huge difference in the development and test process, and meant Rancher could develop, build and release K3s entirely on Arm architecture, efficiently and without the need for cross-compiling and emulation.

**What are your predictions for the acceleration of edge computing?**

Billions of devices in the world right now, from IoT endpoints to smartphones and infrastructure, are powered by Arm-based processors. Traditionally, embedded devices are low-power, low-performance devices but this is changing fast. The market is currently going through a major transformation – each of these gateways and devices are becoming more intelligent; carrying out more tasks than ever before. As connected devices become more important, containerization is driving the shift - pulling traditional cloud development methodologies to the edge.

It’s easy to see why. Everyone wants to benefit from the efficiencies that a microservices-centric, cloud-native environment brings. To unlock the value of IoT, Arm developed [Project Cassini](https://community.arm.com/developer/ip-products/processors/b/processors-ip-blog/posts/taming-of-the-edge) - an ecosystem partnership which aims to develop platform standards and reference systems to enable deployment of cloud-native software stacks at the infrastructure edge. One of the goals of Project Cassini is to make this edge devices cloud native with Kubernetes; and that’s where the value of K3s really comes in. We’re making computing at the edge completely cloud-native and intelligent, scalable and secure.

**Why Kubernetes? Why is it more attractive than some of the other options available?**

Kubernetes is becoming the de facto orchestration for enterprise containers. The next challenge is to take the same, powerful model to the edge, and K3s makes containers edge efficient. How? K3s is purpose-built for the edge, removing millions of lines of code from Kubernetes that aren’t required in edge environments. This makes it incredibly lightweight and easy to deploy in the most remote and unusual circumstances.

One of the major benefits of K3s is how it centralizes the management of vast device estates. Traditionally developed in silos, edge devices were often failure-prone, and managing thousands of individual end-points was onerous. If the master node went down, there was no real way of pushing a coordinated fix to all devices, or being able to roll back if something went wrong. In K3s, developers can create a centrally-managed cluster where an entire device estate can be viewed via a single UI. K3s takes the complexity out of updates and roll-backs and crucially is platform-agnostic, so developers find it easier to manage an estate efficiently with little additional engineering.

**Can you think of a couple of really interesting examples of where you’re seeing edge computing being utilized?**

The most obvious and exciting area of IoT growth is in IIoT (industrial IoT). Smart manufacturing has driven automation across the board over the last few years. Now the challenge for industry is to find innovative and efficient ways of managing expansive estates of connected machines.

Embedded industrial devices, producing data in real-time are not new; factory floors are full of legacy M2M (machine-to-machine) deployments. What we’re starting to see is a move towards the replacement of embedded units with containerized devices. This is a major shift in methodology towards a more centralized approach to managing large-scale IoT deployments. This makes sense; the adoption of robotics, as well as machine learning techniques and AI all point towards the value of containers as a secure scalable way of extracting value from IoT.

Hivecell is a great example of a company working with K3s to extract value from the data produced by IoT devices. Petrochemical companies are using Hivecell’s K3s clusters to extract and analyze the unused data captured by an oil rig’s 30,000 sensors. Likewise, wind farm engineers need the data that their turbines create to better predict, and respond to, environmental changes. Processing the data from 350,000 turbines in the cloud is expensive; Hivecell provides containerized edge clusters that provide all the compute power needed to capture and analyse vast quantities of data.

**How do you see the role of Kubernetes evolving the next few years?**

I predict not only the increased popularity of Kubernetes but also its establishment as the de facto container distribution. We’re seeing a lot of experimentation with open source projects that are now being rolled into managed services - this will only explode in the next few years. Containers provide a way for technology teams to convert projects into active deployments faster and, crucially, to scale them more rapidly. This is important for edge deployments where we’re talking about tens of thousands of connected devices - IoT will continue to drive the need for innovation at the edge, and Kubernetes will have a major role to play in the evolution of the market.

From an Arm perspective, it’s all about driving self-sustainability into these edge and IoT deployments. As an ecosystem, we’re driving secure and reference platforms that enable development teams to deploy containers in an efficient manner, without spending all of their time on device-management activities.

For more information about K3s, visit the K3s website at <https://k3s.io> or the GitHub repository at <https://github.com/rancher/k3s/>.

## Hands-on with K3s GA and Rio Beta Online Meetup

[Join](https://info.rancher.com/hands-on-k3s-ga-rio-beta) the December Online Meetup as Rancher Co-Founder Shannon Williams and Rancher Product Manager Bill Maxwell discuss and demo:

- Key considerations when delivering Kubernetes-as-a-Service to DevOps teams
- Understanding the “Run Kubernetes Everywhere” solution stack from Rancher Labs including RKE, K3s, Rancher 2.3 and Rio
- Getting started with K3s with Rancher 2.3
- Streamlining your application deployment workflows with Rio: build, deploy, and manage containerized applications at scale

[Book your Spot.](https://info.rancher.com/hands-on-k3s-ga-rio-beta)
