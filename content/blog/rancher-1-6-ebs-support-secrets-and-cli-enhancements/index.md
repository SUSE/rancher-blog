---
title: "Rancher 1.6 - EBS Support, Secrets, and CLI Enhancements"
date: 2017-05-04T11:14:00
slug: "rancher-1-6-ebs-support-secrets-and-cli-enhancements"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["storage"]
content_type: "release"
draft: true
migration:
  wp_id: 86884
  original_url: "https://www.suse.com/c/rancher_blog/rancher-1-6-ebs-support-secrets-and-cli-enhancements/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.6 release"
  redirect_target: "https://rancher.com/blog (hub)"
---

![](images/rancher_blog_rancher-logo_stacked-full-color-1-300x157.jpg)We’ve just released
Rancher v1.6, the latest version of our container management platform.
While we still recommend that production or mission-critical deployments
use our most recent stable release, we’re excited to share what’s new in
v1.6. In this release, we’ve built greater control for our users over
their storage and secrets.

#### Validating EBS Support

We first implemented support for EBS before Rancher itself was even
generally available, but in v1.6, we’re removing the ‘experimental’ tag.
In addition to fixing some minor issues flagged by our community, this
release contains:

- \*\*Availability-zone aware scheduling \*\*for better container
  management within the same AZ
- **Additional options for EBS volumes**: now users can specify
  options like volumetype, encrypted, and snapshotltd

Consider our EBS support ready for production! As a side note, Rancher
EBS support and development of Project Longhorn should not be considered
conflicting efforts – we will always support popular and leading
technologies, AWS included. While Project Longhorn is slated for
eventual inclusion into Rancher, it’s still experimental, and for now
Longhorn and Rancher remain separate.

#### Rancher Secrets Support in Compose

In [Rancher v1.4](https://rancher.com/rancher-1-4/), we added the ability
to handle secrets in Rancher using Vault Transit. In Rancher v1.6, this
feature remains experimental, though we’ve fixed bugs identified since
its initial release. Moreover, this latest release also includes the
ability to create secrets using Compose and Rancher CLI. It delivers on
a popular request from our community, as it streamlines the ability to
deploy workloads that rely on secrets rather than pushing users to
administer secrets through the Rancher UI.

#### Rancher CLI versus rancher-compose CLI

For the past couple of releases, we’ve developed Rancher CLI alongside
its older predecessor, rancher-compose CLI. Rancher-compose CLI
functionality has merely become a subset of Rancher CLI functionality.
Going forward, we’ll be combining these efforts and new features will
only be developed on Rancher CLI. We encourage you to read more about
[Rancher v1.6](https://github.com/rancher/rancher/releases/tag/1.6.0) in
the release notes, and to reach out to us on Twitter
[@Rancher\_Labs](https://twitter.com/rancher_labs) or our
[forums](https://forums.rancher.com) with questions and feedback. We’re
always happy to hear more from our community!
