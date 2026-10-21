---
title: "Rancher Desktop v0.3.0 Release"
date: 2021-06-23T10:14:00
slug: "rancher-desktop-v0-3-0-release"
author: "Rancher Admin"
image: "images/rancher_blog_rancher-desktop-featured.png"
products: ["Rancher Desktop"]
tags: ["developer-experience"]
content_type: "release"
draft: false
migration:
  wp_id: 86500
  original_url: "https://www.suse.com/c/rancher_blog/rancher-desktop-v0-3-0-release/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher Desktop v0.3.0 release notes"
  redirect_target: ""
---

We are happy to share the v0.3.0 release of Rancher Desktop. This release brings more stability, some new features, and a fresh look to the UI.

![Image 01](images/rancher_blog_image-01.jpg)

This screenshot shows the preferences screen while in dark mode on Mac.

In the lower left corner the status when performing an action is now displayed. This status will tell you when Rancher Desktop needs to download something, such as a version of Kubernetes you have now used before, or when another step is happening.

![Image 02](images/rancher_blog_image-02.jpg)

When Rancher Desktop cannot link in a supporting utility on Mac it now tells you why it can’t do it. On Windows the utilities are automatically added to the path as path handling works differently.

There are more UI goodies sprinkled throughout the update and there will be more to come.

## Stability

v0.3.0 brings more stability to Rancher Desktop on Windows. Using the Windows Subsystem for Linux (WSL) has the benefit of providing an environment across all Windows users including those on Windows Home where they can’t run their own virtual machines. It also comes with some challenges in learning how WSLv2 manages the environment. Through our use of Rancher Desktop on Windows we’ve learned about some of the rough edges and smoothed them out.

## Faster Restarts

When someone pushes the “Reset Kubernetes” button or changes the Kubernetes version Rancher Desktop needs to make sure the old environment is taken down and the new one comes up. This now happens faster than ever as the handling of the restart was sped up.

## Next Steps

There are several next steps:

- Star [Rancher Desktop on GitHub](https://github.com/rancher-sandbox/rancher-desktop) to show that you like it. This is how we know you like it and want to see development continue.
- Install the [v0.3.0 release](https://github.com/rancher-sandbox/rancher-desktop/releases/tag/v0.3.0).
- Provide feedback in the [issue queue](https://github.com/rancher-sandbox/rancher-desktop/issues).
