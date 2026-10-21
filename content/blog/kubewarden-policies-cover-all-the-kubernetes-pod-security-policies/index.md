---
title: "Kubewarden policies cover all the Kubernetes Pod Security Policies"
date: 2022-01-21T17:33:12
slug: "kubewarden-policies-cover-all-the-kubernetes-pod-security-policies"
authors: ["Flavio Castelli"]
products: ["Kubewarden"]
tags: ["policy", "security"]
content_type: "release"
draft: false
migration:
  wp_id: 92977
  original_url: "https://www.suse.com/c/rancher_blog/kubewarden-policies-cover-all-the-kubernetes-pod-security-policies/"
  disposition: migrate
  commercial: false
  outdated_reason: "PodSecurityPolicy removed"
  redirect_target: ""
---

##### *Post originally published on*[*Kubewarden's blog*](https://kubewarden.io/blog) *by José Guilherme Vanz*

The Kubewarden team worked tirelessly to create equivalent Kubewarden policies for all the deprecated Pod Security Policies (PSP). To reach this significant milestone, the team wrote the policies with the same validations available in the Kubernetes PSPs. We counted on the community's help to map and validate the policies. This will allow our users to replace deprecated PSPs while continuing to enforce their security rules.

The Kubewarden policies, which replace all the Kubernetes PSPs, are available in the [Policy Hub](https://hub.kubewarden.io/), and you can find them by typing the keyword "PSP." And, to have the exact same behavior of the Kubernetes PSPs is necessary a minimum version for some of the Kubewarden components, which are:

- Kubewarden controller v0.4.5
- Policy Server version v0.2.6

You may be thinking: Why do I need to use these specific versions?

The answer is related to "requests mutation." Let me explain.

In the previous versions of the Kubewarden Policy Server, if a policy mutated a request and configured as a "mutating" policy, the Policy Server would always accept the request, which is not aligned with the Kubernetes PSP validation.

Instead, you should be able to reject a request even if a mutation happens. To solve this misalignment, the team changed the Kubewarden controller and Policy Server to allow you to configure a mutating policy to behave like a validated one. However, if you don't need it, you can also use the policies in previous Kubewarden versions.

Since the Kubewarden controller and Policy Server versions update, if you mark a policy as "mutating" (setting `true` in the "mutating" field in the ClusterAdmissionPolicy resource), the mutated requests will be accepted as before. On the other hand, if you deploy a policy that mutates requests with the "mutating" field set to`false`, the requests will be rejected.

This means Kubewarden now have policies that cover 100% of the deprecated PSPs, and they behave the same way as the PSPs.

We thank the community for helping the team spot missing policies and the discrepancies between the Kubernetes PSPs and Kubewarden policies. The combined work is what made Kubewarden reach this critical milestone.
