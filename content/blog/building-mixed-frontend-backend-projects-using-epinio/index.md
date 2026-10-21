---
title: "Building mixed frontend/backend projects using Epinio"
date: 2021-10-03T17:45:59
slug: "building-mixed-frontend-backend-projects-using-epinio"
author: "Andrew Gracey"
products: ["Epinio"]
tags: ["developer-experience"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 93489
  original_url: "https://www.suse.com/c/rancher_blog/building-mixed-frontend-backend-projects-using-epinio/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Epinio discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

I've been using Epinio to build several of my smart home projects in the last few months. I have really enjoyed not needing to worry about the complexity of Kubernetes while iterating on the code.

I recently decided it would be fun to build a wallboard to show me news, weather, and some traffic cameras at the local mountains so I could more easily decide where to ski!

This posed a problem, though. When building the app, I needed to build both the frontend and backend in the same pipeline (because `epinio push` is nice, and I didn't want to require additional steps). If I just did a push, it would build the backend but leave the frontend in whatever state I pushed, so I had to continually rebuild the react app for the node.js backend to host.

**BP\_NODE\_RUN\_SCRIPTS to the rescue!**

I got around this problem by adding a script to npm:
>  "build-client": "cd client; npm i; npm run build; cd -;"

This changes the directory into the client folder, installs the dependencies, builds the project, and then pops back into the main folder.

I got this to run as part of the pipeline by setting BP\_NODE\_RUN\_SCRIPTS to build-client by running:
> epinio app env set traffic BP\_NODE\_RUN\_SCRIPTS build-client

Then all of my builds also ran build-client as part of their build process!

If anyone is interested, my (very incomplete and likely poorly written) code can be found at <https://github.com/agracey/home-weather-traffic>
