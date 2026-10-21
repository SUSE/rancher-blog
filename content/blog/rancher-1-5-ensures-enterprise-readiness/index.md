---
title: "Rancher 1.5 ensures enterprise-readiness"
date: 2017-03-06T11:14:00
slug: "rancher-1-5-ensures-enterprise-readiness"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["networking"]
content_type: "release"
draft: true
migration:
  wp_id: 86883
  original_url: "https://www.suse.com/c/rancher_blog/rancher-1-5-ensures-enterprise-readiness/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x release"
  redirect_target: "rancher.com/blog (hub)"
---

![Rancher
1.5](images/rancher_blog_logos-registered_rancher-1.51-300x137.jpg)On Friday we released version
1.5 of the Rancher container management platform. The enhancements in
this release are designed to help ensure enterprise- as well as
production-readiness. Additional webhooks improve Rancher extensibility
and enable you to optimize overall infrastructure utilization. New
API, networking and container scheduling policies provide fine-grained
control of the container environment. Additional enhancements include
metadata performance improvements and conditional logic support for
catalog templates.

## **Additional webhooks drivers**

With Rancher 1.4, we
added [webhooks](https://rancher.com/webhooks-in-rancher/), with an
initial driver to handle scaling. The key to implementing webhooks is
the ‘receiver’, which enables you to register a webhook and provides a
URL to trigger an action inside Rancher software. Thanks to the
community feedback we received, in Rancher 1.5 we were able to
extend the Rancher webhooks implementation to include two new drivers:

- Host scaling webhook, which scales hosts up or down
- DockerHub service upgrade webhook configured for Dockerhub image
  updates and used to update services in Rancher using that image

As always, we welcome additional feedback on these and other
capabilities via the [forums](https://forums.rancher.com/).

## **Enhanced policy controls**

Rancher 1.5 delivers enhanced policy controls, including the ability to
intercept all API requests. In addition, pre/post filter logic can now
be added to each request, providing administrators with greater
flexibility to define and control API access. Fine grained API policy
management can be enabled to modify the API request as well as
the response payload both to and from Rancher. Two additional networking
policies have been added, which can be configured for each environment.
The first enables you to allow or deny communication outside of a
service. By default, Rancher is setup to allow communication between
all services within an environment. If configured to deny
communication, however, the containers will unable to communicate with
containers outside of a service. The second policy enables link support
so that services or stacks which are configured to deny communication
can be given permission to communicate by using either a Docker link or
selector labels. Additional policy controls are also now available for
container scheduling. Rancher 1.5 supports the ability to add tags
which restrict container scheduling to specific hosts. Placement of
containers is determined by pre-specified labels, providing improved
control over how each host is utilized.

## **Metadata performance improvements**

The Rancher metadata service has been improved by caching metadata
information. This reduces database thrashing as well as the footprint
of the metadata passed on to each metadata service. Since so many
services rely on metadata, depending on your implementation, you should
see an overall improvement in Rancher performance. You will also see
improvements when you launch large volumes of containers at the same
time or when adding a new container after multiple containers are
already running.

## **Conditional logic support for catalog templates**

Rancher container management now supports the ability to use conditional
logic by leveraging the [Go template
system](https://golang.org/pkg/text/template/). Using conditional logic
combined with variable interpolation will provide greater flexibility to
generate more dynamic catalog templates. *More information about
Rancher 1.5 container management can be found in the* [*release
notes*](https://github.com/rancher/rancher/releases)\*. For production
use, we recommend waiting for the stable release, which will be
available shortly.
