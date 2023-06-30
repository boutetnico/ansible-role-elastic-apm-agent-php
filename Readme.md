[![tests](https://github.com/boutetnico/ansible-role-elastic-apm-agent-php/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-elastic-apm-agent-php/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.elastic_apm_agent_php-blue.svg)](https://galaxy.ansible.com/boutetnico/elastic_apm_agent_php)

ansible-role-elastic-apm-agent-php
==================================

This role installs [Elastic APM PHP agent](https://www.elastic.co/guide/en/apm/agent/php/current/index.html).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable                           | Required | Default                       | Choices | Comments      |
|------------------------------------|----------|-------------------------------|---------|---------------|
| elastic_apm_php_agent_dependencies | yes      | `[apt-transport-https,gnupg]` | list    |               |
| elastic_apm_php_agent_version      | yes      | `1.0.1`                       | string  |               |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-elastic-apm-agent-php

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
