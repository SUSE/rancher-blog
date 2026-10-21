---
title: "A Guide to Using Rancher for Multicloud Deployments"
date: 2023-03-08T19:53:46
slug: "a-guide-to-using-rancher-for-multicloud-deployments"
author: "SUSE"
image: "images/rancher-logo-stacked-color.svg"
products: ["Rancher Manager"]
tags: ["multi-cluster", "cloud"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 102638
  original_url: "https://www.suse.com/c/rancher_blog/a-guide-to-using-rancher-for-multicloud-deployments/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Rancher 2.7 era UI"
  redirect_target: ""
---

[Rancher](https://www.rancher.com/) is a [Kubernetes](https://kubernetes.io/) management platform that creates a consistent environment for multicloud container operation. It solves several of the challenges around multicloud Kubernetes deployments, such as poor visibility into where workloads are running and the lack of centralized authentication and access control.

Multicloud improves resiliency by letting you distribute applications across providers. It can also be a competitive advantage since you're able to utilize the benefits of every provider. Moreover, multicloud reduces vendor lock-in because you're less dependent on any one platform.

However, these advantages are often negated by the difficulty in managing multi-cloud Kubernetes. Deploying multiple clusters, using them as one unit and monitoring the entire fleet are daunting tasks for team leaders. You need a way to consistently implement authorization, observability and security best practices.

In this article, you'll learn how Rancher resolves these problems so you can confidently use Kubernetes in multi-cloud scenarios.

## Rancher and multicloud

One of the benefits of Rancher is that it provides a consistent experience when you're using several environments. You can manage the full lifecycle of all your clusters, whether they're in the cloud or on-premises. It also abstracts away the differences between Kubernetes implementations, creating a single surface for monitoring your deployments.

![Diagram showing how Rancher works with all Kubernetes distributions and cloud platforms courtesy of James Walker](images/8c5078-TrUHoHh.png)

Rancher is flexible enough to work with both new and existing clusters, and there are three possible ways to connect your clusters:

1. **Provision a new cluster using a managed cloud Kubernetes service:**Rancher can create new Amazon Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS) and Google Kubernetes Engine (GKE) clusters for you. The process is fully automated within the Rancher UI. You can also import existing clusters.
2. **Provision a new cluster on standalone cloud infrastructure:** Rancher can [deploy an RKE, RKE2, or K3s](https://rancher.com/docs/rke/latest/en/installation) cluster by provisioning new compute nodes from your cloud provider. This option supports Amazon Elastic Compute Cloud (EC2), Microsoft Azure, [DigitalOcean](https://www.digitalocean.com/), [Harvester](https://www.suse.com/products/harvester), [Linode](https://www.linode.com/) and [VMware vSphere](https://www.vmware.com/products/vsphere.html).
3. **Bring your own cluster:** You can manually connect Kubernetes clusters running locally or in other cloud environments. This gives you the versatility to combine on-premises and public cloud infrastructure in hybrid deployment situations.

![Screenshot of adding a cluster in Rancher](images/93c3cd-dtYcUee.png)

Once you've added your multicloud clusters, your single Rancher installation lets you seamlessly manage them all.

### A unified dashboard

One of the biggest multicloud headaches is tracking what's deployed, where it's located and whether it's running correctly. With Rancher, you get a unified dashboard that shows every cluster, including the cloud environment it's hosted in and its resource utilization:

![Screenshot of the Rancher dashboard showing multiple clusters](images/daf72c-QUmIMcm.png)

![Clusters screenshot](images/2f0f93-4vbOmUd.png)

The Rancher home screen provides a centralized view of the clusters you've registered, covering both your cloud and on-premises deployments. Similarly, the sidebar integrates a shortcut list of clusters that helps you quickly move between environments.

After you've navigated to a specific cluster, the **Cluster Dashboard** page offers an at-a-glance view of capacity, utilization, events and deployments:

![Screenshot of Rancher's **Cluster Dashboard**](images/52bd9b-rikVq5m.png)

Scrolling further down, you can view precise cluster metrics that help you analyze performance:

![Screenshot of viewing cluster metrics in Rancher](images/d8a4a6-VH4jJww.png)

Rancher lets you access vital monitoring data for all your Kubernetes environments within one tool, eliminating the need to log into individual cloud provider control panels.

### Centralized authorization and access control

Kubernetes has built-in support for [role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac) to limit the actions that individual user accounts can take. However, this is insufficient for multicloud deployments because you have to manage and maintain your policies individually in each of your clusters.

Rancher improves multicloud Kubernetes usability by adding a centralized user authentication system. You can set up user accounts within Rancher or connect an external service [using protocols such as](https://ranchermanager.docs.rancher.com/pages-for-subheaders/authentication-config) LDAP, SAML and OAuth.

Once you've created your users, you can assign them specific access control rules to limit their rights within Rancher and your clusters. [Global permissions](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/authentication-permissions-and-global-configuration/manage-role-based-access-control-rbac/global-permissions)define how users can manage your Rancher installation. For instance, you can create and modify cluster connections while [cluster- and project-level roles](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/authentication-permissions-and-global-configuration/manage-role-based-access-control-rbac/cluster-and-project-roles)configure the available actions after selecting a cluster.

To create a new user, click the menu icon in the top-left to expand the sidebar, then select the **Users & Authentication** link. Press the **Create** button on the next screen, where your existing users are displayed:

![Screenshot of the Rancher UI](images/e86a2b-AdUvtC6.png)

Fill out your new user's credentials on the following screen:

![Screenshot of creating a new user in Rancher](images/695020-1SakdSI.png)

Then scroll down the page to begin assigning permissions to the new user.

Set the user's global permissions, which control their overall level of access within Rancher. Then you can add more fine-grained policies for specific actions from the roles at the bottom. Once you've finished, click the **Create** button on the bottom-right to add the account. The user can now log into Rancher:

![Screenshot of assigning a user's global roles in Rancher](images/7bf1b9-HlK6J0C.png)

Next, navigate to one of your clusters and head to **Cluster > Cluster Members**in the sidebar. Click the **Add** button in the top-right to grant a user access to the cluster:

![Screenshot of adding a cluster member in Rancher](images/470a3a-WMtPJoJ.png)

Use the next screen to search for the user account, then set their role in the cluster. Once you press **Create** in the bottom-right, the user will be able to perform the cluster interactions you've assigned:

![Screenshot of setting a cluster member's permissions in Rancher](images/03a173-496qhLo.png)

#### Adding a cluster role

For more precise access control, you can set up your own roles that build upon Kubernetes RBAC. These can apply at the global (Rancher) level or within a specific cluster or project/namespace. All three are created in a similar way.

To create a cluster role, expand the Rancher sidebar again and return to the **Users & Authentication** page. Select the **Roles** link from the menu on the left and then select **Cluster** from the tab strip. Press the **Create Cluster Role**button in the top-right:

![Screenshot of Rancher's Cluster Roles interface](images/932889-raxnCID.png)

Give your role a name and enter an optional description. Next, use the **Grant Resources** interface to define the Kubernetes permissions the role includes. This example permits users to create and list pods in the cluster. Press the **Create** button to add your role:

![Screenshot of defining a cluster role's permissions in Rancher](images/2ada70-E2SQ20h.png)

The role will now show up when you're adding new members to your clusters:

![Screenshot of selecting a custom cluster role for a cluster member in Rancher](images/a7ce27-OYPVb07.png)

### Rancher and multicloud security

Rancher enhances multicloud security by providing active mechanisms for tightening your environments. Besides the security benefits of centralized authentication and RBAC, Rancher also integrates [additional security measures](https://ranchermanager.docs.rancher.com/pages-for-subheaders/rancher-security)that protect your clusters and cloud environments.

Rancher maintains a [comprehensive hardening guide](https://ranchermanager.docs.rancher.com/pages-for-subheaders/rancher-v2.7-hardening-guides) based on the [Center for Internet Security (CIS) Benchmarks](https://www.cisecurity.org/benchmark/kubernetes) that help you implement best practices and identify vulnerabilities. You can scan a cluster against the benchmark from within the Rancher application.

To do so, navigate to your cluster, then expand **Apps > Charts** in the left sidebar. Select the CIS Benchmark chart from the list:

![Screenshot of the CIS Benchmark app in Rancher's app list](images/dbe990-GBimemG.png)

Click the **Install** button on the next screen:

![Screenshot of the CIS Benchmark app's details page in Rancher](images/011e15-KW7mfzf.png)

Follow the steps to complete the installation in your cluster:

![Screenshot of the CIS Benchmark app's installation screen in Rancher](images/45cf25-Opwmhhv.png)

It could take several minutes for the process to finish — you'll see a "SUCCESS" message in the logs pane when it's done:

![Screenshot of the CIS Benchmark app's installation logs in Rancher](images/0685c1-Wpj4tc5.png)

Now, navigate back to your cluster. You'll find a new CIS Benchmark item in Rancher's sidebar. Expand this menu and click the **Scan** link; then press the **Create** button on the page that appears:

![Screenshot of the CIS Benchmark interface in Rancher](images/9a05bd-vyYbvx8.png)

On the next screen, you'll be prompted to select a scan profile. This defines the hardening checks that will be performed. You can change the default to choose a different benchmark or Kubernetes version. Press the **Create** button to start the scan:

![Screenshot of creating a CIS Benchmark scan in Rancher](images/bf89e8-Lt078pA.png)

The scan run will then show in the **Scans** table back on the **CIS Benchmark > Scan** screen:

![Screenshot of the CIS Benchmark **Scans** interface in Rancher, with a running scan displayed](images/3f4e51-6tpep9o.png)

Once it is finished, you can view the results in your browser by selecting the scan from the table:

![Screenshot of viewing CIS Benchmark scan results in the Rancher UI](images/c5b778-LWXfpJr.png)

## Rancher helps DevOps teams to scale multicloud environments

Multicloud is hard — more resources normally means higher overheads, a bigger attack surface and a rapidly swelling toolchain. These issues can impede you as you try to scale.

Rancher incorporates unique capabilities that help operators work effectively with different deployments, even when they're distributed across several environments.

### Automatic cluster backups provide safety

Rancher includes a [backup system](https://ranchermanager.docs.rancher.com/pages-for-subheaders/backup-restore-and-disaster-recovery) that you can install as an operator in your clusters. This operator backs up your Kubernetes API resources so you can recover from disasters.

You can add the operator by navigating to a cluster and choosing **Apps > Charts** from the side menu. Then find the Rancher Backups app and follow the prompts to install it:

![Screenshot of the Rancher Backups app description in the Rancher interface](images/335003-nKs18kN.png)

You'll find the **Rancher Backups** item appear in the navigation menu. Click the **Create** button to define a new one-time or recurring backup schedule:

![Screenshot of the **Backups** interface in Rancher](images/645b15-tpnuPqy.png)

Fill out the details to configure your backup routine:

![Screenshot of configuring a backup in Rancher](images/b4a384-lnws70F.png)

Once you've created a backup, you can [restore it in the future](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/backup-restore-and-disaster-recovery/restore-rancher) if data gets accidentally deleted or a disaster occurs. With Rancher, you can create backups for all your clusters with a single consistent procedure, which produces more resilient environments.

### Rancher integrates with multi-cloud solutions

One of the benefits of Rancher is that it's built as a single platform for managing Kubernetes in any cluster. But it gets even better when combined with other ecosystem tools. Rancher has integrations with adjacent components that provide more focused support for specific use cases, including the following:

- **[Longhorn](https://www.suse.com/products/longhorn)** is distributed Cloud native block storage that runs anywhere and supports automated provisioning, security and backups. You can deploy Longhorn to your clusters from within the Rancher UI, enabling more reliable storage for your workloads.
- **[Harvester](https://www.rancher.com/products/harvester)** is a solution for hyperconverged infrastructure on bare-metal servers. It provides a virtual machine (VM) management system that complements Rancher's capabilities for Kubernetes clusters. By combining Harvester and Rancher, you can effectively manage your on-premises clusters and the infrastructure that hosts them.
- **[Helm](https://helm.sh/)** is the standard package manager for Kubernetes applications. It packages an application's Kubernetes manifests into a collection called a chart, ready to deploy with a single command. Rancher natively supports Helm charts and provides a convenient interface for deploying them into your cluster via its apps system.

By utilizing Rancher alongside other common tools, you can make multicloud Kubernetes even more powerful. Automated storage, local infrastructure management and packaged applications allow you to scale up freely without the hassle of manually provisioning environments and creating your app's resources.

### Deploy to large-scale environments with Rancher Fleet

Rancher also helps you deploy applications using automated GitOps methodologies. [Rancher Fleet](https://fleet.rancher.io/) is a dedicated GitOps solution for containerized workloads that offers transparent visibility, flexible control and support for large-scale deployments to multiple environments.

Rancher Fleet manages your Kubernetes manifests, Helm charts and [Kustomize](https://kustomize.io/) templates for you, converting them into Helm charts that can automatically deploy in your clusters. You can set up Fleet in your Rancher installation by clicking the menu icon in the top-left and then choosing **Continuous Delivery** from the slide-out main menu:

![Screenshot of the **Rancher Fleet** landing screen](images/17c89f-QpHQAPd.png)

Click **Get started** to connect your first Git repository and deploy it to your clusters. Once again, Rancher permits you to use standardized delivery workflows in all your environments. You're no longer restricted to a single cloud vendor, delivery channel or platform as a service (PaaS):

![Screenshot of creating a new Rancher Fleet Git repository connection](images/e50090-ywtih5n.png)

## Conclusion

Multicloud presents new opportunities for more flexible and efficient deployments. Mixing solutions from several different cloud providers lets you select the best option for each of your components while avoiding the risk of vendor lock-in.

Nonetheless, organizations that use multicloud with containers and Kubernetes often experience operational challenges. It's difficult to manage clusters that exist in several different environments, such as public clouds and on-premises servers. Moreover, implementing centralized monitoring, access control and security policies yourself is highly taxing.

[Rancher](https://rancher.com/) solves these challenges by providing a single tool for provisioning infrastructure, installing Kubernetes and managing your deployments. It [works with](https://www.suse.com/suse-rancher/support-matrix/all-supported-versions/rancher-v2-7-0/) Google GKE, Amazon EKS, Azure AKS and your own clusters, making it the ultimate solution for achieving multicloud Kubernetes interoperability. [Try Rancher](https://ranchermanager.docs.rancher.com/getting-started/overview) today to provision and scale multicloud Kubernetes.
