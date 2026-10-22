---
title: "Rancher 2.2 Hits the GA Milestone"
date: 2019-03-26T09:42:00
slug: "rancher-2-2-hits-the-ga-milestone"
author: "Rancher Admin"
image: "images/rancher_blog_cover.jpg"
products: ["Rancher Manager"]
tags: ["upgrades"]
content_type: "release"
draft: false
migration:
  wp_id: 85913
  original_url: "https://www.suse.com/c/rancher_blog/rancher-2-2-hits-the-ga-milestone/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.2 GA release"
  redirect_target: ""
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher. [Sign up here](https://rancher.com/training/) We released [version 2.2.0](https://www.rancher.com/products) of Rancher today, and we’re beyond excited. The latest release is the culmination of almost a year’s work and brings new features to the product that will make your Kubernetes installations more stable and easier to manage.

When we released Preview 1 in December and Preview 2 in February, we

covered their features extensively in blog articles, meetups, videos,

demos, and at industry events. I won’t make this an article that

rehashes what others have already written, but in case you haven’t seen

the features we’ve packed into this release, I’ll do a quick recap.

## Rancher Global DNS

There’s a telco concept of the “last mile,” which is the final

communications link between the infrastructure and the end user. If

you’re all in on Kubernetes, then you’re using tools like CI/CD or some

other automation to deploy workloads. Maybe it’s only for testing, or

maybe your teams have full control over what they deploy.

DNS is the last mile for Kubernetes applications. No one wants to deploy

an app via automation and then go manually add or change a DNS record.

Rancher Global DNS solves this by provisioning and maintaining an

external DNS record that corresponds to the IP addresses of the

Kubernetes Ingress for an application. This, by itself, isn’t a new

concept, but Rancher will also do it for applications deployed to

multiple clusters.

Imagine what this means. You can now deploy an app to as many clusters

as you want and have DNS automatically update to point to the Ingress

for that application on **all** of them.

## Rancher Cluster BDR

This is probably my favorite feature in Rancher 2.2. I’m a huge fan of

backup and disaster recovery (BDR) solutions. I’ve seen too many things

fail, and when I know I have backups in place, failure isn’t a big deal.

It’s just a part of the job.

When Rancher spins up a cluster on cloud compute instances, vSphere, or

via the Custom option, it deploys Rancher Kubernetes Engine (RKE).

That’s the CNCF-certified Kubernetes distribution that Rancher

maintains.

Rancher 2.2 adds support for backup and restore of the etcd datastore

directly into the Rancher UI/API and the Kubernetes API. It also adds

support for S3-compatible storage as the endpoint, so you can

immediately get your backups off of the hosts without using NFS.

When the unthinkable happens, you can restore those backups directly

into the cluster via the UI.

You’ve already been making snapshots of your cluster data and moving

them offsite, right? Of course you have.…but just in case you

haven’t, it’s now so easy to do that there’s no reason not to do it.

## Rancher Advanced Monitoring

Rancher has always used Prometheus for monitoring and alerts. This

release enables Prometheus to reach even further into Kubernetes and

deliver even more information back to you. One of the flagship features

in Rancher is [single cluster multi-tenancy](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/projects-and-namespaces),

where one or more users have access to a Project and [can only see the resources within that Project](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/authentication-permissions-and-global-configuration/manage-role-based-access-control-rbac/cluster-and-project-roles)

even if there are other users or other Projects on the cluster.

Rancher Advanced Monitoring deploys Prometheus and Grafana in a way that

respects the boundaries of a multi-tenant environment. Grafana installs

with pre-built cluster and Project dashboards, so once you check the box

to activate the advanced metrics, you’ll be looking at useful graphs a

few minutes later.

Rancher Advanced Monitoring covers everything from the cluster nodes to

the Pods within each Project, and if your application exposes its own

metrics, Prometheus will scrape those and make them available for you to

use.

## Multi-Cluster Applications

Rancher is built to manage multiple clusters. It has a strong

integration with Helm via the [Application Catalog](https://rancher.com/docs/rancher/v2.x/en/catalog/), which takes

Helm’s key/value YAML and turns it into a form that anyone can use.

In Rancher 2.2 the Application Catalog also exists at the Global level,

and you can deploy apps via Helm simultaneously to multiple Projects in

any number of clusters. This saves a tremendous amount of time for

anyone who has to maintain applications in different environments,

particularly when it’s time to upgrade all of those applications.

Rancher will batch upgrades and rollbacks using Helm’s features for

atomic releases.

Because multi-cluster apps are built on top of Helm, they’ll work out of

the box with CI/CD systems or any other automated provisioner.

## Multi-Tenant Catalogs

In earlier versions of Rancher the configuration for the Application

Catalog and any external Helm repositories existed at the Global level

and propagated to the clusters. This meant that every cluster had access

to the same Helm charts, and while that worked for most installations,

it didn’t work for all of them.

Rancher 2.2 has cluster-specific and project-specific configuration for

the Application Catalog. You can remove it completely, change what a

particular cluster or project has access to, or add new Helm

repositories for applications that you’ve approved.

## Conclusion

The latest version of Rancher gives you the tools that you need for “day

two” Kubernetes operations -- those tasks that deal with the management

and maintenance of your clusters after launch. Everything focuses on

reliability, repeatability, and ease of use, because using Rancher is

about helping your developers accelerate innovation and drive value for

your business.

[Rancher 2.2](https://www.rancher.com/products) is available now for deployment in dev and staging environments as `rancher/rancher:latest`. Rancher recommends that production environments hold out for `rancher/rancher:stable` before upgrading, and that tag will be available in the coming days.

If you haven’t yet deployed Rancher, now is a great time to start! With [two easy steps](https://www.rancher.com/quick-start) you can have Rancher up and running, ready to help you manage Kubernetes.

### Join the Rancher 2.2 Online Meetup on April 3rd

To kick off this release and explain in detail each of these new, powerful features, we’re hosting an Online Meetup on April 3rd. It’s free to join and there will be live Q&A with the engineers who directly worked on the project. [Get your spot here.](https://info.rancher.com/meetup-introducing-rancher-2.2)Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher. [Sign up here](https://rancher.com/training/)
