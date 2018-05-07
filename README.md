# amtega.iptables

This is an [Ansible](http://www.ansible.com) role to configure a iptables based firewall segmented by zones

## Requirements

- Ansible >= 2.4


## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`.

## Dependencies

-amtega.network_interfaces ( if you want use the rol with defaults vars )

## Example Playbook

This is an example playbook:

```yaml
---

- hosts: all
  roles:
    - amtega.iptables
```

## Testing
Role was writen for CentOS 6 & 7 and EL 6 & 7

This role not use docker for test, since iptables need kernel specific modules to run.
Deploy n virtual machines to test the rol and configure a inventory in amtega.iptables/test/inventory

Create a task in amtega.iptables/test/main.yml with the following content:
- name: test iptables role
  hosts: <severs>
  roles:
    - amtega.iptables
  tags:
    - idempotence

You can run the test with following commands:
```shell
$ cd amtega-iptables/test
$ ansible-playbook main.yml -i inventory
```

## License

Copyright (C) <YEAR> AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify
it under the terms of:
GNU General Public License version 3, or (at your option) any later version;
or the European Union Public License, either Version 1.2 or – as soon
they will be approved by the European Commission ­subsequent versions of
the EUPL;

This role is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details or European Union Public License for more details.

## Author Information

- José Enrique Mourón Regueira
