---
title: "Do Microservices Make SOA Irrelevant?"
date: 2017-05-09T11:12:00
slug: "do-microservices-make-soa-irrelevant"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["developer-experience"]
content_type: "opinion"
draft: false
migration:
  wp_id: 86820
  original_url: "https://www.suse.com/c/rancher_blog/do-microservices-make-soa-irrelevant/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Is service-oriented architecture, or SOA, dead? You may be tempted to

think so. But that’s not really true. Yes, SOA itself may have receded

into the shadows as newer ideas have come forth, yet the remnants of SOA

are still providing the fuel that is propelling the microservices market

forward. That’s because incorporating SOA principles into the design and

build-out of microservices is the best way to ensure that your product

or service offering is well positioned for the long term. In this sense,

understanding SOA is crucial for succeeding in the microservices world.

In this article, I’ll explain which SOA principles you should adopt when

designing a microservices app.

### Introduction

In today’s mobile-first development environment, where code is king, it

is easier than ever to build a service that has a RESTful interface,

connect it to a datastore and call it a day. If you want to go the extra

mile, piece together a few public software services (free or paid), and

you can have yourself a proper continuous delivery pipeline. Welcome to

the modern Web and your fully buzzworthy-compliant application

development process. In many ways, microservices are a direct descendant

of SOA, and a bit like the punk rock of the services world. No strict

rules, just some basic principles that loosely keep everyone on the same

page. And just like punk rock, microservices initially embraced a

do-it-yourself ethic, but has been evolving and picking up some

structure which moved microservices into the mainstream. It’s not just

the dot com or Web companies that use microservices anymore—all

companies are interested.

### Definitions

For the purposes of this discussion, the following are the definitions I

will be using.

**Microservices:** The implementation of a specific business function,

delivered as a separate deployable artifact, using queuing or a RESTful

(JSON) interface, which can be written in any language, and that

leverages a continuous delivery pipeline.

**SOA:** Component-based architecture which has the goal of driving

reuse across the technology portfolio within an organization. These

components need to be loosely coupled, and can be services or libraries

which are centrally governed and require an organization to use a single

technology stack to maximize reusability.

### Positive things about microservices-based development

As you can tell, microservices possess a couple of distinct features

that SOA lacked, and they are good:

**Allowing smaller, self-sufficient teams to own a product/service**

that supports a specific business function has drastically improved

business agility and IT responsiveness (to any directions that the

business units they support) want to take.

**Automated builds and testing**, while possible under SOA, are now

serious table stakes.

**Allowing teams to use the tools they want**, primarily around which

language and IDE to use.

**Using-agile based development with direct access to the business**.

Microservices and mobile development teams have successfully shown

businesses how technologists can adapt to and accept constant feedback.

Waterfall software delivery methods suffered from unnecessary overhead

and extended delivery dates as the business changed while the

development team was off creating products that often didn’t meet the

business’ needs by the time they were delivered. Even iterative

development methodologies like the Rational Unified Process (RUP) had

layers of abstraction between the business, product development, and the

developers doing the actual work.

**A universal understanding of the minimum granularity of a service.**

There are arguments around “Is adding a client a business function, or

is client management a business function?” So it isn’t perfect, but at

least both can be understood by the business side that actually runs the

business. You may not want to believe it, but technology is not the

entire business (for most of the world’s enterprises anyway). Back in

the days when SOA was the king on the hill, some services performed

nothing but a single database operation, and other services were adding

a client to the system, which led to nothing but confusion from business

when IT did not have a consistent answer.

### How can SOA help?

![](images/rancher_blog_Training.png) Want to learn more about

Docker, Kubernetes, and Rancher? Join us for free online

training After reading those definitions, you are probably

thinking, “Microservices sounds so much better.” You’re right. It is the

next evolution for a reason, except that it threw away a lot of the

lessons that were hard-learned in the SOA world. It gave up all the good

things SOA tried to accomplish because the IT vendors in the space

morphed everything to push more product. Enterprise integration patterns

(which define how new technologies or concepts are adopted by

enterprises) are a key place where microservices are leveraging the work

done by the SOA world. Everyone involved in the integration space can

benefit from these patterns, as they are concepts, and microservices are

a great technological way to implement them. Below, I’ve listed two

other areas where SOA principles are being applied inside the

microservices ecosystem to great success.

#### API Gateways (née ESB)

Microservices encourage point-to-point connections, and that each client

take care of their own translations for dates and other nuanced things.

This is just not sustainable as the number of microservices available

from most companies skyrockets. So in comes the concept of an Enterprise

Service Bus (ESB), which provides a means of communication between

different application in an SOA environment. SOA originally intended the

ESB to be used to carry things between service components—not to be

the hub and spoke of the entire enterprise, which is what vendors

pushed, and large companies bought into, and left such a bad taste in

people’s mouths. The successful products in the ESB have changed into

today’s API gateway vendors, which is a centralized way for a single

organization to manage endpoints they are presenting to the world, and

provide translation to older services (often SOA/SOAP) that haven’t been

touched in years but are vital to the business.

#### Overarching standards

SOA had WS-\* standards. They were heavy-handed, but guaranteed

interoperability (mostly). Having these standards in place, especially

the more common ones like WS-Security and WS-Federation, allowed

enterprises to call services used in their partner systems—in terms

that anyone could understand, though they were just a checklist.

Microservices have begun to formalize a set of standards and the vendors

that provide the services. The OAuth and OpenID authentication

frameworks are two great examples. As microservices mature, building

everything in-house is fun, fulfilling, and great for the ego, but

ultimately frustrating as it creates a lot of technical debt with code

that constantly needs to be massaged as new features are introduced. The

other side where standards are rapidly consolidating is API design and

descriptions. In the SOA world, there was one way. It was ugly and

barely readable by humans, but the Web service definition language

(WSDL), a standardized format for cataloguing network services, was

universal. As of April 2017, all major parties (including Google, IBM,

Microsoft, MuleSoft, and Salesforce.com) involved in providing tools to

build RESTful APIs are members of the OpenAPI Initiative. What was once

a fractured market with multiple standards (JSON API, WASL, RAML, and

Swagger) is now becoming a single way for everything to be described.

### Conclusion

SOA originated as a set of concepts, which are the same core concepts as

microservices architecture. Where SOA fell down was driving too much

governance and not enough “Just get it done.” For microservices to

continue to survive, the teams leveraging them need to embrace their

ancestry, continue to steal the best of the ideas, and reintroduce them

using agile development methodologies—with a healthy dose of

anti-governance to stop [SOA Governance](http://www.opengroup.org/soa/source-book/gov/p4.htm#X_Governed_SOA_Processes)

from reappearing. And then, there’s the side job of keeping ITIL and

friends safely inside the operational teams where they thrive. *Vince Power is a Solution Architect who has a focus on cloud adoption and technology implementations using open source-based technologies. He has extensive experience with core computing and networking (IaaS), identity and access management (IAM), application platforms (PaaS), and continuous delivery.*
