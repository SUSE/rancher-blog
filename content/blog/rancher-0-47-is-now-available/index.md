---
title: "Rancher 0.47 is now available!"
date: 2015-11-25T11:14:00
slug: "rancher-0-47-is-now-available"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["storage"]
content_type: "release"
draft: true
migration:
  wp_id: 86873
  original_url: "https://www.suse.com/c/rancher_blog/rancher-0-47-is-now-available/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 0.47 release, pre-1.0"
  redirect_target: "rancher.com/blog (hub)"
---

[![convoy
gluster](images/rancher_blog_convoy-gluster-300x145.png)](https://cdn.rancher.com/wp-content/uploads/2015/11/11225644/convoy-gluster.png)At
DockerCon a couple weeks back, we announced Rancher’s new capability to
manage [Persistent Storage
Services](https://rancher.com/how-rancher-storage-services-unleash-the-power-of-software-defined-storage/), and
how it can be used to make it easier to manage stateful applications.
Today, with the release of Rancher 0.47.0, I’m excited to finally make
it available for our users to try it as an Experimental feature.
Rancher makes it easy for you to deploy this by allowing you to both
launch a GlusterFS storage service and deploy Convoy-Gluster as the
Docker volume plugin to your environment directly from Rancher’s App
Catalog. Once the stacks are off and running, you will be then be able
to leverage GlusterFS transparently by specifying GlusterFS as your
Docker volume plugin when creating containers and services. The second
major feature you will notice immediately once you deploy Rancher 0.47.0
is the major revamp we have done to our existing UI. Based on customer
and user feedback throughout our Beta period, we have made extensive
changes to the Application UI to make it easier for users to manage more
complicated stacks. Highlights include a “summary” pop-up view for each
service with more pertinent information about the service and its
sidekicks to showing you the exact host and port published per service
that can be clicked on to open a new browser window to the app directly.
Please view our [release
notes](https://github.com/rancher/rancher/releases/tag/v0.47.0) for more
details on the new UI, or better yet, [install
Rancher](https://github.com/rancher/rancher#installation) and let us
know what you think!
[](images/rancher\_blog\_47-screenshot2.png)
[![47
screenshot1](images/rancher_blog_47-screenshot1.png)](images/rancher_blog_47-screenshot1.png)
[![Rancher 0.47
screenshot2](images/rancher_blog_47-screenshot2.png)](images/rancher_blog_47-screenshot1.png)
As always, you will continue to see fixes and updates to these two
major features along with all our previous ones in the coming weeks.
Again, the team here at Rancher is most appreciative of all the
feedback given during our Beta period and will continue to incorporate
as many as we can as we push to our GA goal in early Q1 2016. Happy
Thanksgiving from the Rancher Team! You can view a deep dive on these
new features in a recording of our last meetup, or join us for our next
online meetup in December to see how to tie all of these cool new
features in with Amazon Web Services.
