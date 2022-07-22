import ape
import pytest


@pytest.fixture(scope="session")
def alice(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def return_types(alice):
    return ape.project.ReturnTypes.deploy(sender=alice)