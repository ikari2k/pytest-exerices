import pytest
@pytest.fixture()
def setup_list():
    print("\n in fixtures.. \n")
    city = ['New york', 'London', 'Mumbai', 'Kraków']
    return city

def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'New york'
    assert setup_list[::2] == ['New york','Mumbai']

def test_getItem2(setup_list):
    assert setup_list[::-2] == ['Kraków','London']