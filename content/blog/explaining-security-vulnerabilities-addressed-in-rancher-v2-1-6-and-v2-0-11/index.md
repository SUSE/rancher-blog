---
title: "Explaining security vulnerabilities addressed in Rancher v2.1.6 and v2.0.11"
date: 2019-01-29T09:04:00
slug: "explaining-security-vulnerabilities-addressed-in-rancher-v2-1-6-and-v2-0-11"
author: "Rancher Admin"
products: ["Rancher Manager"]
tags: ["security"]
content_type: "release"
draft: false
migration:
  wp_id: 85838
  original_url: "https://www.suse.com/c/rancher_blog/explaining-security-vulnerabilities-addressed-in-rancher-v2-1-6-and-v2-0-11/"
  disposition: migrate
  commercial: false
  outdated_reason: "Rancher v2.1.6 and v2.0.11 advisory"
  redirect_target: ""
---

Today we announced releases v2.1.6 and v2.0.11 to address two security vulnerabilities recently discovered in Rancher. The first vulnerability allows users in the Default project of a cluster to escalate privileges to that of a cluster admin through a service account. The second vulnerability allows members to have continued access to create, update, read, and delete namespaces in a project after they have been removed from it. You can view the official CVEs here [CVE-2018-20321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20321) and here [CVE-2019-6287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-6287). This blog will explain each of these issues in more detail, their impact to users, and what can and should be done.

## CVE-2018-20321 - Privilege escalation through service account

This vulnerability affects all versions from v2.0.0 - v2.1.5. It allows any project member with access to the default namespace to use a service account created by the Rancher control plane. This service account can be used to execute administrator level API calls against the Kubernetes cluster.

The name of the service account is "netes-default". It is created in the "default" namespace and given the "cluster-admin" clusterRole. This grants full administrator privileges to the cluster. To understand this vulnerability, you must understand that once a service account is created in a namespace, anyone with member level privileges in that namespace is allowed to use that service account. This is known and expected service account behavior (see [the Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) for more details). However, the vulnerability arises from the fact that Rancher placed the service account in the default namespace and that namespace into the Default project. This namespace and project are expected to be used by non-admin users to create and manage workloads. The service account should not be exposed in a normal member-level namespace or project. It should be created in a namespace and project that only administrators have access to.

While we highly recommend that you upgrade to address this problem, we've also written [step-by-step mitigation instructions](https://github.com/rancher/rancher/issues/17725#issuecomment-458730471) you can take to quarantine the default namespace if you cannot immediately upgrade. Additionally, because the fix involves a data migration (deleting a service account and creating it elsewhere), rolling Rancher back from the patched version to a version prior to the patch is more complicated than usual. We have documented these steps [here](https://rancher.com/docs/rancher/v2.x/en/upgrades/rollbacks/).

The new releases address this problem by deleting the service account and recreating it in the cattle-system namespace, which is not placed in the Default project. In versions v2.0.8 and later, it is placed in the "System" project. In versions v2.0.7 and under, the "System" project does not exist and so it is up to the administrator to place the namespace into a project.

Many thanks to Rancher community members Michal Swierczewski and Mateusz Dyminski for discovering and reporting this issue.

## CVE-2019-6287 - Privileges not fully revoked when a member is removed from a project

This vulnerability also affects v2.0.0 - v2.1.5. Unfortunately, there are no practical mitigation steps and you must upgrade to address the issue. It allows members who were removed from a project to continue to be able create, update, read, and delete namespaces in that project. They cannot access resources (ie pods and services) in the namespaces, they can just manipulate the namespace resources themselves.

This vulnerability exists because Rancher is not properly cleaning up all of the roleBindings associated with a user or group when that member is removed from a project. A roleBinding is a Kubernetes construct that defines the access a user or group has to resources. It is used to enforce role-based access control (RBAC). When a user or group is added to a project in Rancher, several roleBindings are created in the Kubernetes cluster. Rancher creates multiple rolebindings in order to enforce proper RBAC controls over our "project" concept, which is not native to Kubernetes. When that user or group is removed from the project, all of these roleBindings should be cleaned up, but this bug is preventing the cleanup of roleBindings that control access to the namespaces in the project. Under the covers, it is caused by two logic flaws in how we determine what roleBindings should be deleted.

For more information on Kubernetes roles and roleBindings and RBAC in general, see the Kubernetes documentation here: <https://kubernetes.io/docs/reference/access-authn-authz/rbac/>. For more information on how Rancher builds on top of Kubernetes RBAC, see our documentation here: <https://rancher.com/docs/rancher/v2.x/en/admin-settings/rbac/>.

Note that this vulnerability can be exploited through the Rancher UI, API, or through kubectl using the kubeconfig that users can create in the Rancher UI. If the user was only added to a single project in a cluster and was then removed from that project, they would not see the cluster in the UI or API any more and thus would not be able to exploit the issue through those means. However, if they previously created and saved a kubeconfig for the cluster from the UI, they would still be able to exploit this vulnerability through kubectl.

The new releases address this vulnerability by removing previously orphaned roleBindings and ensuring that cleanup is properly enforced for all future project member removals.

If you have security related issues to report, please submit them via email to security@rancher.com. We support responsible disclosure and endeavor to resolve all issues in a reasonable time frame.
