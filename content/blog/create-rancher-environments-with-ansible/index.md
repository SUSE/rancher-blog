---
title: "Create Rancher Environments with Ansible"
date: 2017-10-04T10:17:00
slug: "create-rancher-environments-with-ansible"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["installation"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86641
  original_url: "https://www.suse.com/c/rancher_blog/create-rancher-environments-with-ansible/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x Ansible playbooks"
  redirect_target: "docs.rancher.com"
---

Attention, Ansible users! We’ve released the first version of our
[Ansible
playbooks](http://docs.ansible.com/ansible/latest/playbooks.html) for
Rancher. Ansible is a configuration management system that allows you to
write instruction manuals it uses to manage local and remote systems.
These playbooks give full control over the installation and
configuration of Rancher server and agent nodes, with features that
include:

- Static inventory
- Dynamic inventory via EC2 tags
- Detection of multiple servers and automatic configuration of HA
- Support for local, bind-mount, and external databases
- Optional, local HAProxy with SSL termination for single-server
  deployments
- [Ansible
  Vault](http://docs.ansible.com/ansible/latest/playbooks_vault.html)
  for secure storage of secrets

This first release is for Ubuntu and Debian, and it targets EC2 as a
provider. Upcoming releases will support yum-based systems (RHEL,
CentOS, and Fedora) and will add support for other providers for whom
dynamic inventory modules exist. To get started, visit our [Ansible
playbooks repository](https://github.com/rancher/ansible-playbooks) on
GitHub. There you will find instructions for [general
installation](https://github.com/rancher/ansible-playbooks/blob/master/INSTALL.md)
and [setting up
EC2](https://github.com/rancher/ansible-playbooks/blob/master/INSTALL_EC2.md).
