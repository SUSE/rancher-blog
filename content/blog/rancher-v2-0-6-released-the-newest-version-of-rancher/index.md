---
title: "Rancher v2.0.6 Released -- the Newest Version of Rancher"
date: 2018-07-12T09:03:00
slug: "rancher-v2-0-6-released-the-newest-version-of-rancher"
author: "Rancher Admin"
products: ["Rancher Manager"]
tags: []
content_type: "release"
draft: false
migration:
  wp_id: 85823
  original_url: "https://www.suse.com/c/rancher_blog/rancher-v2-0-6-released-the-newest-version-of-rancher/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher v2.0.6 release notes"
  redirect_target: ""
---

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)

### Rancher new release

We are proud to announce that we have released a new version of Rancher, [Rancher v2.0.6](https://forums.rancher.com/t/rancher-release-v2-0-6/11090).

This version provides some nice enhancements and new features from the previous stable v2.0.4. These are some of the new features:

- Nested group membership authentication option for Active Directory and OpenLDAP directory services, which provides permissions to users that are in groups of groups. This feature is disabled by default; to activate it, please review the “Customize Schema” section and select the “Search direct and nested group memberships” option. Enabling nested group membership could cause slower search results/login, due to extensive user search.
- Support for opensource directory services, OpenLDAP and FreeIPA, as authentication providers and can be selected as an option. You can now integrate Rancher with OpenLDAP or FreeIPA to manage and control user authentication and authorization on K8s clusters and projects.
- Cordon/Uncordon K8s cluster nodes. At some point in time in a K8s cluster lifecycle, users may need to execute some maintance tasks (such as patch, update, reboot,…) on K8s nodes. With this new feature, you could temporarily cordon nodes so that no K8s pods will be able to be scheduled on them. Once K8s nodes are ready again, you can uncordon them to make them work normally.
- [Azure AKS advanced networking](https://docs.microsoft.com/en-us/azure/aks/networking-overview#advanced-networking-features) options. Users now have the ability to select a different resource group for Azure AKS advanced networking.
- Support Infrastructure as Code (IaC) at rancher CLI. Two new commands have been added to it to facilitate automation, deployment and reproductability of K8s clusters running on Rancher.

  - `rancher cluster export` - allows the export of a K8s cluster definition as a YAML file.
  - `rancher up` - allows the import of a YAML file for cluster creation within Rancher.

New Docker images are released, tagged and published on Docker Hub. The Rancher server can be pulled as rancher/rancher with one of following tags, `v2.0.6` , `latest` or `stable`.

*Note:* If you are upgrading from a previous Rancher v2.0.x version, please review our Github [Rancher v2.0.6 release info](https://github.com/rancher/rancher/releases/tag/v2.0.6) to check for known issues, upgrades and rollback notes.

Expert Training in Kubernetes and RancherJoin our free online training sessions to learn more about Kubernetes, containers, and Rancher.[Sign up here](https://rancher.com/training/)
