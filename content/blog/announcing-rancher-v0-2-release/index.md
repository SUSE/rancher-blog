---
title: "Announcing Rancher v0.2 Release"
date: 2014-12-03T09:01:00
slug: "announcing-rancher-v0-2-release"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["storage", "networking"]
content_type: "release"
draft: true
migration:
  wp_id: 85801
  original_url: "https://www.suse.com/c/rancher_blog/announcing-rancher-v0-2-release/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher v0.2 release notes, 1.x era"
  redirect_target: "rancher.com/blog (hub)"
---

The Rancher team has been working hard to give users a first taste of
what storage management will look like in Rancher. In addition to
managing container networking across cloud providers, we are excited to
announce the following features in Rancher v0.2. First up, the team has
exposed the building blocks for storage management. Full support has
been added in the API and UI for viewing, creating, and connecting
storage volumes. When creating containers Rancher now supports familiar
Docker `–v` and
`--volumes-from` options.

---

```
                 [![mounts](https://www.rancher.io/wp-content/uploads/2014/12/mounts1.png)](https://www.rancher.io/wp-content/uploads/2014/12/mounts1.png)View mounts attached to a container.
```

[![add-container](https://www.rancher.io/wp-content/uploads/2014/12/add-container.png)](https://www.rancher.io/wp-content/uploads/2014/12/add-container.png)Attach host volumes or volumes from another container.
[![volumes](https://www.rancher.io/wp-content/uploads/2014/12/volumes.png)](https://www.rancher.io/wp-content/uploads/2014/12/volumes.png)See all volumes and associated metadata.

---

Next up, the UI allows you console access to your containers. Now you
can get access to your running containers, the same as if you had run
`docker exec –it /bin/sh`,
from the UI.

---

[![console](https://www.rancher.io/wp-content/uploads/2014/12/console1.png)](https://www.rancher.io/wp-content/uploads/2014/12/console1.png)Console Running VI in a container.

---

Get [Rancher](http://github.com/rancherio/rancher "Rancher") on GitHub.
