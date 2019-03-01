"""Sample test case(s)."""

from logging import getLogger

import pytest

LOGGER = getLogger()


@pytest.fixture(scope='module')
def constructor(request):
    """Constructor fixture."""
    yield


def test_dummy():
    """Sample test case."""
    LOGGER.info('Running test case.')
