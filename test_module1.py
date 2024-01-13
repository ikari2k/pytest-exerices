import pytest

#pytestmark = [, pytest.mark.slow]

def test_a1():
    assert 5+5 == 10
    assert 10 - 5 == 5

@pytest.mark.sanity
def test_a2():
    assert 9 / 5 == 3