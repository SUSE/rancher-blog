---
title: "Kubewarden 1.6.0 is Released!"
date: 2023-04-20T16:51:48
slug: "kubewarden-1-6-0-is-released"
authors: ["Flavio Castelli"]
image: "images/kubewarden.webp"
products: ["Kubewarden"]
tags: ["security", "policy"]
content_type: "release"
draft: false
migration:
  wp_id: 104649
  original_url: "https://www.suse.com/c/rancher_blog/kubewarden-1-6-0-is-released/"
  disposition: migrate
  commercial: false
  outdated_reason: "Kubewarden 1.6.0 release"
  redirect_target: ""
---

We are pleased to announce the availability of the Kubewarden 1.6.0 stack.

This release brings stability, performance and security improvements; all packed with a new major feature. Let’s dig into the changes!

## Security Improvements

The Kubewarden controller is run using a dedicated Service Account. Before this release, the Service Account had access to a series of Kubernetes resources across the entire cluster.

Starting from this release, the Kubewarden controller Service Account has more limited access to the cluster. Access to some resources is now tied to the Namespace inside of which the controller is deployed.

This reduces an attacker's impact if he manages to steal the Service Account used by our controller.

This security issue was reported by [Nanzi Yang](https://github.com/younaman) during an independent security audit. This issue has been assigned the following CVE `CVE-2023-22645`.

This change not only improved the security posture of the controller but also reduced its memory consumption and made it more responsive.

## Context-Aware Policies

The majority of the policies operate in “isolation,” meaning that at evaluation time, they can decide by using only the information provided by the Kubernetes API server.

On the opposite, a Context-Aware Policy requires access to Kubernetes-related information. For example, a Context-Aware Policy that monitors the creation of Ingress objects could request the list of already existing Ingresses during its evaluation time. Based on this data, the policy would be able to understand whether the soon-to-be-created Ingress object would conflict with any of the existing Ingresses.

Context-Aware Policies have read-only access to the cluster. At deployment time, the Kubernetes administrator will define the list of Kubernetes resources the policy has access. The Kubewarden platform will block access to any Kubernetes resources that the Kubernetes administrator didn’t approve.

The allow list is defined on a per-policy basis, making it possible to have really granular access to the Kubernetes resources.

For more details, take a look at [this](https://docs.kubewarden.io/explanations/context-aware-policies) section of our documentation.

## Give it a try!

You can use our official helm chart to upgrade to the latest version.

You can reach out to us on [Slack](https://kubernetes.slack.com/?redir=%2Fmessages%2Fkubewarden) or join our [monthly community meeting](https://teamup.com/ks2bj74dvw132mhjtj?view=a&showProfileAndInfo=0&showSidepanel=1&disableSidepanel=1&showMenu=1&showAgendaHeader=1&showAgendaDetails=0&showYearViewHeader=1) to talk more about Kubewarden!
