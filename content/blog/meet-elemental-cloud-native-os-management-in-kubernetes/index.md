---
title: "Meet Elemental: Cloud Native OS Management in Kubernetes"
date: 2023-07-03T18:10:56
slug: "meet-elemental-cloud-native-os-management-in-kubernetes"
authors: ["Francesco Giudici"]
image: "images/logo.svg"
products: ["Elemental"]
tags: ["edge", "installation"]
content_type: "explainer"
draft: false
migration:
  wp_id: 109568
  original_url: "https://www.suse.com/c/rancher_blog/meet-elemental-cloud-native-os-management-in-kubernetes/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Wouldn’t it be great if Rancher could provision and manage not only Kubernetes clusters but also the OS running on the cluster nodes? This is the goal we had in mind when we started working on Elemental. 

Elemental adds to Rancher the ability to install and manage a minimal OS based on SUSE Linux Enterprise technology, delivered and managed in a fully cloud native way.  This simplifies the infrastructure (you only need a container registry) and day 2 operations. Kubernetes handle operating system installations and updates. To give you a high-level picture of how this is possible and what it exactly means, we have to dig a bit more into what Elemental is and how it works. 

## **What is Elemental?**

Elemental is a software stack made up of three main components: the Elemental Toolkit, the Elemental Operator and the Elemental UI. 

- **The Elemental Toolkit** is a set of tools allowing delivery of a minimal SUSE Linux Enterprise OS as an OCI container image, immutable at its core but still flexible through the support of overlay filesystems and cloud-init configuration.
- **The Elemental Operator** is released as a Helm chart and allows Rancher to harness the functionality of the Elemental Toolkit by enabling Kubernetes native OS and machine management.
- **The Elemental UI** is a Rancher UI extension and sits on top of the Elemental Operator: OS updates and ISO creation are just a few clicks away once installed.

## **How does it work?**

It all starts by defining the desired OS installation configuration: things like the storage device on which the OS should be installed and cloud-init configuration are defined in a MachineRegistration resource. Something like this:

```
apiVersion: elemental.cattle.io/v1beta1 

kind: MachineRegistration 

metadata: 

  name: fire-nodes 

  namespace: fleet-default 

spec: 

  config: 

    cloud-config: 

      users: 

        - name: root 

          passwd: root 

    elemental: 

      install: 

        reboot: true 

        device: /dev/sda 

        debug: true 
```

 

Coupling a MachineRegistration with an Elemental Toolkit OS image allows the creation of a bootable ISO that could be used to provision any number of bare metal and virtual machines. ISO creation is one click away in the Elemental UI, which under the hood, creates a SeedImage resource for you. The build process is carried over in the Rancher cluster. Once finished, the ISO is available for download from an HTTP URL. 

When a machine is booted with the built ISO, it performs an unattended deployment of the Elemental Toolkit OS on its permanent storage. It also registers itself back to the Elemental Operator on the Rancher cluster, triggering the creation of a tracking MachineInventory resource. 

When creating an Elemental cluster, the machines to be provisioned as cluster nodes are identified among the available MachineInventory resources: at that point, Rancher provisioning kicks in, and the Kubernetes stack (k3s or RKE2) is delivered on top of the Elemental Toolkit OS. 

### **Wait… what about OS upgrades?**

As the Elemental OS is immutable at its root, updates are delivered via new OS images published as a container and fully substituted old ones in the machine's storage. Updates can be easily triggered by selecting a target Elemental cluster and a desired OS version in the Elemental UI: the OS upgrade is started automatically, orchestrated by Kubernetes, and performed on each node belonging to the cluster. 

### What's next?

Want to give Elemental a try? Follow our [QuickStart guide](https://elemental.docs.rancher.com/quickstart-ui) or reach out via the #elemental channel on rancher-users.slack.com !
