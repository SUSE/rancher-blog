---
title: "Containers and PostgreSQL vs. MySQL vs. MariaDB"
date: 2017-01-19T10:17:00
slug: "containers-and-postgresql-vs-mysql-vs-mariadb"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["storage"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86603
  original_url: "https://www.suse.com/c/rancher_blog/containers-and-postgresql-vs-mysql-vs-mariadb/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2017 database benchmark, outdated"
  redirect_target: "rancher.com/blog (hub)"
---

[![](images/rancher_blog_relational-databases.png)](images/rancher_blog_relational-databases.png)Which
databases provide the best performance when used with containers? That’s
an important question for people seeking to make the most of
containerized infrastructure. In this post, I take a look at some basic
performance metrics for three relational databases—PostgreSQL, MySQL,
and MariaDB—when they are run as containers.

### Introduction

For the purposes of my tests, I used the official container images
available from Docker Hub to install and start the databases. While the
process of pulling the images and starting the containers is likely
already familiar to anyone using Docker, I’ll run through the commands I
used below, just so that it is clear what my process was in preparing
for the performance tests. **PostgreSQL** To get an official
[![PostgreSQL](images/rancher_blog_Postgresql.png)](images/rancher_blog_Postgresql.png)Docker
image with PostgreSQL, execute

```
$ docker pull postgres
```

To start a PostgreSQL instance:

```
$ docker run --name postgres -d -p 127.0.0.1:5432:5432 postgres
```

This command will start a Docker container nominated as **postgres** and
listen to the **5432** port on **localhost**. The last argument is the
image name. It’s very important to pass the IP and port to enable the
localhost connection. To connect with PostgreSQL via the command line:

```
$ docker run -it --rm --link postgres:postgres postgres psql -h postgres -U postgres
```

This image has a default user (*postgres*) and database ready to be
accessed via psql. You can use the psql interface to create and manage
the database before setting the database’s configurations in your
application. To connect an application with the containerized database,
just set the host, port, user and database name defined in the new
database.
**[![MySQL](images/rancher_blog_MySQL-e1484783414578.png)](https://cdn.rancher.com/wp-content/uploads/2017/01/18164950/MySQL.png)MySQL**
Similar to PostgreSQL, to get an official Docker image with MySQL,
execute:

```
$ docker pull mysql
```

To start a MySQL instance:

```
$ docker run --name mysql -p  127.0.0.1:3306:3306 -e
MYSQL_ROOT_PASSWORD="password" mysql &
```

This command will start a Docker container named **mysql** and listen on
**port 3306** on localhost. It will also be necessary to set a password
that will be used to connect with the database using the default user,
**root**. To connect with MySQL via the command line:

```
$ docker run -it --link mysql:mysql --rm mysql sh -c 'exec mysql
-h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot
-p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'
```

You’ll need to pass host, port, and password as environment variables.

**[![MariaDB](images/rancher_blog_MariaDB.png)](images/rancher_blog_MariaDB.png)MariaDB**
As expected, running this image is almost exactly the same as running
the MySQL image. To get the official Docker image for MariaDB:

```
$ docker pull mariadb
```

To start a MariaDB instance:

```
$ docker run --name mariadb -p 127.0.0.1:3306:3306 -e MYSQL_ROOT_PASSWORD=password mariadb &
```

To connect to MySQL via the command line:

```
$ docker run -it --link mariadb:mysql --rm mariadb sh -c 'exec mysql
-h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot
-p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'
```

[![Rancher Free Ebook 'Comparing Kubernetes, Mesos and Swarm'](images/rancher_blog_Kubernetes_Mesos_Swarm_ebook-e1482279885640.jpg)](images/rancher_blog_Kubernetes_Mesos_Swarm_ebook-e1482279885640.jpg)
Free eBook: Compare architecture, usability, and feature sets for
Kubernetes, Mesos/Marathon, and Docker Swarm

### Comparisons

A simple and fast way to measure the performance of each of these
databases when run as a container is by creating a table with an int
column and inserting 1,000 records, then comparing the time that each
database takes to complete the query. To do that, first create a table
(this command will be the same no matter which database you are using):

```
create function addUsers() returns void as
$$
declare i int;
begin
 for i in 1..1000 loop
   insert into users(id) values (i);
 end loop;
 return;
end;
$$ language plpgsql;
```

Execute the PostgreSQL function with:

```
$ select addUsers();
```

For MySQL and MariaDB, you can create this function to insert 1,000
users:

```
delimiter $$
create procedure addUsers()
 begin
   declare i int default 1;
   while (i <= 1000) do
     insert into users (id) values (i);
     set i=i+1;
   end while;
end$$
delimiter ;
```

Then execute it with:

```
$ call addUsers();
```

### Results

Now, the big question: What are the results?

- \*\*PostgreSQL: \*\*~1 second
- **MySQL: ~**12.32 seconds
- **MariaDB:** ~12.71 seconds

MySQL and MariaDB performed similarly, with a negligible difference.
However, the PostgreSQL results were impressive. They came in 11 seconds
less than MySQL and MariaDB. That’s much faster.

### Conclusion

All of the databases compared in this article require about the same
effort to install and connect. But PostgreSQL clearly came out ahead
when it came to the time required to add data to the database. Why? It’s
hard to say definitively based on the information I collected in this
basic test. But one possible explanation is that PostgreSQL uses heap
tables rather than clustered indexes. This may improve performance.
PostgreSQL’s multiversion concurrency control could also contribute to
the performance bump. I only performed a basic test, of course. You
could run many more benchmarks. Plus, when choosing which database to
use with Docker, there are other factors to consider besides just
performance, like how well the database works with the apps that will
connect to it. Nonetheless, since few people have collected any sort of
benchmarking data for containerized databases, the information above is
a good starting point if you’re trying to decide which relational
database to implement as part of your container infrastructure. *Brena
Monteiro is a software engineer with experience in the analysis and
development of systems. She is a free software enthusiast and an
apprentice of new technologies.*
