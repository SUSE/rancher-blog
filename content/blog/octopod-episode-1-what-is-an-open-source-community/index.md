---
title: "Octopod Episode 1: What is an Open Source Community?"
date: 2021-08-01T20:45:31
slug: "octopod-episode-1-what-is-an-open-source-community"
author: ""
image: "images/oktopod-featured.jpeg"
products: ["Company/community"]
tags: ["developer-experience"]
content_type: "community"
draft: true
migration:
  wp_id: 87654
  original_url: "https://www.suse.com/c/rancher_blog/octopod-episode-1-what-is-an-open-source-community/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Podcast episode from 2021"
  redirect_target: "rancher.com/blog (hub)"
---

[In Episode 1 of the OCTOpod](https://episodes.buzzsprout.com/x3fb1kpqf50yl06v52ww8x2543dp?), Alan Clark talks with Thierry Carrez about open source communities: what they are, how they work and how you can get involved.

Trying to define what an open source community is might sound like a simple task, but it is a layered, nuanced collective with many moving parts. Thierry has been in the open source community for years and is currently the VP of engineering at the Open Infrastructure Foundation. In this episode, Thierry sheds light on some of the key traits that characterize open source communities. We hear about the importance of governance, principles, scope and documentation and find out how everyone, even those who do not code, can contribute. As Thierry notes, it is not about your technical ability, but rather about adding value where you can and being an engaged member of a community. Building a sustainable community requires effort, but that transparency and collaboration make it a worthwhile endeavor.
> “It’s really not about code, it’s really not about being a technical rock star. It is really more about being useful to others.”

*Listen to the OCTOpod [here](https://www.buzzsprout.com/1819621/8899551.mp3) or subscribe on your favorite podcast platform! And please share it with your friends!*

![Image 01](https://rancher.com/img/blog/2021/oktopod/image-01.jpeg)

Here’s the full transcript:

### EPISODE 01

[INTRODUCTION]

**AC:** I am Alan Clark. I have spent my career in enterprise software with the focus on open source advocacy and emerging tech. These days, I’m a member of the SUSE Office of the CTO, that is OCTO for short. Welcome to our new podcast series, The OCTOPod.

Season one is all about open source. I love being part of open-source communities. I’ve contributed in many ways, from code to chairs, for networking, to cloud. This includes serving as chairman of the board for the Open Infrastructure Foundation, the Linux foundation board of directors, Open SUSE chair, open mainframe project board and many more. I’ve met so many great people along the way.

In season one, I’ll sit down with a few of these experts. We’ll talk about the latest trends and challenges in open source, including findings from our latest report on why IT leaders choose open. We’ll talk about how to manage a community, the importance of diversity and inclusion in open source and much more.

Join me on your favorite podcast platform or at community.suse.com.

[INTERVIEW]

**AC:** Hello everyone, welcome to the OCTOPod. Today, I’m excited to sit down with Thierry Carrez, someone that I’ve known in the open source community for many years. We’ve worked together for a long time. He is currently the VP of engineering at the Open Infrastructure Foundation.

Thanks for being here today, Thierry. We want to get started here with some questions and we want to talk a little bit about just the basics of open source and open source communities, how they get started, what they’re like and so forth. Just to get people a flavor of how they kind of operate. Let’s start with the real basic question. What exactly is an open source community and what is it not?

**TC:** Thank you Alan, it’s great to be here. It sounds like a basic question but it’s actually a complex question. An open source community at the very bottom is all the people who contributes to an open source project but obviously, that just kicks the can down the road and now the question is, what is a contribution?

The traditional sense, the contribution to an open source project would be code and code patches but that quickly extended to non-code activities like documentation or user experience studies or walking on the continuous integration for the project and that’s as a result of more using it for tracking everything, not just code but also documentation and other types of documents and infrastructures to us code and those things but sharing your experience is also a form of contribution.

In the end, the community extends to all the users who publicly engage and share their experience and so in the end, the community is all the people who actively engage with the open source project and help it.

Obviously, that definition is working well for open leader block projects where anyone can engage with the project, it works less well for single vendor or open source where the makers are more separated from the consumers and in that case, they call community like more their extended circle of users and conference attendees so it’s not exactly the same meaning as what we call community in a more openly developed project.

**AC:** That’s a good points. I want to come back to that one because I think that’s a very good point and want to delve into that a little bit but let’s start at a different angle a little bit here. What is it that you see that brings people to participate in this communities? As you mentioned, there’s a lot of different types of contributions which means, we have a lot of different types of backgrounds and experience and interest. What is it that brings people to come and participate in a community?

**TC:** I would say they are like two categories of things. There is more classic altruistic motivation like giving back to the project that you’re using or participating in cultivating the commons for resource that you are benefiting from but more and more, we are seeing business sense in the form of shared innovation like a multiple organizations, putting resources together so that they don’t waste energy or inventing the wheel separately, that’s what we saw with the open stack project.

A number of organizations coming together because walking on the same body of code and software in common was better than walking on it separately. For any type of complex technology, if you can join a group of experts having the same kind of issues, you learn a lot from it so that makes complete business sense to engage with the community when you’re tackling a complex problem or seeing it for example, with the large scale [SIG 0:05:21.2] within open stack where several operators of large scale clouds get together to share their experiences, obviously, the project benefits from it because we learn from their experience but they also learn from one another and they see benefit in sharing their experience in that group.

It’s really a complex set of motivations but at the bottom, it’s either altruistic based on your usage and wanting to give back or it makes business sense, which is much more sustainable by the way because then it’s a win-win. If everyone wins, there is no sense of the project benefits from having those organizations involved and this organizations see the value of contributing.

**AC:** Yeah, that makes sense, right? I have to – reminiscing here a little bit, I remember one of the first times I met you, I walked in to I think it was a Nova project meeting, right? Where this was years ago and it was a planning meeting, so planning for the next six months kind of notion.

I was just overwhelmed with the number of people that were in the room at the time. I wouldn’t even dare count but there had to be hundreds of people in that room interested in wanting to participate and contribute to that project.

I remember sitting there to that point, I’ve worked in open source for a long, long time but I had never worked in a project with that many people involved. I was extremely impressed with how you handled the group, able to hear all the voices in the room and enable people to contribute and participate, this is the interesting part that I wanted to ask you.

How does an open-source community work, particularly when you have a large group of people that want to participate? What are the rules, how do you set rules of engagement, so forth, that enables these people to participate, feel like they can participate and contribute and yet when you have a very large group like that, how do you get anything done?

**TC:** It’s a complex question.

**AC:** I know it’s a very complex question, I apologize. I might have to break that one down but I was just so impressed because work happened, right? I was totally impressed with how much work was able to get done and how much people – even new people were able to come in and participate in the project.

**TC:** You have to balance a number of structural elements and allow for a lot of flexibility. Essentially, you have to provide a structure where people would be able to share and at the same time, make it very welcoming so that people feel like they can engage and at the same time, giving – still having a lot of flexibility in terms of the topics that are being discussed or the next steps.

The way we’ve been doing it in our design summits, which we’re referring to the event that you mentioned earlier, those designs summit, the idea was to have anyone be able to join and informs the future of the software and it was based on even to developer summits originally and then we perfected the idea in open stack where we have a theme that is being discussed so there is a first a call for organizing the themes and then every 40 minutes we would switch or 50 minutes we would switch.

During that time, we would discuss, openly discuss that topic with either pads to take notes and fish bowl-type setting where people that are most involved in the discussion sit in the middle but at the same time, you can have like extending circles of people depending on how much they want to get involved and people move in the room and get more involved as the discussion goes.

That provides this structure in which people feel free to communicate and at the same time, a lot of flexibility as to where the discussion goes, that helps with getting that setup. As you said, it’s probably a problem you have once you reach a certain size. In terms of rules of engagement or principles or charters that you have to predefine before you start, I would say, you need three things.

The first one is really to define the scope, what is the problem space your project wants to address and make that very clear from their zero because without scope, you’re really exposed to scope creep and that might – Ultimately, that lack of focus might ultimately kill your projects.

It’s actually one thing we didn’t do well in open stack which is to set a very aggressive scope so that we don’t – just because we are a community, it doesn’t mean that we should address every problem earth practically.

The second one is like the big principles, the big 10x that you want your community to follow and write those down so that it’s really clear to whoever joins the community, what they’re signing up for and finally, governance, which describes how decisions are made, governance is really needed in any social group like absence of rules is in itself a form of governance called anarchy and there is the benevolent dictator model where all decisions go up to one person.

You need to define the governance and you need to do it before any problems arise because if you wait for the problem to arrive to have the rule on how to solve it then it’s a bit too late.

**AC:** Too late, isn’t it?

**TC:** People will discuss forever. They can be simple but in the end, it really needs to be clear where the bucket stops and avoid gray areas and what we’ve seen in OpenStack at least and in other projects since is that usually, writing things down in advance avoids the situation that the rule is designed to address.

Sometimes just saying, “Well, this doesn’t get solved at that level, this gets escalated to that level for resolution” then it forces in a way, the first group to come to terms and not escalate because they don’t want to escalate basically. They don’t want the situation out of their hands. They usually work it out between themselves without needing to call out for the upper governance body.

**AC:** Cool, thank you, that was good. Hey, so, we’re going to run out of time here pretty quick but I wanted to get in for this audience, we have a lot of folks that have not participated in a community and they aren’t sure how to get started, right? It can be very intimidating.

Just maybe very basically, how can someone that perhaps hasn’t been involved with open source in the past and their interest maybe some of those contributions that you talked about earlier that are things beyond writing code? If someone’s time is somewhat limited, can they get involved in a community? How would they begin?

**TC:** We touched on that earlier when we discussed what is a community but even if you don’t write code or if your time is limited, you can definitely participate in and be part of a community, especially like just joining the conference and participating in the discussions and finding a presentation or those are all contributions that are extremely worthwhile because otherwise, you end up with the same speakers every conference, those who are comfortable speaking.

It is really good to have that people feel empowered to do that and teaches like documentation, people that use project, they’re probably not as issues with the documentation as they first try to run it, so talking on documentation is really an easy way to get involved. Showing your experience like I said, we have this example recently where we have interns on the outreach program in open stack where we pair them with a mentor and experienced developer and they walk together on some specific project.

One that outreaching intern did is documenting her full experience of this onboarding on blog posts but also on TikTok posts or on every social media and it was extremely useful for us to hear how difficult or how easy it is to pass some of the hurdles that we throw our newest contributors on. Even that like doing a quick write up of how you handle those first step of contributions is extremely valuable to a project. There shouldn’t be like extremely high expectations and the bar is not high. Even the simplest contribution, just hearing it from a diversity of perspective is really useful.

**AC:** Okay, that’s cool. One last topic before we have to go here and this one maybe too deep, might have to deal on another day but I thought it would be interesting because I know you’ve joined or started projects from the beginning, right? If I have something that I think would be very interesting to start an open source community or start a new project in a community, is that something that somebody should be able to do today? Any advice on how someone would start a new project?

**TC:** Yeah, sure.

**AC:** Like I said, that is a big question, isn’t it?

**TC:** Yeah, that’s like the topic for a whole new episode but I’ll try to make it quick. In terms of creation, I would say today it’s really easy to setup an open source project compared to even ten years ago. It’s really easy to setup shop, you just take a force like GitHub or GitLab or OpenDev that we are using for OpenStack and so it is easy to do it like whether you should do it or not is another good topic.

**AC:** A whole question, isn’t it?

**TC:** Yeah, I guess the key question is whether several people or several organizations have the same issue and would benefit from sharing the solution because ultimately for me, the interest in having an open source project is ultimately to avoid the waste of having several parties develop the same thing proprietary on their side while they could collaborate and contribute and avoid wasting that energy by doing it as a collaborative project in open source.

Which is actually why I’m so motivated by open lead develop open source because I don’t really see the point of open source that is owned by a single body because then, you don’t really have that collaboration that reduces waste. It is just one way to do proprietary software where you just publish a code and have some free labor in and on the side. Ultimately, for me what matters is whether multiple people have the same problem and then yes, there is potential for an open source project and then setting it up is not the most difficult part. It used to be but it is not the most difficult part today.

**AC:** That’s true. That is a good point, so thank you for that, I like your response. All right Thierry, so we wanted to circle back a little bit about how community works and I’ll call them the levels of openness that can be done because some communities are much more directed than others and you know, as we’ve worked together for over these several years, I really like the notion of what we call the four opens.

Could you talk to us a little bit about that and about how that opens up a community and enables a lot of communication and I think a lot more contributions, so give us a little bit of flavor on what we call the Four Opens?

**TC:** Sure, so like we previously talked, we mentioned rules of engagement and I said that we need to define scope, principles and governance and the four opens would be an example of principles. Those are the principles that the open stack community was built on. The four opens are open source, because back then there weren’t any openly developed open source project that was not open core that would do a cloud software.

It was a way of saying that will do we will open source, not open core. There won’t be a proprietary edition of the product, we will not keep some features or to sell a proprietary edition of whatever, everything should be open source. There is open development, which seems really obvious now because like every open source project on earth is on some open GitForce somewhere that you can see what is happening but 12 years ago or 11 years ago when we started OpenStack, there weren’t anything like it.

Open development is about being able to see what’s happening in development transparently so all the patches, all the reeves, all of the issues or all of the discussions everything should be accessible and transparent without needing people to register or anything to see it happening, so transparency in development.

The third one, which was collectively known as well and we touched on it when we discussed design summits is open design. The fact that development is not done behind closed doors by an elite group of core developers, the design is discussed in the open engaging with the users during those open events that we are throwing and that model was replicated in other successful projects like Kubernetes for example.

Finally, open community. Open community is the idea that anyone can join the community and anyone can become a leader in that community. There is no pay to play, there is no like an enforcement that the leaders, the technical leaders from the project out coming from one of the major sponsors or it is completely disconnected. Technical governance is completely disconnected from any other foundation governance or anything.

It is really one contributor, one vote and you end up with elections and the most respected contributors get elected to the leadership buddies for the project. With those four opens, you actually have a very sustainable community because you really empower your community to participate. There is no place that they can’t see, there is no feature that they can’t use, there is no discussion that they can’t participate in and there is no level of leadership that they can’t attain and I feel like it’s been instrumental in the success of open stack.

It is also instrumental in the success of other communities that I’ve adopted them, if not in the letter, in the spirit and so I feel like it is a good model.

**AC:** I’m glad you pointed that out. Back when we first stated those Four Opens you’re right, they seemed almost revolutionary in some sense and they have become very adopted in many of the communities that I have participated in over these last years and to me that just says they work and that’s why I really like them, so thank you for elaborating on those. I want to go to that fourth one there, a little bit about open community and where things like the technical boards and so forth are elected not just appointed.

That kind of alludes that things are based on reputation, right? Your merits are earned in a community, so any advice on dos and don’ts on how a person would build a reputation in an open source community to help them be a strength particularly in that open community portion?

**TC:** Yes, you are right that if you have open elections it can turn into a popularity contests really quickly and then reputation is important. People think that you need to be a technical rock star to get to the level of reputation that will let you be elected as a leader for a project but it is actually not really true. From the things you can do, making yourself useful to others is really the key. Do the things that nobody else does.

Everyone is grateful for that to cover all that blind spot that nobody else is covering, you become really well-known across all of the community including in extremely large communities by doing those things that nobody else is doing and then you can leverage that reputation to get elected to the leadership positions like I said or you can influence decisions because nobody wants to piss off the person that actually does the things they don’t want to do.

That’s actually how I started in most of the communities I got involved in like when I joined Gentu in 2000, I ended up documenting security because it wasn’t documented the way I wanted to be. Clearly, documenting the security processes was not high on everyone’s list and by doing that, I earned a good reputation. I ended up leading the security team there, I ended up elected to the Gentu board of directors. It is really a theme and in open stack, I basically did the same.

I started with waste management, which was a non-development task again by documenting security and I ended up being elected to the technical committee for four years and ended up as a leader for that community by starting with a non-code contribution. It’s really not about code, it’s really not about being a technical rock star. It is really more about being useful to others.

**AC:** That’s great.

**TC:** In terms of don’t, don’t put in things you should not do, I would say you shouldn’t assume malicious intent because 99% of the cases in those communities, people try to do good and what is seen as potential malicious intent is actually breaks down to communication problems in the end and 99% of the time. It is really key to not jump to conclusions, give people a chance to voice their side of the story rather than packed in haste and make for a not very welcoming community and as a result.

**AC:** Well, thank you Thierry. This has been very, very interesting and very educational. I have learned some stuff as well and it reminded me a lot of good stuff. Thank you very much for helping us out today and joining us in this podcast. I very much appreciate it.

**TC:** Well, thanks Alan for the invitation.

**AC:** Thierry, this has been great.

[END OF INTERVIEW]

**AC:** For more information, check out community.suse.com and make sure to subscribe to the OCTOpod on your favorite podcast platform.

[END]
