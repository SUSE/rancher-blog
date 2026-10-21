---
title: "A Journey from Cattle to Kubernetes!"
date: 2018-08-02T14:51:00
slug: "a-journey-from-cattle-to-kubernetes"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["upgrades", "developer-experience"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 87446
  original_url: "https://www.suse.com/c/rancher_blog/a-journey-from-cattle-to-kubernetes/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.6 Cattle migration"
  redirect_target: "rancher.com/blog (hub)"
---

How to Migrate from Rancher 1.6 to Rancher 2.1 Online MeetupKey terminology differences, implementing key elements, and transforming Compose to YAML[Watch the video](https://rancher.com/events/2018/2018-10-23-october-online-meetup-rancher1x-to-rancher2x/)

The past few years I have been developing and enhancing Cattle, which is the default container orchestration and scheduling framework for Rancher 1.6.

Cattle is used extensively by Rancher users to create and manage applications based on Docker containers. One of the key reasons for its extensive adoption is its compatibility with standard Docker Compose syntax.

With the release of Rancher 2.0, we shifted from Cattle as the base orchestration platform to Kubernetes. Kubernetes introduces its own terminologies and yaml specs for deploying application management services and pods that differs from the Docker Compose syntax.

I must say it really is a big learning curve for Cattle developers like me and our users to find ways to migrate apps to the Kubernetes-based 2.0 platform.

In this blog series, we will explore how various features supported using Cattle in Rancher 1.6 can be mapped to their Kubernetes equivalents in Rancher 2.0.

## Who Moved My Stack? :)

In Rancher 1.6, you could easily deploy services running Docker images in one of two ways: using either the Rancher UI or the Rancher Compose Tool, which extends the popular Docker Compose.

With Rancher 2.0, we’ve introduced new grouping boundaries and terminologies to align with Kubernetes. So what happens to your Cattle-based environments and stacks in a 2.0 environment? How can a Cattle user transition their stacks and services to Rancher 2.0?

To solve this problem, lets identify parallels between the two versions.

Some of the key terms around application deployment in 1.6 are:

- Container: The smallest deployment unit. Containers are a lightweight, stand-alone, executable package of software that includes everything required to run it. (https://www.docker.com/what-container)
- Service: A group of one or more containers running an identical Docker image.
- Stack: Services that belong to an application can be grouped together under a stack, which bundles your applications into logical groups.
- Compose config: Rancher allows users to view/export config files for the entire stack. These files, named `docker_compose.yml` and `rancher_compose.yml`, include all services and can be used to replicate the same application stack from a different Rancher setup.

Equivalent key terms for Rancher 2.0 are below. You can find more information about them in the [Rancher 2.0 Documentation](https://rancher.com/docs/rancher/v2.x/en/).

- Pod: In Kubernetes, a pod is the smallest unit of deployment. A pod consist of one or more containers running a specific image. Pods are roughly equivalent to containers in 1.6. An application service consists of one or more running pods. If a Rancher 1.6 service has sidekicks, the pod equivalent would have more than one container, one container launched per sidekick.
- Workload: The term *service* used in 1.6 maps to the term *workload* in 2.0. A workload object defines the specs and deployment rules for a set of pods that comprise the application. However, unlike services in 1.6, workloads are divided into different categories. The workload category most similar to a stateless service from 1.6 is the deployment category.
- Namespace: The term *stack* from 1.6 maps to the Kubernetes concept of a *namespace* in 2.0. After launching a Kubernetes cluster in Rancher 2.0, workloads are deployed to the `default` namespace, unless you explicitly define a namespace yourself. This functionality is similar to the `default` stack in 1.6.
- Kubernetes YAML: This file type is similar to a Docker Compose file. It specifies Kubernetes objects in YAML format. Just as the Docker Compose tool can digest Compose files to deploy specific container services, kubectl is the cli tool that processes Kubernetes YAML as input, which is then used to provision Kubernetes objects. For more information, see the [Kubernetes Documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

### How Do I Move a Simple Application from Rancher 1.6 to 2.0?

After learning the parallels between Cattle and Kubernetes, I began investigating options for transitioning a simple application from Rancher 1.6 to 2.0.

For this exercise, I used the [LetsChat](http://sdelements.github.io/lets-chat/) app, which is formed from a couple of services. I deployed these services to a stack in 1.6 using Cattle. Here is the `docker-compose.yml` file for the services in my stack:

![Imgur](https://i.imgur.com/mBHHbDW.png)

Along with provisioning the service containers, Cattle facilitates service discovery between the services in my stack. This service discovery allows the LetsChat service talk to the Mongo service.

Is provisioning and configuring service discovery in Rancher 2.0 as easy as it was in 1.6?

### A Cluster and Project on Rancher 2.0

First, I needed to create a Rancher 2.0 Kubernetes cluster. You can find instructions for this process in our [Quick Start Guide](https://rancher.com/docs/rancher/v2.x/en/quick-start-guide/deployment/).

In Rancher 1.6, I’m used to deploying my stacks within a [Cattle Environment](https://rancher.com/docs/rancher/v1.6/en/environments/#what-is-an-environment) that has some compute resources assigned.

After inspecting the UI in Rancher 2.0, I recognized that workloads are deployed in a project within the Kubernetes Cluster that I created. It seems that a 2.0 Cluster and a Project together are equivalent to a Cattle environment from 1.6!

![Imgur](https://i.imgur.com/QQIj0An.png)

However, there are some important differences to note:

- In 1.6, Cattle environments have a set of compute nodes assigned to them, and the Rancher Server is the global control plane backed by mysql DB, which provides storage for each environment. In 2.0, each Kubernetes cluster has its own set of compute nodes, nodes running the cluster control plane, and nodes running etcd for storage.
- In 1.6, all Cattle environment users could access any host in the environment. In Rancher 2.0, this access model has changed. You can now restrict users to specific projects. This model allows for multi-tenancy since hosts are owned by the cluster, and the cluster can be further divided into multiple projects where users can manage their apps.

### Deploying Workloads from Rancher 2.0 UI

With my new Kubernetes cluster in place, I was set to launch my applications the 2.0 way!

I navigated to the **Default** project under my cluster. From the **Workloads** tab, I launched a deployment for the LetsChat and Mongo Docker images.

![Imgur](https://i.imgur.com/qD9gEu5.png)

For my LetsChat deployment, I exposed container port `8080` by selecting the **HostPort** option for port mapping. Then I entered my public port `9890` as the listening port.

I selected **HostPort** because Kubernetes exposes the specified port for each host that the workload (and its pods) are deployed to. This behavior is similar to exposing a public port on Cattle.

While Rancher provisioned the deployments, I monitored the status from the **Workloads** view. I could drill down to the deployed Kubernetes pods and monitor the logs. This experience was very similar to launching services using Cattle and drilling down to the service containers!

![Imgur](https://i.imgur.com/FjiwQxx.png)
Once the workloads were provisioned, Rancher provided a convenient link to the public endpoint of my LetsChat app. Upon clicking the link, voilá!

![Imgur](https://i.imgur.com/tqHVxV4.png)

### Docker Compose to Kubernetes Yaml

If you’re migrating multiple application stacks from Rancher 1.6 to 2.0, manually migrating by UI is not ideal. Instead, use a Docker Compose config file to speed things up.

If you are a Rancher 1.6 user, you’re probably familiar with launching services by calling a Compose file from Rancher CLI. Similarly, Rancher 2.0 provides a CLI to launch the Kubernetes resources.

So our next step is to convert our `docker-compose.yml` file to the kubernetes yaml specs and use CLI.

Converting my Compose file to the Kubernetes YAML specs manually didn’t inspire confidence. I’m unfamiliar with Kubernetes YAML, and it’s confusing compared to the simplicity of Docker Compose. A quick Google search led me to this conversion tool—[Kompose](https://github.com/kubernetes/kompose).

![Imgur](https://i.imgur.com/TYHLrjx.png)

Kompose generated two files per service in the `docker-compose.yml`:

- a deployment YAML
- a service YAML

Why is a separate service spec required?

A Kubernetes service is a REST object that abstracts access to the pods in the workload. A service provides a static endpoint to the pods. Therefore, even if the pods change IP address, the public endpoint remains unchanged. A service object points to its corresponding deployment (workload) by using selector labels.

When a service in Docker Compose exposes public ports, Kompose translates that to a service YAML spec for Kubernetes, along with a deployment YAML spec.

Lets see how the compose and Kubernetes YAML specs compare:

![Imgur](https://i.imgur.com/EDLrgsC.png)

As highlighted above, everything under the `chat` service in `docker-compose.yml` is mapped to `spec.containers` in the Kubernetes `chat-deployment.yaml` file.

- The service name in `docker-compose.yml` is placed under `spec.containers.name`
- `image` in `docker-compose.yml` maps to `spec.containers.image`
- `ports` in `docker-compose.yml` maps to `spec.containers.ports.containerPort`
- Any `Labels` present in `docker-compose.yml` are placed as `metadata.annotations`

Note that the separate `chat-service.yaml` file contains the public port mapping of the deployment, and it points to the deployment using a `selector` `io.kompose.service: chat`), which is a `label` on the `chat-deployment` object.

To deploy these files to my cluster namespace, I downloaded and configured the [Rancher CLI tool](https://rancher.com/docs/rancher/v2.x/en/concepts/cli-configuration/).

The workloads launched fine, but…

![Imgur](https://i.imgur.com/oaFdEnL.png)

There was no public endpoint placed for the chat workload. After some troubleshooting, I noticed that the generated file from Kompose was missing the `HostPort` spec in the `chat-deployment.yaml` file! I manually added the missing spec and re-imported the yaml to publicly expose the LetsChat workload.

![Imgur](https://i.imgur.com/GuNBMCs.png)

Troubleshoot successful! I could access the application on the `Host-IP:HostPort`.

![Imgur](https://i.imgur.com/3K964da.png)

### Finished

There you have it! Rancher users can successfully port their application stacks from 1.6 to 2.0 using either the UI or Compose-to-Kubernetes YAML conversion.

Although the complexity of Kubernetes is still apparent, with the help of Rancher 2.0, I found the provisioning flow just as simple and intuitive as Cattle.

This article looked at the bare minimum flow of transitioning simple services from Cattle to Rancher 2.0. However there are more challenges you’ll face when migrating to Rancher 2.0: you’ll need to understand the changes in Rancher 2.0 around scheduling, load balancing, service discovery, and service monitoring. Let’s dig deeper in upcoming articles!

In the next article, we will explore various options for exposing a workload publicly via port mapping options on Kubernetes.

How to Migrate from Rancher 1.6 to Rancher 2.1 Online MeetupKey terminology differences, implementing key elements, and transforming Compose to YAML[Watch the video](https://rancher.com/events/2018/2018-10-23-october-online-meetup-rancher1x-to-rancher2x/)
