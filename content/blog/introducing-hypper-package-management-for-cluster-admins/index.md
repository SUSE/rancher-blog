---
title: "Introducing Hypper: Package Management For Cluster Admins"
date: 2021-05-11T20:29:19
slug: "introducing-hypper-package-management-for-cluster-admins"
authors: ["Matt Farina"]
products: ["Other"]
tags: ["installation"]
content_type: "release"
draft: true
migration:
  wp_id: 98120
  original_url: "https://www.suse.com/c/rancher_blog/introducing-hypper-package-management-for-cluster-admins/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Hypper project abandoned"
  redirect_target: "rancher.com/blog (hub)"
---

[Helm](https://helm.sh/) is the package manager for Kubernetes. It does a great job of enabling applications to be bundled up to be installed in [Kubernetes](https://k8s.io/). Applications can be installed in a way that fits Kubernetes - with multiple instances of applications per namespace and being installed in multiple namespaces.

Yet, cluster administrators have some slightly different needs. They deal with a cluster scope and have privileges to the cluster as a whole. Their use cases often deal with installing and managing cluster services. While Helm is great with packages in general, cluster administrators have long been outside Helm's scope. Helm focuses on application operators and distributors.

![](https://media1-production-mightynetworks.imgix.net/asset/23733833/icon-hypper.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

With that in mind, we (at SUSE) created [Hypper](https://hypper.io/). Hypper is a package manager for cluster administrators.

Hypper is pronounced hip-er and inspired by Zypper, the package manager for SUSE Linux distributions and Helm.

## Built on Helm and Charts

Hypper is built on Helm and charts. This means that once a workload has been installed with Hypper, it can later be managed with Helm or Hypper -- though we hope mostly with Hypper. Tools built to visualize instances of charts or otherwise work with them will also work with Hypper-installed charts.

![](https://media1-production-mightynetworks.imgix.net/asset/23687826/Hypper_Source_Layout_1_.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

This diagram highlights how Hypper works internally. Hypper has a client and SDK. Under the hood, they both use the Helm SDK. This means Hypper uses the same code as Helm to interact with repositories, charts, templates, releases, and Kubernetes.

The Hypper SDK means that other applications can be built on top of it. This is the same way that Helm is built.

What Hypper does differently from Helm is providing some more opinionated features on top of Helm and charts. Opinions targeting cluster administrators.

## Hypper Features

Hypper is under active development, which means features are being actively developed. After we look at a few features, we'll look at the roadmap ahead.

### Install With Release Name and Namespace

You may want to install some services once in every cluster with the same release name and into the same namespace. Logging and monitoring are common examples of this situation. If they are installed in the same location, other services can know where they are to work with them.

Hypper makes this possible by defining the release name and namespace within the *Chart.yaml* file. These are defined in the form of annotations.

```
annotations:
  hypper.cattle.io/namespace: example-namespace
  hypper.cattle.io/release-name: my-example-release
```

When these annotations are added to a chart, Hypper knows where you want to install the chart by default. These can be overridden when installing a chart. If these annotations are added to a normal Helm chart, you can run a command like the following one to install it.

```
$ hypper install mychart
```

In this case, *mychart* is the one with these annotations. Hypper will read the annotations and install it in the right place.

### Shared Dependencies

Sometimes you have multiple systems services that depend on other services. When you install one, you want to ensure another one is already installed. Yet, you don't want it installed like a typical Helm dependency because it's a system service. You want it set apart and managed as its own release. As a cluster singleton. Hypper makes this possible.

![](https://media1-production-mightynetworks.imgix.net/asset/23689550/Picture1.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

To define these dependencies, you again use annotations.

```
annotations:
  hypper.cattle.io/shared-dependencies: |
    - name: fleet
      version: "^0.3.500"
      repository: "https://rancher-sandbox.github.io/hypper-charts/repo"
    - name: rancher-tracing
      version: "^1.20.002"
      repository: "https://rancher-sandbox.github.io/hypper-charts/repo"
```

This example shows an annotation is used to define two dependencies. When the chart is installed, Hypper will ensure each dependency is installed first. These are installed as separate Helm releases.

Hypper knows where to look for those releases and where to install them because it uses the namespace and release name defined in the *Chart.yaml* file.

## Roadmap Ahead

We are rapidly adding new features to Hypper to improve the cluster admin experience. Three of these include:

- Optional/suggests dependencies
- A full SAT solver for dependencies
- Providing information on outdated dependencies running in a cluster

As Hypper is open source, you can contribute to the roadmap. [The project is on GitHub](https://github.com/rancher-sandbox/hypper) where you can download it, star it, file an issue or create a pull request.
