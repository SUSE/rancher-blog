---
title: "A Look at the First year of Kubewarden"
date: 2021-12-22T17:32:40
slug: "a-look-at-the-first-year-of-kubewarden"
authors: ["Flavio Castelli"]
image: "images/icon-kubewarden-1.svg"
products: ["Kubewarden"]
tags: ["policy"]
content_type: "community"
draft: true
migration:
  wp_id: 93038
  original_url: "https://www.suse.com/c/rancher_blog/a-look-at-the-first-year-of-kubewarden/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2021 year in review"
  redirect_target: "/kubewarden"
---

Let’s look back at what has been achieved during the first year of the Kubewarden project.

Finally, I’ll also talk about what we plan to do during the next one.

![Year Progress Bar](https://www.kubewarden.io/images/year-progress.png)

## 2021 Highlights

### Project Announcement

The Kubewarden project has been introduced to the masses for the 1st time during KubeCon Europe 2021. During this presentation, Rafael and I explained what led us to rethink how Kubernetes policies could be written and distributed. The talk recording can be found [here](http://www.youtube.com/watch?v=Bhw5Qi78jj8); watch it to understand Kubewarden’s mission better.

During the remainder of the year, Kubewarden talks featured at conferences like [KubeCon EU Security Day](https://www.youtube.com/watch?v=VF0-VPu6nW0&list=PLj6h78yzYM2ORbHrvs32QYLqfs080dqte&index=10), [Open Source Summit](https://www.youtube.com/watch?v=tDtAcSPr9Ig), [Container Days](https://www.youtube.com/watch?v=4a9aBTKKvzA), [KubeCon NA Wasm Day](https://www.youtube.com/watch?v=oNJxPbvPzLk), [Kubernetes Community Days Italy](https://www.youtube.com/watch?v=HqCXhD6Bckg&list=PLj6h78yzYM2M3cMd-zoDppjMo9eRmQrYU&index=2), and other live streaming events. What a year! ?

### The `kwctl` Utility

Shortly after KubeCon EU, we expanded the Kubewarden toolkit by releasing the [`kwctl`](https://github.com/kubewarden/kwctl/) utility.

This is a command line tool aimed at policy authors and Kubernetes operators. You can picture `kwctl` as a sort of `kubectl` for Kubewarden policies.

This tool is designed to allow quick iterative cycles both when developing policies (code → build → unit test → end-to-end tests → code ) and when gaining confidence with a policy written by a 3rd party (download → run → tune → run).

Kwctl became a central part of all our presentations. For example, you can see it in action during the [Rancher Global Online Meetup](https://www.youtube.com/watch?v=yh_L__CPqhc) of 2021.

### Become the Universal Policy Framework

Another achievement of 2021 has been the ability to execute policies written with Rego. For those unfamiliar with it, Rego is the query language used by Open Policy Agent and Gatekeeper.

Since Rego-based policies can be built into WebAssembly binaries, we extended all our tooling to be able also to handle the policies written for Open Policy Agent and Gatekeeper.

Thanks to that, you can use Kubewarden as the single Policy Engine to keep your Kubernetes clusters secure and compliant.

In case you missed it, [this blog post](https://www.kubewarden.io/blog/2021/09/towards-a-universal-policy-platform/) gives a detailed overview of this feature.

### Observability

One of the major topics we tackled during the last year has been observability.

We worked hard to provide a better observability story for our users: policy authors and operators. This culminated with tight integration between Kubewarden and the [OpenTelemetry project](https://opentelemetry.io/).

By leveraging OpenTelemetry, policy behavior can be analyzed using modern tracing techniques. Trace events can then be collected and inspected using tools like [Jaeger](https://www.jaegertracing.io/). You can learn more about that by reading [this blog post](https://www.kubewarden.io/blog/2021/11/deep-dive-into-policy-logging/).

Moreover, different metrics about policies and the whole Kubewarden stack have been exposed to Prometheus and made [visible in Grafana](https://grafana.com/grafana/dashboards/15314). This allows tight integration with the monitoring ecosystem that most Kubernetes operators already use.

### Life after Pod Security Policy removal

Lately, we have been focusing on providing 1:1 alternatives to the deprecated and soon-dropped [Kubernetes Pod Security Policies](https://kubernetes.io/docs/concepts/policy/pod-security-policy/).

All the original PSPs can now be replaced with Kubewarden policies. You can find all these policies, and even more, on [Kubewarden Policy Hub](https://hub.kubewarden.io/).

When talking about migrating from Kubernetes Pod Security Policies to something maintained, we highly recommend looking at [this](https://github.com/appvia/psp-migration) ongoing work from [AppVia](https://www.appvia.io/). They even made [this](https://appvia.github.io/psp-migration/) fancy UI that allows you to convert a Pod Security Policy to a Kubewarden one! ?

## What to expect from 2022

What should you expect from the Kubewarden project in 2022? Well, our roadmap is [publicly available](https://github.com/orgs/kubewarden/projects/2); however, these are the key points:

### Secure Supply Chain

Due to an unfortunate series of exploits, the topic of a secure supply chain became one of the highest trending topics in the entire IT industry in 2021.

We are currently working to integrate [Sigstore](https://www.sigstore.dev/) into Kubewarden. The integration is tackled from two different angles:

First, we will use Sigstore to sign all the Kubewarden policies available on the Kubewarden Policy Hub. The Policy Server and `kwctl` will be able to consume this information to verify the trustworthiness of the policies before executing them.

Finally, we will expose Sigstore verification API to our policy authors. This will make it possible to create policies that verify the trustworthiness of container images and any other kind of artifacts that can be signed with Sigstore.

We will also provide a ready-to-use policy that implements the most common security checks.

### New Policy Operation Modes

Right now, when deploying Kubewarden policies inside of a Kubernetes cluster, their only operational mode is “enforce.” That means resources violating policies are immediately rejected.

We want to introduce new operation modes to allow Kubernetes operators to deploy the policies in a more “relaxed” way. This can be useful to understand what could be blocked by Kubewarden policies ahead of time.

### Background Scan

Policies inside of a Kubernetes cluster change over time, so they can be added/removed/updated; the same applies to their configuration. Because of that, previously considered acceptable resources could be rejected due to one of these changes.

We want to provide a way for Kubernetes operators to know the compliance status of their clusters. The goal is to simplify the identification of the already existing Kubernetes resources violating the enforced policies.

### Context-Aware Policies

Kubewarden already supports the concept of “context-aware policies.” These are policies that, at evaluation time, can pull additional information about the cluster status to make their final decision.

We have ambitious goals for this feature. We plan to work more on this story and graduate context-aware policies to be fully supported.

## Call for Action

Do you want to learn more about Kubewarden? Excellent!

Start by looking at our [quickstart](https://docs.kubewarden.io/quick-start.html) guide. It will take a few minutes to get Kubewarden up and running and enforce your first policy!

Don’t forget to look at [this page](https://docs.kubewarden.io/tasks.html) to know what to do next!

Lastly, make sure to look at [this](https://www.youtube.com/watch?v=w2tUQUoizP4) video tutorial from [Robert Sirchia](https://twitter.com/robertsirc).
