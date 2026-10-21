---
title: "What Do People Love About Rancher?"
date: 2019-02-28T09:43:00
slug: "what-do-people-love-about-rancher"
author: "Rancher Admin"
image: "images/rancher_blog_rancher-houses.jpg"
products: ["Rancher Manager"]
tags: []
content_type: "company-news"
draft: true
migration:
  wp_id: 85925
  original_url: "https://www.suse.com/c/rancher_blog/what-do-people-love-about-rancher/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "2019 marketing and whitepaper promo"
  redirect_target: "suse.com (new URL pending)"
---

Read the Guide to Kubernetes with RancherThis guide shows the challenges in running Kubernetes in production and how Rancher helps. [Get the whitepaper](https://more.suse.com/fy21-global-web-landing-page-guide-to-kubernetes) More than 20,000 environments have chosen Rancher as the solution to make the Kubernetes adventure painless in as many ways as possible. More than 200 businesses across finance, health care, military, government, retail, manufacturing, and entertainment verticals engage with Rancher commercially because they recognize that Rancher simply works better than other solutions.

Why is this? Is it really about one feature set versus another feature set, or is it about the freedom and breathing room that come from having a better way?

## A Tale of Two Houses

Imagine that you’re walking down a street, and each side of the street is lined with houses. The houses on one side were constructed over time by different builders, and you can see that although every house contains walls, a floor, a roof, doors, and windows, they’re all completely different. Some were built from custom plans, while others were modified over time by the owner to fit a personal need.

You see a person working on his house, and you stop to ask him about the construction. You learn that the company that built his house did so with special red bricks that only come from one place. He paid a great deal of money to import the bricks and have the house built, and he beams with pride as he tells you about it.

“It’s artesenal,” he tells you. “The company who built my house is one of the biggest companies in the world. They’ve been building houses for years, so they know what they’re doing. My house only took a month to build!”

“What if you want to expand?” You point to other houses on his side of the street. “Does the builder come out and do the work?”

“Nope! I decide what I want to build, and then I build it. I like doing it this way. Being hands-on makes me feel like I’m in control.”

Your gaze moves to the other side of the street, where the houses were built by following a different strategy. Each house has an identical core, and where an owner made customizations, each house with that customization has it constructed the same.

You see a man outside of one of the houses, relaxing on his porch and drinking tea. He waves at you, so you walk over and strike up a conversation with him.

“Can you tell me about your house?”

“My house?” He smiles at you. “Sure thing! All of the houses on this side were built by one company. They use pre-fabricated components that are built off-site, brought in and assembled. It only takes a day to build one!”

“What about adding rooms and other features?”

“It’s easy,” he replies. The company has a standard interface for rooms, terraces, and any other add-on. When I want to expand, I just call them, and they come out and connect the room. Everything is pre-wired, so it goes in and comes online almost as fast as I can think of it.”

You ask if he had to do any extra work to connect to public utilities.

“Not at all!” he exclaims. “There’s a panel inside where I can choose which provider I want to connect to. I just had to pick one. If I want to change it in the future, I make a different selection. The house lets me choose everything - lawn care service provider, window cleaner, painter, everything I need to make the house liveable and keep it running. I just go to the panel, make my choice, and then go back to living.

“And best of all, my house was free.”

## Rancher Always Works For You

Rancher Labs has designed Rancher to do the heaviest tasks around building and maintaining Kubernetes clusters.

### Easily Launch Secure Clusters

Let’s start with the installation. Are you installing on bare metal? Cloud instances? Hosted provider? A mix? Do you want to give others the ability to deploy their own clusters, or do you want the flexibility to use multiple providers?

Maybe you just want to use AWS, or GCP, so multiple providers isn’t a big deal. Flexibility is still important. Your requirements today might be different in a month or a year.

With Rancher you can simply fire up a new cluster in another provider and begin migrating workloads, all from within the same interface.

### Global Identity and RBAC

Whether you’re using multiple providers or not, the normal way of configuring access to a single cluster in one provider requires work. Access control policies take time to configure and maintain, and generally, once provisioned, are forgotten. If using multiple providers, it’s like learning multiple languages. Russian for AWS, Swahili for Google, Flemish for Azure, Uzbek for DigitalOcean or Rackspace…and if someone leaves the organization, who knows what they had access to? Who remembers how to speak Latin?

Rancher connects to backend identity providers, and from a global configuration it applies roles and policies to all of the clusters that it manages.

When you can deploy and manage multiple clusters as easily as you can a single one, and when you can do so securely, then it’s no big deal to spin up a cluster for UAT as part of the CI/CD test suite. It’s trivial to let developers have their own cluster to work on. You could even let multiple teams can share one cluster.

### Solutions for Cluster Multi-Tenancy

How do you keep people from stepping on each other?

You can use [Kubernetes Namespaces](https://rancher.com/learning-paths/introduction-to-kubernetes-namespaces "Read an introduction to Kubernetes namespaces"), but provisioning Roles across multiple Namespaces is tedious. Rancher collects Namespaces into Projects and lets you map Roles to the Project. This creates single-cluster multi-tenancy, so now you can have multiple teams, each only able to interact with their own Namespaces, all on the same cluster. You can have a dev/staging environment built exactly like production, and then you can easily get into the CD part of CI/CD.

### Tools for Day Two Operations

What about all of the add-on tools? Monitoring. Alerts. Log shipping. Pipelines. You could provision and configure all of this yourself for every cluster, but it takes time. It’s easy to do wrong. It requires skills that internal staff may not have - do you want your staff learning all of the tools above, or do you want them focusing on business initiatives that generate revenue? To put it another way, do you want to spend your day spinning copper wire to connect to the phone system, or would you rather press a button and be done with it?

Rancher ships with tools for monitoring your clusters, dashboards for visualizing metrics, an engine for generating alerts and sending notifications, a pipeline system to enable CI/CD for those not already using an external system. With a click it ships logs off to Elasticsearch, Kafka, Fluentd, Splunk, or syslog.

### Designed to Grow With You

The more a Kubernetes solution scales (the bigger or more complicated that it gets), the more important it is to have fast, repeatable ways to do things. What about using scripts like Ansible, Terraform, kops, or kubespray to launch clusters? They stop once the cluster is launched. If you want more, you have to script it yourself, and this adds a dependency on an internal asset to maintain and support those scripts. We’ve all been at companies where the person with the special powers left, and everyone who stayed had to scramble to figure out how to keep everything running. Why go down that path when there’s a better way?

Rancher makes everything related to launching and managing clusters easy, repeatable, fast, and within the skill set of everyone on the team. It spins up clusters reliably in any provider in minutes, and then it gives you a standard, unified interface for interacting with those clusters via UI or CLI. You don’t need to learn each provider’s nuances. You don’t need to manage credentials in each provider. You don’t need to create configuration files to add the clusters to monitoring systems. You don’t need to do a bunch of work on the hosts before installing Kubernetes. You don’t need to go to multiple places to do different things – everything is in one place, easy to find, and easy to use.

### No Vendor Lock-In

This is significant. Companies who sell you a Kubernetes solution have a vested interest in keeping you locked to their platform. You have to run their operating system or use their facilities. You can only run certain software versions or use certain components. You can only buy complementary services from vendors they partner with.

Rancher Labs believes in something different. They believe that your success comes from the freedom to choose what’s best for you. Choose the operating system that you want to use. Build your systems in the provider you like best. If you want to build in multiple providers, Rancher gives you the tools to manage them as easily as you manage one. Use any provisioner.

What Rancher accelerates is the time between your decision to do something and when that thing is up and running. Rancher gets you out the gate and onto the track faster than any other solution.

## The Wolf in a DIY Costume

Those who say that they want to “go vanilla” or “DIY” are usually looking at the cost of an alternative solution. Rancher is open source and free to use, so there’s no risk in trying it out and seeing what it does. It will even uninstall cleanly if you decide not to continue with it.

If you’re new to Kubernetes or if you’re not in a hands-on, in-the-trenches role, you might not know just how much work goes into correctly building and maintaining a single Kubernetes cluster, let alone multiple clusters. If you go the “vanilla Kubernetes” route with the hope that you’ll get a better ROI, it won’t work out. You’ll pay for it somewhere else, either in staff time, additional headcount, lost opportunity, downtime, or other places where time constraints interfere with progress.

Rancher takes all of the maintenance tasks for clusters and turns them into a workflow that saves time and money while keeping everything truly enterprise-grade. It will do this for single and multi-cluster Kubernetes environments, on-premise or in the cloud, for direct use or for business units offering Kubernetes-as-a-service, all from the same installation. It will even import the Kubernetes clusters you’ve already deployed and start managing them.

Having more than 20,000 deployments in production is something that we’re proud of. Being the container management platform for mission-critical applications in over 200 companies across so many verticals also makes us proud.

What we would *really* like is to have you be part of our community.

Join us in showing the world that there’s a better way. [Download Rancher](https://rancher.com/quick-start/) and start living in the house you deserve.Read the Guide to Kubernetes with RancherThis guide shows the challenges in running Kubernetes in production and how Rancher helps. [Get the whitepaper](https://more.suse.com/fy21-global-web-landing-page-guide-to-kubernetes)
