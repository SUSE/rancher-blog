---
title: "Disaster Recovery Preparedness for Your Kubernetes Clusters"
date: 2020-08-26T18:58:34
slug: "disaster-recovery-preparedness-for-your-kubernetes-clusters"
author: "Cris Rusu"
image: "images/rancher_blog_disaster-recovery-preparedness-featured.png"
products: ["Rancher Manager"]
tags: ["backup", "multi-cluster"]
content_type: "explainer"
draft: false
migration:
  wp_id: 91977
  original_url: "https://www.suse.com/c/rancher_blog/disaster-recovery-preparedness-for-your-kubernetes-clusters/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "RKE1 etcd snapshot steps"
  redirect_target: ""
---

## **Introduction**

In the pre-Kubernetes, pre-container world, backup and recovery solutions were generally implemented at the virtual machine (VM) level. That works for traditional applications when an application runs on a single VM. But when applications are containerized and managed with an orchestrator like Kubernetes, this system falls apart. That means effective disaster recovery (DR) plans for Kubernetes must be designed for containerized architectures and natively understand the way Kubernetes functions.

Rancher provides a mechanism to automatically configure recurring backups of the etcd database, for both the Rancher management cluster (RMC) and the downstream Kubernetes clusters. In case of disaster, you can use these backups (also called snapshots) to recover the Kubernetes configuration and the Rancher database and state. This way, Rancher helps ensure that your clusters are protected, and recovery is possible in a disaster situation.

As you can imagine, there are many other steps required to fully recover user workloads in a DR scenario. In this blog post, we’ll point out the major components of a DR scenario and how to implement them safely in a Kubernetes environment.

There are different levels of DR preparedness, depending on a multitude of factors. These include the level of automation for providing infrastructure, app structure and deployment procedures, storage, networking, expertise in cloud-native apps and microservices, and Kubernetes management experience. However, the most critical component of a successful DR strategy, a Level 0 of sorts, is [testing and documenting your procedures](https://rancher.com/blog/2020/number-one-rule-disaster-recovery) as often as possible. Just like backups are useless without testing recovery procedures, so is a DR plan without solid documentation and repeated validation.

## Components of a Successful Disaster Recovery Scenario

The following is a list of components to think about in a DR scenario. How you handle these components in a DR situation determines the level of enterprise preparedness for fast crisis recovery. The goal is to have automated procedures whenever possible for as many of the components.

1. Backups

- etcd (cluster database)
- statefile (cluster configuration)
- cluster configuration file (cluster configuration)
- certificates (cluster configuration)
- persistent storage (stateful apps)
- containers (images used by apps)

2. Infrastructure

- cluster nodes
- load balancers
- backups

  ```
    *         etcd 
    *         statefile 
    *         cluster config
  ```

3. Apps

- container images (repositories)
- manifests (Helm or Kubernetes)

4. DNS

- control of your domain is required

This is not a comprehensive list. You may have more (or fewer) items to consider for your specific environment. Enterprise IT teams already manage some of these components, which furthers the idea of a collaborative work environment promoted by DevOps concepts and methods.

## Levels of Disaster Recovery Preparedness

Many companies are in a digital transformation period, and Kubernetes is an integral part of that journey. Every organization has a unique environment with specific capabilities and expertise, which means they have different levels of DR preparedness. These skills and capabilities range from the state of infrastructure automation to CI/CD processes, source control management to backup strategy, etc. The good news is that the more your organization develops these capabilities, the higher your level of preparedness. This way, DR becomes an almost banal event that your organization can handle quickly and with minimal human intervention.

### Level 1: Manual Redeployment

- Backups: Automatic recurring.
- Procedures: Tested and documented procedures.
- Infrastructure: Standby infrastructure.
- DNS: Manual failover changes.
- Apps: Manual Restoration of apps.

This is one of the most common scenarios. The automatically recurring backups are used to restore the cluster(s) state to the standby infrastructure at the DR site. The procedures are well documented and tested regularly. A good test for recovery is to have your team's newest member follow the documentation to implement a fully functional DR environment.

The infrastructure is on standby at the DR site, making the environment a hot-warm system. The DNS changes required for failover are going to be done manually on the spot (based on documentation). The running apps are going to be restored manually to ensure full functionality.

This level of DR preparedness is sufficient for most enterprises because it creates a repeatable, well-documented process. It may be perceived as slower than other processes since most of the activities are manual and have to follow a very rigid timeline. You also need to consider the human element at this level. As we all know, humans introduce an element of risk in some processes due to unpredictable implementation mistakes. That’s why there is room for improvement through the use of scripting and automation.

### Level 2: Scripted Redeployment

- Backups: Automatic recurring.
- Procedures: Tested and documented procedures.
- Infrastructure: Scripted deployment.
- DNS: Scripted failover changes.
- Apps: Scripted restoration of apps.

This is a more advanced scenario where the restore of your clusters is done on infrastructure deployed on demand. Backups are still required to provide the restore source. The procedures are well documented and tested regularly.  The infrastructure at the DR site is deployed using scripted methods, providing an identical environment every time the DR plan is tested or executed. The scripted method can also be applied to the implementation of DNS changes and apps deployment.

This level of DR preparedness is extremely effective because it eliminates randomness in the DR process outcome. While it requires more work to configure and internal expertise to maintain, the result is better protection for your enterprises against any disaster situation. Also, this scenario dramatically reduces recovery time, which can be a great advantage for enterprises where regulatory requirements mandate that.

### Level 3: Fully Automated Redeployment

- Backups: Automatic recurring. Persistent data is enterprise-managed and replicated to the DR site automatically.
- Procedures: Automated regular testing of DR procedures.
- Infrastructure: Fully automated redeployment of infrastructure.
- Apps: Fully automated redeployment of apps.
- DNS: Automated failover changes.

This is the most advanced level where everything is automated and can be redeployed "at the touch of a button." In this scenario, there is NO restore performed.

You'll use the recurring backups in the case of the same site recovery of a particular cluster. The infrastructure, Rancher management cluster and downstream clusters are all deployed on demand. DNS changes are also automated for failover using a Global Traffic Management (GTM) tool. Apps deployment is fully automated.

If this level sounds a bit like a unicorn project, that’s because it is difficult to achieve. It requires in-depth expertise around all the components involved in executing the DR plan. Of course, it also takes a lot longer to configure, but the results are worth it. In some respect, this is the ultimate goal for a microservices architecture: to be able to redeploy the entire environment, from infrastructure to apps, in a matter of minutes without any manual intervention.

### Automated Rancher Management Cluster Disaster Recovery

- Backups: Automatic recurring.
- Procedures: Regular testing of DR procedures.
- Infrastructure: Standby Rancher management cluster.
- DNS: Manual/scripted failover changes.

This scenario applies to the Rancher management cluster only, and you'll find it in enterprises where there is a requirement for a DR plan to cover each application. The infrastructure at the DR site is already built as a standby target for the recovery operation. The main site (Rancher) is monitored and if DR conditions are met, failover is declared and the Rancher management cluster is restored to the standby cluster using a scripted approach. DNS is redirected either manually or through an enterprise solution like BIG-IP's Global Traffic Management (GTM). As soon as the Rancher cluster comes back up, the downstream Kubernetes clusters automatically reconnect to the new Rancher server within minutes. This scenario assumes that downstream clusters are not affected by the disaster (i.e., running in the cloud).

## Conclusion

We can't understate the importance of a disaster recovery plan. Only through robust planning, testing and documentation can enterprises ensure that recovery is fast and without significant data loss. You should test your DR plan and procedures regularly (i.e., once a quarter).

Rancher manages Kubernetes clusters, which are highly available distributed systems to begin with. These systems are extremely important to the enterprises due to their very nature of expected high availability and zero downtime. In a Kubernetes world, it is important to reduce the recovery time to a minimum and restore apps functionality within minutes. You can accomplish this with automation, scripting and regularly testing your DR plan and procedures.

If you are looking for a place to start, check out our master class on [Disaster Recovery Strategies for Kubernetes](https://www.youtube.com/watch?v=qD2kFA8THrY).
