---
title: "Fast Five Things to Get Ready for the Cloud"
date: 2021-11-30T15:04:59
slug: "fast-five-things-to-get-ready-for-the-cloud"
author: "Robert Sirchia"
products: ["Kubernetes (generic)"]
tags: ["cloud"]
content_type: "explainer"
draft: false
migration:
  wp_id: 93081
  original_url: "https://www.suse.com/c/rancher_blog/fast-five-things-to-get-ready-for-the-cloud/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

### The Fast Five

#### Steps to prepare for the cloud

When it comes to the first steps of app modernization to the cloud, there are a few things you can do now to be ready. It’s important to note that this is more for apps going *into* the cloud - we are not talking about apps *for* the cloud. Let’s look at the “fast five” things you can do to your app today to prepare for the cloud tomorrow. These are taken from the [12 Factors](https://12factor.net/).

We’ll focus on some things that are not as invasive but still impactful when modernizing. So, in no particular order, here are the fast five:

- Codebase
- Configuration
- Build, Run, Release
- Disposability
- Logs

 Now that we’ve got our list, we’ll dive deeper into these concepts.

### Codebase

#### One codebase tracked in revision control, many deploys

Codebases will focus more on the process within your organization than anything else. Once you have identified all core components, your app needs to centralize it all onto one codebase. Now, this seems like a crazy idea. Thinking it through, this is one area for you to refactor and decompose your monolith. But figuring out what to collapse into one codebase is not easy. The complexity of any organization has way too many nuances.

Branching strategy is part of this. Establish a branching strategy and stick with it; there are plenty of them to choose from (GitFlow, GitHub Flow, etc.). Focus on not allowing long-running branches either; this is a management nightmare and should be avoided at all costs. 

### Configuration

#### Store config in the environment

We have constantly deployed configuration with our apps for years. This worked great when we only deployed a few components to an environment to get an app running, but deployment points will grow as we move to the cloud. It is the simple nature of building a distributed system. So a simple config change requires a change in a lot of places. To address this is centralizing configuration. 

This moves configuration from being deployed with our apps to being served up by the environment. Our apps consume the configuration being served up through a lightweight client.

### Build, Run, Release

#### Strictly separate build and run stages

This is once again a more significant change in an organization's process rather than a technical change. Once a change is built, you should treat it as immutable. Changes to that artifact should go through the build process. If a build artifact has the wrong reference, don’t add the correct binary to the artifact. Change the code to call the correct reference and rebuild and deploy that artifact.

### Disposability

#### Maximize robustness with fast start-up and graceful shutdown

This one isn’t the easiest to implement of all the fast five. There are two sides to this: *start-up* and *shutdown,* where each needs some careful consideration. One of your goals should be getting the start-up time to be less than 15 seconds. It isn’t critical now, but it will be when deployed to the cloud. A shutdown is just as necessary - you should target getting your shutdown time to less than five seconds, and it should not result in data loss.

### Logs

#### Treat logs as event streams

Logs are again, a technical change, meaning a code change. It would be best if you centralized on a single logging library; each deployment point should have a single point where it is writing a log externally. This makes it easy to change how your app logs when moving to the cloud.

#### Want to make sure you don't miss any of the action? [Join the SUSE & Rancher Community](https://community.suse.com/sign_up?space_id=3669174&from=https%3A%2F%2Fcommunity.suse.com%2Ffeed%3Fautojoin%3D1%26autojoin_space_id%3D3669174) to get updates on new content coming your way!
