---
title: "Announcing the Elemental CAPI Infrastructure Provider"
date: 2023-12-14T17:44:38
slug: "announcing-the-elemental-capi-infrastructure-provider"
author: "andrea.mazzotti@suse.com"
products: ["Elemental"]
tags: ["edge", "multi-cluster"]
content_type: "release"
draft: false
migration:
  wp_id: 120637
  original_url: "https://www.suse.com/c/rancher_blog/announcing-the-elemental-capi-infrastructure-provider/"
  disposition: migrate
  commercial: false
  outdated_reason: "Pilot announcement, superseded"
  redirect_target: ""
---

# **Elemental CAPI Infrastructure Provider**

Within the last few months, we’ve worked on bringing the [Elemental toolkit](https://rancher.github.io/elemental-toolkit/docs/) into the Kubernetes Cluster API ecosystem. [Cluster API](https://cluster-api.sigs.k8s.io/) is a Kubernetes sub-project focused on providing declarative APIs and tooling to simplify provisioning, upgrading, and operating multiple Kubernetes clusters.

A pilot of the [Elemental CAPI Infrastructure Provider](https://github.com/rancher-sandbox/cluster-api-provider-elemental) is available for you to try. You can deploy the provider in any CAPI-enabled management cluster and use it to automatically bootstrap any bare metal host. The integration with the Elemental toolkit provides full lifecycle support for hosts, from installation to reset and repurposing.

 Integration with Rancher can be enabled by installing the [Rancher Turtles](https://docs.rancher-turtles.com/) extension. You can follow this [guide](https://github.com/rancher-sandbox/cluster-api-provider-elemental/blob/main/doc/RANCHER.md) on how to use the Rancher Turtles integration to import your Elemental CAPI cluster into Rancher.

 The goal for this project is to reach feature parity with the current [Elemental operator](https://elemental.docs.rancher.com/). However, the core features, like managed OS image channels, downloadable images and automated system upgrades, have not yet been implemented.

 

## **Features**

1. **CAPI Infrastructure Provider:** This provider implements the CAPI [Machine Infrastructure](https://cluster-api.sigs.k8s.io/developer/providers/machine-infrastructure) and [Cluster Infrastructure](https://cluster-api.sigs.k8s.io/developer/providers/cluster-infrastructure) contracts.

 

2. [**clusterctl**](https://cluster-api.sigs.k8s.io/clusterctl/overview) **support:** You can use `clusterctl` to init this provider into any CAPI management cluster. `clusterctl` can also be used to generate CAPI Cluster manifests. [k3s](https://github.com/cluster-api-provider-k3s/cluster-api-k3s) and [rke2](https://github.com/rancher-sandbox/cluster-api-provider-rke2) template flavors are supported by this project.

 

3. [**Elemental CAPI Agent**](https://github.com/rancher-sandbox/cluster-api-provider-elemental/blob/main/cmd/agent/README.md): The elemental agent can be installed into any machine to provide inventory management and CAPI bootstrapping capabilities.

 

4. [**OS Management interface**](https://github.com/rancher-sandbox/cluster-api-provider-elemental/blob/main/cmd/agent/README.md#plugins): The elemental-agent can be extended with plugins to embed your custom operating system logic.

 

5. [**Registration tokens and host identity**](https://github.com/rancher-sandbox/cluster-api-provider-elemental/blob/main/doc/AUTH.md): Tokens allow only trusted hosts to register with the Elemental CAPI Provider. Each host also comes with its own identity to forbid impersonation and add a layer of trust once a new host is registered.

 

## **What's Next?**

We seek your feedback on improving and enhancing our Cluster API Elemental story and accelerating our journey toward GA next year. We are working with the upstream community on day-2 operations like in-place upgrades in Cluster API. In-place upgrades utilize fewer resources, which matters in many edge use cases. Don’t forget to check out [Cluster API Office Hours](https://www.youtube.com/watch?v=rhNCUWReca4&t=487s) to better understand the CAPI Infrastructure Provider. 

Lastly, If you would like to participate in the Early Adopter Program and collaborate closely with CAPI in Rancher, please reach out to your Account Manager or directly to [david.stauffer@suse.com](mailto:david.stauffer@suse.com)

Please don't hesitate to reach out with your thoughts, feedback or questions.
