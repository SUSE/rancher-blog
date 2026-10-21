---
title: "Container Management - Decoding Kubernetes Management Platforms Part 2"
date: 2023-05-12T10:45:46
slug: "container-management-decoding-kubernetes-management-platforms-part-2"
author: "Andrés Valero"
image: "images/Kubernetes_logo_without_workmark.svg.png"
products: ["Kubernetes (generic)"]
tags: ["multi-cluster"]
content_type: "opinion"
draft: false
migration:
  wp_id: 106399
  original_url: "https://www.suse.com/c/rancher_blog/container-management-decoding-kubernetes-management-platforms-part-2/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

# ![](images/Decoding-KMP-2.jpg)

# Non-Hosted KMPs

This article is the second in a series covering Kubernetes Management Platforms (KMPs). In the first article, we analyzed hosted KMPs, exploring their potential benefits and customer base. This blog will examine non-hosted KMPs and the organizational customer profiles that can benefit the most from this solution.

After the first article, you may think that hosted KMPs are the way to go, but there are many things to consider before deciding. In this blog post, we want to help you to choose the best option for your use case and needs, so let's start analyzing the pros and cons for each one.

Before jumping on the pros and cons of non-hosted KMPs, let's give some context about the market and why non-hosted KMPs are the preferred option for most prominent organizations worldwide. Some of the most widely used KMPs in the market include Rancher Prime and Red Hat Advanced Cluster Management. These platforms are known for simplifying the deployment, scaling, and management of Kubernetes clusters and offering a centralized control plane for managing clusters at scale and easy integration with other technologies. Additionally, these platforms provide security features and automatic updates to ensure that clusters are highly available and secure.

However, the main reason for their popularity among organizations is their level of control and adaptability. Despite their differences, these platforms give organizations full control over their clusters, security, configuration, applications, and any other Kubernetes-related matter and adapt to any architecture used within the organization. This means you have the power and the responsibility to manage the platform with all that implies.

You can consult the Rancher by SUSE [buyer's guide](https://more.suse.com/fy21-global-web-landing-page-enterprise-kubernetes-management-buyers-guide?utm_source=blog&utm_medium=blog&utm_campaign=Decoding_Kubernetes_Management_Platforms_Part_2) If you are eager to know more about the differences between these solutions and others.

### Advantages of non-hosted KMPs:

- **Greater flexibility:** 
  - Non-hosted platforms offer more flexibility in terms of customization and configuration options, which can benefit complex environments.
- **Hybrid cloud or multi-cloud:** 
  - Non-hosted KMPs have an on-premises focus without crippling the possibilities to use and expand your environments using public cloud providers and managed services.
- **EDGE architectures:**
  - Solutions like Rancher Prime are developed to integrate EDGE deployments into your management layer without disrupting your tools and processes.
- **More control and security:**
  - In a non-hosted Kubernetes management platform, your operators control what's happening and decide which security measures and tools are better for your applications and your concrete requirements. It's the way to go for industries that require strict compliance or are highly regulated.
- **Cost-effective:**
  - Non-hosted platforms are more cost-effective than hosted platforms, especially for large-scale deployments.
- **Community:**
  - [Kubernetes management platforms](https://www.suse.com/c/should-your-business-be-using-a-kubernetes-management-platform/) like Rancher are open source and have built a community over the years. Open source communities have proven crucial in driving innovation and helping projects become global solutions, like Kubernetes.

### Disadvantages of non-hosted KMPs:

- **More complex:**
  - Non-hosted platforms may be more challenging to set up and manage than hosted platforms, which can require more technical expertise.
- **Responsibility:**
  - Users are responsible for the security, configuration, maintenance, data security, and updates of the Kubernetes cluster, which can be time-consuming and require high expertise and more resources.

###

### The user profiles

The advantages of non-hosted KMPs require, in most cases, a team of operators and SREs. Not all organizations have the resources to manage Kubernetes, even having a KMP to simplify their job and ease operations.

- **Large enterprises:**
  - These organizations typically have a dedicated IT infrastructure and IT staff and may prefer to manage their KMPs in-house to maintain full control and visibility over their cloud infrastructure.
- **Companies with compliance requirements:**
  - Some companies may have specific regulatory or data privacy requirements that cannot be met by hosted KMPs, making non-hosted KMPs a more suitable option.
- **DevOps teams:**
  - DevOps teams highly skilled in cloud infrastructure and Kubernetes may prefer the added control and customization options offered by non-hosted KMPs.
- **Organizations with multiple cloud deployments:**
  - Companies with numerous cloud deployments may find it more cost-effective to manage their KMPs in-house instead of paying for multiple hosted KMPs from different providers.

### Conclusion

Non-hosted platforms require higher expertise, but they also offer greater flexibility in terms of use cases, such as hybrid cloud, [EDGE](https://www.suse.com/c/rancher_blog/suse-edge-2-0-a-cloud-native-solution-to-manage-edge/?utm_source=blog&utm_medium=blog&utm_campaign=Decoding_Kubernetes_Management_Platforms_Part_2), and on-premises deployments. They can also accommodate multi-cloud use cases without a problem. Non-hosted solutions are widely used in the market because they provide almost all the benefits of a hosted solution through automation while offering the advantages of non-hosted solutions.

Choosing the right platform is fundamental to helping your organization adapt and grow quickly to meet your business needs. If you need to scale rapidly and want the support of a highly skilled team, [Rancher Prime Hosted](https://www.rancher.com/products/rancher?utm_source=blog&utm_medium=blog&utm_campaign=Decoding_Kubernetes_Management_Platforms_Part_2) may be the solution for you. It includes all the features of Rancher Prime but eliminates the burden of administrative tasks for your operations team.

Enterprises adopting Kubernetes and utilizing Rancher Prime have seen substantial economic benefits, which you can learn more about in [Forrester’s ‘Total Economic Impact’ Report on Rancher Prime](https://more.suse.com/tei-rancher-prime-kubernetes.html?utm_source=blog&utm_medium=blog&utm_campaign=Decoding_Kubernetes_Management_Platforms_Part_2).
