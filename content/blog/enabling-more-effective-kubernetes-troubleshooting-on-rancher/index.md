---
title: "Enabling More Effective Kubernetes Troubleshooting on Rancher"
date: 2020-04-16T09:48:00
slug: "enabling-more-effective-kubernetes-troubleshooting-on-rancher"
author: "Rancher Admin"
image: "images/rancher_blog_kubernetes-troubleshooting-featured.png"
products: ["Rancher Manager"]
tags: ["networking", "observability"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86070
  original_url: "https://www.suse.com/c/rancher_blog/enabling-more-effective-kubernetes-troubleshooting-on-rancher/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 2.x and Calico tooling from 2020"
  redirect_target: "https://www.rancher.com/blog/debugging-your-rancher-kubernetes-cluster-the-genai-way-with-k8sgpt-ollama-rancher-desktop/"
---

As a leading, open-source multi-cluster orchestration platform, Rancher lets operations teams deploy, manage and secure enterprise Kubernetes. Rancher also gives users a set of container network interface (CNI) options to choose from, including open source [Project Calico](https://www.projectcalico.org/). Calico provides native Layer 3 routing capability for Kubernetes pods, which simplifies the networking architecture, increases networking performance and provides a rich network policy model makes it easy to lock down communication so the only traffic that flows is the traffic you want to flow.

A common challenge in deploying Kubernetes is gaining the necessary visibility into the cluster environment to effectively monitor and troubleshoot networking and security issues. [Visibility and troubleshooting](https://www.tigera.io/tigera-products/visibility-and-troubleshooting/) is one of the top three Kubernetes use cases that we see at Tigera. It’s especially critical in production deployments because downtime is expensive and distributed applications are extremely hard to troubleshoot. If you’re with the platform team, you’re under pressure to meet SLAs. If you’re on the DevOps team, you have production workloads you need to launch. For both teams, the common goal is to resolve the problem as quickly as possible.

## Why Troubleshooting Kubernetes is Challenging

Since Kubernetes workloads are extremely dynamic, connectivity issues are difficult to resolve. Conventional network monitoring tools were designed for static environments. They don’t understand Kubernetes context and are not effective when applied to Kubernetes. Without Kubernetes-specific diagnostic tools, troubleshooting for platform teams is an exercise in frustration. For example, when a pod-to-pod connection is denied, it’s nearly impossible to identify which network security policy denied the traffic. You can manually log in to nodes and review system logs, but this is neither practical nor scalable.

You’ll need a way to quickly pinpoint the source of any connectivity or security issue. Or better yet, gain insight to avoid issues in the first place. As Kubernetes deployments scale up, the limitations around visibility, monitoring and logging can result in undiagnosed system failures that cause service interruptions and impact customer satisfaction and your business.

## Flow Logs and Flow Visualization

For Rancher users who are running production environments, [Calico Enterprise](https://www.tigera.io/tigera-products/calico-enterprise/) network flow logs provide a strong foundation for [troubleshooting Kubernetes](https://www.suse.com/c/observability-the-total-kubernetes-troubleshooting-guide/) networking and security issues. For example, flow logs can be used to run queries to analyze all traffic from a given namespace or workload label. But to effectively troubleshoot your Kubernetes environment, you’ll need flow logs with Kubernetes-specific data like pod, label and namespace, and which policies accepted or denied the connection.

![Calico Enterprise Flow Visualizer](images/rancher_blog_image1.png)

Calico Enterprise Flow Visualizer

A large proportion of Rancher users are DevOps teams. While ITOps has traditionally managed network and security policy, we see DevOps teams looking for solutions that enable self-sufficiency and accelerate the CI/CD pipeline. For Rancher users who are running production environments, Calico Enterprise includes a Flow Visualizer, a powerful tool that simplifies connectivity troubleshooting. It’s a more intuitive way to interact with and drill down into network flows. DevOps can use this tool for troubleshooting and policy creation, while ITOps can establish a policy hierarchy using RBAC to implement guardrails so DevOps teams don’t override any enterprisewide policies.

## Firewalls Can Create a Visibility Void for Security Teams

Kubernetes workloads make heavy use of the network and generate a lot of east/west traffic. If you are deploying a conventional firewall within your Kubernetes architecture, you will lose all visibility into this traffic and the ability to troubleshoot. Firewalls don’t have the context required to understand Kubernetes traffic (namespace, pod, labels, container id, etc.). This makes it impossible to troubleshoot networking issues, perform forensic analysis or report on security controls for compliance.

To get the visibility they need, Rancher users can deploy Calico Enterprise to translate zone-based firewall rules into Kubernetes network policies that segment the cluster into zones and apply the correct firewall rules. Your existing firewalls and firewall managers can then be used to define zones and create rules in Kubernetes the same way all other rules have been created. Traffic crossing zones can be sent to the Security team’s security information and event management (SIEM), providing them with the same visibility for troubleshooting purposes that they would have received using their conventional firewall.

## Other Kubernetes Troubleshooting Considerations

For Platform, Networking, DevOps and Security teams using the Rancher platform, Tigera provides additional visibility and monitoring tools that facilitate faster troubleshooting:

- The ability to add thresholds and alarms to all of your monitored data. For example, a spike in denied traffic triggers an alarm to your DevOps team or Security Operations Center (SOC) for further investigation.
- Filters that enable you to drill down by namespace, pod and view status (such as allowed or denied traffic)
- The ability to store logs in an EFK (Elasticsearch, Fluentd and Kibana) stack for future accessibility

Whether you are in the early stages of your Kubernetes journey and simply want to understand the “why” of unexpected cluster behavior, or you are in large-scale production with revenue-generating workloads, having the right tools to effectively troubleshoot will help you avoid downtime and service disruption. During the upcoming Master Class, we’ll share troubleshooting tips and demonstrate some of the tools covered in this blog, including flow logs and Flow Visualizer.

Join our [free Master Class: Enabling More Effective Kubernetes Troubleshooting on Rancher](https://info.rancher.com/kubernetes-master-class-may7-2020-tigera) on May 7 at 1pm PT.
