def test_collectd(Service):
    assert Service('collectd').is_running
