---
title: "Harvester v1.9.1 and what changes with SUSE Virtualization"
date: 2026-11-13T09:00:00
slug: "harvester-v1-9-1-and-suse-virtualization"
authors: ["Alex Settle"]
products: ["Harvester"]
tags: ["release"]
description: "Harvester v1.9.1 is out and stays 100% open source. Here is the release schedule and the upgrade paths now that SUSE Virtualization ships from its own build pipeline."
draft: false
---

Big news for the Harvester community! We are thrilled to share what is coming next with Harvester v1.9.1 alongside the debut of SUSE Virtualization v1.9.1.

First things first: **Harvester is and will always remain 100% open source.** As enterprise security and compliance requirements evolve, such as the upcoming EU Cyber Resilience Act and SLSA L3 standards, we are updating our build infrastructure. SUSE is establishing dedicated build pipelines for our community releases and enterprise builds so we can maintain rapid open-source innovation while delivering hardened software for enterprise needs.

What does this mean for you? Harvester releases will keep pushing the boundaries of development at full speed. Harvester v1.9.1 is available now, while SUSE Virtualization v1.9.1 will follow shortly for SUSE customers focused on new (fresh) installations. Read on for the full breakdown of timelines and upgrade paths!

## Release schedule and availability

- **Harvester v1.9.1:** Available now.
- **SUSE Virtualization v1.9.1:** Releasing in November 2026, restricted to fresh installations.
- **Harvester v1.10.0:** Target release December 2026.
- **SUSE Virtualization v1.10.1:** Target release February 2027.

## Key highlights and upgrade paths

- **Fresh installs only for v1.9.1 SUSE Virtualization:** SUSE Virtualization v1.9.1 will be offered exclusively for new cluster deployments.
- **No same-version switching in v1.9.1:** Switching an existing v1.9.1 Harvester cluster directly to v1.9.1 SUSE Virtualization is not supported.
- **Direct cross-minor upgrade at v1.10.1:** Upgrades to v1.10.1 SUSE Virtualization will be fully supported from both v1.9.1 Harvester and v1.9.1 SUSE Virtualization installations.

## Contributor acknowledgments

The release of Harvester v1.9.1 is made possible by the dedicated contributions of our open-source community. We extend our sincere gratitude to all the developers, testers, documentation writers, and community members who reported issues, submitted code reviews, and shared valuable feedback throughout this release cycle.

## Community feedback and support channels

We encourage community participation and value your input. You can share your feedback, report bugs, or request new features through our public [GitHub repository](https://github.com/harvester/harvester). For real-time discussions, join the [#harvester](https://rancher-users.slack.com/archives/C01GKHKAG0K) or [#harvester-dev](https://rancher-users.slack.com/archives/C01LRF1G7RD) channel on the official Rancher Slack workspace.

Enterprise customers seeking formal SLA-backed support for SUSE Virtualization should submit tickets directly through the [SUSE Customer Center](https://scc.suse.com/customer-management) portal or contact their designated account technical support manager.

For SUSE Virtualization customers, a blog post with more information is coming soon!

Have questions about these updates? Check the community FAQ pinned in the [#harvester](https://rancher-users.slack.com/archives/C01GKHKAG0K) and [#harvester-dev](https://rancher-users.slack.com/archives/C01LRF1G7RD) Slack channels, or join the conversation there.
