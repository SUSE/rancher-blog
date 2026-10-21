---
title: "Verify Image Signatures with GitHub Actions and KeylessPrefix"
date: 2022-07-21T09:07:41
slug: "verify-image-signatures-with-github-actions-and-keylessprefix"
author: "Raul Cabello"
image: "images/rancher_blog_kubewarden.jpeg"
products: ["Kubewarden"]
tags: ["security", "ci-cd"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 93139
  original_url: "https://www.suse.com/c/rancher_blog/verify-image-signatures-with-github-actions-and-keylessprefix/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Kubewarden v1.1 versions"
  redirect_target: ""
---

With the latest releases of Kubewarden v1.1.0 and the [verify-image-signatures](https://github.com/kubewarden/verify-image-signatures) policy, it’s now possible to use `GithubActions` or `KeylessPrefix` for verifying images. Read our previous [blog post](https://www.kubewarden.io/blog/2022/05/verifying-image-signatures/) if you want to learn more about how to verify container images with Sigstore using Kubewarden.

## **Let’s see it in action!**

We want to verify the image `ghcr.io/raulcabello/app-example` built and signed inside a GitHub Action using this [GitHub Action](https://github.com/raulcabello/app-example/blob/master/.github/workflows/ci.yml).

Out of the box, GitHub Actions have a specially crafted environment that makes Sigstore keyless signing work in a non-interactive way. The signatures produced in this way contain unique secure information that allows us to identify the GitHub owner (be it an individual or an organization) and the GitHub repository inside of which the GitHub Action has been executed.

Starting today, Kubewarden provides a convenient way to check signatures produced by GitHub Actions.

For this example, a Kubernetes cluster with Kubewarden already installed is required. The installation process is explained in the [quick start guide](https://docs.kubewarden.io/quick-start).

### **GitHub Actions**

```
apiVersion: policies.kubewarden.io/v1
kind: ClusterAdmissionPolicy
metadata:
  name: verify-image-signatures-policy
spec:
  module: registry://ghcr.io/kubewarden/policies/verify-image-signatures:v0.1.4
  rules:
  - apiGroups: [""]
    apiVersions: ["v1"]
    resources: ["pods"]
    operations:
    - CREATE
    - UPDATE
  mutating: true
  settings:
    signatures:
      - image: "ghcr.io/raulcabello/app-example:*" # match all tags 
        github_actions:
        - owner: "raulcabello"
          repo: "app-example" #optional. if omited all signatures performed in repos from the owner will be valid.
```

This policy verifies all containers with an image that is `ghcr.io/raulcabello/app-example`. It will accept containers that were assigned inside a GitHub Action job, run under the owner `raulcabello`, and the repo `app-example`.

### **KeylessPrefix**

`KeylessPrefix` is similar to the existing keyless verification; the only difference is that it will validate the subject based on a prefix instead of an exact match.

```
apiVersion: policies.kubewarden.io/v1
kind: ClusterAdmissionPolicy
metadata:
  name: verify-image-signatures-policy
spec:
  module: registry://ghcr.io/kubewarden/policies/verify-image-signatures:v0.1.4
  rules:
  - apiGroups: [""]
    apiVersions: ["v1"]
    resources: ["pods"]
    operations:
    - CREATE
    - UPDATE
  mutating: true
  settings:
    signatures:
      - image: "ghcr.io/raulcabello/app-example:*" # match all tags 
        keyless_prefix:
          - issuer: "https://token.actions.githubusercontent.com"
            subject: "https://github.com/raulcabello/app-example/.github/workflows/ci.yml@refs/tags/" # match all tags
```

This will accept containers whose signature contains the issuer `https://token.actions.githubusercontent.com` and the subject starts with `https://github.com/raulcabello/app-example/.github/workflows/ci.yml@refs/tags/`.

Like in the previous example, this will accept the image `ghcr.io/raulcabello/app-example`, however, we **don’t** recommend using `KeylessPrefix` for GitHub Actions validation. When GitHub creates the OIDC token used for the signatures, it sets the subject as the URL containing the GHA workflow code, which doesn’t necessarily match where it has run in the case of reusable workflows; this is by design. If one wants to check for the repo where the job was run, corresponding to that workflow code, GitHub has added an x509 certificate extension `github_workflow_repository` that contains it. In future releases `KeylessPrefix` validation that has `https://token.actions.githubusercontent.com` as an issuer will fail.

Please let us know if you have any questions! Stay tuned for more blogs on how to secure your supply chain with Kubewarden!

## **Next Steps: Learn More at the Kubewarden Meetup**

Join our Global Online Meetup: Kubewarden on Wednesday, August 10th, 2022, at 11 AM EST. Flavio Castelli from the Kubewarden team will tell you more about Kubewarden, give you a live demo and answer your questions. [Register now.](https://more.suse.com/global_rancher_online_meetup_kubewarden.html)
