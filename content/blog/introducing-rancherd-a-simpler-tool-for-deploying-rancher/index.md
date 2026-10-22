---
title: "Introducing RancherD: A Simpler Tool for Deploying Rancher"
date: 2020-10-06T09:57:00
slug: "introducing-rancherd-a-simpler-tool-for-deploying-rancher"
author: "Rancher Admin"
image: "images/rancher_blog_rancher-2-5-blog-featured.png"
products: ["Other"]
tags: ["installation"]
content_type: "release"
draft: true
migration:
  wp_id: 86320
  original_url: "https://www.suse.com/c/rancher_blog/introducing-rancherd-a-simpler-tool-for-deploying-rancher/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RancherD discontinued"
  redirect_target: "docs.rancher.com"
---

Discover what’s new in Rancher 2.5[Learn More](https://www.rancher.com/products)

As part of Rancher 2.5, we are excited to introduce a new, simpler way to install Rancher called RancherD.

RancherD is a single binary you can launch on a host to bring up a Kubernetes cluster bundled with a deployment of Rancher itself.

This means you just have one thing to manage: RancherD. Configuration and upgrading are no longer two-step processes where you first have to deal with the underlying Kubernetes cluster and *then* deal with the Rancher deployment.

> **Note:** This feature is still in preview as we gather feedback about its usability and address bugs found by the community. It’s not quite ready for production use.

## Getting Started with RancherD

Let’s take a look at how you can get started with RancherD.

First, run the installer:

```
curl -sfL https://get.rancher.io | sh -
```

This will download RancherD and install it as a systemd unit on your host.

> If that systemd note caught your eye: yes, at this time, only OSes that leverage systemd are supported.

Once installed, the `rancherd` binary will be on your path. You can check out its help text like this:

```
rancherd --help
NAME:
   rancherd - Rancher Kubernetes Engine 2

USAGE:
   rancherd [global options] command [command options] [arguments...]

VERSION:
   v2.5.0-rc8 (HEAD)

COMMANDS:
   server       Run management server
   agent        Run node agent
   reset-admin  Bootstrap and reset admin password
   help, h      Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --debug        Turn on debug logs [$RKE2_DEBUG]
   --help, -h     show help
   --version, -v  print the version
```

Next, let’s launch RancherD. You can launch the binary directly via `rancherd server`, but we’re going to stick with the systemd service for this demo.

```
systemctl enable rancherd-server.service
systemctl start rancherd-server.service
```

You can follow the logs of the cluster coming up thusly:

```
journalctl -eu rancherd-server -f
```

It will take a couple minutes to come up.

Once the cluster is up and the logs have stabilized, you can start interacting with the cluster. Here’s how:

First, setup RancherD’s kubeconfig file and kubectl:

```
export KUBECONFIG=/etc/rancher/rke2/rke2.yaml PATH=$PATH:/var/lib/rancher/rke2/bin
```

Now, you can start issuing kubectl commands. Rancher is deployed as a daemonset on the cluster, let’s take a look:

```
kubectl get daemonset rancher -n cattle-system

kubectl get pod -n cattle-system
```

We’re almost ready to jump into the Rancher UI, but first you need to set the initial Rancher password. Once the `rancher` pod is up and running, run the following:

```
rancherd reset-admin
```

This will give you the URL, username and password needed to log into Rancher. Follow that URL, plug in the credentials, and you’re up and running with Rancher!

## A Few Advanced Options in RancherD

*But wait there’s more!*

I’d like to answer a few advanced configuration questions that you might ask once you start trying this out.

**How do I get a highly available cluster?**

This is as simple as adding nodes to the cluster. Since Rancher is running as a daemonset, it will automatically launch on the nodes you add.

*Important:* For HA, you need an odd number of nodes in your RancherD cluster. We recommend three.

As mentioned, RancherD is powered by our new Kubernetes distribution, RKE Government (also known as RKE2). [Check out its documentation](https://docs.rke2.io/install/ha/) for adding nodes to an HA cluster.

**How do I customize the Rancher application?**

Rancher is launched as a [Helm](https://helm.sh/) chart using the cluster’s [Helm integration](https://docs.rke2.io/helm/). This means that you can easily customize the application through a manifest file describing your custom parameters. See our [chart customization doc](https://github.com/rancher/rancher/tree/master/cmd/rancherd/chart#customize-chart) for more details.

**How do I configure Rancher to use my custom SSL certificates?**

RancherD allows you to bring your own self-signed or trusted certs by storing the .pem files in `/etc/rancher/ssl/`. When doing this you should also set the `publicCA` parameter to `true` in your HelmChartConfig (see above about customizing the Rancher application). You can see more details in our [cert configuration doc](https://github.com/rancher/rancher/tree/master/cmd/rancherd/chart#configuring-certs-for-rancher-server).

## Conclusion

That wraps up our introduction to RancherD. We’re very excited to preview this feature and look forward to hearing your feedback. To learn more about our new Kubernetes distribution that powers this, [visit here](https://docs.rke2.io/). If you find problems or have questions you can [reach us on Slack](https://slack.rancher.io/) or [open an issue](https://github.com/rancher/rancher/issues/new).

Discover what’s new in Rancher 2.5[Learn More](https://www.rancher.com/products)
