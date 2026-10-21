---
title: "Improve Security with this One-Liner"
date: 2021-11-04T14:07:21
slug: "improve-security-with-this-one-liner"
authors: ["Brice Dekany"]
products: ["Other"]
tags: ["security"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 93386
  original_url: "https://www.suse.com/c/rancher_blog/improve-security-with-this-one-liner/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "SLE BCI topic belongs to suse.com"
  redirect_target: "suse.com"
---

Picture this: You are searching through the backlog for a nice feature to develop and play with. The day looks nice, the sky is clear, and you're listening to lo-fi on youtube.

That's when the infamous security team entered the room/slack channel with their usual complaint: We want more security!

[![](https://media1-production-mightynetworks.imgix.net/asset/30772071/1636038348140.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)](https://media1-production-mightynetworks.imgix.net/asset/30772071/1636038348140.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format)

We know that security is essential. I am pretty sure you've read Project Unicorn and know this quote: "If a developer ever has a choice between working on a feature or security, they should always choose security."

The worst security issue of your cloud native app is the part you don't manage: The Base layer in your containerized app.

Palo Alto found that [96% of third-party container applications deployed in cloud infrastructure contain known vulnerabilities](https://www.zdnet.com/article/96-of-third-party-container-applications-deployed-in-cloud-infrastructure-contain-known-vulnerabilities-unit-42/). Scary.

What if I told you that you could improve security just by changing the FROM in your Dockerfile?

Wait, don't run away!

What if I told you that changing the FROM image won't break all the language frameworks or dependencies?

[SUSE has just released a brand new set of lightweight hardened tech-preview container images (SLE BCI) targeted to developers and operators.](https://community.suse.com/posts/17842991)

Let's take a look at the security number with [Trivy](https://github.com/aquasecurity/trivy). Trivy scans existing OCI Images or source files and detects Known Security Issues (aka CVE).

## **Golang: Official Docker Hub vs. SLE Registry**

The result is quite Hardcore. Let's say it's a no-match:

```
# trivy image golang | grep Total -B2
golang (debian 11.1)
====================
Total: 307 (UNKNOWN: 1, LOW: 240, MEDIUM: 39, HIGH: 16, CRITICAL: 11)

# trivy image registry.suse.com/bci/golang:1.16 | grep Total -B2
registry.suse.com/bci/golang:1.16 (suse linux enterprise server 15.3)
=====================================================================
Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)
```

## **NodeJS: Official Docker Hub vs. SLE Registry**

If you thought golang was a slice of swiss cheese, take a look at node's official image:

```
# trivy image node | grep Total -B2
node (debian 11.1)
==================
Total: 713 (UNKNOWN: 2, LOW: 497, MEDIUM: 140, HIGH: 59, CRITICAL: 15)
--
Node.js (node-pkg)
==================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

# trivy image registry.suse.com/bci/nodejs:14 | grep Total -B2
registry.suse.com/bci/nodejs:14 (suse linux enterprise server 15.3)
===================================================================
Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)
--
Node.js (node-pkg)
==================
Total: 6 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 6, CRITICAL: 0)
```

## **Python: Official Docker Hub vs. SLE Registry**

Last but not least, my favorite language: Python. And it's a shame:

```
# trivy image python:3.9 | grep Total -B2
python:3.9 (debian 11.1)
========================
Total: 738 (UNKNOWN: 2, LOW: 520, MEDIUM: 142, HIGH: 59, CRITICAL: 15)
--
Python (python-pkg)
===================
Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)

# trivy image registry.suse.com/bci/python:3.9 | grep Total -B2
registry.suse.com/bci/python:3.9 (suse linux enterprise server 15.3)
====================================================================
Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)
--
Python (python-pkg)
===================
Total: 2 (UNKNOWN: 1, LOW: 0, MEDIUM: 1, HIGH: 0, CRITICAL: 0)
```

Of course, all the SLE BCI images have the development and build tool dedicated to a specific language. Give it a try!

Just replace the FROM line in your Dockerfile with one of the base Images built and maintained by SUSE.

[registry.suse.com/bci/nodejs:12](http://registry.suse.com/bci/nodejs:12) (NodeJS 12)

[registry.suse.com/bci/nodejs:14](http://registry.suse.com/bci/nodejs:14) (NodeJS 14)

[registry.suse.com/bci/openjdk:11](http://registry.suse.com/bci/openjdk:11) (Java 11 runtime only)

[registry.suse.com/bci/openjdk-devel:11](http://registry.suse.com/bci/openjdk-devel:11) (Java 11 development kit + tools)

[registry.suse.com/bci/python:3.6](http://registry.suse.com/bci/python:3.6) (Python 3.6)

[registry.suse.com/bci/python:3.9](http://registry.suse.com/bci/python:3.9) (Python 3.9)

[registry.suse.com/bci/golang:1.16](http://registry.suse.com/bci/golang:1.16) (Golang 1.16)

[registry.suse.com/suse/dotnet-aspnet:5.0](http://registry.suse.com/suse/dotnet-aspnet:5.0) (.NET 5.0 runtime only)

[registry.suse.com/suse/dotnet-aspnet:3.1](http://registry.suse.com/suse/dotnet-aspnet:3.1) (.NET 3.1 runtime only)

[registry.suse.com/suse/dotnet-sdk:5.0](http://registry.suse.com/suse/dotnet-sdk:5.0) (.NET 5.0 development kit)

[registry.suse.com/suse/dotnet-sdk:3.1](http://registry.suse.com/suse/dotnet-sdk:3.1) (.NET 3.1 development kit)
