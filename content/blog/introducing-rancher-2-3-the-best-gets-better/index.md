---
title: "Introducing Rancher 2.3: The Best Gets Better"
date: 2019-10-08T09:42:00
slug: "introducing-rancher-2-3-the-best-gets-better"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_rancher.png"
products: ["Rancher Manager"]
tags: ["windows", "multi-cluster"]
content_type: "release"
draft: true
migration:
  wp_id: 85912
  original_url: "https://www.suse.com/c/rancher_blog/introducing-rancher-2-3-the-best-gets-better/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "Rancher 2.3 release announcement"
  redirect_target: "suse.com (new URL pending)"
---

Today we are excited to announce the general availability of Rancher 2.3,
the latest version of our flagship product. Rancher, already the
industry’s most widely adopted Kubernetes management platform, adds
major new features with v2.3, including:

- Industry’s first generally available support for Windows containers, bringing the benefits of Kubernetes to Windows Server applications.
- Introduction of cluster templates for secure, consistent deployment of clusters in large scale deployments
- Simplified installation and configuration of Istio service mesh

These new capabilities strengthen our *Run Kubernetes Everywhere* strategy
by enabling an even broader range of enterprises to leverage the
transformative power of Kubernetes.

## Bringing the Benefits of Kubernetes to Windows Server Applications

Today, 70% of on-premises workloads are running on the Windows Server
operating system, and in March of this year, Windows Server Container
support was built into the release of Kubernetes v1.14

Not surprisingly, Windows containers have been one of the most desired technologies within the Kubernetes ecosystem in recent years. We are proud to be partnering with Microsoft on this launch and are excited to be the first Kubernetes management platform to deliver GA support for Windows Containers and Kubernetes with Windows worker nodes! To get Microsoft’s perspective on Rancher 2.3, check out [this blog](/blog/windows-containers-and-rancher-2-3/) from Mike Kostersitz, Principal Program Manager at Microsoft.

By bringing all the benefits of Kubernetes to Windows, Rancher 2.3 eases
complexity and provides a fast and straightforward path for modernizing
legacy Windows-based applications, regardless of whether they will run
on-premises or in a multi-cloud environment. Alternatively, Rancher 2.3
can eliminate the need to go through the process of rewriting
applications by containerizing and transforming them into efficient,
secure and portable multi-cloud applications.

![Windows Workloads](images/rancher_blog_image1.png)

## Secure, Consistent Deployment of Kubernetes Clusters with Cluster Templates

With most businesses managing multiple clusters at any one time,
security is a key priority for all organizations. Cluster templates help
organizations reduce risk by enabling them to enforce consistent cluster
configurations across their entire infrastructure. Specifically, with
cluster templates:

- Operators can create, save, and confidently reuse well-tested Kubernetes configurations across all their cluster deployments.
- Administrators can enable configuration enforcement, thereby eliminating configuration drift or improper misconfigurations which, left unchecked, can introduce security risks as more clusters are created.

![Cluster Templates](images/rancher_blog_image2.png)

Additionally, admins can scan existing Kubernetes clusters using industry tools like CIS and NIST to identify and report on unsecure cluster settings in order to facilitate a plan for remediation.

## Tighter Integration with the Leading Service Mesh Solution

A big part of Rancher’s value is its rich ecosystem catalogue of
Kubernetes services, including service mesh. Istio, the leading service
mesh, eliminates the need for developers to write specific code to enable
key Kubernetes capabilities like fault tolerance, canary rollouts,
A/B testing, monitoring and metrics, tracing and observability, and
authentication and authorization.

Rancher 2.3 delivers simplified installation and configuration of
Istio including:

- Kiali dashboards for traffic and telemetry visualization
- Jaeger for tracing
- Prometheus and Grafana for observability

![Istio](images/rancher_blog_image3.png)

Rancher 2.3 also introduces support for Kubernetes v1.15.x and Docker
19.03. Getting started with Rancher v2.3 is easy. See [our documentation](https://rancher.com/docs/rancher/v2.x/en/quick-start-guide/deployment/quickstart-manual-setup/) for instructions on how to be up and running in a flash.

## Our Momentum Continues

Rancher 2.3 is just the latest proof point of our momentum in 2019.
Other highlights include:

- 161 percent year-on-year [revenue growth](https://rancher.com/press/2019-07-23-rancher-labs-accelerates-momentum-release/), community growth to more than 30,000 active users, oftware downloads have surpassed 100M.
- Rancher was [named a leader](https://more.suse.com/fy21-global-web-landing-page-forrester-new-wave-enterprise-container-platform) in Forrester New WaveTM , Enterprise Container Platform Software Suites
- Rancher [is included](https://rancher.com/press/2019-08-27-gartner-cycles-press-release/) in Five Gartner Hype Cycles in 2019
- Rancher [was recognized](https://info.rancher.com/451-research-firestarter-award-winner) by 451 Research as a Firestarter in Q3’19

And, maybe the best part of the story is that we have more exciting news coming very soon! Stay tuned to [our blog](https://rancher.com/blog/) to learn more.

We also look forward to seeing everyone at KubeCon 2019 in San Diego, California. Come to booth P19 to talk with us or get a personalized demo.
