---
title: "When to Use K3s and RKE2"
date: 2022-12-14T15:01:55
slug: "when-to-use-k3s-and-rke2"
author: "SUSE"
image: "images/download.png"
products: ["K3s"]
tags: ["edge", "installation"]
content_type: "explainer"
draft: false
migration:
  wp_id: 98538
  original_url: "https://www.suse.com/c/rancher_blog/when-to-use-k3s-and-rke2/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "RKE2 v1.25 era"
  redirect_target: ""
---

[K3s](https://k3s.io/) and [Rancher Kubernetes Engine (RKE2)](https://docs.rke2.io/) are two [Kubernetes](https://kubernetes.io/) distributions from the [SUSE Rancher container platform](https://www.rancher.com/). Either project can be used to run a production-ready cluster; however, they target different use cases and consequently possess unique characteristics.

This article will explain the similarities and differences between the projects. You'll learn when it makes sense to use RKE2 instead of K3s and vice versa. Selecting the right choice is important because it affects the security and compliance of the containerized workloads you deploy.

## K3s and RKE2

K3s provides a production-ready Kubernetes cluster from a single binary that weighs in at under 60MB. Because K3s is so lightweight, it's a great option for running Kubernetes at the edge on IoT devices, low-power servers and your developer workstations.

Meanwhile, RKE2 is an alternative project that also runs a production-ready cluster. It offers similar simplicity to K3s while adding additional security and conformance layers, including [Federal Information Processing Standard (FIPS) 140-2 compliance](https://csrc.nist.gov/publications/detail/fips/140/2/final) for use in the U.S. federal government and DISA STIG compliance.

RKE2 has evolved from the original RKE project. It's also known as RKE Government, reflecting its suitability for the most demanding sectors. It's not just government agencies that can benefit, though — the distribution is ideal for all organizations that prioritize security and compliance, so it continues to be primarily marketed as RKE2.

## Similarities between K3s and RKE2

K3s and RKE2 are both lightweight Cloud Native Computing Foundation (CNCF)-certified Kubernetes distributions that Rancher fully supports. Although they diverge in their target use cases, the two platforms have several intentional similarities in how they're launched and operated. Both can be deployed with [Rancher Manager](https://docs.ranchermanager.rancher.io/), and they each run your containers using the industry-standard [containerd runtime](https://containerd.io/).

### Usability

K3s and RKE2 each offer good usability with a quick setup experience.

Starting a K3s cluster on a new host can be achieved with one command and around 30 seconds of waiting:

```
$ curl -sfL https://get.k3s.io | sudo sh -
```

The service is registered and started for you, so you can immediately run kubectl commands to interact with your cluster:

```
$ k3s kubectl get pods
```

RKE2 doesn't fare much worse. A similarly straightforward installation script is available to download its binary:

```
$ curl -sfL https://get.rke2.io | sudo sh -
```

RKE2 doesn't start its service by default. Run the following commands to enable and start RKE2 in server (control plane) mode:

```
$ sudo systemctl enable rke2-server.service
$ sudo systemctl start rke2-server.service
```

You can find the bundled kubectl binary at `/var/lib/rancher/rke2/bin`. It's not added to your `PATH` by default; a kubeconfig file is deposited to `/etc/rancher/rke2/rke2.yaml`:

```
$ export KUBECONFIG=/etc/rancher/rke2/rke2.yaml
$ /var/lib/rancher/rke2/bin/kubectl get pods
```

### Ease of operation

In addition to their usability, K3s and RKE2 are simple to operate. You can upgrade clusters created with either project by repeating the installation script on each node:

```
# K3s
$ curl -sfL https://get.k3s.io | sh -

# RKE2
$ curl -sfL https://get.rke2.io | sh -
```

You should repeat any flags you supplied to the original installation command.

Automated upgrades [are supported](https://docs.k3s.io/upgrades/automated) using Rancher's [system-upgrade-controller](https://github.com/rancher/system-upgrade-controller). After installing the controller, you can declaratively [create Plan objects](/blog/upgrade-a-k3s-kubernetes-cluster-with-system-upgrade-controller/) that describe how to migrate the cluster to a new version. Plan is a [custom resource definition (CRD)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources) provided by the controller.

Backing up and restoring data is another common Kubernetes challenge. K3s and RKE2 also mirror each other in this field. Snapshots are automatically written and retained for a configurable period. You can easily restore a cluster from a snapshot by running the following command:

```
# K3s
$ k3s server \
    --cluster-reset \
    --cluster-reset-restore-path=/var/lib/rancher/k3s/server/db/etcd-old-<BACKUP_DATE>

# RKE2
$ rke2 server \
    --cluster-reset \
    --cluster-reset-restore-path=/var/lib/rancher/rke2/server/db/etcd-old-<BACKUP_DATE>
```

### Deployment model

K3s and RKE2 share their single-binary deployment model. They bundle all their dependencies into one download, allowing you to deploy a functioning cluster with minimal Kubernetes experience.

The projects also support [air-gapped environments](https://docs.rke2.io/install/airgap) to accommodate critical machines that are physically separated from your network. Air-gapped images are provided in the release artifacts. Once you've transferred the images to your machine, running the regular installation script will bootstrap your cluster.

### High availability and multiple nodes

K3s and RKE2 are designed to run in production. K3s is often used in the development, too, having gained a reputation as an ideal single-node cluster. It has robust [multi-node management](https://docs.k3s.io/installation/requirements) and is capable of supporting fleets of IoT devices.

Both projects can run the control plane with [high availability](https://docs.k3s.io/installation/ha), too. You can distribute replicas of control plane components over several server nodes and use external data stores instead of the embedded ones.

## Differences between K3s and RKE2

K3s and RKE2 both offer single-binary Kubernetes, high availability and easy backups, with many commands interchangeable between the two. However, some key differences affect where and when they should be used. It's these characteristics that justify the distributions existing as two independent projects.

### RKE2 is closer to upstream Kubernetes

K3s is CNCF-certified, but it deviates from upstream Kubernetes in a few ways. It uses [SQLite](https://www.sqlite.org/index.html) instead of [etcd](https://etcd.io/) as its default data store, although an embedded etcd instance [is available as an option](https://docs.k3s.io/installation/datastore) in modern releases. K3s also bundles additional utilities, [such as the Traefik Ingress controller](https://docs.k3s.io/networking#traefik-ingress-controller).

RKE2 sticks closer to standard Kubernetes, [promoting conformance](https://docs.rke2.io/) as one of its main features. This gives you confidence that workloads developed for other distributions will run reliably in RKE2. It reduces the risk of inconvenient gotchas that can occur when K3s steps out of alignment with upstream Kubernetes. RKE2 automatically uses etcd for data storage and omits nonstandard components included in K3s.

### RKE2 uses embedded etcd

The standard SQLite database in K3s is beneficial for compactness and can optimize performance in small clusters. In contrast, RKE2's default use of etcd creates a more conformant experience, allowing you to integrate directly with other Kubernetes tools that expect an etcd data store.

While K3s can be configured with etcd, it's an option you need to turn on. RKE2 is designed around it, which reduces the risk of misconfiguration and subpar performance.

K3s also supports MySQL and PostgreSQL as alternative storage solutions. These let you manage your Kubernetes data using your existing tooling for relational databases, such as backups and maintenance operations. RKE2 only works with etcd, offering no support for SQL-based storage.

### RKE2 is more security-minded

RKE2 has a much stronger focus on security. Whereas edge operation is K3s's specialism, RKE2 prioritizes security as its greatest strength.

#### Hardened against the CIS benchmark

The distribution [comes configured](https://docs.rke2.io/security/hardening_guide) for compatibility with the CIS Kubernetes Hardening Benchmark v1.23 (v1.6 in RKE2 v1.25 and earlier). The defaults that RKE2 applies allow your clusters to reach the standard with minimal manual work.

You're still responsible for tightening the OS-level controls on your nodes. This includes applying appropriate [kernel parameters](https://docs.rke2.io/security/hardening_guide/#setting-up-hosts) and ensuring the [etcd data directory](https://docs.rke2.io/security/hardening_guide/#ensure-etcd-is-configured-properly) is correctly protected.

You can enforce that a safe configuration is required by starting RKE2 with the `profile` flag set to `cis-1.23`. RKE2 will then exit with a fatal error if the operating system hasn't been suitably hardened.

Beyond configuring the OS, you must also set up suitable network policies](<https://kubernetes.io/docs/concepts/services-networking/network-policies>) and [Pod security admission rules] to secure your cluster’s workloads. The security admission controller can be configured to use [profiles which meet the CIS benchmark](https://docs.rke2.io/security/hardening_guide). This will prevent non-compliant Pods from being deployed to your cluster.

#### Regularly scanned for threats

The safety of the RKE2 distribution is maintained within its build pipeline. Components [are regularly scanned](https://docs.rke2.io/) for new common vulnerabilities and exposures (CVEs) using the [Trivy](https://github.com/aquasecurity/trivy) container vulnerability tool. This provides confidence that RKE2 itself isn't harboring threats that could let attackers into your environment.

#### FIPS 140-2 compliant

K3s lacks any formal security accreditations. RKE2 [meets the FIPS 140-2 standard](https://docs.rke2.io/security/fips_support/) that the U.S. government uses to approve cryptographic modules.

The project's [Go code is compiled](https://docs.rke2.io/security/fips_support) using FIPS-validated crypto modules instead of the versions in the Go standard library. Each of the distribution's components, from the Kubernetes API server through to kubelet and the bundled kubectl binary, are compiled with the FIPS-compatible compiler.

The FIPS mandate means RKE2 can be deployed in government environments and other contexts that mandate verifiable cryptographic performance. The entire RKE2 stack is compliant when you use the built-in components, such as the containerd runtime and etcd data store.

## When to use K3s

K3s should be your preferred solution when you're seeking a performant Kubernetes distribution to run on the edge. It's also a good choice for single-node development clusters as well as ephemeral environments used in your CI pipelines and other build tools.

This distribution makes the most sense in situations where your primary objective is deploying Kubernetes with all dependencies from a single binary. It's lightweight, quick to start and easy to manage, so you can focus on writing and testing your application.

## When to use RKE2

You should use RKE2 whenever security is critical, such as in government services and other highly regulated industries, including finance and healthcare. As previously stated, the complete RKE2 distribution is FIPS 140-2 compliant and comes hardened with the CIS Kubernetes Benchmark. It’s also [the only DISA STIG-certified](https://public.cyber.mil/announcement/disa-releases-the-rancher-government-solutions-rke2-security-technical-implementation-guide) Kubernetes distribution, meaning it’s approved for use in the most stringent U.S. government environments, including the Department of Defense.

RKE2 is fully certified and tightly aligned with upstream Kubernetes. It omits the K3s components that aren't standard Kubernetes or that are unstable alpha features. This increases the probability that your deployments will be interoperable across different environments. It also reduces the risk of nonconformance that can occur through oversight when you're manually hardening Kubernetes clusters.

Near edge computing is another primary use case for RKE2 over K3s. RKE2 ships with support for [multiple CNI networking plugins](https://rancher.com/docs/rancher/v2.6/en/cluster-admin/editing-clusters/rke2-config-reference), including Cilium, Calico, and Multus. [Multus](https://github.com/k8snetworkplumbingwg/multus-cni) allows pods to have multiple network interfaces attached, making it ideal for use cases such as [telco](https://www.telco.com/) distribution centers and factories with several different production facilities. In these situations, it's critical to have robust networking support with different network adapters. K3s bundles Flannel as its built-in CNI plugin; you can [install a different provider](https://docs.k3s.io/installation/network-options#custom-cni), but all configuration has to be performed manually. RKE2's default distribution provides integrated options for common networking solutions.

## Conclusion

K3s and RKE2 are two popular Kubernetes distributions that overlap each other in several ways. They both offer a simple deployment experience, frictionless long-term maintenance, and high performance and compatibility.

While designed for [tiny](https://www.suse.com/c/preparing-for-the-new-needs-of-edge-computing) and far-edge use cases, K3s are not limited to these scenarios. It's also widely used for development, in labs, or in resource-constrained environments. However, K3s is not focused on security, so you'll need to secure and enforce your clusters.

RKE2 takes the usability ethos from K3s and applies it to a fully conformant distribution. It's tailored for security, close alignment with upstream Kubernetes, and compliance in regulated environments such as government agencies. RKE2 is suitable for both data centers and near-edge situations as it offers built-in support for advanced networking plugins, including [Multus](https://github.com/k8snetworkplumbingwg/multus-cni).

Which you should choose depends on where your cluster will run and the workloads you'll deploy. You should use RKE2 if you want a hardened distribution for security-critical workloads or if you need FIPS 140-2 compliance. It will help you establish and maintain a healthy security baseline. K3s remain an actively supported alternative for less sensitive situations and edge workloads. It's a batteries-included project for when you want to focus on your apps instead of the environment that runs them.

Both distributions can be managed by [Rancher](https://www.rancher.com/) and integrated with your DevOps toolbox. You can use solutions [like Fleet](/blog/fleet-management-for-kubernetes-is-here/) to deploy applications at scale with GitOps strategies, then head to the [Rancher dashboard](/blog/rancher-desktop-now-includes-the-rancher-dashboard/) to monitor your workloads.
