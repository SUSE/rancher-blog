---
title: "The No. 1 Rule of Disaster Recovery"
date: 2020-08-07T09:55:00
slug: "the-no-1-rule-of-disaster-recovery"
author: "Mikhail Kozorovitskiy"
image: "images/rancher_blog_disaster-recovery-featured.png"
products: ["Kubernetes (generic)"]
tags: ["backup"]
content_type: "opinion"
draft: false
migration:
  wp_id: 86267
  original_url: "https://www.suse.com/c/rancher_blog/the-no-1-rule-of-disaster-recovery/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Let’s imagine you are running a hosting shop with highly visible production applications. Your team has backups, and you have a disaster recovery (DR) policy. You think you are ready to handle any real-world scenario in addition to checking all your compliance boxes. Your third-party backup tools are creating backups, and your implemented solutions have a brochure indicating restore capability.

## So, You Think You’re Ready for a Disaster?

A year later, your primary data center or hosting cloud goes out; the city is underwater; someone forgot to refill the generator. It’s time to execute your pre-prepared disaster recovery strategy, and it feels good to be prepared. You pull out the policy, which states to take backups and use the restore feature in your infrastructure to recover at a new location.

All of a sudden, your mind explodes.

- Who knows how to do that?
- Have we done this before?
- When was the last time we tested this?

Eventually, the right people get online. They follow the documentation to retrieve the backups, which may not be in the right place. They follow the orchestration platform’s instructions, which may not be completely useful for your use case. Finally, everything gets deployed and spun up. Then – you guessed it – it doesn’t work. One of the myriads of things that can go wrong in a disaster recovery scenario does (you are in a *disaster* after all). In my work in the professional services team here at Rancher, this is usually when a team realizes they forgot to follow the number one rule of disaster recovery.

## What Disaster Preparedness Looks Like

Let’s imagine another scenario. Your data center goes down, and automated alerts trigger a rebuild in your DR designated data centers. You go to your plan of reference. Your plan or policy contains the names of people who are responsible and capable of handling the restoration. Still, even if one is missing, each step in the process is documented either with actual automation code or detailed manual instructions. More so, those team members have already been alerted and are collaborating in chat. The backups that you must use and configuration and state files were automatically copied on regular bases to your backup datacenter. Your configuration data spun up your new infrastructure, the data backups – that are regularly tested – attach and your team follows the detailed documentation to flip DNS over to your new data center and restore service. All of this happened because we followed the number one rule in disaster recovery.

## And Now, the Big Reveal

The number one rule of disaster recovery is that having an untested plan is like having no plan.

No matter how redundant your storage says it is, no matter what any third party claims their system can do, without testing, executing disaster recovery in a real scenario will be difficult at best. The added adrenaline of the situation can add to an already stressful situation that practice and the process can help mitigate. You can always get better and faster at disaster recovery, and working toward the scenario above can decrease your time and quality of service restoration. By validating your backups and process, you will at least know how and when you will get to recovery and be able to get there, as you have repeatedly in your testing.

A good rule of thumb is if a new team member can perform a DR from your process manuals, you are in a great place. Automation of testing of both the backups and the restoration can help decrease the effort required to test continually. Still, teams do need to take active participation to keep their skills fresh. Good luck, and I hope this advice never comes to use!

If you are looking for a place to start, check out our master class on Disaster Recovery Strategies for Kubernetes.
