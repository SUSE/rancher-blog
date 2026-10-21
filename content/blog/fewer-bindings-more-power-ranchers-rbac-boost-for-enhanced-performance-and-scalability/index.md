---
title: "Fewer Bindings, More Power: Rancher's RBAC Boost for Enhanced Performance and Scalability"
date: 2025-06-18T00:00:47
slug: "fewer-bindings-more-power-ranchers-rbac-boost-for-enhanced-performance-and-scalability"
author: "Silvio Moioli"
image: "images/AdobeStock_294534296-1200x557-677b356.png"
products: ["Rancher Manager"]
tags: ["security", "multi-cluster"]
content_type: "explainer"
draft: false
migration:
  wp_id: 157768
  original_url: "https://www.suse.com/c/rancher_blog/fewer-bindings-more-power-ranchers-rbac-boost-for-enhanced-performance-and-scalability/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Managing permissions in sprawling Kubernetes landscapes can often feel like untangling an ever-growing knot. As clusters and user bases expand, so does the intricate web of RoleBindings, impacting everything from UI responsiveness to the very stability of etcd. This complexity, if unaddressed, can become a significant hurdle to achieving scalability and maintaining optimal performance in Rancher.

SUSE is committed to improving its container management platform. We want it to meet the needs of our current operations and grow with our growing goals.

A significant, under-the-hood improvement has been developed to address these RBAC challenges—a smarter way to handle Role Based Access Control (RBAC) that directly boosts Rancher's performance and scalability, especially when dealing with complex role inheritance. This technical deep-dive explores this recent advancement, detailing how Rancher is evolving to provide a more efficient and scalable experience.

## **The Challenge: When More Roles Mean More Headaches**

### **Understanding RoleBinding Proliferation**

In many large-scale Rancher deployments, RoleBindings can become one of the most numerous Kubernetes objects[1], and it comes at a cost. An internal review for this improvement highlighted a real-world customer scenario where RoleBindings constituted a staggering 27% of all Kubernetes resources, numbering in the tens of thousands. This sheer volume can approach the known limits of well-functioning etcd databases[2].

Rancher utilizes RoleTemplates to define reusable sets of permissions. A common and useful practice for organizing access is to create a custom role and inherit permissions from other RoleTemplates. This traditional approach involves Rancher creating a distinct RoleBinding for *each* inherited role. This multiplication occurred for *each* user or group, in *each* relevant scope, such as a project or cluster namespace. Rancher-specific RBAC concepts like Project Role Template Bindings (PRTBs) and Cluster Role Template Bindings (CRTBs) are the mechanisms that trigger the creation of these underlying Kubernetes RBAC resources.

The design of creating individual RoleBindings for each inherited role is logical for basic cases. However, as users increasingly leverage Rancher's features like projects[3] and RoleTemplate inheritance for better organization and soft multi-tenancy, the number of underlying Kubernetes objects (RoleBindings) grows multiplicatively. This growth isn't always immediately obvious to the end-user defining high-level permissions, but its effects become apparent as systems scale.

### **Impacts on Performance and Scalability**

This proliferation of RoleBindings can lead to significant performance degradation. The consequences are multifaceted:

- **etcd Strain**: Kubernetes' etcd database, the central datastore for cluster state, has practical limits on the number of objects it can efficiently manage. Pushing these limits with an excessive volume of RoleBindings can slow down etcd itself, impacting overall cluster operations.
- **UI Slowdown**: Users might experience noticeable slowdowns within the Rancher UI, as it queries Rancher’s backend API, Steve, which needs to process this vast amount of RBAC information to determine access and display relevant resources.
- **API Latency**: The increased load on etcd and the sheer number of RBAC objects can also lead to higher latency for API server requests, particularly those involving RBAC policy evaluation.

RoleBinding proliferation can be seen as a "silent scalability killer." It's not an immediate functional bug but rather a creeping performance degradation that becomes critical as systems grow.

## **Introducing a Smarter Solution: Cluster Role Aggregation in Rancher**

To tackle the challenge of RoleBinding proliferation head-on, Rancher developers turned to a powerful, yet underutilized feature within Kubernetes itself: Aggregated ClusterRoles[4].

An Aggregated ClusterRole can be thought of as a dynamic "parent" role that automatically collects permissions from other "child" ClusterRoles based on label selectors. Kubernetes controllers handle the task of keeping the rules within these aggregated roles synchronized.

Instead of creating a multitude of RoleBindings for each inherited permission set, Rancher now intelligently uses these aggregated ClusterRoles. For a given RoleTemplate with inherited roles, Rancher creates a single, consolidated Aggregated ClusterRole that encompasses all those inherited permissions.

Therefore, a user or group usually only needs one RoleBinding for this combined role. This greatly reduces the number of bindings needed, no matter how complex the inheritance chain is.

This new mechanism is applied to how Rancher materializes permissions for both Project Role Template Bindings (PRTBs) and Cluster Role Template Bindings (CRTBs).

## **Under the Hood: Architecting Efficiency with Aggregated Cluster Roles**

### **A Quick Look at Aggregated Cluster Roles**

To understand how Rancher achieves this efficiency, it's helpful to recap how Aggregated ClusterRoles function in Kubernetes. A ClusterRole can have an aggregationRule defined, which specifies clusterRoleSelectors (label selectors). Any other ClusterRole that has matching labels will have its rules automatically included in the "aggregator" ClusterRole. The Kubernetes controller plane watches for these and keeps the rules field of the aggregator role updated. For example, a ClusterRole named monitoring-viewer might have an aggregationRule selecting on the presence of an aggregate-to-monitoring-viewer label. Other ClusterRoles (e.g., one for viewing pod logs, another for viewing metrics) could then be labeled with aggregate-to-monitoring-viewer and their rules would automatically appear in monitoring-viewer. It is important to note that this aggregation mechanism only applies to ClusterRoles; regular, namespaced Roles with matching labels are not aggregated. To apply Aggregated ClusterRoles rules to a subject in a namespaced way, a RoleBinding can be used to bind a user/group to the ACR in a specific namespace.

### **Rancher's New RBAC Blueprint: Before and After**

With the new design, when a RoleTemplate is created or updated, Rancher now creates two key resources:

1. A standard ClusterRole (CR1) containing all the rules *directly* defined in the RoleTemplate.
2. An Aggregated ClusterRole (ACR1) that is configured to aggregate CR1 *and* the Aggregated ClusterRoles of any RoleTemplates it inherits from. Both CR1 and ACR1 will share ACR1's aggregation label, ensuring CR1's rules are included in ACR1.

This has important consequences on how CRTBs and PRTBs are translated to Kubernetes RBAC objects, in particular:

- **Impact on CRTBs (Cluster Role Template Bindings)**:

- **Local (Upstream) Cluster**: Previously, for a CRTB with inherited roles, Rancher would create multiple Roles and RoleBindings *per project*, *per downstream cluster*, in each project's corresponding namespace within the local cluster. Now, with aggregation, only *two* ClusterRoles are created (the direct one and the aggregator) per downstream cluster, *irrespective of the number of projects*. Additionally, only *one* RoleBinding per subject to the main Aggregated ClusterRole for that CRTB is needed per project namespace. This significantly reduces RoleBindings as the number of projects or inherited roles grows.
- **Downstream (Managed) Clusters**: Similarly, in downstream clusters, instead of multiple ClusterRoleBindings to multiple ClusterRoles (one for direct rules, one for each inherited set), a subject is now bound via a *single* ClusterRoleBinding to the main Aggregated ClusterRole. While this might slightly increase the number of ClusterRole objects per RoleTemplate (one direct, one aggregator), the reduction in ClusterRoleBindings per user is a much larger win, especially in systems with many users (not infrequently, for our customers, counting in the hundreds or thousands).

- **Impact on PRTBs (Project Role Template Bindings)**:
- **Local (Upstream) Cluster**: For PRTBs involving management plane rules, the story is similar. The system moves from *multiple* Roles and RoleBindings *per project* to *one pair* of ClusterRoles (direct and aggregator) and *a single* RoleBinding *per project* to the aggregator per project in the local cluster.
- **Downstream (Managed) Clusters**: For PRTBs, instead of creating *multiple* RoleBindings per project for every direct and inherited rule set, Rancher now creates *a single* RoleBinding per project, binding the subject to the Aggregated ClusterRole.

This architectural change embodies a "less is more" principle crucial for Kubernetes efficiency, as it prevents the combinatorial explosion that happened before.

By centralizing permission definitions into fewer, “smarter” Aggregated ClusterRoles and drastically reducing the number of binding objects, Rancher alleviates pressure on the Kubernetes control plane, especially etcd. An additional side effect is an improvement in the performance of its own management layers. Fewer objects mean less data for etcd to store, manage and watch. Therefore, less data for Rancher components to query and reconcile, directly translating to improved performance and scalability.

Furthermore, Rancher is building a more robust abstraction by deeply leveraging an existing Kubernetes primitive (Aggregated ClusterRoles) rather than implementing all the aggregation logic purely within Rancher's controllers. The new design shifts a significant portion of this consolidation logic to Kubernetes itself, reducing the custom logic Rancher needs to maintain for this aspect of RBAC, potentially leading to fewer bugs and better alignment with Kubernetes evolution.

## **The Payoff: Real-World Gains in Performance and Scalability**

### **Slashing Resource Counts: A Numbers Game We Win**

The most direct benefit of this new architecture is a dramatic reduction in the number of RBAC resources, particularly RoleBindings. The following table illustrates the potential savings in a hypothetical scenario.

Consider a setup with 100 users, 10 projects in a downstream cluster and 10 RoleTemplates where each user is given 1 CRTB to one RoleTemplate. Assume also that one RoleTemplate inherits from the other nine.

**Resource Count in the Upstream Cluster** **Old Design (10 Inherited RTs Scenario)** | **New Design (10 Inherited RTs Scenario)** || ClusterRoles | 0 | 20 ClusterRoles (2 per RT) |
| Roles | 1000 Roles (1 per RT, per project) | 0 |
| RoleBindings | 10,000 (1 per RT, per project, per user) | 1,000 (1 per project, per user)   As the table shows, while there's an increase in ClusterRoles that does not depend on project count, it is more than compensated by the decrease in Roles, which did depend on project count.   Moreover, the number of RoleBindings does not depend on RoleTemplates and their inheritance relationships any longer, which can represent a very significant reduction in RoleBindings.**Smoother Sailing: What This Means for End Users**Fewer objects mean a lighter load on etcd, leading to better overall cluster stability and responsiveness. For engineers and administrators, this translates to a snappier Rancher UI, faster reconciliation of permissions, and a more scalable platform as the organization's Kubernetes footprint grows.**Fortifying Security with Simplified RBAC**A significant security advantage of using Aggregated ClusterRoles is improved visibility for escalation prevention. Because the ACR consolidates all rules from the ClusterRoles it aggregates, Rancher's admission webhook—responsible for preventing users from granting permissions they do not themselves possess — can see the complete set of effective permissions when a binding is created or modified. This simplifies the checks needed to ensure that privilege escalation does not occur. This is a notable improvement, as it reduces the “attack surface” that could cause CVEs compared to the previous design.   The design also thoughtfully considers a scenario where a user, able to create ClusterRoles but not bindings, might try to add a label to their ClusterRole to get its rules included in an existing ACR used by others. However, Rancher's existing escalation checks prevent the user from creating a ClusterRole with permissions they don't already have. So, while they could get their (limited) permissions aggregated into a broader set, they could not use this mechanism to escalate privileges for themselves or others beyond what they are already authorized for.   The proactive identification and discussion of such potential security implications within the design process demonstrated that security was an integral consideration, not an afterthought.**The Road Ahead: Phased Rollout and Future Innovations****Enabling the Future: How This Improvement is Being Rolled Out**Changes to core components like RBAC need to be introduced carefully. That's why this Cluster Role Aggregation feature is being rolled out in phases:  - **Rancher v2.11 and 2.12 (Experimental)**: The feature, identified by the feature flag aggregated-roletemplates, is available but off by default. Crucially, for those wishing to test it, it **must be enabled during a fresh Rancher installation**. The feature flag value is locked after the initial setup. - **Rancher v2.13 (Beta Target)**: The plan is to enable users to migrate existing RoleTemplates selectively to the new model. The default behavior of the feature flag may also change in this release, and further feedback will be gathered. - **Future Rancher versions**: The new implementation is expected to become the standard, with the older controllers responsible for RBAC generation being removed.  This multi-stage migration plan, incorporating feature flags and options for gradual adoption, underscores our commitment to stability. It provides users with control during the transition, which is critical for production systems, rather than imposing an immediate, disruptive change. This allows the Rancher team to gather feedback and address any unforeseen issues, while users can plan and adopt the change at a pace suitable for their environments.**Conclusion: SUSE’s Commitment to Scalable Container Management with Rancher**The transition to Cluster Role Aggregation for RoleTemplate inheritance is a prime example of Rancher's ongoing commitment to delivering robust, scalable and performant container management. By intelligently reducing the number of RBAC objects, Rancher is enhancing UI responsiveness, easing the load on etcd and fortifying security through clearer permission visibility.   This is more than just an update — it's an architectural evolution designed to ensure Rancher grows effectively with its users, no matter the scale of their Kubernetes deployments. These improvements reflect a dedication to continuous innovation in the container management space.Resources  1. See the “Tuning and Best Practices for Rancher at Scale” guide in the Rancher documentation for more information and a formula to calculate the binding count: <https://ranchermanager.docs.rancher.com/reference-guides/best-practices/rancher-server/tuning-and-best-practices-for-rancher-at-scale#rolebinding-count-estimation> 2. The sig-scalability Kubernetes group documents the known limits of resource counts per type via standardized benchmarks. Although RoleBindings are not specifically listed at the time of writing, most other studied resources don’t go past the tens of thousands of instances <https://github.com/kubernetes/community/blob/master/sig-scalability/configs-and-limits/thresholds.md> 3. See the Rancher manual for more information about Projects: <https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/projects-and-namespaces> 4. See the Kubernetes manual for more information about Aggregated ClusterRoles: <https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles>  **Try It Out and Share Your Feedback!**The Cluster Role Aggregation feature, identified by the feature flag aggregated-roletemplates, is available experimentally in Rancher v2.11 and later versions.   Rancher is targeting beta availability in v2.13, and General Availability in future versions.   You can read more about how to enable this feature in [Rancher’s documentation](https://ranchermanager.docs.rancher.com/how-to-guides/advanced-user-guides/enable-experimental-features/cluster-role-aggregation).   As with any other open source project, feedback is invaluable as this feature is refined. Experiences, reported issues or suggestions for improvement can be shared by [opening an issue on GitHub](https://github.com/rancher/rancher/issues) and don't hesitate to join the [Rancher users Slack](https://rancher-users.slack.com).   Community input helps make Rancher better!   ---  Special CreditsA very special thank you to our amazing engineers who designed and implemented the feature: ![Alejandro Ruiz](images/aruiz14-150x150.jpg)  Alejandro Ruiz  ![Jonathan Crowther](images/jcrowther-e1750253120284-150x150.jpg)  Jonathan Crowther |
