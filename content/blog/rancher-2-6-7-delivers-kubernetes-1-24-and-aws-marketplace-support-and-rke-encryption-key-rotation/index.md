---
title: "Rancher 2.6.7 Delivers Kubernetes 1.24 and AWS Marketplace Support and RKE Encryption Key Rotation"
date: 2022-08-23T20:28:09
slug: "rancher-2-6-7-delivers-kubernetes-1-24-and-aws-marketplace-support-and-rke-encryption-key-rotation"
authors: ["William Jimenez"]
image: "images/rancher-logo-stacked-color-2.png"
products: ["Rancher Manager"]
tags: ["cloud", "aws"]
content_type: "release"
draft: false
migration:
  wp_id: 93799
  original_url: "https://www.suse.com/c/rancher_blog/rancher-2-6-7-delivers-kubernetes-1-24-and-aws-marketplace-support-and-rke-encryption-key-rotation/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher 2.6.7 release notes"
  redirect_target: ""
---

SUSE is happy to announce the latest release of Rancher, 2.6.7. In this release, we have added several new features:

- Kubernetes 1.24 support
- AWS Marketplace support
- Azure Active Directory (Azure AD) with MSAL (Microsoft Authentication Library)
- RKE2 Encryption Key Rotation

Our latest Kubernetes release addition means Rancher can now manage clusters with the newer capabilities offered by upstream Kubernetes 1.24. This applies to RKE, RKE2, and K3s distributions as well as any CNCF-certified Kubernetes you wish to manage through Rancher.

With our AWS Marketplace support, customers can now purchase support contracts for Rancher directly through the AWS marketplace. This means there are no additional procurement processes to go through if your organization already has a commercial relationship with AWS. This also allows customers to use their Enterprise Discount Program (EDP) spending commitments with AWS towards Rancher, which is helpful for large consumers of AWS products and services. Look for a detailed blog on this AWS Marketplace support to follow shortly.

Rancher’s support for integrating with Azure AD has been upgraded to use the new Microsoft Graph API (AKA MSAL). Microsoft is decommissioning the old API before the end of the year, and all users will need to switch to the newer standard. You can read more about this change and any steps you may need to take [here](https://www.suse.com/support/kb/doc/?id=000020682).

RKE2 Encryption Key Rotation gives security-minded customers an easy way to increase their security posture. Rotating encryption keys are a best practice with many security standards and compliance frameworks, so this feature makes it easier to uplevel the security of your RKE2 clusters. Key rotation is another way that RKE2 continues to invest in increasing the security posture of Kubernetes for the enterprise.

## Learn More and Try Rancher 2.6.7

Do you know that Rancher customers can join a quarterly Customer Advisory Board and share direct feedback with Product and Engineering leaders? Speak to your CSM or Account executive if you aren’t already signed up. We look forward to your feedback on this latest Rancher release!

[Try out the latest Rancher release here](https://github.com/rancher/rancher/releases)
