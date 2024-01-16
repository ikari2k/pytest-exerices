from utils.my_utils import getAPIData
from utils.congigParser import *
import requests,json, pytest

baseURI = getPetAPIURL()
petID = '191'

# test valid response or response is not empty
def test_getPetById_response():
    url = baseURI + petID
    data, resp_status, timeTaken = getAPIData(url)
    assert data['id'] == int(petID)
    assert resp_status == 200
    print('Time Taken: ', timeTaken)

def test_addNewPet():
    url = baseURI
    header = {'Content-Type': 'application/json'}
    payload = {"id": 191, "name": "Cutie", "status": "available"}
    response = requests.post(url, verify=False, json=payload, headers=header)
    data = response.json()
    assert data['id'] == 191
    assert len(data) > 0
    print(data)