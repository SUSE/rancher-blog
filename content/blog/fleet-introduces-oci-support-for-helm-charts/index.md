---
title: "Fleet Introduces OCI Support for Helm Charts"
date: 2022-11-29T15:49:31
slug: "fleet-introduces-oci-support-for-helm-charts"
authors: ["Mario Manno"]
image: "images/icon-fleet.png"
products: ["Fleet"]
tags: ["gitops"]
content_type: "release"
draft: false
migration:
  wp_id: 97643
  original_url: "https://www.suse.com/c/rancher_blog/fleet-introduces-oci-support-for-helm-charts/"
  disposition: migrate
  commercial: false
  outdated_reason: "Fleet 0.5.0 / Rancher 2.7.0 release news"
  redirect_target: ""
---

Rancher, the open source container management platform, uses Fleet to enable its continuous deployment features. Fleet brings GitOps functionality to Rancher.

Fleet in Rancher 2.7.0 can fetch Helm charts from OCI registries. Using OCI registries to store Helm charts is an increasingly popular storage method. It allows storing your charts in a registry alongside your container images. This unifies the storage options for charts and reduces friction.

Using a chart in an OCI registry is fairly simple. In your git repository, you reference the chart like this in a `fleet.yaml` file:

```
helm:
  chart: "oci://ghcr.io/fleetrepoci/guestbook"
```

You can use the version key if you want to reference a specific chart version.

```
helm:
  chart: "oci://ghcr.io/fleetrepoci/guestbook"
  version: 0.1.0
```

To use authenticated registries the GitRepo resource needs to [reference a k8s secret](https://github.com/rancher/fleet/blob/master/e2e/assets/single-cluster/helm-oci-with-auth.yaml).
Try it out with Fleet [v0.5.0](https://github.com/rancher/fleet/releases/tag/v0.5.0) or in Rancher [v2.7.0](https://github.com/rancher/rancher/releases/tag/v2.7.0). You can learn more about using Fleet with and without OCI registries in the [Fleet documentation](https://fleet.rancher.io/).
