---
title: "Up and Running: Windows Containers With Rancher 2.3 and Terraform"
date: 2019-10-17T09:04:00
slug: "up-and-running-windows-containers-with-rancher-2-3-and-terraform"
author: "Rancher Admin"
products: ["Rancher Manager"]
tags: ["windows", "azure"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 85845
  original_url: "https://www.suse.com/c/rancher_blog/up-and-running-windows-containers-with-rancher-2-3-and-terraform/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 2.3, Terraform 0.12, K8s 1.16"
  redirect_target: "docs.rancher.com"
---

## Introduction

Windows Support went GA for Kubernetes in version 1.14 and represented years of work. This has been the effort of excellent engineers from companies including Microsoft, Pivotal, VMWare, RedHat, and the now-defunct Apprenda, among others. I’ve been a lurker and occasional contributor to the sig-windows community going back to my days with Apprenda, and I’ve continued to follow it in my current role with Rancher Labs. So, when the company decided to tackle Windows support in Rancher, I was immediately excited.

Today we’re going to provision a Rancher cluster on top of an Kubernetes cluster running RKE. We’re also going to provision a Kubernetes cluster that supports both Linux and Windows containers. Once that’s done, we’ll talk about OS targeting as the Kubernetes scheduler will need to know where to deploy the various Linux and Windows containers as they’re launched.

The goal is to do this in a completely automated fashion. This won’t be quite production grade, but it will be a good start for your team, if you’re looking to attack infrastructure automation with Azure and Rancher. Even if you don’t use Azure, many of the concepts and code in this example can be applied to other environments.

## Considerations

### Windows vs. Linux

There are a number of caveats and gotchas we need to talk about before we get started. First, the obvious: Windows is not Linux. The subsystems required to support containerized applications in a network mesh are new to Windows. They are proprietary to the Windows operating system and implemented by the [Windows Host Network Service](https://docs.microsoft.com/en-us/virtualization/windowscontainers/container-networking/architecture) and the [Windows Host Compute Service](https://docs.microsoft.com/en-us/virtualization/community/team-blog/2017/20170127-introducing-the-host-compute-service-hcs). Configuration, troubleshooting, and operational maintenance of the operating system and the underlying container runtime will obviously differ. Furthermore, Windows nodes are subject to [Windows Server licensing](https://www.microsoft.com/en-us/cloud-platform/windows-server-pricing), and the container images are subject to the [Supplemental License Terms for Windows containers](https://docs.microsoft.com/en-us/virtualization/windowscontainers/images-eula).

### Windows OS Versions

[Windows OS Versions are tied to specific container image versions](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility). This is unique to Windows. This can be overcome using Hyper-V isolation, but as of Kubernetes 1.16, Hyper-V isolation is not [supported by Kubernetes](https://kubernetes.io/docs/setup/production-environment/windows/intro-windows-in-kubernetes/#supported-functionality). So for this reason, Kubernetes and Rancher will only function with versions no earlier than Windows Server 1809/Windows Server 2019 with Windows Server containers Builds 17763 and Docker EE-basic 18.09.

### Persistence Support and CSI Plugins

CSI Plugin support is in alpha since 1.16. There are a number of in-tree and flex volume drivers supported by Windows nodes.

### CNI Plugins

Rancher support is limited to the Host Gateway (L2Bridge) and VXLAN (Overlay) network support provided by flannel. In our scenario, we’re going to take advantage of VXLAN, which is the default, because the Host Gateway option requires the configuration of User Defined Routes, when nodes are not all on the same network. This is provider-dependent, so we’re going to rely on the simplicity of the VXLAN functionality. This is alpha-level support according to the Kubernetes documentation. There is currently no open-source Windows network plugin that supports the Kuberenetes Network Policy API.

### Other Limitations

Make sure you [read the Kubernetes documentation](https://kubernetes.io/docs/setup/production-environment/windows/intro-windows-in-kubernetes/#limitations) as there are many things that do not function in Windows containers, or that function differently than they do in their Linux counterparts.

## Infrastructure as Code

One of the practices that enables [The First Way of DevOps](https://itrevolution.com/the-three-ways-principles-underpinning-devops/) is automation. We are going to automate the infrastructure of our Rancher cluster and the Azure nodes we’re going to provision in this cluster.

### Terraform

[Terraform by Hashicorp](https://terraform.io) is an open-source infrastructure as-code-tool with a [rich provider](https://www.terraform.io/docs/providers/index.html) ecosystem. We’ll be using it today to automate the provisioning for this example. Make sure you’re running at least Terraform 12. As of the time of this post, the current Terraform version is v0.12.9.

```
$ terraform version
Terraform v0.12.9
```

#### RKE Provider

The [RKE Provider for Terraform](https://github.com/yamamoto-febc/terraform-provider-rke) is a community project and not developed by Rancher, but it’s used by Rancher Labs engineers like myself, as well as other community members. Because this is a community provider and not a Terraform-supported provider you will need to install the latest release into your Terraform plugins directory. For most Linux distributions you can use the [setup-rke-terraform-provider.sh](https://github.com/JasonvanBrackel/cattle-drive/blob/master/setup-rke-terraform-provider.sh) script included in the repository for this post.

#### Rancher Provider

The [Rancher 2 Provider for Terraform](https://www.terraform.io/docs/providers/rancher2/index.html) is a terrform-supported provider used to automate Rancher, via the Rancher REST API. We will use this to create the Kubernetes cluster from the virutal machines created by Terraform with the [Azure Resource Manager](https://www.terraform.io/docs/providers/azurerm/index.html) and [Azure Active Directory](https://www.terraform.io/docs/providers/azuread/index.html) Terraform Providers

## Format of This Example

Each step of this Terraform module will be separated into submodules. This is to enhance readibility and reuse in other automations that you create in the future.

## Part 1: Set Up the Rancher Cluster

### Login to Azure

The [Azure Resource Manager](https://www.terraform.io/docs/providers/azurerm/index.html) and [Azure Active Directory](https://www.terraform.io/docs/providers/azuread/index.html) Terraform Providers will use an active Azure Cli login to access Azure. They can use other authentication methods, but for this example I log in prior to running Terraform.

```
az login
Note, we have launched a browser for you to login. For old experience with device code, use "az login --use-device-code"
You have logged in. Now let us find all the subscriptions to which you have access...
[
  {
    "cloudName": "AzureCloud",
    "id": "14a619f7-a887-4635-8647-d8f46f92eaac",
    "isDefault": true,
    "name": "Rancher Labs Shared",
    "state": "Enabled",
    "tenantId": "abb5adde-bee8-4821-8b03-e63efdc7701c",
    "user": {
      "name": "jvb@rancher.com",
      "type": "user"
    }
  }
]
```

### Setup the Resource Group

The Azure Resource Group is a location-scoped area where our Rancher Cluster’s nodes and other virutal hardware will reside. We’re actually going to create two groups. One is for the Rancher Cluster, and the other is for the Kubernetes Cluster. That’s done in the [resource-group module](https://github.com/JasonvanBrackel/cattle-drive/tree/master/terraform-module/resourcegroup-module).

```
resource "azurerm_resource_group" "resource-group" {
  name     = var.group-name
  location = var.region
}
```

### Setting Up the Hardware

#### Virtual Networking

We’ll need a virtual network and subnet. We’ll set up each of these in their respective resource groups using the [network-module](https://github.com/JasonvanBrackel/cattle-drive/tree/master/terraform-module/network-module).

We’ll set up each node with the [node-module](https://github.com/JasonvanBrackel/cattle-drive/tree/master/terraform-module/node-module). Since each node requires that Docker be installed, we will have a cloud-init file run during provisioning and install Docker with the [Rancher install-docker](https://github.com/rancher/install-docker) script. This script will detect the Linux distribution and install Docker appropriately

```
os_profile {
    computer_name = "${local.prefix}-${count.index}-vm"
    admin_username = var.node-definition.admin-username
    custom_data    = templatefile("./cloud-init.template", { docker-version = var.node-definition.docker-version, admin-username = var.node-definition.admin-username, additionalCommand = "${var.commandToExecute} --address ${azurerm_public_ip.publicIp[count.index].ip_address} --internal-address ${azurerm_network_interface.nic[count.index].ip_configuration[0].private_ip_address}"  })
  }
```

```
#cloud-config
repo_update: true
repo_upgrade: all

runcmd:
    - [ sh, -c, "curl https://releases.rancher.com/install-docker/${docker-version}.sh | sh && sudo usermod -a -G docker  ${admin-username}" ]
    - [ sh, -c, "${additionalCommand}"]
```

The additional command block in the template is filled with `sleep 0` for these nodes, but that command will be used later for linux nodes to join the Rancher managed custom cluster nodes to the platform.

#### Setup the Nodes

Next we’re going to create sets of nodes for each role: control plane, etcd, and worker. There are a couple of things that we need to take into account, as there are some indosycracies in how Azure handles its virtual networks. It reserves the first several IPs for its own use, so we need to take account of that when we create the static IPs. That’s the 4 you see here in the NIC creation. Since we’re also managaging the IPs for the subnet, we address that in each ip.

```
resource "azurerm_network_interface" "nic" {
  count               = var.node-count
  name                = "${local.prefix}-${count.index}-nic"
  location            = var.resource-group.location
  resource_group_name = var.resource-group.name

  ip_configuration {
    name                          = "${local.prefix}-ip-config-${count.index}"
    subnet_id                     = var.subnet-id
    private_ip_address_allocation = "static"
    private_ip_address            = cidrhost("10.0.1.0/24", count.index + var.address-starting-index + 4)
    public_ip_address_id          = azurerm_public_ip.publicIp[count.index].id
  }
}
```

##### Why Not Use Dynamic Allocation For Private IPs?

The terraform provider for Azure will not be aware of the IP addresses until nodes are created and completely provisioned. By handling this statically we can use the addresses during generation of the RKE cluster. There are ways around this, usually by breaking the infrastructure provisioning into multiple runs. To keep this simple, the IP addresses are managed statically.

#### Setup the Front End Load Balancer

The Rancher installation, by default, will install an ingress controller on every worker node. That means we should load balance any traffic between the available worker nodes. We’re also going to take advantage of Azure’s ability to create a public DNS entry for the public IP and use that for the cluster. This is done in the [loadbalancer-module](https://github.com/JasonvanBrackel/cattle-drive/tree/master/terraform-module/loadbalancer-module).

```
resource "azurerm_public_ip" "frontendloadbalancer_publicip" {
  name                = "rke-lb-publicip"
  location            = var.resource-group.location
  resource_group_name = var.resource-group.name
  allocation_method   = "Static"
  domain_name_label   = replace(var.domain-name-label, ".", "-")
}
```

As an alternative, there’s code included to use [cloudflare DNS](https://github.com/JasonvanBrackel/cattle-drive/tree/master/terraform-module/cloudflare-module). It isn’t used in the example but provided as an option. If you use this approach, you’ll need either a DNS cache reset or a hosts file entry to take advantage of it, so your local machine can call into Rancher to use the Rancher terraform provider.

```
provider "cloudflare" {
  email = "${var.cloudflare-email}"
  api_key = "${var.cloudflare-token}"
}

data "cloudflare_zones" "zones" {
  filter {
    name   = "${replace(var.domain-name, ".com", "")}.*" # Modify for other suffixes
    status = "active"
    paused = false
  }
}

# Add a record to the domain
resource "cloudflare_record" "domain" {
  zone_id = data.cloudflare_zones.zones.zones[0].id
  name   = var.domain-name
  value  = var.ip-address
  type   = "A"
  ttl    = "120"
  proxied = "false"
}
```

#### Install Kubernetes with RKE

We’re using the nodes created in Azure and [Terraform’s dynamic blocks](https://www.terraform.io/docs/configuration/expressions.html#dynamic-blocks) to create an RKE cluster with the [open source RKE Terraform Provider](https://github.com/yamamoto-febc/terraform-provider-rke).

```
  dynamic nodes {
    for_each = module.rancher-control.nodes
    content {
      address = module.rancher-control.publicIps[nodes.key].ip_address
      internal_address = module.rancher-control.privateIps[nodes.key].private_ip_address
      user    = module.rancher-control.node-definition.admin-username
      role    = ["controlplane"]
      ssh_key = file(module.rancher-control.node-definition.ssh-keypath-private)
    }
  }
```

##### Install Tiller with RKE

There are a number of ways to install Tiller. You can use the method in the Rancher documentation, but in this example we’re using the [RKE addon feature](https://rancher.com/docs/rke/latest/en/config-options/add-ons/).

```
  addons = <<EOL
---
kind: ServiceAccount
apiVersion: v1
metadata:
  name: tiller
  namespace: kube-system
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: tiller
  namespace: kube-system
subjects:
- kind: ServiceAccount
  name: tiller
  namespace: kube-system
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
EOL
}
```

#### Initialize Helm

[Terrform can run local scripts](https://www.terraform.io/docs/provisioners/local-exec.html). So we initialize Helm, since we’re going to use it to install cert-manager and Rancher.

#### Install cert-manager

This step is consistent with the Rancher documentation for [installing cert-manager with Tiller](https://rancher.com/docs/rancher/v2.x/en/installation/ha/helm-rancher/#let-s-encrypt).

```
resource "null_resource" "install-cert-manager" {
  depends_on = [null_resource.initialize-helm]
  provisioner "local-exec" {
    command = file("../install-cert-manager.sh")
  }
}
```

#### Install Rancher

This step is consistent with the Rancher documentation for [installing Rancher](https://rancher.com/docs/rancher/v2.x/en/installation/ha/helm-rancher/).

There are multiple versions of the `install-rancher` script. The one we’re using will request a certificate from Let’s Encrypt. If you prefer to use a self-signed certificate, you can change the symlink for `install-rancher.sh` to point to the other version and remove the `lets-encrypt` variables from the sample code below.

```
resource "null_resource" "install-rancher" {
  depends_on = [null_resource.install-cert-manager]
  provisioner "local-exec" {
    command = templatefile("../install-rancher.sh", { lets-encrypt-email = var.lets-encrypt-email, lets-encrypt-environment = var.lets-encrypt-environment, rancher-domain-name = local.domain-name })
  }
}
```

#### Bootstrap Rancher

[The Rancher2 Provider for Terraform](https://www.terraform.io/docs/providers/rancher2/r/bootstrap.html) includes a bootstrap mode. This allows us to set an admin password. You can see this step in the [rancherbootstrap-module](https://github.com/JasonvanBrackel/cattle-drive/tree/master/terraform-module/rancherbootstrap-module)

```
provider "rancher2"  {
  alias = "bootstrap"

  api_url   = var.rancher-url
  bootstrap = true

  insecure = true
}

resource "rancher2_bootstrap" "admin" {
  provider = rancher2.bootstrap
  password = var.admin-password
  telemetry = true
}
```

From there we set the cluster url.

```
provider "rancher2" {
  alias = "admin"

  api_url = rancher2_bootstrap.admin.url
  token_key = rancher2_bootstrap.admin.token

  insecure = true
}

resource "rancher2_setting" "url" {
  provider = rancher2.admin
  name = "server-url"
  value = var.rancher-url
}
```

## Part 2: Set Up the Kubernetes Cluster Managed by Rancher

### Create a Service Principal for Azure

Before we can use the Azure cloud to create [Load Balancer services](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) and [Azure Storage](https://docs.microsoft.com/en-us/azure/aks/concepts-storage), we first need to configure the connector for the [Cloud Controller Manager](https://kubernetes.io/docs/concepts/architecture/cloud-controller/). So we create a service principal scoped to the resource Group of the cluster in the [cluster-module](https://github.com/JasonvanBrackel/cattle-drive/tree/master/terraform-module/cluster-module) and [serviceprincipal-module](https://github.com/JasonvanBrackel/cattle-drive/tree/master/terraform-module/serviceprincipal-module).

```
resource "azuread_application" "ad-application" {
  name                       = var.application-name
  homepage                   = "https://${var.application-name}"
  identifier_uris            = ["http://${var.application-name}"]
  available_to_other_tenants = false
}

resource "azuread_service_principal" "service-principal" {
  application_id                = azuread_application.ad-application.application_id
  app_role_assignment_required  = true
}

resource "azurerm_role_assignment" "serviceprincipal-role" {
  scope                = var.resource-group-id
  role_definition_name = "Contributor"
  principal_id         = azuread_service_principal.service-principal.id
}

resource "random_string" "random" {
  length = 32
  special = true
}

resource "azuread_service_principal_password" "service-principal-password" {
  service_principal_id = azuread_service_principal.service-principal.id
  value                = random_string.random.result
  end_date             = timeadd(timestamp(), "720h")
}
```

### Define the Custom Cluster

We have to set the flannel network options to support the Windows flannel driver. You’ll also notice the configuration of the azure provider.

```
resource "rancher2_cluster" "manager" {
  name = var.cluster-name
  description = "Hybrid cluster with Windows and Linux workloads"
  # windows_prefered_cluster = true Not currently supported
  rke_config {
    network {
      plugin = "flannel"
      options = {
        flannel_backend_port = 4789
        flannel_backend_type = "vxlan"
        flannel_backend_vni = 4096
      }
    }
    cloud_provider {
      azure_cloud_provider {
        aad_client_id = var.service-principal.client-id
        aad_client_secret = var.service-principal.client-secret
        subscription_id = var.service-principal.subscription-id
        tenant_id = var.service-principal.tenant-id
      }
    }
  }
}
```

### Create the Virtual Machines

These virtual machines are created with the same process as the earlier machines and include the Docker install scripts. The only change is the additional command using the [linux node command](https://www.terraform.io/docs/providers/rancher2/r/cluster.html#node_command) from the previously created cluster.

```
module "k8s-worker" {
  source = "./node-module"
  prefix = "worker"

  resource-group = module.k8s-resource-group.resource-group
  node-count = var.k8s-worker-node-count
  subnet-id = module.k8s-network.subnet-id
  address-starting-index = var.k8s-etcd-node-count + var.k8s-controlplane-node-count
  node-definition = local.node-definition
  commandToExecute = "${module.cluster-module.linux-node-command} --worker"
}
```

### Create the Windows Workers

The Windows worker process is similar to the Linux process with a few notable exceptions. Since Windows does not support a cloud-init file, we have to create a [Windows Custom Script Extension](https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/custom-script-windows). You’ll see this in the [windowsnode-module](https://github.com/JasonvanBrackel/cattle-drive/tree/master/terraform-module/windowsnode-module)

The Windows worker uses a password to authenticate. The VM Agent is also required to run Custom Script Extensions.

```
os_profile {
  computer_name = "${local.prefix}-${count.index}-vm"
  admin_username = var.node-definition.admin-username
  admin_password = var.node-definition.admin-password
}

os_profile_windows_config {
  provision_vm_agent = true
}
```

### Join Rancher

After provisioning the nodes the Custom Script Extension will run the [Windows Node Command](https://www.terraform.io/docs/providers/rancher2/r/cluster.html#windows_node_command).

> **Note**
>
> This is a different type of Custom Script Extension then is in the [Terrform documentation](https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_extension.html), which is for Linux virtual machines. Azure will let you attempt to use the Terraform type against a Windows node, but it will ultimately fail.

### BE PATIENT

This whole process takes a while. When Terraform is done, there will be items that are still provisioning. Even once the Kubernetes cluster is up, the Windows node may take 10 minutes or more to completely initialize. A working Windows node will look something like the terminal output below.

```
C:Usersiamsuperman>docker ps
CONTAINER ID        IMAGE                                COMMAND                  CREATED             STATUS              PORTS               NAMES
832ef7adaeca        rancher/rke-tools:v0.1.50            "pwsh -NoLogo -NonIn…"   10 minutes ago      Up 9 minutes                            nginx-proxy
7e75dffce642        rancher/hyperkube:v1.15.4-rancher1   "pwsh -NoLogo -NonIn…"   10 minutes ago      Up 10 minutes                           kubelet
e22b656e22e0        rancher/hyperkube:v1.15.4-rancher1   "pwsh -NoLogo -NonIn…"   10 minutes ago      Up 9 minutes                            kube-proxy
5a2a773f85ed        rancher/rke-tools:v0.1.50            "pwsh -NoLogo -NonIn…"   17 minutes ago      Up 17 minutes                           service-sidekick
603bf5a4f2bd        rancher/rancher-agent:v2.3.0         "pwsh -NoLogo -NonIn…"   24 minutes ago      Up 24 minutes                           gifted_poincare
```

Terraform will output the credentials for the new platform.

```
Outputs:

lets-encrypt-email = jason@vanbrackel.net
lets-encrypt-environment = production
rancher-admin-password = {REDACTED}
rancher-domain-name = https://jvb-win-hybrid.eastus2.cloudapp.azure.com/
windows-admin-password = {REDACTED}
```

## Part 3: Working With Windows Workloads

### Targetting Workload by OS

Because Windows container images and Linux container images are not the same, we need to target our deployments using [Kubernetes node affinity](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity). Each node has OS labels to assist with this purpose.

```
> kubectl get nodes
NAME           STATUS   ROLES          AGE     VERSION
control-0-vm   Ready    controlplane   16m     v1.15.4
etcd-0-vm      Ready    etcd           16m     v1.15.4
win-0-vm       Ready    worker         5m52s   v1.15.4
worker-0-vm    Ready    worker         12m     v1.15.4
> kubectl describe node worker-0-vm
Name:               worker-0-vm
Roles:              worker
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/arch=amd64
                    kubernetes.io/hostname=worker-0-vm
                    kubernetes.io/os=linux
                    node-role.kubernetes.io/worker=true
...
> kubectl describe node win-0-vm
Name:               win-0-vm
Roles:              worker
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=windows
                    kubernetes.io/arch=amd64
                    kubernetes.io/hostname=win-0-vm
                    kubernetes.io/os=windows
```

Clusters deployed by Rancher 2.3 automatically taint Linux worker nodes with `NoSchedule`, which means that workloads will always go to the Windows nodes unless specifically scheduled to the Linux nodes and also configured to tolerate the taint.

Depending on how you plan to use the cluster, you might find that setting a similar default preference of Windows or Linux results in less overhead when launching workloads.
