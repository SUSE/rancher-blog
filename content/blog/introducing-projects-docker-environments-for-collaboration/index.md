---
title: "Introducing Projects: Docker Environments for Collaboration"
date: 2015-03-02T11:14:00
slug: "introducing-projects-docker-environments-for-collaboration"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["developer-experience"]
content_type: "release"
draft: true
migration:
  wp_id: 86889
  original_url: "https://www.suse.com/c/rancher_blog/introducing-projects-docker-environments-for-collaboration/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 0.9 projects feature, 1.x era"
  redirect_target: "rancher.com/blog (hub)"
---

In last week’s 0.9 release we added support in Rancher for users to
create new deployment environments that can be shared with colleagues.
These docker environments are called projects, and are an extension of the
GitHub OAuth integration we added to Rancher last month. The focus of
projects is to allow teams to collaborate on Docker environments, and
since our user management is connected with GitHub today, we leverage
standard GitHub abstractions, such as users, teams and organizations, to
support Rancher Projects.

(If you haven’t read my earlier post on
[GitHub OAuth on Rancher](http://sidharthamani.github.io/rancher-stuff/2015/02/02/rancher-github_integration.html),
I would recommend you to read it as it provides an introduction to
Rancher authentication using GitHub.)

## Projects demo

This demo will show you how to create projects on Rancher for various
levels of access control.

## The project use case

One of the most obvious use cases for this new feature is to
control access to environments and resources within an organization.
For example, a common request from users is to have development teams
and production teams own their own environments and resources. With
projects, access to production environments can be shared among an
approved group, and restricted from unauthorized users. At the same
time, developers can have unfettered access to development environments,
and can collaborate on testing, confident it will not be accessed by
anyone else. Every project is a fully isolated environment for managing
resources and deploying containers. Anyone who has access to a project
can register new computing resources (virtual machines or physical
servers) and deploy containers, configure networking, and consume all of
the other capabilities of Rancher. Rancher supports three kinds of
projects

1. User Projects
2. Team projects
3. Org projects

### User projects

User projects allow resources to be orchestrated by an individual user.
They are meant to be used when a single user is the sole manager of the
resources. Users can create multiple projects for different environments
they are working on. One of the caveats of this type of project is
that, users can create “user-level” projects only for themselves.

### Team projects

Team projects allow users to allocate resources and provide access to a
team of people. Team projects are ideal for collaborating with a
predefined GitHub group. In the use case above, an organization could
create separate team projects for the dev and operations teams.
Giving both teams the ability to access their own resources.

### Org projects

Organization level projects allocate resources and provides access to
all members of the organization. For example, if you wanted to create a
resource called demo, that everyone in your organization could
orchestrate, this type of project would be the ideal choice. I hope this
project feature will be useful to you and your team. If you’d like to
get more information on using Rancher, or see it in action, please
don’t hesitate to schedule a demo.

###
