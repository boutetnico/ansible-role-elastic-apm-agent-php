import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("apm-agent-php"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed
