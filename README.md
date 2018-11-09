# amtega.iptables

This is an [Ansible](http://www.ansible.com) role to configure an iptables based firewall segmented by zones.

## Requirements

[Ansible 2.7+](http://docs.ansible.com/ansible/latest/intro_installation.html)

## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`. The role setups the following facts:

- iptables_hostvars_zones: list of zones loaded from host vars.
- iptables_zones_managed: list of zones managed by the role.
- iptables_hostvars_services: list of services loaded from host vars.
- iptables_services_managed: list of services managed by the role.

## Dependencies

- [amtega.check_platform](https://galaxy.ansible.com/amtega/check_platform)
- [amtega.proxy_client](https://galaxy.ansible.com/amtega/proxy_client). If you need internet access to download packages fill this role variables.

## Example Playbook

This is an example playbook:

```yaml
---

- hosts: all
  roles:
    - amtega.iptables
  vars:
    iptables_zones:
      - name: SERVICE
        interfaces: eth0
        log: yes

    iptables_services:
      - name: ssh
        ports: 22
        zones: SERVICE

      - name: http
        protocol: tcp
        ports:
          - 80
          - 8080
        zones: SERVICE
```

## Testing

Tests are based on vagrant virtual machines. You can setup vagrant engine quickly using the playbook `files/setup.yml` available in the role [amtega.vagrant_engine](https://galaxy.ansible.com/amtega/vagrant_engine).

Once you have vagrant, you can run the tests with the following commands:

```shell
$ cd amtega-iptables/test
$ ansible-playbook main.yml
```

## License

Copyright (C) 2018 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify it under the terms of:

GNU General Public License version 3, or (at your option) any later version; or the European Union Public License, either Version 1.2 or – as soon they will be approved by the European Commission ­subsequent versions of the EUPL.

This role is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details or European Union Public License for more details.

## Author Information

- José Enrique Mourón Regueira
- Juan Antonio Valiño García
