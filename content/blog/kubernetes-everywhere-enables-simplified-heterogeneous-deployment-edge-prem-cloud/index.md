---
title: "Kubernetes Everywhere Enables Simplified Heterogeneous Deployment: Edge, Prem, Cloud"
date: 2020-06-26T09:52:00
slug: "kubernetes-everywhere-enables-simplified-heterogeneous-deployment-edge-prem-cloud"
authors: ["Mikhail Kozorovitskiy"]
image: "images/rancher_blog_kubernetes-everywhere-featured.png"
products: ["Kubernetes (generic)"]
tags: ["edge", "multi-cluster"]
content_type: "opinion"
draft: false
migration:
  wp_id: 86189
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-everywhere-enables-simplified-heterogeneous-deployment-edge-prem-cloud/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Read our free white paper: How to Build a Kubernetes Strategy[Download Now](https://more.suse.com/fy21-global-web-landing-page-how-to-build-enterprise-kubernetes-strategy)

Since almost the beginning of programming, the idea of write-once and deploy everywhere, on all platforms, has been an unreachable ideal to minimize development costs for cross-platform applications, drive UI consistency and reduce security service area. In programming, the cross-platform languages Java and Python have topped developer utilization charts for decades. Kubernetes provides the next step in that evolution, providing a consistent platform that can be used for development in the cloud, on prem and in edge devices, allowing many modern application languages to be used. Used properly, Kubernetes can simplify and speed up development to get value to customers faster and where they need it. The immense flexibility of Kubernetes is almost overwhelming and the path of success mined with craters to failure. In this blog, I will outline an effective approach for the myriad of choices available in the Kubernetes ecosystem to realize the vision of simplified application development and deployment.

## Let’s Start with Microservices

The story starts with the application itself. This is no place for monoliths – microservices enable decoupled deployment, which drives velocity. Any database changes should only be additive and any changes should be coded with migrations that will run on deployment. The development team works with a DevOps engineer to wrap their code to run in Docker containers and to build the Kubernetes configuration data that determines how it behaves inside Kubernetes and how it is accessed externally. This has to be flexible and dynamic enough to allow it to run in any environment provided with the right configuration. Then they set up a service mesh to automate the deployment and rollback of the application based on passing a set of automated tests and manual approvals. The Helm application is used to package the Kubernetes configuration data and keep it in Git for versioning that allows automated rollbacks in case of failures. The combination of the Docker images and the Kubernetes configuration comprises the immutable artifact that could be deployed to any Kubernetes environment, provided it has the right amount of CPU and memory.

## Simplifying Edge Deployments

In microservice deployments on the edge, resources are much smaller and the Internet may be unavailable or intermittent. We will use [k3OS](https://k3os.io/), Rancher’s lightweight Linux distribution for Kubernetes. It includes [K3s](https://k3s.io/), our lightweight Kubernetes distribution designed for the edge. The value of k3os is its lightweight-focused nature and the ability to be updated from K3s, allowing remote updates for both the operating system, Kubernetes and the application via the standard kubectl command through the K3s API.

## Rancher: A Single Pane of Glass to Manage Your Clusters

To manage the plethora of clusters from development, cloud, on prem and at the edge, we can use a single tool for managing fleets of individual clusters: Rancher. It provides push-button monitoring and observability, uptime alerting and Grafana dashboards with Rancher’s Cluster Monitoring for direct monitoring of at-edge operators. So now we have clusters anywhere with local observability and monitoring, as well as centralized views. In addition, fleet management allows simple updates to the entire edge stack.

## Deployment Flexibility Drives Efficiency

This flexibility of being able to deploy on the cloud, on prem and at the edge can be leveraged in many use cases to speed up time to value, reduce costs and drive durability by concentrating developer and development focus on a smaller reshared codebase. Developers can increase efficiency by optimizing, refactoring and writing tests instead of spending time recording a different version of their software for yet another stack. For AI-based edge analytics, you can move the machine learning model and rules to the edge, providing offline analytics for maritime, heavy and extractive industries. This allows operators to have the same situational awareness on the edge that is currently done only in the cloud or hacked together with custom solutions. Many industries will also benefit from the development and testing that runs in the same type of environment that runs on the fleet edges. The [US Air Force is already using Kubernetes](https://thenewstack.io/how-the-u-s-air-force-deployed-kubernetes-and-istio-on-an-f-16-in-45-days/) to run microservices on the upgraded F-16 fighter planes – and your enterprise can as well.

## Conclusion

In summary, this holistic vision of application deployment and environments brings developers, operators and decision makers all the tools to run their applications with confidence and reliability. Kubernetes minimizes rework to bring microservices from the cloud to the edge and simplifies the management of large amounts of edge agents.

Read our free white paper: How to Build a Kubernetes Strategy[Download Now](https://more.suse.com/fy21-global-web-landing-page-how-to-build-enterprise-kubernetes-strategy)
