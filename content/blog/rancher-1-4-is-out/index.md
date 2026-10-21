---
title: "Rancher 1.4 is out!"
date: 2017-02-06T11:14:00
slug: "rancher-1-4-is-out"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["upgrades"]
content_type: "release"
draft: true
migration:
  wp_id: 86881
  original_url: "https://www.suse.com/c/rancher_blog/rancher-1-4-is-out/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x release"
  redirect_target: "rancher.com/blog (hub)"
---

[![](images/rancher_blog_rancher-logo_stacked-full-color-1-300x157.jpg)](https://cdn.rancher.com/wp-content/uploads/2017/02/05132759/rancher-logo_stacked-full-color-1.jpg)Rancher
1.4 is out today! As always, we encourage you [to review the release
notes](https://github.com/rancher/rancher/releases/tag/v1.4.0). However,
we’d like to run through a few notable changes, and the rationale behind
them here. First, we’ve continued our move towards a friendlier
Kubernetes experience by transitioning to
[Dashboard](https://github.com/kubernetes/dashboard) and
[Helm](https://github.com/kubernetes/helm), which replace the Rancher
Kubernetes UI and Catalog Kubernetes templates, respectively. We started
this move in 1.3 as both Dashboard and Helm have matured tremendously in
the past year, and we feel they’ve reached production stability and
feature parity with what they’re replacing. Our goal at Rancher Labs is
always to support mainstream container technologies, and integrating
Dashboard and Helm is a natural part of that philosophy. In this
release, we’re also including:

**Webhooks:** Naturally, as container usage grows, so does demand for
webhooks as both are well-suited for optimizing your infrastructure
usage. In Rancher 1.4, we implement
[webhooks](https://docs.rancher.com/rancher/v1.4/en/cattle/webhook-service/)
as its own microservice, and an initial driver for scaling. We’ll dive
into this in more detail with another blog post this week, but we’re
pleased to begin working more with our community on webhooks,
particularly on new drivers and functionality.

**Network Policies**: Starting with 1.4, we will provide more fine
grained control of network policies within an environment. Initially, we
will allow the ability to set basic ALLOW or DENY default policies for
container network access. With each subsequent release, more features,
such as allowing inter-service access but denying intra-service
communications, will be possible.

**Secrets Management**: In 1.4, we’ve also introduced the ability to
handle secrets within Rancher using [Vault
Transit](https://www.vaultproject.io/docs/secrets/transit/). Previously,
secrets could be managed with third-party solutions via Rancher catalog,
but as growing numbers of users utilize Rancher and containers in
production, it makes sense to build this functionality directly into our
platform.

We invite you to [download the latest
version](https://github.com/rancher/rancher) and let us know what you think. Our product grows and evolves based on what our users need and request.
Please let us know in the forums, or on Twitter
[@Rancher\_Labs](http://twitter.com/rancher_labs). **To get started
with Rancher 1.4, join our free, monthly online training:**

- **Date**: Thursday, February 9th (online)
- **Time**: 1 PM, US Eastern Time

[[ [![Register
Now](https://no-cache.hubspot.com/cta/default/468859/d89352ca-9dc8-49fa-95a1-d7cdf4a963e3.png)](http://cta-redirect.hubspot.com/cta/redirect/468859/d89352ca-9dc8-49fa-95a1-d7cdf4a963e3)
]
]
