collectd
########

.. image:: https://travis-ci.org/adarnimrod/collectd.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/collectd

Provision collectd. Configuration templates can be placed inside
:code:`templates/collectd.conf.d` either inside the role or relative to the
playbook. Out of the box the only plugin used is log to syslog.

Requirements
------------

See :code:`meta/main.yml` and assertions at the top of :code:`tasks/main.yml`.

Role Variables
--------------

See :code:`defaults/main.yml`.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

Testing requires Python 2.7, Tox, Vagrant and Virtualbox. To test simply run
:code:`tox`. `Pre-commit <http://pre-commit.com/>`_ is also setup for this
project.

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
