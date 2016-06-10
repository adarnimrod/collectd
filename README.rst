collectd
########

An Ansible role to install and configure collectd. Configuration templates can
be placed inside :code:`templates/collectd.conf.d` either inside the role or
relative to the playbook. Out of the box the only plugin used is log to syslog.

Requirements
------------

- `Ansible 2.0 or later <https://www.ansible.com/>`_.
- Supported OSes:
  - `OpenBSD 5.9 <http://www.openbsd.org/>`_ (previous versions should
    also work but aren't tested).
  - `Debian Jessie <https://www.debian.org/>`_ (previous versions and other
    distros based on Debian should work but aren't tested).

Role Variables
--------------

None.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

To install the dependencies:

.. code:: shell

    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD)

To run the full test suite:

.. code:: shell

    molecule test

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.
