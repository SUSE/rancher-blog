---
title: "What’s New in Rancher’s Security Release Only Versions"
date: 2023-01-25T04:50:13
slug: "whats-new-in-ranchers-security-release-only-versions"
author: "Wendie Cheung"
products: ["Rancher Manager"]
tags: ["security", "upgrades"]
content_type: "release"
draft: false
migration:
  wp_id: 100821
  original_url: "https://www.suse.com/c/rancher_blog/whats-new-in-ranchers-security-release-only-versions/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.5 to 2.7 security-only releases"
  redirect_target: ""
---

The Rancher Security team are happy to announce the availability of new Rancher versions 2.7.1, 2.6.10 and 2.5.17 that contain exclusively fixes for security-related issues (CVEs).

These new versions are based on the last stable version of each release branch, 2.7.0, 2.6.9 and 2.5.16, respectively. For the full list of security advisories and CVEs released for these versions, please see [Rancher’s GitHub repository security page](https://github.com/rancher/rancher/security/advisories) and [Rancher Docs](https://ranchermanager.docs.rancher.com/reference-guides/rancher-security/security-advisories-and-cves) .

These new security-only releases will allow you to run Rancher in production with the additional assurance of an improved security posture.

It also introduces a new milestone in Rancher’s development process to bring it more in line with industry standards regarding security disclosure of vulnerabilities. Going forward, the Rancher team will strive to release security-only versions quarterly, to ensure a consistent cadence in cleaning up product-related CVEs in Rancher every 90 days (also called “the application layer”).

This will not necessarily include CVE fixes in the image layer-related components as these are dependent on upstream components. Future security releases of Rancher will look into introducing further updates in Rancher-provided container images and third-party dependencies, to further increase the security posture of Rancher for customers and users.

In case of more severe vulnerabilities or issues that are being exploited in the wild, also known as zero-day (0-day) vulnerabilities, out-of-band releases of Rancher will be done as necessary to support customers and maintain Rancher’s security posture.

This release also marks the end of life (EOL) support for Rancher 2.5. No further bug fixes, stability improvements or security patches will be released for the 2.5 line.

Customers and users are strongly advised to update their setups to releases 2.7 or 2.6, to benefit from better improvements and security fixes. Please consult SUSE’s product support lifecycle dates at <https://www.suse.com/lifecycle/>
