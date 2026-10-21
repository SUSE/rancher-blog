---
title: "Kubernetes for the Edge: Key Developments & Implementations"
date: 2021-05-11T21:11:11
slug: "kubernetes-for-the-edge-key-developments-implementations"
author: "SUSE"
products: ["Kubernetes (generic)"]
tags: ["edge"]
content_type: "explainer"
draft: false
migration:
  wp_id: 98123
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-for-the-edge-key-developments-implementations/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Kubernetes is the key component in the data centers that are modernizing and adopting cloud native development architecture to deliver applications using containers. Capabilities like orchestrating VMs and containers together make Kubernetes the go-to platform for modern application infrastructure adopters. Telecom operators also use Kubernetes to orchestrate their applications in a distributed environment involving many edge nodes.

But due to the large scale of Telco networks that includes disparate cloud systems, Kubernetes adoption requires different architectures for different use cases. Specifically, if we look at a use case where [Kubernetes is used to orchestrate edge](https://www.calsoftinc.com/resources/ebriefs/a-deep-dive-into-kubernetes-for-edge/?utm_source=CloudTech&utm_medium=Article&utm_campaign=K8sEdgeeBrief&utm_term=SN) workloads, there are various frameworks and public cloud-managed Kubernetes solutions available that offer different benefits and give telecom operators choices to select the best fit. In a recent [Kubernetes on Edge Day sessions](https://kubenetesedgedayeu21.sched.com/) at KubeCon Europe 2021, many new use cases of Kubernetes for the edge have been discussed along with a showcase of cross-platform integration that may help enterprises adopting 5G edge and telecom operators to scale it to a high level.

Here is a high-level overview of some of the key sessions.

**The Edge concept**

Different concepts of edge have been discussed so far by different communities and technology solution experts. But when Kubernetes is coming into infrastructure, IT operators need to clearly understand the key pillars on which the Kubernetes deployment will seamlessly deliver low latency performance in telco or private 5G use cases. First, there should be a strong implementation of Kubernetes management at scale. Second, operators need to choose the lightweight K8s for edge solution, preferably certified by CNCF. And third, [a lightweight OS](https://www.suse.com/products/micro/) should be deployed at every node from Cloud to the far edge.

**Microsoft’s Akri Project:** Microsoft’s Akri project is an innovation that will surely break into multiple Kubernetes-based edge implementations. It discovers and monitors far edge devices of brownfield devices that cannot have their own compute – can be a part of Kubernetes cluster. Akri platform will let these devices be exposed to the Kubernetes cluster.

**AI/ML with TensorFlow:**TensorFlow is a machine learning platform that takes inputs to generate insights. It can be deployed on the cloud, on-premises, or edge nodes where ML operations need to perform. One session showed that Kubernetes clusters deployed in the cloud and edge can host analytics tools set (Prometheus, EnMasse/MQQT, Apache Camel, AlertManager, Jupyter, etc.) to process ML requests with the lowest latency.

**Architectures for Kubernetes on the edge:**While deploying Kubernetes for an edge, many architecture choices are varied per use case. And each architecture poses new challenges. But the bottom line is that there is no one-size-fits-all solution as various workloads have different requirements and IT teams focus on connecting network nodes. So, the overall architecture needs to evolve into centralized and distributed control planes.

**Robotics:** Kubernetes has also been implemented in Robotics. Sony engineers have showcased how the K8s cluster systems can be used for distributed system integration of robots and to perform specific tasks collaboratively.

**Laser-based Manufacturing:** Another interesting use case discussed by Moritz Kröger, a Researcher at RWTH Chair for Lasertechnology leveraged a Kubernetes-based distributed system. Kubernetes features like automation configuration management and flexibility in moving workloads in clusters give operational benefits to Laser manufacturing machines.

**OpenYurt + EdgeXFoundry**: OpenYurt is yet another open source framework that extends the orchestration features of upstream Kubernetes to the edge. It is showcased that – it can integrate with EdgeXFoundtry in [5G IoT edge computing](https://www.suse.com/c/understanding-iot-edge-computing/) use cases where EdgeXFoundtry is used to manage the IoT devices and OpenYurt is used to handle server environments using OpenYurt plugins set.

**Using GitOps**: Kubernetes supports the cloud native application orchestration and declarative orchestration. Applying the GitOps approach to achieve the Zero Touch Provisioning at multiple edges from the central data center is possible.

**Hong Kong-Zhuhai-Macao Bridge**: Another use case discussed is – Kubernetes is implemented in edge infrastructure for managing applications that are managing sensors at Hong Kong-Zhuhai-Macao Bridge. The use case is unique as it focuses on defining the sensor devices on the bridge as CRD in Kubernetes, associating each device with the CI/CD, and managing and operating the Applications deployed on edge nodes.

**Node Feature Discovery:** Many end devices can be part of thousands of edge nodes connected to data centers. Similar to the Akri project, the Node Feature Discovery (NFD) add-on can detect and push into Kubernetes clusters to orchestrate with edge servers and cloud systems.

**Kuiper and KubeEdge:** EMQ’s Kuiper is open source data analytics/streaming software that runs on edge devices with low resource requirements. It can integrate with KubeEdge where we get a combined solution that leverages KubeEdge’s application orchestration capabilities and streaming analytics. The combined solution delivers low latency, saving cost on bandwidth, ease in implementing business logic, and operators can manage and deploy Kuiper software applications from the cloud.
