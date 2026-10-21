---
title: "Rancher-Istio will be deprecated in upcoming Rancher releases"
date: 2025-02-05T19:54:28
slug: "rancher-istio-will-be-deprecated-in-upcoming-rancher-releases"
authors: ["Nuno Do Carmo"]
products: ["Rancher Manager"]
tags: ["upgrades"]
content_type: "company-news"
draft: true
migration:
  wp_id: 145685
  original_url: "https://www.suse.com/c/rancher_blog/rancher-istio-will-be-deprecated-in-upcoming-rancher-releases/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "Rancher-Istio deprecation notice, time-bound"
  redirect_target: "suse.com (new URL pending)"
---

Rancher-Istio will be deprecated in future Rancher versions, starting with Rancher 2.12, and it will no longer receive updates or support from Rancher 2.13.

SUSE Rancher Prime subscribers are encouraged to turn to the [SUSE Application Collection build of Istio](https://apps.rancher.com/applications/istio). This will ensure continued access to a trusted, reliable, and up-to-date version of Istio, which benefits from the [SUSE Application Collection](https://apps.rancher.com/)’s curated content and enhanced security features such as vulnerability scanning, SBOMs, and SLSA level 3 compliance.

The deprecation of Rancher-Istio will occur over the next few Rancher releases, following the schedule below:

**⚠️ Rancher 2.12 (due date: July 2025)**: Rancher-Istio is officially deprecated

**⛔ Rancher 2.13 (due date: Nov. 2025)**: Rancher-Istio will no longer receive updates or support of any kind

## Why turning to the SUSE Application Collection build of Istio?

SUSE Rancher is dedicated to providing a secure and reliable cloud native platform, and customers will benefit from the SUSE Application Collection build of Istio due to:

**Enhanced Security:** Applications in the SUSE Application Collection adhere to SLSA Level 3 standards using SUSE build pipelines, have continuous vulnerability scanning, and include Software Bill of Materials (SBOMs).

**Consistent Updates:** The SUSE Application Collection provides up-to-date content, the latest security patches and features.

**Optimized Container Images:** The SUSE Application Collection utilizes optimized Container images built on the [SUSE Linux Enterprise Base Container Image](https://www.suse.com/products/base-container-images/) (SLE BCI), which provides a reduced Container size and minimizes vulnerabilities.

**Standardization:** The SUSE Application Collection ensures consistent builds, configurations, and engineering practices, which simplifies management and security policies.

## Call to Action!

We strongly advise all Rancher-Istio users to switch to the SUSE Application Collection build of Istio. This will ensure continued functionality, security and support for your Istio deployments.

Detailed steps are available in [the SUSE Knowledge Base](https://www.suse.com/support/kb/doc/?id=000021759). In a nutshell, the process involves removing the Rancher-Istio instance and then deploying the [SUSE Application Collection version of Istio](https://apps.rancher.io/applications/istio). SUSE Rancher Prime subscription includes subscription to the [SUSE Application Collection](https://apps.rancher.io/).

## Support and Questions

If you have any questions or require assistance with this switch, please do not hesitate to contact us. Our support team is ready to help you. We understand that this can require effort, but we are confident that the benefits provided by the Application Collection will greatly enhance your Istio experience and overall platform security and reliability.

Thank you for your understanding and cooperation as we strive to enhance your Rancher experience.
