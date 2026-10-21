---
title: "Clean Install Rancher Desktop    "
date: 2022-01-18T14:35:07
slug: "clean-install-rancher-desktop"
authors: ["Robert Sirchia"]
image: "images/rancher-desktop.jpeg"
products: ["Rancher Desktop"]
tags: ["installation"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 93034
  original_url: "https://www.suse.com/c/rancher_blog/clean-install-rancher-desktop/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher Desktop 2022 clean install"
  redirect_target: "/rancher-desktop"
---

With any type of open-source project Rancher Desktop sometimes brings hiccups. We should expect this, and as the engineers address these issues. There could be a gap in the features or functionality that puts the app in an unrecoverable state - this happened to me recently. Rancher Desktop restarted Kubernetes, and everything hung and didn't work.  
I deleted the app from my Mac and tried a different version of Rancher Desktop, thinking my recent upgrade was the issue. Come to find out the version wasn't the issue. Something went wrong, and no matter what I tried Rancher Desktop wasn't working. At the time I didn't care why it wasn't working. I needed to demo something else and couldn't get it to work.

I got a moment to sit with one of the engineers to get past this. So, if Rancher Desktop ever gets to a state where it's stuck, here is how to fix it:

#### Remove the App

Go to the **Applications** directory and delete the app.

#### Remove Supporting files

```
~/Library/rancher-desktop
~/Library/Logs/rancher-desktop
~/Library/Preferences/rancher-desktop
~/Library/Application Support/Caches/rancher-desktop-updater
~/Library/Application Support/rancher-desktop
```

#### Reinstall

Reinstall the version of the Rancher Desktop you want to use.

This should clear up any issues with using Rancher Desktop and any problems you might run into.
