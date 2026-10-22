---
title: "Transport Layer Security Termination In Rancher 2.x, Part One"
date: 2020-02-04T10:11:00
slug: "transport-layer-security-termination-in-rancher-2-x-part-one"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_security.png"
products: ["Rancher Manager"]
tags: ["security", "installation"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 86432
  original_url: "https://www.suse.com/c/rancher_blog/transport-layer-security-termination-in-rancher-2-x-part-one/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Rancher 2.x docs, Docker install references"
  redirect_target: "docs.rancher.com"
---

## Introduction

In this blog series, we’ll explore a few different ways that Rancher uses TLS certificates. Here in in part one, we’ll look at UI security, agent<->API communication security and using self-signed certificates. In [part two](/blog/transport-layer-security-termination-in-rancher-2-x-part-two/), we’ll look at Let’s Encrypt and Bring-your-own certificates.

TLS, or Transport Layer Security, is a cryptographic protocol used to secure network communication. It is the successor to the now-deprecated Secure Sockets Layer, or SSL.

You can expect to walk away with an understanding of how TLS integrates into various Rancher components, and how you can prepare your environment to properly leverage TLS in Rancher.

## Why Transport Layer Security Matters

Rancher uses TLS *everywhere*. It’s important to determine your TLS termination option *before* you install Rancher.

1. Make sure you know what kind of TLS termination you want to do. This can be:
   1. Self-signed, terminated by Rancher. *This is the default.*
   2. Let’s Encrypt, terminated by Rancher.
   3. Bring-your-own certificates, terminated by Rancher.
   4. External TLS termination.
2. If you are doing options #3 or #4, make sure you have a copy of the CA certificate (just the cert, not the key) used to sign your certificate. Rancher needs this.
3. Make sure you know what hostname you want Rancher to use. ***This cannot be changed after installation.***

Also, read through our [documentation](https://rancher.com/docs). There are more details available there.

---

## Planning Your Approach to Transport Layer Security

With any enterprise software, you need to decide on specific requirements before installation and use. These include storage requirements, networking, cloud versus on-prem, etc. You should answer these questions before proceeding with installation.

For Rancher, one of these considerations is TLS. It is *essential* to understand and plan your approach to TLS with Rancher in order to arrive at a supported, well-functioning solution.

Besides HTTPS security, there are two other areas where TLS is important:

1. `kubectl`
2. Node and cluster agent communication

*This is not an exhaustive list of locations where TLS is used. Rather, these are the more common places where user interaction will coincide with TLS certificates.*

### Understanding `kubectl` TLS

Take a look at this sample `kubeconfig` file:

```
apiVersion: v1
kind: Config
clusters:
- name: "sample"
  cluster:
    server: "https://rancher.example.org/k8s/clusters/c-1234"
    certificate-authority-data: "LS0t..."
```

Note specifically the existence of `certificate-authority-data`. That field is a base64-encoded version of the CA certificate used to sign the TLS certificate that the Kubernetes API server presents. Or, in this case, the TLS certificate that *Rancher* presents when proxying calls to `kube-apiserver`.

Why is this important? `kubectl` uses this `certificate-authority-data` to ensure that you (not an imposter) are connecting to the correct cluster. If the certificate that is presented by the `server` has not been signed by the certificate in `certificate-authority-data`, `kubectl` warns you and exits. Basically, you are being protected from [MITM](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) attacks. Cool, huh?

The value in the `certificate-authority-data` is either going to be the CA certificate from `kube-ca` (non-Rancher clusters, and Rancher clusters using [Authorized Cluster Endpoint](https://rancher.com/docs/rancher/v2.x/en/cluster-provisioning/rke-clusters/options/#authorized-cluster-endpoint)), or the Rancher CA certificate (any Rancher cluster).

It’s important that the correct value be in this field, otherwise `kubectl` will not validate the connection to your Kubernetes cluster. That’s why you need to get the TLS configuration right when setting up Rancher.

### Understanding Node and Cluster Agent Communication

In any Rancher-connected cluster (imported or otherwise), two workloads are deployed:

1. `cattle-cluster-agent` Deployment
2. `cattle-node-agent` DaemonSet

Each of these workloads performs a specific function. Our [documentation](https://rancher.com/docs/rancher/v2.x/en/cluster-provisioning/rancher-agents/) has more information about these workloads. In summary, these two agents connect to Rancher’s API and establish a secure websocket connection on tcp/443. That websocket connection is then used for bidirectional communication between Rancher and the node or cluster being managed.

The cluster agent connects to the Kubernetes API of the managed cluster which allows Rancher to perform API actions via the websocket tunnel. The node agent is used to interact with nodes in an RKE cluster when performing cluster operations such as upgrades, etcd snapshots, etc.

These two agents both use a configuration value called “CA checksum,” passed as an environment variable to the pod as `CATTLE_CA_CHECKSUM`. The need for this value is the same as `kubectl` – to ensure connection to the correct endpoint and prevent MITM. However, the checksum works a little differently.

The CA checksum for the cattle agents verifies that the agents are connecting to the correct instance of the Rancher API. Since Rancher uses TLS to secure its HTTPS API endpoints, the agent containers can use this checksum to validate that the TLS certificate being presented by the API endpoint is correct.

Secondly, the `CATTLE_CA_CHECKSUM` is not configured as a base64-encoded copy of the CA certificate. Instead, Rancher generates a `sha256` checksum of the CA certificate used to sign the Rancher TLS certificate and places that value in the `CATTLE_CA_CHECKSUM` field. The result looks something like:

```
CATTLE_CA_CHECKSUM=b0af09b35ef086fcfc21e990fbd750720abe5c811dbea3ae40fe050a67f0bdb0e
```

When a Rancher cluster or node agent dials the Rancher API, it compares the CA certificate to the one configured in the Deployment or DaemonSet. If they match, communication is established.

## Transport Layer Security Termination

There are four main ways to terminate TLS when installing Rancher:

- Using Rancher’s self-signed certificates
- Using Let’s Encrypt
- Bringing your own certificates
- External TLS termination

Each one of these approaches has specific requirements and trade-offs.

## Using Rancher’s Self-Signed Certificates

Of the four options for terminating TLS, this is probably the most straightforward. It is also the option that Rancher uses by *default* in both HA and single-node installation scenarios. That is, by passing no TLS-specific arguments to either `helm` installation or `docker run`, Rancher will use this configuration.

Upon installation, Rancher generates a CA certificate (`CN=cattle-ca`) and uses that certificate to sign a cert for itself. There are some differences in how self-signed certificates work based on the type of installation you perform.

### Single Node Installation

Upon container start, but before setup, Rancher will respond on port 443 to any HTTPS requests, regardless of their destination `Host` value. How is that possible?

In this state, Rancher auto-generates a certificate for whichever hostname you reach it on. If that’s an IP such as 10.11.12.13, Rancher generate a self-signed (using `cattle-ca`) certificate for that IP. If you reach this new install of Rancher at a hostname, say `my-rancher.example.org`, the same thing (self-signing) occurs.

You need to go through the setup steps (set the admin password and confirm the Rancher hostname) before Rancher will use a single certificate. The certificate will be valid for the hostname configured during Rancher initial setup.

### HA Installation

Self-signed certificates in an HA install scenario require you to install an application called `cert-manager`. Instead of single node Rancher managing the CA certificate itself, HA rancher uses `cert-manager` to handle the certificate lifecycle. Follow the instructions [here](https://rancher.com/docs/rancher/v2.x/en/installation/ha/helm-rancher/#optional-install-cert-manager) to install `cert-manager` into the Kubernetes cluster you’ve prepared.

Once you’ve installed `cert-manager`, the next step is to install `rancher`. Using self-signed certificates is the default setting for Rancher, so there’s really only one mandatory argument when executing `helm install`:

```
--set hostname=<YOUR.DNS.NAME>
```

This argument is mandatory, since Rancher HA installations don’t have the same on-the-fly certificate generation capabilities as the single node install. So, once the you’ve set the hostname, that hostname will be used *for the lifetime of the Rancher install*. Be sure you set it correctly.

Then `cert-manager` generates a certificate. This certificate is stored as a secret in the `cattle-system` namespace with the name `tls-rancher-ingress`.

## Next Post: More Tranport Layer Security Termination Options

In [Part Two](/blog/transport-layer-security-termination-in-rancher-2-x-part-two/) in this series we’ll examine two more TLS termination types:

1. Using Let’s Encrypt
2. Bringing your own certificates

## More Resources

Watch the recent [Security Online Meetup](https://info.rancher.com/online-meetup-securing-production-k8s-clusters) to get the latest on security challenges in an Enterprise Kubernetes Strategy and the security-related features in Rancher.
