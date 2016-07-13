def test_collectd_service(Service):
    service = Service('collectd')
    assert service.is_running
    try:
        assert service.is_enabled
    except NotImplementedError:
        pass


def test_collectd_config(File, Command):
    assert Command('collectd -t').rc == 0
    assert File('/etc/collectd.conf').is_file or File(
        '/etc/collectd/collectd.conf').is_file
    assert File('/etc/collectd.conf.d').is_directory or File(
        '/etc/collectd/collectd.conf.d').is_directory


def test_collectd_alias(File, Ansible):
    ansible_os_family = Ansible('setup')['ansible_facts']['ansible_os_family']
    if ansible_os_family == 'Debian':
        assert File('/etc/aliases').contains('collectd: root')
    elif ansible_os_family == 'OpenBSD':
        assert File('/etc/mail/aliases').contains('_collectd: root')
