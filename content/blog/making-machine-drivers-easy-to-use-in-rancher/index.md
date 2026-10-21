---
title: "Making Machine Drivers Easy to Use in Rancher"
date: 2016-06-28T11:11:00
slug: "making-machine-drivers-easy-to-use-in-rancher"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["cloud"]
content_type: "explainer"
draft: true
migration:
  wp_id: 86807
  original_url: "https://www.suse.com/c/rancher_blog/making-machine-drivers-easy-to-use-in-rancher/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x machine drivers, catalog v1"
  redirect_target: "rancher.com/blog (hub)"
---

A few months back, we launched a new feature at Rancher aptly named
[Rancher Catalog](https://github.com/rancher/rancher-catalog) and
subsequently [Community
Catalog](https://github.com/rancher/community-catalog). This feature had
been brewing in the minds of quite a few people around the office, so by
the time it was placed on my plate it was highly anticipated by the
team. The concept on a whole is not unfamiliar to the majority of our
users: a single page through which users can search for commonly
deployed applications, with sane defaults and a repeatable launch
process. We wanted to provide our users with a clean, simple UI to
showcase the variety of platforms, applications, and machines available
to the community. When a user first launches the Rancher UI and has no
stacks or services, they’ll be prompted to deploy their first service
either manually or from the the Catalog. After the initial setup, users
may return to the catalog via the top level navigation. On the catalog
page, the user is presented with a simple grid of catalog entries. Users
can search and filter from this page to easily pare down an ever-growing
collection of catalog entries. [![Rancher Catalog
overview](images/rancher_blog_catalog_overview-1024x640.png)](https://cdn.rancher.com/wp-content/uploads/2016/06/24165957/catalog_overview.png)
**Snapshot of the Rancher Catalog** Each catalog entry
allows the user to view further details about the entry. Additionally,
this is also where the catalog entry is launched. While viewing a
catalog entry, users may select the desired version, name and
configuration for the service, and finally preview the corresponding
YAML files used to deploy: [![Cloudflare DNS community catalog
entry](images/rancher_blog_catalog_detail-1024x639.png)](https://cdn.rancher.com/wp-content/uploads/2016/06/24170729/catalog_detail.png)
**An example of a Rancher Catalog item (CloudFlare DNS)** We
have also provided a mechanism for users to add their own catalog hosted
on Github. To add new catalogs, a user simply has to add the Github
‘.git’ URL to Rancher via the Settings page and the Catalog section.
The user’s new catalog will be merged (front end only) with existing
catalogs. Don’t worry, you can select your catalog’s name from the
dropdown to see only those entries. Catalog has been around for some
time; I hope you’ve had a chance to use it. ​ Not long ago, we decided
to open
the [Community Catalog](https://github.com/rancher/community-catalog)
and allow users to provide their own machine drivers. You may have used
our Machine Drivers page: it is a simple way for users to interact with
a variety of docker-machine drivers, allowing users to customize the
machine drivers they use regularly. Users have had the capability of
adding custom machine drivers in Rancher for quite some time via the
‘Add Machine Driver’ button. Until recently, this was the only way to
do so within our platform, but we have added an additional resource for
users who need custom machine drivers through user catalogs. Users can
add a new machine-templates folder to their catalog repo - once the
catalog has been added to Rancher, we’ll pull these drivers on to the
new Rancher Machine Driver page. [![Rancher Machine Driver
Catalog](images/rancher_blog_machine_drivers-1024x638.png)](https://cdn.rancher.com/wp-content/uploads/2016/06/24170451/machine_drivers.png)
**Rancher Machine Driver catalog; activating machine drivers is as
simple as hitting the play button on each item.** To be
clear, your machine drivers will not show up on the Catalog page, even
though they live in the same Github repo. Activating machine drivers
through Rancher is as simple as hitting the play button. It’s just as
easy to disable machine drivers that do not apply to you or your
company. This easy to deploy workflow has an equally simple upgrade
process: if you’ve deployed an older version of the machine driver in
your catalog, you’ll see an upgrade icon. Simply click the upgrade
icon, and we’ll upgrade you to the latest version in your catalog. We
feel that this new Machine Driver catalog will give our customers the
ability to add repeatable, maintainable, easily deployable machine
drivers to their company catalog. ​ While it’s only a quick overview, I
would like to invite you to head over and checkout the [Rancher
Catalog](https://github.com/rancher/rancher-catalog) and Machine Driver
pages. Play around with the applications you can deploy or add your own
for ease of use. Feel free to reach out over on the
[forums](https://forums.rancher.com/) or on our
[Github](https://github.com/rancher/) if you’d like to provide
feedback! *Wes works on all things UI at Rancher Labs.*
