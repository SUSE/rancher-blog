---
title: "Kubewarden v1.1.1 Is Out: Policy Manager For Kubernetes"
date: 2022-07-27T17:25:03
slug: "kubewarden-v1-1-1-is-out-kubernetes-policy-manager"
author: "Víctor Cuadrado Juan"
image: "images/icon-kubewarden.png"
products: ["Kubewarden"]
tags: ["policy"]
content_type: "release"
draft: false
migration:
  wp_id: 93379
  original_url: "https://www.suse.com/c/rancher_blog/kubewarden-v1-1-1-is-out-kubernetes-policy-manager/"
  disposition: migrate
  commercial: false
  outdated_reason: "Kubewarden v1.1.1 release notes"
  redirect_target: ""
---

We are happy to announce the first minor release of Kubewarden v1.0: **v1.1.1** is now available! For those of you new to [Kubewarden](https://www.kubewarden.io/), it is a policy manager for Kubernetes.

### **Changes**

Apart from being a nice-looking number, **v1.1.1** includes:

- Improved API policies for Sigstore verification by adding a new backward-compatible WaPC host callback `v2/verify` functions to the API. [Check them out here](https://docs.kubewarden.io/writing-policies/spec/host-capabilities/signature-verifier-policies) to add support for your language of choice. This has been used in the verify-image-signatures policy to simplify verification of GitHub Actions signatures and others. Read about it in [this blog post](https://www.kubewarden.io/blog/2022/07/verify-signatures-with-gha-and-prefix/).
- Made `policy-server` and `kwctl` resilient to hiccups in the upstream Sigstore’s repository for Fulcio and Rekor by making it optional. With this change, Kubewarden tools will proceed forward instead of aborting by informing the user and failing safely by issuing false negatives of signature verifications if needed. This overcomes last week's metadata update in the upstream Sigstore repository, which sadly was non-[TUF spec](https://theupdateframework.github.io/specification/latest)-compliant. This is also a part of the groundwork for making air-gapped installations easier to use.

Try it out! It is just a `helm upgrade` away, and as usual, we look forward to your feedback! :)

## **Next Steps: Learn More at the Kubewarden Meetup**

Join our Global Online Meetup: Kubewarden on Wednesday, August 10th, 2022, at 11 AM EST. Flavio Castelli from the Kubewarden team will tell you more about Kubewarden, give you a live demo and answer your questions. [Register now.](https://more.suse.com/global_rancher_online_meetup_kubewarden.html)
