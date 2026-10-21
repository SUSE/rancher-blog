---
title: "Using Habitat to Create Rancher Catalog Templates"
date: 2016-06-14T11:29:00
slug: "using-habitat-to-create-rancher-catalog-templates"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["developer-experience"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 87256
  original_url: "https://www.suse.com/c/rancher_blog/using-habitat-to-create-rancher-catalog-templates/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher catalog v1 discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

Today, [Chef announced the release of
Habitat](https://www.chef.io/blog/2016/06/14/chef-launches-habitat-new-open-source-project-to-automate-applications/),
a new approach to automate applications.
[Habitat](https://www.habitat.sh/) shifts the focus of application
management and configuration from the infrastructure to the application
itself. In a nutshell, it allows users to create packages that
encapsulate the application logic itself, runtime dependencies, and
configuration. These packages can then auto-update accordingly to
policies set by your organization. In this article, I will show you how
to leverage the runtime configuration and service member discovery
capabilities of Habitat to build a Rancher Catalog template. For
illustration purposes, we will look at the [Habitat
plan](https://www.habitat.sh/docs/create-plans/) and the Rancher Catalog
item for RabbitMQ.

### Habitat plans

To create a Habitat package, you’ll need to start with a Habitat plan. A
Habitat plan is a collection of shell scripts that define what the
package contains, how it is built, and how it can be configured. The
Habitat plan for RabbitMQ discussed in this post is available
[here](https://github.com/janeczku/habitat-plans), in GitHub. Let’s walk
through each of the files in the RabbitMQ plan.

#### default.toml (available [here](https://github.com/janeczku/habitat-plans/blob/master/rabbitmq/default.toml))

The default.toml file specifies which configuration options Habitat
should expose for this package, as well as their default values. In our
case, the first five options are rabbitmq-server configuration options,
and are used to populate the “config/rabbitmq.conf” template. For
example, the following section sets up the configuration variables that
are referred in the {{cfg.default\_user}} and {{cfg\_default\_pass}}
expressions in
the [config/rabbitmq-server.conf](https://github.com/janeczku/habitat-plans/blob/master/rabbitmq/config/rabbitmq.config) template:

```
# Default user name
default_user = "guest"

# Default user password
default_pass = "guest"
```

The last two configuration variables:

```
# Erlang cookie
# Used for authenticating nodes in a cluster
# Must be an alphanumeric string of any length
erlang_cookie = "SUPERSECRETSTRING"

# Enable the management plugin (HTTP API on port 15672)
enable_management="false"
```

are not used in the configuration template but in the init hook shell
script to create the Erlang cookie required for clustering and to enable
the RabbitMQ management plugin.

#### plan.sh (available [here](https://github.com/janeczku/habitat-plans/blob/master/rabbitmq/plan.sh))

The top most part of the plan.sh file specifies basic information about
the plan. To learn what all of those mean, check out the [Habitat
documentation for the plan
syntax](https://www.habitat.sh/docs/reference/plan-syntax/). For now,
let’s just look at the following settings:

```
pkg_source=https://www.rabbitmq.com/releases/rabbitmq-server/v${pkg_version}/rabbitmq-server-generic-unix-${pkg_version}.tar.xz
pkg_deps=(core/coreutils core/erlang/18.3)
pkg_expose=(4369 25672 5672 15672)
```

As you can see, *pkg\_source* points to the release archive for the
3.6.2 version of RabbitMQ. When building the package, Habitat will
automatically download and extract this archive. In *pkg\_deps*, we
specified the runtime dependencies for our package. Since RabbitMQ is an
Erlang application, we reference the Erlang package available from the
“core” depot (which is a public repository containing a number of key
dependency packages). *pkg\_expose* lists all the ports on which
RabbitMQ exposes services. When Habitat builds a Docker image from this
package, each of the specified ports will be set as an EXPOSE attribute
of the image. Next, let’s take a look at the *do\_install()* block:

```
do_install()
 cat > ${pkg_prefix}/etc/rabbitmq/rabbitmq-env.conf << EOF
CONFIG_FILE=$pkg_svc_config_path/rabbitmq
LOGS=-
SASL_LOGS=-
EOF
 chmod 644 ${pkg_prefix}/etc/rabbitmq/rabbitmq-env.conf
}
```

Here, we first copy the extracted RabbitMQ source files from the
temporary build path into the actual package directory. Then we create a
rabbitmq-env.conf file and populate it with the required options to make
the rabbitmq-server use the dynamically generated
rabbitmq-server.config, and write its log to stdout instead of to
syslog.

#### init (available [here](https://github.com/janeczku/habitat-plans/blob/master/rabbitmq/hooks/init))

The init file is executed by the Habitat supervisor before the
application is started. For our purposes, it’s the perfect place to
write the Erlang cookie so it’s picked up when the rabbitmq-server is
started. As you can see, the value we write to the erlang.cookie file is
once again a handlebar expression referring to a variable in the
default.toml file:

```
erlang_cookie_file={{pkg.svc_path}}/var/lib/rabbitmq/.erlang.cookie
echo -n "{{cfg.erlang_cookie}}" > $erlang_cookie_file
chmod 600 $erlang_cookie_file
```

Finally, the init script also takes care of enabling the RabbitMQ
management plugin.

#### run (available [here](https://github.com/janeczku/habitat-plans/blob/master/rabbitmq/hooks/run))

The script in the “run” file takes care of starting the rabbitmq-server.
Note that this sets the HOME environment variable to the directory in
which we wrote the Erlang cookie earlier.

#### health\_check (available [here](https://github.com/janeczku/habitat-plans/blob/master/rabbitmq/hooks/health_check))

The supervisor calls the “health\_check” hook to check whether the
application has fully started. Here we leverage the “rabbitmqctl” tool’s
“node\_health\_check” command to check whether the rabbitmq-server is
fully started. We use the “health\_check” hook for the RabbitMQ package
because it allows us to block the followers in our census from starting
their rabbitmq nodes until RabbitMQ node on the leader has fully started
up and is able to accept clustering requests.

#### rabbitmq.conf (available [here](https://github.com/janeczku/habitat-plans/blob/master/rabbitmq/hooks/health_check))

Finally, the config/rabbitmq.config file includes the Erlang syntax and
handlebars expressions which the supervisor uses to dynamically create a
valid configuration file for the rabbitmq-server. Let’s look at the most
interesting section here:

```
{{~#if svc.me.follower}}
  {mnesia_table_loading_timeout, 30000},
{{~#with svc.leader}}
  {cluster_nodes, {['rabbit@{{hostname}}'], disc}}
{{~/with}}
{{else}}
  {mnesia_table_loading_timeout, 30000}
{{~/if}}
```

As you can see, we are using if/else expressions to selectively enable
automatic clustering for followers using the hostname of the leader
(*svc.leader*).

### Building a Docker image from a Habitat plan

Since our goal is to deploy this Habitat package as a service in
Rancher, we first need to build a Docker image using the following
steps:

```
cd ~/plans/rabbitmq
hab studio -k rancher enter
[default:/src:0]# build
hab pkg export docker rancher/rabbitmq
```

This will result in a Docker image tagged as rancher/rabbitmq:latest.

### Rancher Catalog Template

Next, let’s see how we can use this image in a Rancher Catalog template
to deploy a RabbitMQ cluster. The template is available on GitHub
[here](https://github.com/janeczku/hab-catalog/tree/master/templates/rabbitmq-cluster).
Let’s have a closer look at the docker-compose.ymp for this template,
starting with the rabbitmq-master service:

```
rabbitmq-master:
  image: janeczku/rabbitmq:dev
  command:
  - "--topology"
  - "initializer"
  - "--listen-peer"
  - "0.0.0.0"
  ports:
  - "15672:15672"
  - "${AMQP_PORT}:${AMQP_PORT}"
  expose:
    - "9634/udp"
  environment:
   HAB_RABBITMQ: 'enable_management="${ENABLE_MANAGEMENT}" default_user="${USER_NAME}" default_pass="${USER_PASS}" (...)
  labels:
    io.rancher.container.hostname_override: container_name
```

Note the command passed to the Habitat container. The arguments are
configuration flags for the supervisor, which runs as PID1 in Habitat
service containers. We configure the supervisor with a topology of type
“initializer” (which is a leader-follower topology where the followers
are blocked until the leader’s application is fully initialized). This
ensures that the RabbitMQ node running on the supervisor elected as
leader is fully started, so the other nodes don’t fail to join the
cluster with it. Finally, notice how we assign the values entered in the
Catalog UI to the variables specified in the plan’s default.toml file in
a single environment variable named HAB\_APPLICATIONNAME. Next, let’s
check out the “rabbitmq-slave” service:

```
rabbitmq-slave:
  image: janeczku/rabbitmq:dev
  command:
    - "--topology"
    - "initializer"
    - "--listen-peer"
    - "0.0.0.0"
    - "--peer"
    - "rabbitmq-master"
  expose:
    - "9634/udp"
  environment:
   HAB_RABBITMQ: 'enable_management="${ENABLE_MANAGEMENT}" default_user="${USER_NAME}" default_pass="${USER_PASS}" (...)
  labels:
    io.rancher.container.hostname_override: container_name
    io.rancher.scheduler.affinity:container_label_soft_ne: io.rancher.stack_service.name=$${stack_name}/$${service_name
  links:
    - rabbitmq-master
```

As you’ll notice, we are passing the additional flag
`--peer rabbitmq-master` in the command instruction to the container.
This makes both rabbitmq-slave services and the rabbitmq-master service
members of the same census, and eventually elect a leader to become the
first RabbitMQ node started. When you launch this Catalog stack, a
single instance of the rabbitmq-master service is going to be started
first, followed by the configured number of rabbitmq-slave instances.
The census of supervisors will elect a leader, which becomes the first
to run a RabbitMQ node. Once this first node has become fully
operational, the other service instances (followers) are going to join
this node and form a RabbitMQ cluster. And with that, we’ve launched
RabbitMQ with Habitat and the Rancher Catalog! If you have additional
questions, please reach out to me (jan@rancher.com), or on Twitter
[@Rancher\_Labs](http://twitter.com/rancher_labs).
