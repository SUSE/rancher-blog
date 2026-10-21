---
title: "Introducing Epinio 0.6:  Smaller, Faster *and* More Capable!"
date: 2022-03-14T19:20:36
slug: "introducing-epinio-0-6-smaller-faster-and-more-capable"
author: "Andrew Gracey"
image: "images/icon-epinio.png"
products: ["Epinio"]
tags: ["developer-experience"]
content_type: "release"
draft: true
migration:
  wp_id: 90473
  original_url: "https://www.suse.com/c/rancher_blog/introducing-epinio-0-6-smaller-faster-and-more-capable/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Epinio discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

With our latest releases of Epinio, we’ve focused on making both the setup and developer experience much more streamlined. We’ve looked at where users are having issues and removed many of the roadblocks. This reduced footprint also allows for more customizability and easier long-term maintenance.

If you are not familiar with Epinio, it is an [application development engine for Kubernetes](https://epinio.io) that lets you go from code to URL in a single step. This allows for a better Developer Experience without needing to learn all of Kubernetes.

# What’s new

## Access shell on workloads

Sometimes during development, you might need to access the pod that’s running your workload to check assumptions and try simple changes. To make this possible, we’ve added the `epinio app exec` command which will drop you into a bash session without needing to know how to find the right pod and exec into it with `kubectl`.

## Port forward and attaching debuggers

Similarly, we’ve added the ability to port-forward an app to your localhost. This can be useful in a few ways, namely, attaching a debugger to your app to set breakpoint or see the current stack! To do so, use `epinio app port-forward`.

## Simplified installation

We’ve made several of the components optional so we could pull all of the installation into a single chart. The only thing now that’s needed prior to installation is cert-manager (<https://cert-manager.io/docs/installation/>) and any Kubernetes ingress controller (which comes default with K3s, RKE2 and Rancher Desktop!)

## Faster builds

By simplifying the build process, we were able to reduce the build time significantly. Now you can see the results of your latest changes sooner.

## Application customizability

For our first step in allowing more control over what gets deployed, we’ve moved the spec for what’s deployed when a developer pushes their code from in our code to a Helm chart. While editing this chart is not easy at the moment, we will continue working to extend this functionality in the next few milestones.

## Web UI

We've also built out a Web UI to allow for better discovery of features and management of applications. Through this UI you can do much of what the CLI allows and we are working to close the gap quickly!

# What’s next

Our next steps will be around filling out some of the functionality to better enable developers and operators to work more closely with each other. We are also taking some time to improve our documentation to catch them up to the most recent changes.

We have two upcoming milestones: one for Operators and one for Developers

# Try it out

Epinio can be installed using Helm onto any compliant Kubernetes Cluster. The latest CLI release can be found at <https://github.com/epinio/epinio/releases>

On Rancher Desktop, the install looks like this:

```
$ kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.7.1/cert-manager.yaml
$ helm repo add epinio https://epinio.github.io/helm-charts
$ INGRESS_IP=`kubectl describe svc traefik --namespace kube-system |awk '/Ingress/ { print $3 }'`
$ helm upgrade --install epinio epinio/epinio -n epinio --create-namespace --set global.domain=$INGRESS_IP.sslip.io
$ epinio config update
```

For other clusters check out our [documentation](https://docs.epinio.io/installation/installation.html).

If you like this project, help us out by playing with it and letting us know what you would like to see in our GitHub project.

![](images/icon-epinio-300x248.png)
