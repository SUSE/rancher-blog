---
title: "Focus on Services, Not on Containers"
date: 2017-06-07T10:18:00
slug: "focus-on-services-not-on-containers"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["developer-experience"]
content_type: "opinion"
draft: false
migration:
  wp_id: 86664
  original_url: "https://www.suse.com/c/rancher_blog/focus-on-services-not-on-containers/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Containers may be super cool, but at the end of the day, they’re just
another kind of infrastructure. A seasoned developer is probably already
familiar with several other kinds of infrastructure and approaches to
deploying applications. Another is not really that big of a deal.
However, when the infrastructure creates new possibilities with the way
an application is architected—as containers do—that’s a huge
deal. That is why the services in a microservice application are far
more important than the containerized infrastructure they run on.
Modularity has always been a goal of application architectures, and now
that the concept of microservices is possible, how you build those
services end up dictating where they run and how they are deployed.
Services are where application functionality meets the user, and where
the value your application can provide is realized. That’s why if you
want to make the most of containers, you should be thinking about more
than just containers. You have to focus on services, because they’re the
really cool thing that containers enable.

### Services v. Containers

For conversation’s sake, using services and containers interchangeably
is fine—because the ideal use case for a containerized application is
one that is deconstructed into services, where each service is deployed
as a container (or containers). However, the tactics cannot be
synonymous. Services are an implied infrastructure, but more
importantly, an application architecture. When you talk about a service
that is part of your application, that service is persistent. You can’t
suddenly have an application without a login page or a shopping cart,
for example, and expect things to go well. Containers, on the other
hand, are designed to live and die in very short time frames. Ideally,
with every deployment or revert, the container is killed as soon as the
new deployment is live and the traffic is routed to it. So containers
are not persistent. And if the delivery chain is working correctly, that
should not matter at all. Microservices, as both an application and an
infrastructure term, does have some unique elements associated with it,
which diverge the relationship even further.

1. A single service can be deployed in multiple regions.
2. Each region could have multiple versions—for example, for A/B
   testing or canary releases.
3. Each service might have different lifecycles. Services tied
   specifically to the backend may be deployed less frequently than
   front-end services.

It doesn’t even necessarily mean that one service = one container, or
one host. The service is the logical abstraction of functionality from
your application, and not directly correlated to any infrastructure.

### What does it mean to be service-focused?

Focusing on your services means that developers do not spend time
optimizing or tinkering with container orchestration or configuration.
If a gold master image is ready to go, an EDGAR vessel for code, then
the developer should only be concerned about committing their code to
it. If the developer is thinking about containers, then something is
broken. Where the developer will need to think about containers is their
development environment. A parity between their development environment
and production is important. Making sure developers are testing on the
right Docker image and have access to the other services and shift-left
quality assurance (QA) are the only way to mitigate the “worked on my
machine” issue. This is accomplished by leveraging strong container
registries. However, even the development environment should be
cookie-cutter, with minimal consideration.

### How to accomplish a service-centric workflow

I wish I could say that being service-focused was an individual
developer task. It’s not. The developer already wants to be
hyper-focused on the functionality they are building, and if and when
they get distracted by containers and their orchestration, it’s because
they are nerds and want to tinker, not because they feel it’s their core
responsibility. Maintaining a service focus is the responsibility of the
entire team. It includes how the delivery chain is architected—not
only to be fast, but to avoid the broader team’s need to interact with
it. So service focus starts from management and trickles down to the
delivery chain, or DevOps, to tooling, and the developer is either
finally left holding the infrastructure bag, or is free to work. Here
are the three key tenets of service focus:

- **Standardize development environments.** You do this by finding a
  robust container registry, vetting images, and standardizing the
  tooling that developers have in their boxes. Because services are
  developed independently, one of the challenges is seeing new
  functionality in a service with the application at large. So
  on-demand integration environments that developers can deploy per
  commit are extremely useful.
- **Be immutable, don’t just say you are.** To even think about being
  service-focused, you have to practice immutable infrastructure, not
  just talk about it. This means no changes to containers after they
  are deployed. Your option is run or delete. That’s it. Snowflake
  images or configurations are strictly forbidden, and there is no
  real reason to give access to individual containers beyond the
  functionality required by the service itself.
- **Create visibility.** Service-based applications do have many times
  the moving parts of a monolithic application. This means that
  creating visibility and providing access to it for all relevant
  stakeholders is critical. Visibility should support infrastructure
  and application visibility as well. The team should be able to see
  the entire application and all the services in it, with inspection
  of individual containers. For the development team, application
  visibility is most important.

DevOps teams also need to do whatever they can to minimize the impact of
things like networking and security, as these can be huge hurdles. The
objective would be to offload as much as possible to orchestration
tools. The service obsession goal is to avoid distractions, and focus on
service functionality. If developers focus on building a great product,
and DevOps focuses on building the best delivery chain, then the
toolchain and processes will fall into place to support that—which,
today, means containers and great orchestration. The outcome of better
quality applications in the user’s hands, sooner rather than later, is
what impacts your company’s bottom line. The mechanism to get there is
not as critical. So the next time you talk about containers, consider
turning the focus to how you can build better services. *Chris Riley
([@HoardingInfo](https://twitter.com/hoardinginfo)) is a technologist
who has spent 12 years helping organizations transition from traditional
development practices to a modern set of culture, processes and tooling.
In addition to being a research analyst, he is an O’Reilly author,
regular speaker, and subject matter expert in the areas of DevOps
strategy and culture. Chris believes the biggest challenges faced in the
tech market are not tools, but rather people and planning.*
