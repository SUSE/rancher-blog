---
title: "Adding custom nodes to your Kubernetes cluster in Rancher 2.0 Tech Preview 2"
date: 2018-02-13T09:00:00
slug: "adding-custom-nodes-to-your-kubernetes-cluster-in-rancher-2-0-tech-preview-2"
author: "Rancher Admin"
products: ["Rancher Manager"]
tags: ["installation"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 85789
  original_url: "https://www.suse.com/c/rancher_blog/adding-custom-nodes-to-your-kubernetes-cluster-in-rancher-2-0-tech-preview-2/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 2.0 tech preview 2 UI"
  redirect_target: "docs.rancher.com"
---

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)

Recently, we
[announced](https://forums.suse.com/t/rancher-tech-preview-update-2-7-2018/9334)
our second milestone release of Rancher 2.0 Tech Preview 2. This
includes the possibility to add custom nodes (nodes that are already
provisioned with a Linux operating system and Docker) by running a
generated `docker run` command to launch the `rancher/agent` container,
or by connecting over SSH to that node. In this post, we will explore
how we can automate the generation of the command to add nodes using the
`docker run`command. *Warning: this is not a production ready product
yet, don’t put your production workloads on it just yet.*
**Requirements**

- Host running Linux and Docker
- JSON utility `jq` installed, to parse API responses
- `sha256sum` binary to calculate CA certificate checksum

#### Start Rancher server

Before we can execute any action, we need to launch the
`rancher/server`container. The image to use for the 2.0 Tech Preview 2
is `rancher/server:preview` . Another change from 1.6 to 2.0, is that we
no longer expose on port 8080. Instead, we expose port 80 and 443, where
80 is by default redirected to 443. You can start the container as
follows:

```
docker run -d -p 80:80 -p 443:443 rancher/server:preview
```

If you want the data for this setup to be persistent, you can mount a
host volume to `/var/lib/rancher` as shown below:

```
docker run -d -p 80:80 -p 443:443 -v /data:/var/lib/rancher rancher/server:preview
```

#### Logging in and creating API key

In Rancher 1.x, there was no authentication enabled by default. After
launching the `rancher/server` container, you could access the API/UI
without any credentials. In Rancher 2.0, we enable authentication with
the default username and password `admin`. After logging in, we get a
Bearer token, which allows us to change the password. After changing the
password, we will create an API key to execute the other requests. The
API key is also a Bearer token, which we call `automation` to be used
for automation purposes. *Logging in*

```
# Login
LOGINRESPONSE=`curl -s 'https://127.0.0.1/v3-public/localProviders/local?action=login' -H 'content-type: application/json' --data-binary '{"username":"admin","password":"admin"}' --insecure`
LOGINTOKEN=`echo $LOGINRESPONSE | jq -r .token`
```

\*Changing the password (\****thisisyournewpassword****)*

```
# Change password
curl -s 'https://127.0.0.1/v3/users?action=changepassword' -H 'content-type: application/json' -H "Authorization: Bearer $LOGINTOKEN" --data-binary '{"currentPassword":"admin","newPassword":"thisisyournewpassword"}' --insecure
```

*Create API key*

```
# Create API key
APIRESPONSE=`curl -s 'https://127.0.0.1/v3/token' -H 'content-type: application/json' -H "Authorization: Bearer $LOGINTOKEN" --data-binary '{"type":"token","description":"automation"}' --insecure`

# Extract and store token
APITOKEN=`echo $APIRESPONSE | jq -r .token`
```

#### Creating the cluster

With the newly generated API key, we can create a Cluster. When you
create a cluster, you have 3 options:

- Launch a Cloud Cluster (Google Kubernetes Engine/GKE for now)
- Create a Cluster (our own Kubernetes installer, [Rancher Kubernetes
  Engine](https://medium.com/r/?url=https%3A%2F%2Fgithub.com%2Francher%2Frke%2F),
  is used for this)
- Import an Existing Cluster (if you already have a Kubernetes
  cluster, you can import it by inserting the kubeconfig file from
  that cluster)

For this post, we’ll be creating a cluster using Rancher Kubernetes
Engine (rke). When you are creating a cluster, you can choose to create
new nodes directly when creating the cluster (by creating nodes from
cloud providers like DigitalOcean/Amazon) or use pre-existing nodes and
let Rancher connect to the node using provided SSH credentials. The
method we are discussing in this post (adding node by running the
`docker run` command) is only available after the cluster has been
created. You can create the cluster (**yournewcluster**) using the
following commands. As you can see, only the parameter
`ignoreDockerVersion` is included here (which ignores an unsupported
Docker version for Kubernetes). The rest will be default, which we will
go into in another post. Till then you can discover the configurable
options through the UI.

```
# Create cluster
CLUSTERRESPONSE=`curl -s 'https://127.0.0.1/v3/cluster' -H 'content-type: application/json' -H "Authorization: Bearer $APITOKEN" --data-binary '{"type":"cluster","nodes":[],"rancherKubernetesEngineConfig":{"ignoreDockerVersion":true},"name":"yournewcluster"}' --insecure`

# Extract clusterid to use for generating the docker run command
CLUSTERID=`echo $CLUSTERRESPONSE | jq -r .id`
```

After running this, you should see your new cluster in the UI. The
status will be `waiting for nodes to provision or a valid configuration`
as there are no nodes added yet. **Assembling the**`docker run`**command
to launch the**`rancher/agent` The final part of adding the node, is to
launch the `rancher/agent` container which will add the node to the
cluster. For this to succeed we need:

- The agent image that is coupled with the Rancher version
- The roles for the node (etcd and/or controlplane and/or worker)
- The address where the `rancher/server` container can be reached
- Cluster token which the agent uses to join the cluster
- Checksum of the CA certificate

The agent image can be retrieved from the `settings` endpoint in the
API:

```
AGENTIMAGE=`curl -s -H "Authorization: Bearer $APITOKEN" https://127.0.0.1/v3/settings/agent-image --insecure | jq -r .value`
```

The roles for the node, you can decide for yourself. (For this example,
we’ll be using all three roles):

```
ROLEFLAGS="--etcd --controlplane --worker"
```

The address where the `rancher/server` container can be reached, should
be self explanatory. The `rancher/agent` will connect to that endpoint.

```
RANCHERSERVER="https://rancher_server_address"
```

The cluster token can be retrieved from the created cluster. We saved
the created clusterid in `CLUSTERID` , which we can now use to generate
a token.

```
# Generate token (clusterRegistrationToken)
AGENTTOKEN=`curl -s 'https://127.0.0.1/v3/clusterregistrationtoken' -H 'content-type: application/json' -H "Authorization: Bearer $APITOKEN" --data-binary '{"type":"clusterRegistrationToken","clusterId":"'$CLUSTERID'"}' --insecure | jq -r .token`
```

The generated CA certificate is stored in the API as well, and can be
retrieved as shown below. We append `sha256sum` to generate the checksum
we need to join the cluster.

```
# Retrieve CA certificate and generate checksum
CACHECKSUM=`curl -s -H "Authorization: Bearer $APITOKEN" https://127.0.0.1/v3/settings/cacerts --insecure | jq -r .value | sha256sum | awk '{ print $1 }'`
```

All data needed to join the cluster is now available, we only need to
assemble the command.

```
# Assemble the docker run command
AGENTCOMMAND="docker run -d --restart=unless-stopped -v /var/run/docker.sock:/var/run/docker.sock --net=host $AGENTIMAGE $ROLEFLAGS --server $RANCHERSERVER --token $AGENTTOKEN --ca-checksum $CACHECKSUM"

# Show the command
echo $AGENTCOMMAND
```

The last command ( `echo $AGENTCOMMAND` ) should look like this

```
docker run -d --restart=unless-stopped -v /var/run/docker.sock:/var/run/docker.sock --net=host rancher/agent:v2.0.2 --etcd --controlplane --worker --server https://rancher_server_address --token xg2hdr8rwljjbv8r94qhrbzpwbbfnkhphq5vjjs4dfxgmb4wrt9rpq --ca-checksum 3d6f14b44763184519a98697d4a5cc169a409e8dde143edeca38aebc1512c31d
```

After running this command on a node, you should see it join the cluster
and get provisioned by Rancher. *Protip: the tokens can also directly be
used as basic authentication, for example:*

```
curl -u $APITOKEN https://127.0.0.1/v3/settings --insecure
```

### Complete GitHub gist for reference

Hopefully this post helped with the first steps of automating your
Rancher 2.0 Tech Preview 2 setup. We explored what steps you need to
take to automatically generate the `docker run` command to add a node to
a Cluster. Keep an eye on this blog for other post regarding Rancher
2.0. Also, if you have any questions, join our Rancher Users Slack by
visiting [https://slack.rancher.io](https://slack.rancher.io/) and join
the #2–0-tech-preview channel. You can also visit our forums to ask any
question: <https://forums.suse.com/>

A Detailed Overview of Rancher's ArchitectureThis newly-updated, in-depth guidebook provides a detailed overview of the features and functionality of the new Rancher: an open-source enterprise Kubernetes platform.[Get the eBook](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)
