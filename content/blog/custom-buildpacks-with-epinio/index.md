---
title: "Custom Buildpacks with Epinio"
date: 2021-11-17T19:54:51
slug: "custom-buildpacks-with-epinio"
author: "Matthew Casperson"
image: "images/rancher_blog_epinio.jpeg"
products: ["Epinio"]
tags: ["developer-experience"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 93279
  original_url: "https://www.suse.com/c/rancher_blog/custom-buildpacks-with-epinio/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Epinio discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

[Epinio](https://epinio.io/)is a build and application hosting platform running on Kubernetes. Developers push their source code to Epinio with a simple CLI command, Epinio builds an Open Container Initiative (OCI) image using Buildpacks, and the image is deployed within the Kubernetes cluster.

[![](https://media1-production-mightynetworks.imgix.net/asset/31258499/epinio.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)](https://media1-production-mightynetworks.imgix.net/asset/31258499/epinio.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format)

The process is mostly transparent thanks to the wide range of languages supported by the default [Paketo buildpacks](https://paketo.io/) utilized by Epinio. But not every codebase can be built by Paketo, or you may want to build your code with your own custom buildpacks, which requires using a custom builder.

In this post, you’ll learn how to build a custom builder and use it with Epinio to build your application.

## Buildpacks and Builders

In a [previous post](https://community.suse.com/posts/creating-a-custom-java-buildpack), I documented the process of building a custom buildpack with the end result being a custom Java buildpack able to build Maven projects.

The source code to the custom buildpack and builder is available on [GitHub](https://github.com/mcasperson/JavaBuildPack).

In order to use this buildpack in Epinio, it is important to understand the distinction between a buildpack and a builder.

A [buildpack](https://buildpacks.io/docs/concepts/components/buildpack/)contains the logic required to detect and build a specific language. Popular projects, like Paketo, include a number of buildpacks supporting popular languages such as Java, PHP, .NET Core, Node.js, Ruby etc.

Buildpacks are then combined into a single [builder](https://buildpacks.io/docs/concepts/components/builder/). A builder gives each of its child buildpacks an opportunity to scan the application source code, and selects the first buildpack to report that it is compatible with the code to complete the build.

If you followed the previous post, you would have created a single buildpack. To use this buildpack with Epinio, you must package the buildpack as a builder. Creating a builder is simple, requiring only two new files.

## Creating a Builder

The first step is to add a package.toml file, which allows the pack command to package the buildpack. The contents of the file are shown below:

```
[buildpack]
uri = "."
```

The URI property specifies the directory containing the buildpack code. The URI is set to the current directory because the package.toml file has been saved alongside the buildpack files.

The next file you must add is builder.toml:

```
[[buildpacks]]
uri = "."

[[order]]
[[order.group]]
id = "mcasperson/java"
version = "0.0.1"

[stack]
id = "heroku-20"
run-image = "heroku/pack:20"
build-image = "heroku/pack:20-build"
```

The buildpacks array references one or more buildpacks to include in the builder. You include the buildpack from the same directory by setting the URI property to a period.

The order array defines the order in which the builder will execute buildpacks looking for one that is able to build the supplied source code. As this builder only has one buildpack, there is only one buildpack defined in this array. The id and version properties must match the same values from the buildpack buildpack.toml file.

The stack section defines the stack this builder uses to compile and run applications. Each stack has two OCI images: one called build-image, used while building the applications, and one called run-image, used to execute the built application.

You can find stacks by running the command:

```
pack stack suggest
```

The following is a snippet from the command output. Note the id, run-image, and build-image values from the buildpack.toml file match the values returned by the pack command:

```
Stack ID: heroku-20
Description: The official Heroku stack based on Ubuntu 20.04
Maintainer: Heroku
Build Image: heroku/pack:20-build
Run Image: heroku/pack:20
```

To create the builder image, run the following command, replacing mcasperson with your Docker Hub username:

```
pack builder create mcasperson/my-builder:latest --config ./builder.toml
```

The resulting image is then pushed to Docker Hub with the command:

```
docker push mcasperson/my-builder:latest
```

You now have a custom builder published to Docker Hub ready to use with your Epinio builds.

## Custom Builders with Epinio

The ability to use a custom builder with Epinio was [recently added](https://github.com/epinio/epinio/pull/623), allowing the builder to be specified with the --builder-image argument:

```
epinio push --name my-java-app --builder-image mcasperson/my-builder
```

This command instructs Epinio to download and use the custom builder when compiling your application code. You can also supply any other publicly available builders, such as those provided by [Heroku](https://devcenter.heroku.com/articles/buildpacks)or [Google](https://github.com/GoogleCloudPlatform/buildpacks).

## Conclusion

By creating your own custom buildpacks and builders, you gain complete control over how your code is compiled. And thanks to Epinio’s ability to utilize custom builders, integrating your own builder into established build and deployment workflows is as simple as a single command line argument.

### Learn more about Epinio! Read [Mario Manno](https://community.suse.com/members/8310471)'s post,  [New Ideas on How to Install Epinio](https://community.suse.com/posts/new-ideas-on-how-to-install-epinio).
