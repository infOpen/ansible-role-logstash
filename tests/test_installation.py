"""
Role tests
"""

from testinfra.utils.ansible_runner import AnsibleRunner
import pytest

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('name', [
    ('python-apt-common'),
    ('python-apt'),
    ('logstash'),
    ('openjdk-9-jre'),
])
def test_packages(host, name):
    """
    Tests about packages installed on all systems
    """

    assert host.package(name).is_installed


def test_group(host):
    """
    Test about logstash group
    """

    assert host.group('logstash').exists


def test_user(host):
    """
    Test about logstash user
    """

    user = host.user('logstash')

    assert user.exists
    assert user.group == 'logstash'
    assert user.shell == '/usr/sbin/nologin'
    assert user.home == '/usr/share/logstash'


def test_service(host):
    """
    Test about logstash service
    """

    assert host.service('logstash').is_enabled
    assert host.service('logstash').is_running
    assert host.run('systemctl status logstash').rc == 0
