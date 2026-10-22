---
title: "Epinio v0.2.0 Release    "
date: 2021-11-22T16:03:03
slug: "epinio-v0-2-0-release"
authors: ["Mario Manno"]
products: ["Epinio"]
tags: ["developer-experience"]
content_type: "release"
draft: true
migration:
  wp_id: 93190
  original_url: "https://www.suse.com/c/rancher_blog/epinio-v0-2-0-release/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Epinio discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

The new [Epinio v0.2.0](https://github.com/epinio/epinio/releases) is out and marks an important milestone.![](https://media1-production-mightynetworks.imgix.net/asset/31494529/epinio.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

This release adds Epinio to the Rancher UI dashboard, but that is not the only significant change; many more features have been added.

![](https://media1-production-mightynetworks.imgix.net/asset/31483644/epinio-screenshot-4.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

A future blog post might talk more about the new UI, but in short, once you install Epinio on your cluster, it shows up automatically in Rancher’s web interface. Then you can upload your app sources, which will automatically deploy. Please look at [Epinio UI installation instructions](https://github.com/epinio/ui/blob/beta2/README.md) for more instructions.

This update was possible due to redesigning the Epinio API server, making it easier to manage multiple users.

Under the hood, Epinio became more modular and can optionally use existing S3 storage and container registries. Gitea was removed, but Epinio can still deploy apps from a Git source, and Linkerd is also optional.

Upstream no longer maintains the service catalog component, so Epinio services are now just secrets containing the service’s connection details provided to the workloads. In contrast to the env var feature, the service secrets can be shared between applications.

This release was tested with more public, private, and local cluster offerings. You can find the growing list in the [installation docs](https://docs.epinio.io/installation/installation.html#installation-on-specific-kubernetes-offerings). Epinio v0.2.0 also comes with a [Helm chart](https://artifacthub.io/packages/helm/epinio/epinio) that supports the integration into Rancher.

Several improvements were implemented regarding the application workloads:

- Workloads are now deployed with a manifest. The manifest can also be generated from an existing workload.
- Application health is reported in more detail.
- Workloads were previously limited to the system domain. However, different domains per workload are now possible, and path-based routing is supported.

### [Get Started with Epinio!](https://epinio.io/)
