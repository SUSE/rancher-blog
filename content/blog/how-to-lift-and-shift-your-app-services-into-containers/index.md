---
title: "How to Lift and Shift Your App Services into Containers"
date: 2017-10-02T11:11:00
slug: "how-to-lift-and-shift-your-app-services-into-containers"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["developer-experience"]
content_type: "explainer"
draft: false
migration:
  wp_id: 86792
  original_url: "https://www.suse.com/c/rancher_blog/how-to-lift-and-shift-your-app-services-into-containers/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Ready to make the big move to containers? If you’re thinking of moving
services from an existing, non-containerized system to a container-based
environment, you’re probably wondering how to do it. Is there a right
way? Is there a best way? Is there even a single lift-and-shift process
that can be applied to all applications? The answer to those questions
is—in general, yes. While the specifics of a migration to containers
and microservices will vary from organization to organization, there are
general principles and best practices that you should follow to achieve
a seamless lift-and-shift of your apps from legacy infrastructure to a
containerized environment. This post outlines guidelines for
successfully lifting and shifting your application into containers.

## Microservices—What Are They?

When you’re at the initial planning stage of such a move, the single
most important thing to keep in mind about containerization is that
container-system architecture is (or should be) based on microservices.
What is a microservice architecture? The actual criteria for determining what is and
what isn’t a microservice are somewhat imprecise, and necessarily so,
because different methods of designing a container-based application
(we’ll get to those in a bit) are based on somewhat different methods
of defining microservices. In general, though, a microservice can be
described as a basic, functionally discrete service used by other parts
of an application. A service that retrieves data from a database could
be a microservice, as could one that sends data to a storage device, or
that handles user input. In an online store, for example, access to the
inventory database could be handled by one microservice, the customer
shopping cart could be updated by another microservice, and transactions
could be handled by yet another microservice, while a separate
microservice takes care of credit card authorization. But the same store
could be broken down into a different set of microservices, with one
microservice handling all database access (inventory, customer, and
sales), and another handling both the shopping cart and sales
transactions, while a third microservice takes care of shipping.
Specific microservice structure is, to quite a degree, a design choice,
based on the overall architecture chosen for the system.

## What Is Your Current Architecture?

Before you start laying out the architecture of your containerized
application, however, it is important to take a look at your current
architecture. Starting at the largest scale, non-container applications
can generally be broken down into two groups: monolithic and
service-oriented. They each require a somewhat different approach to
refactoring for containers, so we’ll start by looking at them
separately, then discuss design choices and overall refactoring
strategies.

### Monolithic Applications

Most traditionally designed programs are monolithic. They may be made up
of a single program, with supporting libraries, services, and
configuration files, or a handful of programs with supporting resources.
In both cases, however, most or all of the core functionality is
contained in one or a few binary files, with the services making up that
functionality operating and communicating with each other within the
application boundaries defined by those binaries. Desktop applications
have traditionally been monolithic, as have most network-based
applications. In a desktop or local area network environment, monolithic
architecture generally makes good sense. It’s usually fairly easy to
install and update, the monolithic design makes it easy to keep track of
the components, and desktop/LAN use generally doesn’t put too much
strain on the application’s resources. In a cloud- or Internet-based
environment, however, monolithic applications can be large, clumsy,
slow, difficult to update, and inadequate for handling large volumes of
traffic. They are also unsuitable for continuous delivery, and for most
of the practices that make up DevOps. Refactoring a monolithic
application for containers can require a wholesale redesign at the
conceptual level. Even if the application’s architecture defines its
internal services in a reasonably clear and discrete manner, the actual
breakdown into microservices is likely to require significant changes to
the boundaries of those services, and the ways in which they communicate
with each other. For most monolithic applications, it will require many
of the services to be completely redefined, or to be defined from
scratch.

### Service-Oriented Applications

It is also possible for a large, non-container application to already
have a service-based architecture. A point-of-sale application, for
example, might consist of separate programs to handle sales, inventory,
customer records, ordering, shipping, variances, taxes, accounts
receivable, and accounts payable. Since each module is a separate
program, it has a clearly defined application boundary, with
communication between modules crossing that boundary, very much like a
container-based application. This architecture (assuming that it is
satisfactory) can serve as the basis for any further breakdown into
microservices, if such a breakdown is necessary. Further breakdown could
be based on the existing modules into smaller services, on abstracting
generalized services (such as a single database-access or
receipt-printing microservice), or on both. On the other hand, if the
existing modules are already small, discrete in function, and
well-organized, it might be sufficient to place them into containers
with a minimum of modification.
![](images/rancher_blog_container-2568196_1920-1024x683.jpg)

## What Do You Do With a Monolith?

It should be clear at this point, then, that breaking down a monolithic
application into microservices is generally a much more complex and
challenging task. As indicated above, the first step is to redefine the
architecture in terms of microservices, This redefinition, along with
the actual breakdown into the microservices themselves, is often
referred to as decomposition. There are some basic patterns for
decomposition; in many ways, which pattern you choose is less important
than understanding the basis and fundamental nature of the pattern. In
practice, decomposition of a monolithic application into microservices
frequently involves more than one pattern, depending on the functional
requirements of the system.

### Use Case

A use case is a set of actions that a user would generally take when
carrying out a task. A user can be an actual human being, another part
of the application, or an outside application. The key element of a use
case is that it is a definable set of actions associated with a task. In
the online store example, a set of customer actions, such as selecting
and purchasing items, could be a use case, as could a purely internal
action, such as updating the inventory, customer, and transaction
databases after a sale.

### Function

Breakdown by functions is another common pattern of decomposition. A
sales transaction could be defined as one functional unit, for example,
with credit authorization as another functionally defined service. You
could define functional domains based on such things as variance
tracking, shipping, and automatic restocking. Functional decomposition
is very similar to use cases, but it is defined more by the actions
being performed than by the actors.

### Resources

There are many situations where it is best to define specific
microservices in terms of resources. You could, for example, define a
single microservice for handling all interactions with a specific
database or set of databases, or all interactions with persistent
storage. In many ways, device drivers are resource-based microservices;
if it makes sense to interact with a resource by means of a
general-purpose service resembling a device driver, it probably makes
sense to define it as a separate microservice.

## The Breakdown Path

Once you’ve settled on an overall pattern for decomposing your
monolithic application, you can start the process of breaking it down
into microservices. Ultimately, your goal should be to reduce the entire
application to a set of microservice-level containers which can be
managed and deployed as needed to provide the same set of services (with
any required additions or enhancements) as your original monolithic
application, only with greater speed, traffic volume, and flexibility.
The good news is that you don’t need to break it down all at once.
Large-scale service-oriented architecture of the type described above
can serve as an intermediary stage. You can initially break your
monolithic application into large service-based chunks, then break those
down into smaller services, and smaller services after that, until you
finally reach your target level of microservices. Or, as an alternative,
you could start by separating out clearly definable services and
breaking those down into container-based microservices, then breaking
down the remaining parts of the application in a similar manner, a few
at a time. Whichever approach you take, the key points to keep in mind
are that your microservices should be clearly defined, and that those
definitions should make sense in terms of your application’s overall
function and architecture. As long as you follow those principles, your
lift-and-shift effort should be successful.
