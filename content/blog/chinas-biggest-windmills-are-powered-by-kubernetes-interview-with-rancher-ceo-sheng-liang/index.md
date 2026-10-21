---
title: "China's biggest windmills are powered by Kubernetes: Interview with Rancher CEO Sheng Liang"
date: 2018-12-17T09:03:00
slug: "chinas-biggest-windmills-are-powered-by-kubernetes-interview-with-rancher-ceo-sheng-liang"
author: "Rancher Admin"
products: ["Company/community"]
tags: ["edge"]
content_type: "company-news"
draft: true
migration:
  wp_id: 85834
  original_url: "https://www.suse.com/c/rancher_blog/chinas-biggest-windmills-are-powered-by-kubernetes-interview-with-rancher-ceo-sheng-liang/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2018 KubeCon interview"
  redirect_target: "rancher.com/blog (hub)"
---

## Video Transcription

**Swapnil:** Hi, this is Swapnil Bhartiya, and we are here at KubeCon and CloudNativeCon in Shanghai, China, and today we have Sheng Leng from Rancher Labs.

**Sheng:** That’s right.

**Swapnil:** It’s nice to see you.

**Sheng:** Very nice to see you too.

**Swapnil:** It’s been a pleasure, because I’ve been chasing you for a while, so it’s good to be sitting down with you and talking again.

**Sheng:** Likewise.

**Swapnil:** Yeah. And you delivered a talk with Goldwind, which I think is one of the largest manufacturers of wind turbines in China.

**Sheng:** That’s right. They’re the largest in China, third largest in the world.

**Swapnil:** Excellent. Because when I think about wind turbines, I just think about machines. I don’t think about IT infrastructure, but I am aware that they may have a lot of sensors there, how they detect everything. So can you talk about what kind of IT infrastructure they have, because you’ve worked very closely with them.

**Sheng:** It turns out that one of the biggest problems they actually needed to solve was to gather all the sensor data they have with all the wind turbines, and then use that to forecast the status of the system. And also, especially, the situation with the weather, with the wind speed, because that has a very big impact on the power output, which impacts the grid stability.

So because of the large amount of power these power stations actually generate, it’s a very difficult problem. And it’s a [distributed edge computing](https://www.suse.com/c/distributed-edge-computing-unlocking-the-power-of-decentralized-networks-to-drive-innovation/) problem by nature, because even though the power companies, the headquarters are largely centralized, they actually function in many different states and provinces. And then inside each province, they actually have many different plants and a plant would have many different machines… So they basically have this three level IT structure. They have a central location, where the headquarters of one of the power utilities is, and then that utility would serve a number of provinces or states in China. And then each of the states, essentially, would have a second level data center that does a lot of data processing. And then finally, at each power plant, which could be built in fairly remote locations, there would be some edge computing nodes. And each edge computing nodes would manage a few to dozens, maybe up to 100 wind turbines.

**Swapnil:** In what capacity are they using … open-source technologies?

**Sheng:** They developed this whole technology pretty much in-house, built using open source technologies from the ground up. They use a lot of storage technologies. They use object storage technologies, they use sort of analytical big data storage technologies, like Hadoop-like technologies. And then they use AI technologies that they use to try to learn about the weather patterns, and predict the speed of the wind and direction of the wind. So it’s a fairly sophisticated system.

**Sheng:** So the challenge they have, really, was how to distribute this software stack to a number of locations, both their central location and the regional … the state and province level data centers, and especially all the way out to the edge locations. And there’s actually a lot of commonality, they have a common sort of AI big data platform. They actually distribute everywhere, and it’s microservice based. It’s built out of pretty much the same set of open source components that big data, and storage, and AI that I talked about. And then that’s why they used Kubernetes, so they have a unique challenge of actually running a multiple Kubernetes clusters.

We investigated potentially using one big Kubernetes cluster, because these locations are connected, but the bandwidth is not that high. And that bandwidth has to be primarily used to actually take in the sensor data itself. So there’s really not that much extra bandwidth available to run hundreds or thousands of kubelets across half of China, or half of a major big country. And they sell worldwide, right, and then collect the data.

**Sheng:** So I think in one particular deployment they talked about, in the talk, there’re actually over 600 Kubernetes clusters. Most of them exist in these edge locations, and they have to have a way to distribute and deploy these Kubernetes clusters. And then they have to have a way to manage these Kubernetes clusters.

**Sheng:** Rancher basically provided two pieces of technology, that was all part of Rancher product that solved their problem. One is, we have a Kubernetes distro, a Kubernetes installer. I mean, in principle, it’s not unlike many other Kubernetes installers. But I think we built it to be particularly easy to use, and particularly efficient. So it’s called Rancher Kubernetes Engine, and they find it very useful. So they use Rancher Kubernetes Engine to basically build these Kubernetes clusters, both in the central or regional data center, as well as on the edge.

**Sheng:** Then, the other aspect of Rancher that they finded useful was multi-cluster management. So Rancher provides a unified management plane across, really, any Kubernetes cluster, in theory. Other Rancher customers actually use Rancher to manage GKE clusters, or Huawei CCE clusters, as well as clusters they built themselves. But in this particular case, they just use Rancher to manage their Kubernetes clusters they built with RKE. And then they can pretty much write a script once, and through Rancher, it can kind of get all of their software updated. Then we’d be monitoring the health of these clusters, and also the applications running on top of these clusters. We’d be upgrading the clusters, as well as the applications running on top of these clusters. And so this is basically the challenge that they have, that Rancher solved.

**Swapnil:** So as you help Goldwind, what are the biggest challenges that you saw they were facing?

**Sheng:** They talked about it yesterday as well. It’s really quite fascinating. So there were technical challenges, and sort of not so technical challenges. A lot of the technical challenge was around the resource consumption of Kubernetes itself. So it turned out, we’re actually not able to completely use Kubernetes across all their edge nodes. Some of their edge nodes are fairly sizeable, so Kubernetes is okay. But some of the smaller ones, they only have 8 gigabytes of memory. And once you deploy even a single node Kubernetes there, it takes up half of the resource, so it’s a little too heavyweight. And we’re motivated by this, and by a bunch of other customers with similar requirements.

**Sheng:** At Rancher, we’ve actually embarked on an effort to try to dramatically slim down the weight of Kubernetes. Kubernetes is really nicely modularized code, so you can really remove a lot of stuff you don’t need without really impacting the rest. So I think this problem could be solved. We really want to push the envelope of how small Kubernetes can go. I know a lot of developers run Kubernetes like Minikube on a laptop, it doesn’t seem to take that much memory.

But the reality is, once you put on real workload, right, it actually increases the memory footprint quite a bit, even in a Minikube situation. So we’re going through a round of optimization, and I’m fairly optimistic. Working with the community, we can make progress in this direction.

**Sheng:** The challenge is, in this case we don’t really want to just run kubelet. If we could get away with just running kubelet on the edge, it would have taken a lot less memory footprint. But the problem is, then the whole system is just not as isolated, not as reliable. And because, like I said earlier, the networking is kind of really their bottleneck, and it’s not entirely reliable because it goes through telcodes and stuff. So they really wanted an independent Kubernetes cluster at the edge. So I would say this is one of the major technical challenges that they’re still working through, and we’re working with them.

**Sheng:** Then there are more organizational challenges. It comes from two directions. One direction is their internal operations team are actually struggling with Kubernetes quite a bit, even today. Especially, they say, some of the more experienced IT operations personnel just really struggle to learn some of these concepts, because a lot of these guys are not really DevOps engineers, by traditional definition. They’re more just IT admins, and they’re more comfortable with virtual machines, or physical machines, or networking, and this is just all new. It’s a little overwhelming.

**Sheng:** And another thing is, I think, this whole technology is not quite completely built up. So some of the complexities of the infrastructure in Kubernetes is actually exposed to some of the AI data scientists, and they don’t quite like some of the worries that they now have to pay toward the infrastructure. So we basically need to do more work to really abstract some of the Kubernetes complexity away, so data scientists and AI engineers would feel more comfortable with it.

**Swapnil:** You rightly said, “These are some of the smartest people, and they’ll be solving this problem, and they’ll keep making Kubernetes better and better.” So thank you again, for talking to me today, and as usual, I look forward to meeting you again. Thank you so much.

**Sheng:** Thank you very much.
