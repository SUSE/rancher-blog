---
title: "Introducing Rio - Containers at Their Best"
date: 2019-05-21T09:06:00
slug: "introducing-rio-containers-at-their-best"
author: "Rancher Admin"
image: "images/rancher_blog_cable_car.jpg"
products: ["Rancher 1.x"]
tags: ["developer-experience"]
content_type: "release"
draft: true
migration:
  wp_id: 85866
  original_url: "https://www.suse.com/c/rancher_blog/introducing-rio-containers-at-their-best/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rio discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

Today I’m excited to announce a new Rancher Labs project called Rio. Rio is a MicroPaaS that can be layered on any standard Kubernetes cluster. Consisting of a few Kubernetes custom resources and a CLI to enhance the user experience, users can easily deploy services to Kubernetes and automatically get continuous delivery, DNS, HTTPS, routing, monitoring, autoscaling, canary deployments, git-triggered builds, and much more. All it takes to get going is an existing Kubernetes cluster and the rio CLI.

## Download the CLI

The CLI is available for macOS, Windows, and Linux. To perform an install on your local system, run the following command.

```
curl -sfL https://get.rio.io | sh -
```

If you’re uncomfortable piping curl output to a shell, you can also install Rio manually from <https://github.com/rancher/rio/releases>.

## Set Your Cluster Up for Rio

Rio uses the active Kubernetes cluster, so set `KUBECONFIG` to point to the cluster where you want to install Rio, and make sure you have the correct namespace selected.

(On an unrelated note - check out [kubectx](https://github.com/ahmetb/kubectx) for quick commands to change your Kubernetes context and namespace using tab completion and `fzf` for dynamic target selection.)

When you’re ready, run `rio install` to install Rio into the active cluster/namespace.

```
rio install
```

## Run a Sample Service

```
rio run https://github.com/rancher/rio-demo
```

## Check the Status

```
rio ps
rio console
```

## What’s a MicroPaaS?

PaaS offerings have always promised a set of desirable features, but historically PaaS systems have struggled to deliver an acceptable experience. They are often heavyweight and difficult to run requiring large dedicated projects to deploy them and afterwards a dedicated team to manage them. PaaS users often find them to be overly prescriptive and restrictive. They may work well with specific workflows, but those might not be the workflows the developer is comfortable with.

Rio comes from a line of Rancher Labs projects ([k3s](https://k3s.io), [k3OS](https://k3os.io)) that are focused on lightweight, simple, and flexible Kubernetes-based projects. All features are specifically designed to provide a sane default implementation to get you running right away, but with the flexibility to be configured, replaced, or disabled according to your needs. If you just want one feature in Rio you can use that and ignore the rest. This is all possible because Rio is very closely aligned with the Kubernetes ecosystem and draws heavily from it.

Rio consists of a few Kubernetes custom resources, an optional, yet delightful, CLI, and a controller that runs in your cluster. Running Rio is no different than running any other operator in your cluster.

## Rio Run

With a single command you can get a production-worthy service running:

```
rio run https://github.com/rancher/rio-demo
```

First, your service is automatically given a valid public DNS name. This even works if you are running Kubernetes on your laptop. Once we have a DNS name Rio will also request and assign a production [Let’s Encrypt](https://letsencrypt.org) certificate to your service. All services run by default as HTTPS.

Rio includes an integrated service mesh so all services get detailed visibility. Prometheus and Grafana are included with Rio and HTTP-level metrics are gathered by default.

By collecting HTTP-level metrics, Rio can autoscale your services using concurrency based scaling. By default, the concurrency is set to 10, so if 30 concurrent requests come in Rio will autoscale your service to 3. Rio can even scale your service to 0. This means no pods will run until the first request comes in.

If you tell Rio to run a git location it will watch and deploy from git as changes are pushed. One can still provide a Docker image to run directly, but git provides an easy continuous deployment flow. The git location must build a Docker image from source. By default, we run Dockerfile-based builds. Using multi-staged Dockerfile builds, this approach is very flexible. Additional templates can be used for builds to enable features such as buildpacks or OpenFaaS templates.

Rio, being powered by a service mesh, can easily do canary deployments. When a new git commit is pushed, a new revision of a service is automatically built and a new revision is deployed. Once the revision is ready we can then automatically roll out traffic to the new service by shifting weight from the prevision revision to the new one.

All of this functionality and much more is available from just a single simple `rio run` command.

## Try It Out Yourself

We are very excited to release Rio to the world today. Head over to <https://rio.io> for more information or just run `curl -sfL https://get.rio.io | sh -` and get started right now.
