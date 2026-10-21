---
title: "Container Management - Decoding Kubernetes Management Platforms Part 1"
date: 2023-05-12T10:44:08
slug: "container-management-decoding-kubernetes-management-platforms-part-1"
authors: ["Andrés Valero"]
image: "images/Kubernetes_logo_without_workmark.svg.png"
products: ["Kubernetes (generic)"]
tags: ["multi-cluster", "cloud"]
content_type: "opinion"
draft: false
migration:
  wp_id: 106393
  original_url: "https://www.suse.com/c/rancher_blog/container-management-decoding-kubernetes-management-platforms-part-1/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

![](images/Decoding-KMP-1.jpg)

# **Hosted KMPs**

This is the first article of a series of two covering the advantages and disadvantages of hosted and non-hosted Kubernetes management platforms. First, let's introduce hosted what is hosted Kubernetes management platform (KMP) and provide a broader view of hosted KMPs.

A hosted Kubernetes management platform is a service provided by a third-party vendor that manages the deployment and operation of Kubernetes clusters for you or helps you to do so. It abstracts away the underlying infrastructure and provides a convenient, user-friendly interface for managing your applications and services running on the cluster. The vendor typically takes care of tasks such as cluster provisioning, scaling, monitoring, and maintenance, freeing you to focus on developing and deploying applications. While the idea may seem appealing, it's important to carefully assess various factors before making a decision. For instance, we should evaluate the specific environment and applications we'll be working with, consider the platform's costs, and explore its capabilities and integrations. It's worth noting that many hosted KMPs heavily prioritize Kubernetes services on public clouds, which may result in limited capabilities and integrations in on-premises or edge environments.

Organizations may choose hosted [Kubernetes management platforms](https://www.suse.com/c/should-your-business-be-using-a-kubernetes-management-platform/) for various reasons, including simplifying the management of complex underlying infrastructure, automatic scaling to meet business needs without additional investment in infrastructure and staff, and access to expert technical support. These benefits make hosted solutions particularly well-suited for startups or growing organizations that may not have the resources to invest in infrastructure and Kubernetes professionals in a concrete moment.

In this blog post series, I want to provide information and perspective to help you to choose the best option for your use case and needs, so let’s start analyzing the pros and cons of hosted KMPs.

### **Hosted KMPs have multiple advantages, such as:**

- **Ease of use:** Hosted platforms typically provide a user-friendly interface and are SaaS-based tools, making it easy for users to deploy and manage their Kubernetes clusters.
- **Automatic updates and upgrades:** Hosted platforms handle the updates and upgrades of the Kubernetes cluster, which can save operators time and effort.
- **Expertise:** Vendors that provide hosted [managed Kubernetes](https://www.suse.com/c/ensuring-high-availability-with-cloud-managed-kubernetes/) platforms have expertise in deploying and operating Kubernetes clusters and can provide support and troubleshooting assistance to their customers.
- **Scalability:** Hosted platforms can automatically scale the underlying infrastructure, making it easier to accommodate growth in the number of applications and users.
- **Simplified security:** Hosted platforms typically provide out-of-the-box basic security features such as built-in authentication and authorization, network segmentation, CVE scanning, and automatic backups.
- **Focus on application development:** With the operational overhead of managing a Kubernetes cluster handled by a third party, you can focus on developing and deploying your applications on the cluster without worrying about infrastructure management.

### Disadvantages of hosted Kubernetes management platforms:

- **Cost:** Hosted platforms are more expensive than non-hosted platforms, especially for large-scale deployments. They are SaaS tools running on hyperscalers. While there are different licensing or subscription models available, in the end, hosted platform providers charge for both their costs and the service they provide. These costs include the cloud provider bill, which can make the overall price of these services more expensive. The pricing for hosted solutions is usually complex to understand, making cost analysis difficult.
- **Limited flexibility:** Hosted platforms may have limitations in terms of customization and configuration options compared to non-hosted platforms. Additionally, they may not be well-suited for on-premises environments. As an organization's resource and capacity needs grow, they may reach the maximum capacity offered by the hosted services provider, potentially limiting further growth.
- **Lack of Community:** The hosted Kubernetes platforms or Kubernetes management platforms usually are not open source, or even if part of their code is open source, they don't have a community behind them.
- **Dependence on the provider:** Users may depend on the provider to ensure the platform is available and running smoothly, which can be an issue if the provider experiences an outage or other problems. As they usually run on the public cloud, there are two sources of uncertainty, the public cloud provider infra and the software company providing the service.
- **EDGE Architecture:** As stated before, the best option depends on the user's concrete use case and circumstances. However, you may want smaller deployments (including management) to implement a most distributed architecture in different locations. In that case, the hosted platforms won't be the best option, but they can be a good fit if you plan a centralized management architecture and they have the capacity.
- **Data Security:** Data and who has access to it are always a concern for any organization. When you provide access to a third-party company to your clusters, you still have the responsibility over the data managed by your company, but there is a new source of potential troubles. Many companies have been hacked through third-party companies providing software or services.

### **The user profiles**

Once we have reviewed the pros and cons and have introduced the potential benefits of this type of solution are a good moment to elaborate on the different user profiles that would benefit from a hosted KMP service. Here, you’ll find some of them:

- **Startups:** Hosted platforms can provide a cost-effective and scalable solution for startups looking to deploy and manage applications on a Kubernetes cluster quickly.
- **Small to medium-sized businesses (SMBs):** SMBs can benefit from the expertise and support a hosted platform provides with outsourcing infrastructure management.
- **Developer teams:** Hosted platforms can help DevOps teams focus on developing and deploying applications rather than spending time managing the underlying infrastructure and the platform.
- **Heavy public cloud users:** Most hosted KMPs focus on Kubernetes-managed services like AKS, EKS or GKE. Organizations who have invested in the public cloud find that managed services fit very well with their strategy.

### **Conclusion**

Hosted Kubernetes management platforms are a good option if you are starting with Kubernetes and do not need to manage a large number of clusters and applications. They can also be a good choice when the cost is not a significant concern and you want your operations team to focus on innovation instead of maintenance tasks. However, when security is a high priority, or when EDGE or on-premises deployments are the focus of your IT strategy, there may be better options than hosted services.

At SUSE, we offer [Rancher Prime](https://www.rancher.com/products/rancher?utm_source=blog&utm_medium=blog&utm_campaign=Decoding_Kubernetes_Management_Platforms_Part_1) Hosted, which has the same features as Rancher but with a different approach. With Rancher Prime Hosted, you can easily create and manage Kubernetes clusters, streamline your deployment workflows, and monitor the performance of your applications. It also includes built-in security features to help protect your applications from potential threats. In addition, Rancher Prime Hosted provides a user-friendly interface that simplifies the management of your containerized applications and allows you to scale your infrastructure when your business demands it. Whether using a multi-cloud, [EDGE](https://www.suse.com/solutions/edge-computing/?utm_source=blog&utm_medium=blog&utm_campaign=Decoding_Kubernetes_Management_Platforms_Part_1), on-premises, or hybrid-cloud strategy, Rancher Prime Hosted can support your needs. By removing the burden of operating your Kubernetes management platform, your teams can focus on getting the most value out of your cloud native investment with a hosted Kubernetes management platform like Rancher Prime Hosted.
