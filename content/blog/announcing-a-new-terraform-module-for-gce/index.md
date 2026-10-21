---
title: "Announcing a New Terraform Module for GCE"
date: 2017-08-31T09:00:00
slug: "announcing-a-new-terraform-module-for-gce"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["cloud", "gcp"]
content_type: "release"
draft: true
migration:
  wp_id: 85795
  original_url: "https://www.suse.com/c/rancher_blog/announcing-a-new-terraform-module-for-gce/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x Terraform module"
  redirect_target: "https://rancher.com/blog (hub)"
---

I’m pleased to announce that Rancher has released a [new Terraform
module](https://github.com/rancher/terraform-modules) for deploying
Rancher on Google Compute Engine (GCE). This complements our existing
module for Amazon Web Services (AWS). Terraform is an excellent tool for
managing infrastructure as code, and many of our users already make use
of it elsewhere in their environments. Using this module along with
either GCE or AWS to orchestrate Rancher gives you the ability to
define the entirety of the stack—from the application layer being
managed by Docker Compose or Kubernetes resource YML in Rancher all the
way down to the servers and networks in the Terraform plan. This ability
to create an entire production stack in one click is very powerful. For
instance, if you want to replicate production to simulate a change, just
spin up a clone in another account. Once you’re done with your tests,
you can throw that environment away to save on costs as well as to avoid
keeping state around that is prone to getting stale, or out of date with
production. To get started, we’ve provide a sample terraform plan that
implements the module. You’ll need to provide a few parameters to the
plan, which you can do interactively when you run it or by adding a file
called “terraform.tfvars” to the same directory as the [example](https://github.com/rancher/terraform-modules/tree/master/example_ha/gce).

First you’ll want to run the database plan to create the GCE CloudSQL
instance. From the above directory:

```
cd database

terraform apply
```

Once this is complete, then you can run the management server plan. This
plan will reference the previous database plan to get the connection
details of the database.

```
cd ../management-cluster

terraform apply
```

This should create the GCE instances running RancherOS and Rancher
server. Head over to the GCE management console to get the public IP
address of your instance. You can connect to it on port 8080. Remember
the above is just an example plan that implements the module. You can
also reference the module in an existing plan like so:

```
module "gce_compute" {

   source = "../../../modules/gce/compute"  // replace with relative path if you checked out module to different location

   name = "my-rancher-cluster"

   gce_project = "myproject"

   ... // remaining parameters

}
```

You can read more about how to use [Terraform modules here](https://www.terraform.io/docs/modules/usage.html). Our terraform
modules for both AWS and GCE are located on [Github](https://github.com/rancher/terraform-modules). Happy Terraforming!
