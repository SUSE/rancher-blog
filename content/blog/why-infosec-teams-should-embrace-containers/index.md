---
title: "Why InfoSec Teams Should Embrace Containers"
date: 2017-06-12T10:19:00
slug: "why-infosec-teams-should-embrace-containers"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["security"]
content_type: "opinion"
draft: false
migration:
  wp_id: 86706
  original_url: "https://www.suse.com/c/rancher_blog/why-infosec-teams-should-embrace-containers/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Each time a new software technology arrives on the scene, InfoSec teams
can get a little anxious. And why shouldn’t they? Their job is to assess
and mitigate risk – and new software introduces unknown variables that
equate to additional risk for the enterprise. It’s a tough job to make
judgments about new, evolving, and complex technologies; that these
teams approach unknown, new technologies with skepticism should be
appreciated. This article is an appeal to the InfoSec people of the
world to be optimistic when it comes to containers, as containers come
with some inherent security advantages: **Immutability** In a typical
production environment, you have a number of things managing state on
your servers. These include system imaging, configuration management
(CM), and deployment tools. The end state of the system is very dynamic
(particularly with CM tools), with libraries and packages determined
based on various runtime variables. Here’s some examples of when this
can be problematic:

- The version of OpenSSL you have running on your hosts may vary based
  on the operating system you’re using – your RHEL 6 hosts might have
  one version, while your Ubuntu hosts using a different patch release
  have a different version. Even these small differences can have a
  measurable impact, and can enable recent OpenSSL exploits like
  Heartbleed.
- If you’re ahead of the game and don’t have different operating
  systems, what if the CM tool you’re running on a particular set of
  hosts encounters a bug and stops before it can ensure package
  versions (assuming you have defined explicit versions!)? Now, an
  outdated package lives on in the system until someone notices. In a
  small environment, you might have a good pulse on successful CM
  runs, but in a large environment with thousands of hosts and some
  level of complexity, you’ll have some number of hosts on which you
  lack assurances of consistency, either because you don’t know about
  it, or you haven’t addressed it yet. The lack of determinate state
  creates the need for inventory and CVE scanning technologies in your
  environment.

This is where containers offer an extra benefit. Because of the
immutable nature of a container image, I can know the state of my
runtime before it’s deployed. This provides me with a single point to
inspect and reason about the state of runtime, rather than constantly
taking inventory of every runtime deployed in my system. It’s much
easier to scan images once during the build process for known CVEs and
other vulnerabilities, and to catch risks before deployed.
**Isolation** With containers, the Linux kernel has been engineered to
provide isolation between the containers on a host. It allows each
process to have a different runtime than its neighbor. For InfoSec, this
reduces the abilities of an attack vector to affect other parts of the
system if an application is compromised. While this compartmentalization
isn’t airtight, no security mechanism truly is. **Easy adoption for
developers and application teams** And finally another reason this
should appeal to InfoSec is that you can get all the above benefits much
more easily than security-only tools because of the shared advantages to
developers and application teams. No security group operates in a vacuum
and even the most security minded org needs to balance control with
productivity. But when your solution satisfies both, you have very
little resistance toadoption and justifying the resources required. As
much as this sounds like a paradox that shouldn’t exist, you can to
some degree have both increased agility and security with containers.
**Conclusion** I hope that these points have encouraged you to further
explore and see for yourself how containers can benefit security in your
organization, if only to start an internal conversation on using them in
production. As always, the Rancher team is here to help along with your
container journey – reach out to us on Twitter
[@Rancher\_Labs](https://twitter.com/rancher_labs)

*William Jimenez is a Solutions Architect at Rancher Labs.*
