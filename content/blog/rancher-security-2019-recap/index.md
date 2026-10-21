---
title: "Rancher Security: 2019 Recap"
date: 2019-12-19T09:42:00
slug: "rancher-security-2019-recap"
authors: ["Bill Maxwell"]
image: "images/rancher_blog_featured-images-inside-threats.png"
products: ["Rancher Manager"]
tags: ["security"]
content_type: "company-news"
draft: true
migration:
  wp_id: 85918
  original_url: "https://www.suse.com/c/rancher_blog/rancher-security-2019-recap/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2019 security recap, Rancher 2.3"
  redirect_target: "rancher.com/blog (hub)"
---

It’s that time of year again, the time for retrospective articles and “Top 10 of the Year” posts. We decided to focus our recap on how CVEs and changes in the threat landscape affected Kubernetes in 2019, and what changes that brought about inside of Rancher.

Throughout 2019, solutions across the CNCF stack prioritized security and brought it to the forefront of both mind and action. The Kubernetes project [published the initial results](https://www.cncf.io/blog/2019/08/06/open-sourcing-the-kubernetes-security-audit/) of its security review and presented its plan for moving security forward in the project.

We made it easier for people outside of Rancher to raise security concerns, and we overhauled the procedures for how we fix those issues. We also implemented new procedures for how we safely bring the issues and their resolution to the attention of our users. The result is a process that enables the swift release of security updates for both Rancher and Kubernetes, with additional support available from Rancher engineers when needed. We published CIS self-assessments, hardening guides, and engaged third-party firms to conduct penetration testing of the Rancher product. Our entire incident management process is now more efficient than ever, and we added features into our products that make securing Kubernetes environments even easier.

The security audits were carried out by two independent firms who conducted white box penetration testing of the Rancher platform. Cure53, the company that performed security audits of Prometheus and CoreDNS for the CNCF, conducted the most recent test. We also hired Untamed Theory, who tested the platform and identified areas where we could improve. Our engineering department incorporated both sets of findings, and all issues have been fixed and verified. [The reports are now publicly available](https://rancher.com/docs/rancher/v2.x/en/security/#third-party-pen-test-reports). We continue to monitor and improve the process to maximize the security of the platform.

Over the past year, we added several features to Rancher and RKE that make it easier to harden Kubernetes clusters.

RKE now allows for:

- Direct enablement of the encryption provider
- Configuration of audit logging and rate-limiting
- Easy deployment of securely provisioned clusters via cluster templates

Beginning with Rancher 2.3, administrators can upgrade clusters to new versions of Kubernetes without being required to first upgrade Rancher itself. This feature demonstrates our commitment to keeping Rancher users secure by disconnecting the Rancher release cycle from the Kubernetes release cycle.

Our work continues on the 2.4 release of Rancher, scheduled for early Q2 2020. Clusters will have CIS scanning embedded into the heart of the product, enabling the observability that security and operations teams require for enterprise deployments of Kubernetes.

For more information on security in Kubernetes and Rancher, or to review remediated CVE or download the Rancher Hardening Guide, please visit the [security section of the Rancher documentation](https://rancher.com/docs/rancher/v2.x/en/security/).

Some might look back on 2019 as the year that challenged Kubernetes to make security a first-class concern. As Kubernetes continues to gain traction in the enterprise, cluster administrators must understand how to deploy and secure Kubernetes and its workloads properly. Rancher transforms that complexity into something manageable, and we’re honored to be with you on your journey.

Have a safe and happy holiday, and we look forward to celebrating another fantastic year of cloud-native technology with you at the end of 2020.
