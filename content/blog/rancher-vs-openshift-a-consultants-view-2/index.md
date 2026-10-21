---
title: "Rancher vs. OpenShift – A Consultant’s View"
date: 2020-01-28T09:57:00
slug: "rancher-vs-openshift-a-consultants-view-2"
author: ""
image: "images/rancher_blog_featured-image-rancher-v-openshift.png"
products: ["Rancher Manager"]
tags: []
content_type: "opinion"
draft: true
migration:
  wp_id: 86318
  original_url: "https://www.suse.com/c/rancher_blog/rancher-vs-openshift-a-consultants-view-2/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "2019 competitor comparison, sales-led"
  redirect_target: "suse.com (new URL pending)"
---

In any rapidly emerging market, consultants can be a great source for vendor-neutral insights, as they typically work with multiple technologies to help their customers make informed decisions. In that vein, Derya (Dorian) Sezen of kloia, a new-era consulting organization that provides services toward transition of legacy workloads to frontline technologies in Cloud, DevOps and Microservices, recently wrote a blog summarizing his experience with Rancher and Red Hat OpenShift. In his [blog](https://www.kloia.com/blog/openshift-vs-rancher), Dorian compared and scored the two Kubernetes management tools across 13 categories including installation easiness, CNCF/industry standards, open-source, licensing, multi-cluster, upgrades, Kubernetes version, vendor-lock, Windows container support, support, sales, partner ecosystem and bundle options.

Dorian’s comparison is based on Rancher and OpenShift customer feedback, technical evidence and his experience with both platforms as a cloud and DevOps consultant. The final score was Rancher 33 points, OpenShift 25 points. Check out Dorian’s key points and our associated takeaways:

## Installation Easiness

- **Rancher:** Installation [takes] between 20 minutes to 2 hours.
- **OpenShift:** Installation is reported [to take] from 3 days to weeks, mostly reported [it] takes more than a week.
- **Key Takeaway:** Fast and simple installation is critical to widespread adoption of open-source software across your organization. It’s no surprise that Rancher is already the industry’s most widely adopted Kubernetes management platform with over 100M downloads and more than 30k active users.

## Upgrades

- **Rancher:** Version upgrades are smooth.
- **OpenShift:** Failed version upgrades and rollbacks are reported. Several disruptions after upgrades are reported.

“OpenShift has relatively longer installation and upgrade times,” says Sezen. “This is not suitable for CI/CD solutions that deploy the entire clusters during the platform deployment pipelines. Version upgrades on OpenShift are reported to be risky and painful. Some major upgrades have been reported to take all night till the morning. And a specific version upgrade has been reported [to have] created disruption on the overall system.”

- **Key takeaway:** Upgrades should be smooth and without risk. With the release of Rancher 2.3, we disconnected the Rancher upgrade process from the Kubernetes cluster upgrade process, so now, you can update the metadata store for available Kubernetes versions without updating Rancher.

## CNCF/Industry Standards/Open Source

- **Rancher:** follows and extends industry standards.
- **OpenShift:** Although Red Hat contributes to upstream Kubernetes projects, OpenShift is reported to favor its own non-CNCF tools and practices during OpenShift onboarding.
- **Key takeaway:** Favoring your own non-CNCF tools and practices equates to vendor lock-in. As Dorian states, “Once installed, switching to vanilla Kubernetes is not possible.” Rancher is 100% open-source on native upstream Kubernetes with no forks and no vendor lock-in. If you ever decide to not use Rancher, your transition will be easy. That is not the case with Red Hat.

## Support

- **Rancher:** Supports not only the platform but also the tools in the Kubernetes ecosystem.
- **OpenShift:** Support platform is provided.
- **Key takeaway:** Rancher’s focus is on the best customer experience. A Rancher enterprise subscription includes not only 24/7 worldwide support but also onboarding and professional services to ensure customers get the most out of their investment in not just Rancher, but Kubernetes overall.

## Partner Ecosystem

- **Rancher:** Limited partner channel.
- **OpenShift:** IBM partners worldwide are OCP partners.
- **Key takeaway:** Size does matter, but so does focus. Every IBM partner may be an OCP partner, but that doesn’t mean they are qualified Kubernetes experts. Rancher’s rapidly growing ecosystem of premium partners consists of partners who put the time and resources into qualifying their staff on Kubernetes and Rancher technologies.

Of course, this is one organization’s experience and your mileage may vary. But it’s valuable insight, nonetheless, and why we wanted to share the information.

## More Resources

Learn more about Rancher’s benefits in [A Buyer’s Guide to Enterprise Kubernetes Management Platforms](https://more.suse.com/fy21-global-web-landing-page-enterprise-kubernetes-management-buyers-guide).
