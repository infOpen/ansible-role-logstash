"""
Role tests
"""
import pytest


# pytestmark = pytest.mark.docker_images(
pytestmark = pytest.mark.docker_images('infopen/ubuntu-xenial-ssh-py27:0.2.0')


def test_packages(Package):
    """
    Tests about packages installed on all systems
    """

    packages = [
        'python-apt-common', 'python-apt', 'logstash', 'openjdk-8-jre'
    ]

    for package in packages:
        assert Package(package).is_installed is True


def test_group(Group):
    """
    Test about logstash group
    """

    assert Group('logstash').exists


def test_user(User):
    """
    Test about logstash user
    """

    user = User('logstash')

    assert user.exists
    assert user.group == 'logstash'
    assert user.shell == '/usr/sbin/nologin'
    assert user.home == '/var/lib/logstash'


def test_service(Command, Service):
    """
    Test about logstash service
    """

    assert Service('logstash').is_enabled
    assert Service('logstash').is_running
    assert Command('systemctl status logstash').rc == 0
