from utils.testConfigParser import *
from utils.my_utils import getAPIData,postAPIData,putAPIData
import pytest, logging
LOGGER = logging.getLogger(__name__)

baseURI = getPetAPIURL()
petID = '191'

def test_postAPI():
    payload = {"id": int(petID), "name": "Cutie", "status": "available"}
    data, resp_status, timeTaken = postAPIData(baseURI, payload)
    LOGGER.info('API Call Done')
    assert data['id'] == int(petID)
    assert resp_status == 200

# test valid response or response is not empty
def test_getPetById_response():
    data, resp_status, timeTaken = getAPIData(baseURI + petID)
    assert data['id'] == int(petID)
    assert resp_status == 200
    print('Time Taken:', timeTaken)

def test_updatingPet():
    payload = {"id": int(petID), "name": "Cutie", "status": "pending"}
    data, resp_status, timeTaken = putAPIData(baseURI, payload)
    assert data['id'] == int(petID)
    assert resp_status == 200