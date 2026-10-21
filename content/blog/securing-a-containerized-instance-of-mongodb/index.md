---
title: "Securing a Containerized Instance of MongoDB"
date: 2017-03-09T11:20:00
slug: "securing-a-containerized-instance-of-mongodb"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["security"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 87043
  original_url: "https://www.suse.com/c/rancher_blog/securing-a-containerized-instance-of-mongodb/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2017 MongoDB ransomware, Docker-era"
  redirect_target: "rancher.com/blog (hub)"
---

![Securing
MongoDB](images/rancher_blog_mongodb-300x81.png)MongoDB, the popular
open source NoSQL database, has been in the news a lot recently—and
not for reasons that are good for MongoDB admins. Early this year,
[reports began
appearing](https://arstechnica.com/information-technology/2017/01/more-than-10000-online-databases-taken-hostage-by-ransomware-attackers/)
of MongoDB databases being “taken hostage” by attackers who delete all
of the data stored inside the databases, then demand ransoms to restore
it. Security is always important, no matter which type of database
you’re using. But the recent spate of MongoDB attacks makes it
especially crucial to secure any MongoDB databases that you may use as
part of your container stack. This article explains what you need to
know to keep MongoDB secure when it is running as a container. We’ll go
over how to close the vulnerability behind the recent ransomware attacks
using a MongoDB container while the container is running—as well as
how to modify a MongoDB Dockerfile to change the default behavior
permanently.

### Why the Ransomware Happened: MongoDB’s Default Security Configuration

[![](images/rancher_blog_Training.png)](https://attendee.gotowebinar.com/rt/2905734731496917249)
Register now for free online training on deploying containers with
Rancher The ransomware attacks against MongoDB weren’t
enabled by a flaw inherent in MongoDB itself, per se, but rather by some
weaknesses that result from default configuration parameters in an
out-of-the-box installation of MongoDB. By default, MongoDB databases,
unlike most other popular database platforms, don’t require login
credentials. That means anyone can log into the database and start
modifying or removing data. **Securing a MongoDB Container** In order to
mitigate that vulnerability and run a secure containerized instance of
MongoDB, follow the steps below. **Start a MongoDB instance** First of
all, start a MongoDB instance in Docker using the most up-to-date image
available. Since Docker uses the most recent image by default, a simple
command like this will start a MongoDB instance based on an up-to-date
image:

```
docker run --name mongo-database -d mongo
```

**Create a secure MongoDB account** Before disabling password-less
authentication to MongoDB, we need to create an account that we can use
to log in after we change the default settings. To do this, first log
into the MongoDB container with:

```
docker exec -it mongo-database bash
```

Then, from inside the container, log into the MongoDB admin interface:

```
mongo
```

Now, enter this stanza of code and press Enter:

```
use admin
db.createUser(
{
user: "db_user",
pwd: "your_super_secure_password",
roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
}
)
```

This creates a MongoDB user with username db\_user and password
your\_super\_secure\_password (Feel free to change this, of course, to
something more secure!) The user has admin privileges. **Changing
default behavior in Dockerfile** If you want to make the MongoDB process
start with authentication required by default all of the time, you can
do so by editing the Dockerfile used to build the container. To do this
locally, we’ll first pull the MongoDB Dockerfile from GitHub with:

```
git clone https://github.com/dockerfile/mongodb
```

Now, cd into the mongodb directory that Git just created and open the
Dockerfile inside using your favorite text editor. Look for the
following section of the Dockerfile:

```
# Define default command.
CMD ["mongod"]

Change this to:

# Define default command.
CMD ["mongod --auth"]
```

This way, when mongodb is called when the container starts, it will run
with the --auth flag by default.

### Conclusion

If you follow the steps above, you’ll be able to run MongoDB as a Docker
container without becoming one of the tens of thousands of admins whose
MongoDB databases were wiped out and held for ransom by attackers. And
there really is not much to it, other than being aware of the
vulnerabilities inherent in a default MongoDB installation and the steps
for resolving them. *Chris Riley (@HoardingInfo) is a technologist who
has spent 12 years helping organizations transition from traditional
development practices to a modern set of culture, processes and tooling.
In addition to being a research analyst, he is an O’Reilly author,
regular speaker, and subject matter expert in the areas of DevOps
strategy and culture. Chris believes the biggest challenges faced in the
tech market are not tools, but rather people and planning.*
