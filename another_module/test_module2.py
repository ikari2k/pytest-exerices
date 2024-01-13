import pytest

pytestmark = [pytest.mark.sanity, pytest.mark.slow]

def test_a1():
    assert 1 == 1