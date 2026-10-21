---
title: "The Story of the First Kubernetes Critical CVE"
date: 2018-12-04T09:03:00
slug: "the-story-of-the-first-kubernetes-critical-cve"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["security"]
content_type: "opinion"
draft: false
migration:
  wp_id: 85832
  original_url: "https://www.suse.com/c/rancher_blog/the-story-of-the-first-kubernetes-critical-cve/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

[CVE CVE-2018-1002105](https://github.com/kubernetes/kubernetes/issues/71411) was just announced in Kubernetes. I discovered this issue in early November, but the bug actually goes back a couple years and is a pretty interesting story and technical issue. Since this is the first critical CVE for Kubernetes, it is getting a lot of attention, but I don’t think it’s as bad as most people think. In fact, I think quite the opposite: this CVE shows how strong the community is and how well run it is.

## Issues with Amazon ALB

This all started back in 2016 when we released Rancher 1.6. Mid-2016 Amazon released ALB, which was a new HTTP (layer 7) load balancer. The setup of ALB was much easier than ELB, so in Rancher 1.2 we told users to use ALB. Fairly quickly we started getting reports that setups behind ALB were failing and a lot of random requests would just get 401, 403, 404, 503. We could never reproduce the issue ourselves and all the logs we got from community members made no sense. We were seeing HTTP requests and responses that we couldn’t correlate to code. Quite stupidly we just assumed ALB was new and probably had bugs. We never had issues with any other load balancer, just ALB. We ended up telling users to just not use ALB.

Fast forward to August this year, and a community member filed the same issue against Rancher 2.1 (https://github.com/rancher/rancher/issues/14931). Again, using ALB was resulting in odd 401 and 403 errors. This spiked my interest because Rancher 1.x and 2.x have no common code between them, and ALB should be fairly mature now. After some digging around, I found the issue had to do with not handling non-101 responses and reverse proxies caching TCP connections. In order to understand this issue, you have to understand TCP connection reuse, how websockets use TCP connections, and HTTP reverse proxies.

## TCP Connection Reuse

In a very naive approach to HTTP, a client would open a TCP socket, send a HTTP request, read the HTTP response, and then close the TCP socket. Quite quickly you’ll find that you spend too much time opening and closing TCP connections. As such the HTTP protocol has mechanisms built-in so that clients can reuse TCP connections across requests.

## Websockets

Websockets are a bidirectional communication that works differently from the HTTP request/response flow. In order to use websockets a client first sends a HTTP Upgrade request, the server responses with a HTTP 101 Switch Protocols response. After the 101 is received, the TCP connection is now dedicated to the websocket. It is assumed for the rest of the life of the TCP connection that it is dedicated to that websocket connection. That means this TCP connection will never be reused.

## HTTP Reverse Proxy

A HTTP reverse proxy (a load balancer is a type of reverse proxy) takes requests from a client and then sends them to a different server. For a standard HTTP request it just writes the request, reads the response, and then sends the response to the client. It’s fairly straight forward and Go includes a built in reverse proxy https://golang.org/pkg/net/http/httputil/#ReverseProxy. Websockets are a bit harder. For a websocket you have to look at the request, see that it is a upgrade request, send the request, read the 101 response and then hijack the TCP connections and just start copying bytes back and forth. For the reverse proxy, it does not look at the contents of the connection after that, it just creates a “dumb pipe”. This logic does not exist in a standard Go library and many open source projects have written code to do this.

## The Bug

The TL;DR is that Kubernetes did not check for 101 response before starting the “dumb pipe.” In the defense of the code, this is very common to not check for 101. This is actually why Rancher 1.x and Rancher 2.0 had the same issue even though it uses completed different code. A broken scenario is as follows.

1. Client sends websocket upgrade request
2. Reverse proxy send upgrade request to backend server
3. Backend server responds with 404
4. Reverse proxy starts copy loop and writes 404 to client
5. Client sees 404 response and adds TCP connection to “free connection pool”

In this scenario, if the client reuses the TCP connection it will write a request to the TCP connection and it will go through the “dumb pipe” in the reverse proxy and send it to the previous backend. Normally this wouldn’t be terrible, for example in the case of a load balancer, because all requests go to the same homogeneous set of backends. The issue occurs when the reverse proxy is intelligent and performs authentication, authorization, and routing (all of which Kubernetes does).

## The Security Flaw

Because the 101 is not handled, the client ends up with a TCP connection that is “dumb pipe” to some previously accessed backend service. This leads to a privilege escalation. The issue is that Kubernetes will perform authorization only in the reverse proxy for many requests. This means if I do an authorized failed websocket request that routes to a kubelet, I can hold a persistent connection to that kubelet and then run any API command I chose whether or not I’m authorized to it. For example you can run exec on any pod and copy out the secrets. So in this scenario, an already authorized users can basically get full API access to kubelet (same thing applies with services running through the kube-aggregation).

Another issue arises when you add yet another reverse proxy. In this situation you put a HTTP Load Balancer in front of Kubernetes API (not a layer 4 load balancer). If you do this then the authenticated TCP connection that has the “dumb pipe” running will be added to a free pool that any user can get ahold of. So user A creates the TCP connection and then user B reuses the connection. In this situation, non-authenticated users can get access to your cluster.

At this point you might be panicking, because of course everybody puts a load balancer in front of kube-apiserver. Well…. First, you have to be running a HTTP load balancer, not a TCP load balancer. The load balancer must understand HTTP semantics to produce this issue. Second, luckily most reverse proxies don’t care about 101 responses. This is why this issue has gone on so long (in actually a lot of open source projects) not detected. Most load balancers will not reuse a TCP connection after it sees the Upgrade request, not the 101 response. So the interesting thing is that if you are vulnerable to this issue, your Kubernetes setup should already be unreliable, and you should be seeing random failing or hung requests. I know ALB works this way, so don’t use ALB until you patch Kubernetes.

In short, this issue can allow any authenticated users with the right privileges to get more privileges. If you are running a hard multi-tenant cluster (untrusted users) you should be concerned. If you aren’t concerned about your users actively attacking each other (most multi-tenant clusters are like this), then don’t panic and just upgrade. If the conditions are just right an unauthenticated users could get in to your cluster. Good chance your load balancer prevents this, but just don’t expose the API to the world, put some proper ACLs on it and you most likely should be good.

## Thanks to Open Source

I wanted to point out that this CVE was discovered, fixed, and delivered all by the open source community. It is a testament to how well Kubernetes is ran. I first found this issue because of non-paying open source users of Rancher. In fact, we already knew the reported issue did not impact our customers of Rancher 2.0 because our HA architecture happens to negate the behavior of ALB. We fixed this just because we love our open source users. Only while fixing this bug did we discover it had security implications. I filed the issue to the Kubernetes community through their established security disclosure process and very quickly the issue was properly patched upstream and backported to 1.10, 1.11, 1.12, and 1.13.

Take comfort knowing that users of Kubernetes are in good hands. Don’t panic, just upgrade your clusters and carry on.
