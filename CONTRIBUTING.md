# Contributing to the Rancher blog

The Rancher blog is for people who build and run Rancher, K3s, RKE2, Longhorn, Fleet, Harvester, NeuVector, Rancher Desktop, Kubewarden and the rest of the open source stack. Engineers, maintainers and community members are all welcome to write.

## What fits here

- How-tos you can follow end to end, with real commands
- Engineering deep dives: how a feature works, why it was built that way, benchmark results
- Release walkthroughs for the open source projects
- Community stories: talks, meetups, projects built on Rancher

Commercial content (Rancher Prime, SUSE Rancher for AWS, pricing, support, customer case studies) goes to the SUSE blog on suse.com instead. A post here can link to suse.com once, at the end, when the enterprise option is relevant.

## How to propose a post

1. Open an issue with a title and three lines on what the reader will be able to do after reading. This avoids two people writing the same post.
2. Create a branch and add a folder for your post:

   ```
   content/blog/your-post-slug/
     index.md
     images/
   ```

3. Start `index.md` with this front matter:

   ```
   ---
   title: "Run your first K3s cluster in ten minutes"
   date: 2026-11-03T09:00:00
   slug: "run-your-first-k3s-cluster"
   authors: ["Your Name"]
   products: ["K3s"]
   tags: ["installation", "edge"]
   description: "One sentence that shows up in search results and social cards."
   draft: false
   ---
   ```

   Use the project names already in use on the blog for `products`: Rancher Manager, K3s, RKE2, Longhorn, Fleet, Harvester, NeuVector, Rancher Desktop, Kubewarden, Elemental, K3k.

4. Preview it locally with `hugo server` and open http://localhost:1313/blog/.
5. Open a pull request against `main`. The template lists what reviewers will check.

## Writing guidelines

- Write for a practitioner. Address the reader as "you".
- Lead with the job, not the feature name: "Run your first cluster in ten minutes", then name K3s.
- Sentence case for titles and headings. No emoji in titles.
- Show real commands in code blocks and say which versions you tested with.
- No marketing claims you cannot back up, no pricing, no customer logos.

## Images

- Put them in your post's `images/` folder and reference them as `![What the image shows](images/file.png)`.
- Always write alt text that describes the image.
- PNG or JPG, under 1 MB each. Screenshots at 2x are fine, Hugo resizes the thumbnails.
- To set the card image, add `image: "images/file.png"` to the front matter.

## Author pages

Your name in `authors` links to your author page. To add a bio, create `content/authors/your-name/_index.md`:

```
---
title: "Your Name"
---
One or two sentences about what you work on.
```

## Review and publishing

A maintainer reviews every pull request for accuracy, tone and links. Merging to `main` publishes the post within a few minutes.
