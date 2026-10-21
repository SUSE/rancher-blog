---
title: "Installing and Running Kubewarden In Air-Gapped Environments"
date: 2022-11-29T21:16:27
slug: "installing-and-running-kubewarden-in-air-gapped-environments"
authors: ["Raul Cabello"]
image: "images/m7brY_b9_400x400.jpg"
products: ["Kubewarden"]
tags: ["policy", "installation"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 97783
  original_url: "https://www.suse.com/c/rancher_blog/installing-and-running-kubewarden-in-air-gapped-environments/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "kwctl 1.3.1 era commands"
  redirect_target: ""
---

We are excited to announce that deploying Kubewarden in air gap environments has been simplified and documented!

You will need a private OCI registry accessible by your Kubernetes cluster. If you're unfamiliar with Kubewarden, it's a policy engine for Kubernetes. Its mission is to simplify the adoption of **policy-as-code**. Kubewarden policies are WebAssembly modules; therefore they can be stored inside an OCI-compliant registry as OCI artifacts. For an air gap installation, you need to download all the Kubewarden container images and policies in your workstation, then move them to your private OCI registry. Check the Kubewarden [docs](https://docs.kubewarden.io/operator-manual/airgap/install) for a step-by-step guide.

We have added new commands to `kwctl` [v1.3.1](https://github.com/kubewarden/kwctl/releases/tag/v1.3.1) in order to simplify air gap deployment:

- `save`: saves a list of Kubewarden policies provided as input in a tar.gz file.
- `load`: loads Kubewarden policies from a tar.gz file into an OCI registry.

There are helpers' scripts that make easier the air gap installation. You can find them in our [utils repository](https://github.com/kubewarden/utils/tree/main/scripts):

- `kubewarden-save-images.sh` and `kubewarden-load-images.sh`, which takes a text file with all the container images as input.
- `kubewarden-save-policies.sh` and `kubewarden-load-policies.sh`, which takes a text file with all the policies as input.

From now on, all Kubewarden [releases](https://github.com/kubewarden/helm-charts/releases) will contain a text file with all the container images required to use Kubewarden and another one with the default policies referenced by the `kubewarden-defaults` chart. These files can be used to perform the air gap installation of a specific Kubewarden version.

Give it a try and [reach out to us](https://kubernetes.slack.com/?redir=%2Fmessages%2Fkubewarden) if you have any questions or want to share your feedback!
