import pytest
from test_utils.my_utils import *
from test_utils.congigParser import *

baseURI = getPetAPIURL()
petID = '191'

@pytest.fixture()
def setup():
    url = baseURI
    payload = {"id": int(petID), "name": "Cutie", "status": "available"}
    data, resp_status, timeTaken = postAPIData(url, payload)
    assert data['id'] == int(petID)

# test valid response or response is not empty
def test_getPetById_response():
    url = baseURI + petID
    data, resp_status, timeTaken = getAPIData(url)
    assert data['id'] == int(petID)
    assert resp_status == 200