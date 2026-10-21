---
title: "Faster Kubernetes Development with Rancher, DevSpace and Loft"
date: 2020-09-23T09:48:00
slug: "faster-kubernetes-development-with-rancher-devspace-and-loft"
author: "Rancher Admin"
image: "images/rancher_blog_devspace-featured.png"
products: ["Rancher Manager"]
tags: ["developer-experience", "ci-cd"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 86080
  original_url: "https://www.suse.com/c/rancher_blog/faster-kubernetes-development-with-rancher-devspace-and-loft/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Rancher 2.x era tooling versions"
  redirect_target: ""
---

Don’t miss the Computing on the Edge with Kubernetes conference on October 21.[Register Now](https://www.accelevents.com/e/edgeconference2020)

## Introduction

Today, Kubernetes is getting more and more important, not only in the world of operations but also in the world of development. Knowledge in Kubernetes is a highly sought after skill. Yet the question remains whether developers should get access to Kubernetes and if they even need to know about Kubernetes at all.

A common approach to circumvent this problem is to abstract the complexity of Kubernetes away from the developer by providing a platform, or CI/CD pipelines, that make it easier for a developer to test an application within Kubernetes without a direct access to Kubernetes.

However, it often makes sense to give the developer direct access to Kubernetes and for them to develop some applications directly inside Kubernetes because this makes it possible to work in an environment very close to production.

This raises the question of how to allow developers to work with Kubernetes without overwhelming them with its complexity. One answer to this question could be developer tooling for Kubernetes, such as DevSpace. In this blog, we’ll explore how developers can use DevSpace and Rancher to simplify Kubernetes development.

## DevSpace: Development with Rancher Made Easy

[DevSpace](https://github.com/devspace-cloud/devspace) is a client-only, open source developer tool for Kubernetes. It allows you to:

- Build, test and debug applications directly inside Kubernetes
- Develop with hot reloading by updating your running containers without rebuilding images or restarting containers
- Unify deployment workflows within your team and across dev, staging and production
- Automate repetitive tasks for image building and deployment

DevSpace complements Rancher as a client tool for developers, where developers get assigned projects within Rancher and then develop or test applications directly inside Kubernetes.

This brings the development environment even closer to the production environment, giving you greater confidence that everything will work in production when shipping new features.

### Setting up DevSpace

To install DevSpace, first [download the DevSpace binary](https://devspace.sh/cli/docs/getting-started/installation).
Next, create a new project by running `devspace init` in an already containerized project. If you don’t have a project at hand you can use one of our [example projects](https://devspace.sh/cli/docs/getting-started/initialize-project#choose-a-project)):

```
$ devspace init

     ____              ____
    |  _   _____   __/ ___| _ __   __ _  ___ ___
    | | | |/ _   / /___ | '_  / _` |/ __/ _ 
    | |_| |  __/ V /  ___) | |_) | (_| | (_|  __/
    |____/ ___| _/  |____/| .__/ __,_|______|
                            |_|

? How do you want to initialize this project?
 Use the Dockerfile in ./Dockerfile

? Which registry do you want to use for storing your Docker images?
 Use hub.docker.com => you are logged in as devspacecloud

? Which image name do you want to use on Docker Hub? devspacecloud/quickstart

? Which port is your application listening on? (Enter to skip) 8080

[done] √ Project successfully initialized
```

After you answer a few questions about the project that should be initialized, DevSpace will create a `devspace.yaml` for you. The `devspace.yaml` contains the configuration of how to deploy and develop the project with DevSpace and looks similar to this:

```
version: v1beta9
# This section defines the images that should be built
images:
  app:
    image: devspacecloud/quickstart
    preferSyncOverRebuild: true
    # this option tells devspace to automatically wrap the Dockerfile entrypoint in memory
    # with a small restart helper script so that the process can be easily restarted from within the
    # container.
    injectRestartHelper: true
# Defines an array of everything (component, Helm chart, Kubernetes maninfests)
# that will be deployed with DevSpace in the specified order
deployments:
- name: quickstart
  helm:
    # Uses a special helm chart provided by devspace to complement projects that don't have an own
    # helm chart
    componentChart: true
    values:
      containers:
      - image: devspacecloud/quickstart
      service:
        ports:
        - port: 8080
# Configuration that will be used for developing the application
dev:
  # Port forward certain ports from the application to the local computer
  ports:
  - imageName: app
    forward:
    - port: 8080
  # Hot reload changes instead of rebuilding the complete docker image all the time
  sync:
  - imageName: app
    # This tells devspace to restart the container after a file was synced into it
    onUpload:
      restartContainer: true
profiles:
...
```

Now you can share this configuration across the team. It specifies how to develop the application inside Kubernetes independently of the local setup.

To start developing the application, you’ll need access to a Kubernetes cluster or Rancher project. A best practice is to create a Rancher project for each developer or one single project for a team of developers inside a single shared cluster.

To ensure a simple isolation between the different projects and namespaces, use common Kubernetes resources, such as [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/), [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/), [Pod Security Policies](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) and [Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/).

## Develop an Application with DevSpace

To actually start developing, run the command `devspace dev`. This will do the following:

- Build and deploy your application
- Stream the logs of all containers deployed during the deployment process
- Forward all ports specified in the dev.ports section in the devspace.yaml
- Sync all file changes according to the sync config in dev.sync, so you can restart your application inside the running container without having to rebuild images or redeploy anything

```
$ devspace dev -n test
[info]   Using kube context 'docker-desktop'
[info]   Using namespace 'test'
[done] √ Created namespace: test
[info]   Building image 'myusername/devspace:C5992q4' with engine 'docker'
Step 1/7 : FROM node:13.12-alpine
...
[done] √ Done processing image 'myusername/devspace'
[done] √ Deployed helm chart (Release revision: 0)
[done] √ Successfully deployed quickstart with helm
[done] √ Port forwarding started on 3000:3000
[done] √ Sync started on /devspace/examples/quickstart <-> . (Pod: test/quickstart-5d7f4d8fd-w95cx)

#########################################################
[info]   DevSpace UI available at: http://localhost:8090
#########################################################

[info]   Starting log streaming for containers that use images defined in devspace.yaml

[quickstart]
[quickstart] > node-js-sample@0.0.1 start /app
[quickstart] > nodemon index.js
[quickstart]
[quickstart] [nodemon] 1.19.4
[quickstart] [nodemon] to restart at any time, enter `rs`
[quickstart] [nodemon] watching dir(s): *.*
[quickstart] [nodemon] watching extensions: js,mjs,json
[quickstart] [nodemon] starting `node index.js`
[quickstart] Example app listening on port 3000!
```

After a local change of a file, the file will be synced into the container. The container restarts without a complete rebuild via Docker, which speeds up the development process greatly.

Then DevSpace starts a local UI, where you can access and inspect the pods that were created. This simplifies interaction with Kubernetes, especially for users who are not familiar with `kubectl`.

![Image 01](images/rancher_blog_image-01.jpg)

Besides `devspace dev`, the command `devspace deploy` can be used to package and deploy an application without hot-reloading, port-forwarding, or log streaming.
DevSpace offers many customizations to adjust its behavior to your use case and setup. These include:

- [Dependencies](https://devspace.sh/cli/docs/configuration/dependencies/basics) that allow you to develop and deploy projects that depend on other projects
- [Profiles](https://devspace.sh/cli/docs/configuration/profiles/basics) that allow multiple configurations in a single `devspace.yaml`
- [Variables](https://devspace.sh/cli/docs/configuration/variables/basics) that allow specifying dynamic config values
- [Commands](https://devspace.sh/cli/docs/configuration/commands/basics) that allow configuration of custom commands for your project
- [Hooks](https://devspace.sh/cli/docs/configuration/hooks/basics) to execute certain functionality on specific DevSpace events
- [Environment Variables](https://devspace.sh/cli/docs/configuration/env-file) that automatically add flags to devspace commands
- Plugins to extend DevSpace and its commands

While DevSpace standardizes and simplifies the way developers interact with Kubernetes, Rancher manages the server-side of how the developers can work inside Kubernetes.

Rancher lets you spin up development clusters and divide them into separate projects where development teams can work and test together.

[Project Resource Quotas](https://rancher.com/docs/rancher/v2.x/en/project-admin/resource-quotas/) are useful in addition to common Kubernetes isolation resources to constrain teams in terms of resources and to allow a fair usage in a shared Kubernetes cluster. Sharing Kubernetes clusters reduces the infrastructure cost and still allows effective development directly inside Kubernetes.

## Adding loft to the Tool Mix

[loft](https://loft.sh/) is another useful tool that adds several other handy features to the development process. These include:

- [Virtual Clusters](https://loft.sh/blog/introduction-into-virtual-clusters-in-kubernetes/) that are much cheaper than “real” clusters and can be created and cleaned up again in seconds, while they are also more powerful than simple namespaces
- Self-service provisioning of namespaces for developers within a shared cluster
- A sleep mode that puts namespaces after a certain time of inactivity to sleep to save computing cost

You can easily add loft to Rancher by [installing the loft helm chart](https://loft.sh/docs/getting-started/setup). loft CLI is also available as a [plugin for DevSpace](https://github.com/loft-sh/loft-devspace-plugin).

## Conclusion

Kubernetes is tough for developers – and many companies still struggle to find a way to abstract the complexity of Kubernetes away from them. This often results in custom-tailored platforms that lack many features, limit the potential of Kubernetes and are just another maintainence burden.

Combining DevSpace, Rancher and loft gives developers direct access to Kubernetes while making the interaction with it as easy as possible by running just a single command: `devspace dev`.

Rancher is great at creating and managing multiple clusters. DevSpace is great at providing developer tooling. Combining Rancher and DevSpace is straightforward and also can have a big impact on developer productivity.

loft provides additional useful features for development teams and allows developers to get a Kubernetes work environment whenever they need it while keeping cost low. Combining the three tools – Rancher, DevSpace and loft – is the ideal setup for development teams that work with Kubernetes.

Don’t miss the Computing on the Edge with Kubernetes conference on October 21.[Register Now](https://www.accelevents.com/e/edgeconference2020)
