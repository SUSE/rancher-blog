---
title: "Customizing and Securing Your Epinio Installation"
date: 2022-09-08T22:24:46
slug: "customizing-and-securing-your-epinio-installation"
authors: ["Andrew Gracey"]
image: "images/icon-epinio.png"
products: ["Epinio"]
tags: ["security"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 94155
  original_url: "https://www.suse.com/c/rancher_blog/customizing-and-securing-your-epinio-installation/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Epinio discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

As I’ve [written about before](https://www.suse.com/c/rancher_blog/customizing-your-application-with-epinio/), Epinio is built to be very flexible. In this blog, I will highlight several places we can hook into the rest of your existing infrastructure to give you a better experience.

If you’re new to Epinio, it’s the application development engine for Kubernetes that lets you to go from code to URL in one step. Epinio installs into any Kubernetes cluster to bring your application from source code to deployment and allow developers and operators to work better together.

## **Asset Storage in Epinio**

Up first is the storage of intermediates that we use while building a developer’s code and deploying it. We use both object storage for uncompiled code caching and an OCI registry for image caching and propagation. The object storage can be any S3- compatible storage and is controlled by the `s3.` values provided to Helm on installation. This allows you to hook into existing storage that’s a cheaper rate or more performant than what may be attached to your Kubernetes cluster.

For the docs on setting up an external object store, see: <https://docs.epinio.io/howtos/setup_external_s3>

Similarly, Epinio supports using an external registry for build images. This allows for automated scanning by tools like [NeuVector](https://www.suse.com/products/neuvector/) or Trivy to provide a more secure environment and is highly recommended for production use!

For the docs on setting up an external registry, see: <https://docs.epinio.io/howtos/setup_external_registry>

## **Build Process in Epinio**

While the Paketo Full builder image is quite comprehensive, there may be times that you need to adjust how images are getting built. To do this, we allow for using custom builder images. Builder images in the cloud native buildpack are container images that know how to build and publish other images. Using your own is as easy as running epinio push with the `--builder-image` flag set.

The full docs on this can be found at <https://docs.epinio.io/howtos/custom_builder>

What’s not documented is the ability to set this platform-wide by setting `image.builder.repository` and `image.builder.tag` appropriately in Epinio’s Helm chart values.

## **Application Templates in Epinio**

I discussed this in my last blog, so I won’t go into much detail. But you can change Epinio’s opinion of what a Kubernetes application looks like when deployed. This allows for a huge amount of additional flexibility and security.

We recommend changing this in production by adding things like NetworkPolicies and observability functionality like the open-telemetry operator.

This is documented in: <https://docs.epinio.io/howtos/using_custom_appcharts>

## **Services in Epinio**

Most application components don’t live in isolation and must work with others to function correctly. To allow a better developer experience, we’ve added a service marketplace to the platform that can be configured by the platform operators to give developers access to services they may need. Like Application Templates, this was also discussed in my last post.

## **Security in Epinio**

Lastly, one of the reasons that we want to add on to or configure Epinio in certain ways is to provide a better security posture to the platform. While this is custom to your environment and regulatory concerns, there are some best practices that we’ve found:

**Run a Kubernetes security suite** (I’m naturally biased toward NeuVector) underneath the platform to lock down the control plane and build a process that can only run what you want to run.

**Lock down the build to only pull through artifact caches**. For example, use Nexus or Artifactory to host your own Maven repository and enforce the pipeline. These types of enforcements are provided via buildpack configuration and should be backed up by Network Policies and NeuVector. (Docs for this still need to be written so this step is still “exercise left for reader”)

**Scan your images as they are published**. I’m also biased here toward NeuVector. This will ensure that nothing slips through the cracks and that there is a comprehensive view of what’s running in your environment.

**Split your networking**. With Ingress Classes, we can split the workload traffic from control plane traffic and then put the ingress for each on its own network. This allows for running in a DMZ where the workload traffic is public, but an attacker doesn’t have access to the Epinio API.

**Push to production only via CI pipeline**. When running Epinio in production, it’s best only to have one user for CI use. This makes sure that no one else can gain access to the system or its workloads.

## Conclusion

Many (if not all) of these steps are not new ideas and have been best practices for a long time. Epinio allows for pulling these best practices into the Kubernetes world in a way that stays out of the way of developers. This means that they won't just get disabled or otherwise worked around at the first chance possible!

## **Next Steps: Learn More at the Global Online Meetup on Epinio**

Join our Global Online Meetup: Epinio on Wednesday, September 14th, 2022, at 11 AM EST.  We will discuss the Epinio GA 1.0 release and how it delivers applications to Kubernetes faster, along with a live demo! [**Sign up here.**](https://more.suse.com/global_online_meetup_epinio_developer_platform.html)
