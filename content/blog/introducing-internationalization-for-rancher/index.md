---
title: "Introducing Internationalization for Rancher"
date: 2016-07-06T10:20:00
slug: "introducing-internationalization-for-rancher"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["developer-experience"]
content_type: "explainer"
draft: true
migration:
  wp_id: 86745
  original_url: "https://www.suse.com/c/rancher_blog/introducing-internationalization-for-rancher/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x UI localization"
  redirect_target: "rancher.com/blog (hub)"
---

Rancher has users all over the world, and for a long time we’ve wanted
to internationalize our UI. Recently, this project became a reality and
I embarked on the simple, yet massive, task of making our UI
i18n-compliant. The task itself did not present a massive engineering
challenge; short of hot loading translations scripts as to not bloat the
UI javascript, the majority of the project was moving strings around. I
won’t focus on that effort here - what I want to draw your attention to
is how to develop and add new translations to the UI. We are using the
fantastic
[ember-intl](https://github.com/jasonmit/ember-intl/tree/master/packages/ember-intl)
framework to bring i18n support to the Rancher UI. If you have any
questions on how the translation yaml file is consumed, or on the APIs
we are using, I would refer to
their [wiki](https://github.com/jasonmit/ember-intl/wiki) first.
Hopefully you won’t need to, as we’ve tried to make this as easy for our
end user as possible.

### Getting Started with Translation

Translation files can be found in the Rancher UI GitHub repo in the
[translations](https://github.com/rancher/ui/tree/master/translations)
folder. You’ll also find a simple
[readme](https://github.com/rancher/ui/blob/master/translations/README.md) that
highlights the main points of this blog post. To get started, either
create a new translations file here or copy and rename the `en-us.yaml`
file (I suggest the latter, this will ensure you have all the latest
localizable keys). Note: Regardless of the method of creation, the file
name must match a locale in this [supported locale
list](https://github.com/andyearnshaw/Intl.js/tree/master/locale-data/jsonp).
Next, start the ember server as you normally would. If you started with
a fresh yaml translation file instead of copy/renaming the English file,
you may see ember-intl print a large wall of text about missing
translations. This is a feature ember-intl provides to showcase the
missing keys in translations file from the default loaded language
(Rancher defaults to en-us). This tool is especially useful to
translation maintainers, as the only translations Rancher maintains at
the time of this post are en-us and zh-Hans-CN. At this point, you’re
ready to translate, and in most cases this is as simple as replacing the
English value with your locale’s value throughout the translation file.
Do not change the key names: those should remain in English. These keys
are the same in every translation file and are simply the keys consumed
by ember-intl to map translation values.

### Variable Substitution and Pluralization

There are a couple items I would like to address that may not be as cut
and dry as we’d like. First is variable substitution. Lets take the
following key as an example:

```
 unrestricted: "{appName} is configured to allow access to any {github} user."
```

The strings appName and github that are wrapped in mustaches are
variables. When dealing with values like this in the translation file,
simply keep the mustaches and variable name, and add it to your
translation value where the variable would be appropriate in your
language. The second item to address is pluralization. We have cases
where text may or may not be plural based on some incoming variable. The
following example showcases this:

```
 restricted: |
{appName} is configured to allow access to environment members, {orgs, plural,
=0 {no organizations}
=1
other
} and {users, plural,
=0 {no users}
=1
other
}.
```

As you can see, we have the `appName` variable as before, but we also
have this new multiline content. This is how ember-intl deals with
pluralization. In the first pluralization, the variable `orgs` is our
check for pluralization. So if `orgs` is 0, we print the string
`no organizations`. If `orgs` is 1, we print the string `# organization`
where `#` is replaced with the `orgs` variable value and so on. It’s
really quite clever on ember-intl’s part, even if it is quite confusing
to read at first. As you’re working, you may want to see missing
translations or simply toggle between languages. In the lower right of
the UI, you will find a new Language Dropdown. You can also take
advantage of a new shortcut and use `SHFT+L` to toggle between a special
`None` language and the last selected language. When using this special
`None` language, all keyed strings will be replaced with a string
highlighting the path to the value in the translation file or you will
see a `*%MISSING%*` message. This provides a simple way for the
developer to see the path of the key in the translation file or that the
translation is missing respectively. Please note the API has not been
internationalized, so strings that are received from the API (e.g.,
status messages or logs) will not be translated.

### Contributing a New Translation

If you’d like to add a translation to Rancher’s UI, feel free to open a
pull request after you’ve created your translation. Please take into
account that we do not maintain third party translations, so as we
change the UI and add/remove content, the English and Chinese
translations will change and your translation will fall out of sync.
This is where the missing translations tool mentioned above will come in
handy. That’s the basics of adding a new translation file. Again, we’ve
attempted to make this as simple to the end user and translation
maintainers as possible. If you have any questions, as usual feel free
to reach out to us over on the [forums](https://forums.rancher.com/) or
on GitHub!
*[![Wes_Author](images/rancher_blog_IMG_0568-150x150.jpg)](https://cdn.rancher.com/wp-content/uploads/2016/07/05170317/IMG_0568.jpg)Wes
works on all things UI at Rancher Labs.*
