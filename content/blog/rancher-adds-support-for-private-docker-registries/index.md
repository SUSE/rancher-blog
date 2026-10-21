---
title: "Rancher Adds Support for Private Docker Registries"
date: 2015-03-31T11:15:00
slug: "rancher-adds-support-for-private-docker-registries"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["installation"]
content_type: "release"
draft: true
migration:
  wp_id: 86898
  original_url: "https://www.suse.com/c/rancher_blog/rancher-adds-support-for-private-docker-registries/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 0.12 registries, 1.x era"
  redirect_target: "rancher.com/blog (hub)"
---

When we shipped Rancher 0.12 last week we added one of the more
frequently requested features, support for private Docker registries.
Rancher had always allowed users to provision containers from
DockerHub, but many organizations run their own registries, or use
private hosted registries such as [Quay.io](http://quay.io), and
[private DockerHub accounts](https://hub.docker.com/). Beginning with
this release, users will be able to connect their private registry
directly to their Rancher environment, and deploy containers
from private Docker images. To use this new feature navigate to the new
“Registries” tab on your Rancher instance. You’ll see that you now
have the option to “Add a Privae Registry,” then fill out the form,
add your credentials and you are done. Credentials aren’t required
unless the registry or images you want to use require a password. [![Add
Private Docker
Registry](images/rancher_blog_Add-Private-Docker-Registry-1024x298.png)](https://cdn.rancher.com/wp-content/uploads/2015/03/01061953/Add-Private-Docker-Registry.png)
Once you’ve set up your private registry, you’ll be able to launch
containers from images hosted in your private registry from the launch
container workflow. You can access your private registry by clicking on
the “docker” image, and selecting the name of your private registry.
From that point, simply provide the name of your Docker image on the
private registry and continue the provisioning process. [![provision
from private
registry](images/rancher_blog_provision-from-private-registry-1024x312.png)](https://cdn.rancher.com/wp-content/uploads/2015/03/01061953/provision-from-private-registry.png)
The video below gives a more complete explanation of how to register a
private registry and credentials within Rancher. Hope you enjoy the new
feature. If you would like to set up some time to talk with us about
getting started with Rancher, please request a
demonstration.
