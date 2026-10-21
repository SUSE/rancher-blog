---
title: "Welcome to the Era of Immutable Infrastructure"
date: 2017-12-19T11:30:00
slug: "welcome-to-the-era-of-immutable-infrastructure"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["developer-experience"]
content_type: "opinion"
draft: false
migration:
  wp_id: 87284
  original_url: "https://www.suse.com/c/rancher_blog/welcome-to-the-era-of-immutable-infrastructure/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

With the recent “container revolution,” a seemingly new idea became

popular: immutable infrastructure. In fact, it wasn’t particularly new,

nor did it specifically require containers. However, it was through

containers that it became more practical, understandable, and got the

attention of many in the industry. So, what is immutable

infrastructure? I’ll attempt to define it as the practice of making

infrastructure changes only in production by replacing components

instead of modifying them. More specifically, it means once we deploy a

component, we don’t modify (mutate) it. This doesn’t mean the component

(once deployed) is without any change in state; otherwise, it wouldn’t

be a very functional software component. But, it does mean that as the

operator we don’t introduce any change outside of the program’s

original API/design. Take for example this not too uncommon scenario.

Say our application uses a configuration file that we want to change.

In

the dynamic infrastructure world, we might have used some scripting or a

configuration management tool to make this change. It would make a

network call to the server in question (or more likely many of them),

and execute some code to modify the file. It might also have some way of

knowing about the dependencies of that file that might need to be

altered as a result of this change (say a program needing a restart).

These relationships could become complex over time, which is why many CM

tools came up with a resource dependency model that helps to manage

them. The trade-offs between the two approaches are pretty simple.

Dynamic infrastructure is a lot more efficient with resources such as

network and disk IO. Because of this efficiency, it’s traditionally

faster than immutable because it doesn’t require pushing as many bits

or storing as many versions of a component. Back to our example of

changing a file. You could traditionally change a single file much

faster than you could replace the entire server. Immutable

infrastructure, on the other hand, offers stronger guarantees about the

outcome. Immutable components can be prebuilt before deploy, and build

once and then reused, unlike dynamic infrastructure which has logic that

needs to be evaluated in each instance. This leaves opportunity for

surprises about the outcome, as some of your environment might be in a

different state that you expect, causing errors in your deployment.

It’s also possible that you simply make a mistake in your configuration

management code, but you aren’t able to sufficiently replicate

production locally to test that outcome and catch the mistake. After

all, these configuration management languages themselves are complex. In

an [article from *ACM Queue*](http://queue.acm.org/detail.cfm?id=2898444), an Association for

Computing Machinery (ACM) magazine, engineers at Google articulated this

challenge well:
> “The result is the kind of inscrutable ‘configuration is code’ that  
> people were trying to avoid by eliminating hard-coded parameters in  
> the application’s source code. It doesn’t reduce operational  
> complexity or make the configurations easier to debug or change; it  
> just moves the computations from a real programming language to a  
> domain-specific one, which typically has weaker development tools  
> (e.g., debuggers, unit test frameworks, etc).”

Trade-offs of efficiency have long been central to computer engineering.

However, the economics (both technological and financial) of these

decisions change over time. In the early days of programming, for

instance, developers were taught to use short variable names to save a

few bytes of precious memory at the expense of readability. Dynamic

linking libraries were developed to solve the space limitation of early

hard disk drives so that programs could share common C libraries instead

of each requiring their own copies. Both these things changed in the

last decade due to changes in the power of computer systems where now a

developer’s time is far more expensive than the bytes we save from

shortening our variables. New languages like Golang and Rust have even

brought back the statically compiled binary because it’s not worth the

headache of dealing with platform compatibility because of the wrong

DLL. Infrastructure management is at a similar crossroad. Not only has

the public cloud and virtualization made replacing a server (virtual

machine) orders of magnitude faster, but tools like Docker have created

easy to use tooling to work with pre-built server runtimes and efficient

resource usage with layer caching and compression. These features have

made immutable infrastructure practical because they are so lightweight

and frictionless. Kuberentes arrived on the scene not long after Docker

and took the torch further towards this goal, creating an API of “cloud

native” primitives that assume and encourage an immutable philosophy.

For instance, the ReplicaSet assumes that at any time in the lifecycle

of our application we can (and might need to) redeploy our application.

And, to balance this out, Pod Disruption Budgets tell Kubernetes how the

application will tolerate being redeployed. This confluence of

advancement has brought us to the era of immutable infrastructure. And

it’s only going to increase as more companies participate. [Today’s tools](https://rancher.com/quick-start/) have made it easier than ever to

embrace these patterns. So, what are you waiting for?

### About the Author

![](images/rancher_blog_wjimenez-photo-300x300.jpeg)William Jimenez

is a curious solutions architect at Rancher Labs in Cupertino, CA, who

enjoys solving problems with computers, software, and just about any

complex system he can get his hands on. He enjoys helping others make

sense of difficult problems. In his free time, he likes to tinker with

amateur radio, cycle on the open road, and spend time with his family

(so they don’t think he forgot about them).
