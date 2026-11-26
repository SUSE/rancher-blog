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

## Publishing a post (maintainers)

1. Review the pull request against its checklist and the mistakes list in `CONTRIBUTING.md`. Fix small things (slug, authors, links) with a commit on the contributor's branch, or with a follow-up pull request after merging.
2. Merge to `main`. The "Deploy blog to GitHub Pages" workflow runs and takes a few minutes.
3. Hugo skips posts dated in the future, and nothing rebuilds on a timer. For a scheduled post, merge after its `date`, or open Actions > Deploy blog to GitHub Pages > Run workflow once the time has passed.
4. Check the post at `https://www.rancher.com/blog/<slug>/` and on the blog home. If it is on the Pages origin (`https://opensource.suse.com/rancher-blog/blog/<slug>/`) but not on rancher.com, the CloudFront cache has not refreshed yet.

To take a post down, set `draft: true` and merge. If the URL was shared, also add a redirect (below).

## Redirects

`cloudfront/` holds the viewer-request function for the rancher.com `/blog/*` behaviour. It sends archived posts and pre-2021 rancher.com URLs (`/blog/YYYY/<old-slug>`) to their new home with a 301, using a CloudFront KeyValueStore loaded from `cloudfront/redirects-kvs.json`, and adds the trailing slash GitHub Pages would otherwise add with a redirect to its own host.

To archive another post, set `draft: true` on it, add its slug and target to `redirects-kvs.json` (or regenerate it with `tools/make_redirects.py` from the redirect map), run `node cloudfront/test.mjs`, and reload the KeyValueStore.

To check every old URL after a change to the redirects, run `python3 tools/check_redirects.py <redirect-map.csv>`. Before the CloudFront switch, add `--origin https://opensource.suse.com/rancher-blog` to check the posts on the Pages origin instead.

## Analytics and consent

`layouts/partials/tracking.html` loads the rancher.com Google Tag Manager container and OneTrust banner, with the IDs in `hugo.toml`. They load only when the page is served on rancher.com, so the Pages origin does not count as traffic.
