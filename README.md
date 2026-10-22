# Rancher blog

Source of the Rancher blog at https://www.rancher.com/blog/, built with [Hugo](https://gohugo.io/) and published to GitHub Pages.

## Run it locally

Install Hugo extended 0.168 or later (`brew install hugo` on macOS), then:

```
hugo server        # published posts only
hugo server -D     # also archived posts kept as drafts
```

Open http://localhost:1313/blog/.

## Write a post

Each post is a folder with an `index.md` and its images next to it:

```
content/blog/my-post-slug/
  index.md
  images/screenshot.png
```

Front matter:

```
---
title: "Run your first K3s cluster"
date: 2026-11-03T09:00:00
slug: "run-your-first-k3s-cluster"
authors: ["Your Name"]
products: ["K3s"]
tags: ["installation"]
draft: false
---
```

Open a pull request against `main`. Merging publishes the post.

## Publishing

`.github/workflows/hugo.yml` builds the site on every push to `main` and deploys it to GitHub Pages at https://opensource.suse.com/rancher-blog/blog/. Links are relative, so the same build is served on https://www.rancher.com/blog/ through CloudFront.

## Redirects

`cloudfront/` holds the viewer-request function for the rancher.com `/blog/*` behaviour. It sends archived posts to their new home with a 301, using a CloudFront KeyValueStore loaded from `cloudfront/redirects-kvs.json`, and adds the trailing slash GitHub Pages would otherwise add with a redirect to its own host.

To archive another post, set `draft: true` on it, add its slug and target to `redirects-kvs.json` (or regenerate it with `tools/make_redirects.py` from the redirect map), run `node cloudfront/test.mjs`, and reload the KeyValueStore.
