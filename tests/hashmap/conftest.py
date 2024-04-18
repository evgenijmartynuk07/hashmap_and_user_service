import pytest

from hashmap.main import HashMap


@pytest.fixture(scope="function")
def hashmap():
    return HashMap()
