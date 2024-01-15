import requests,json, pytest

baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '151'

# test valid response or response is not empty
def test_getPetById_response():
    url = baseURI + petID
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    print(json.dumps(data, indent=3))
    assert len(data) > 0, "empty response"

def test_getPetById_id():
    url = baseURI + petID
    header = {'Content-Type': 'application/json'}
    print ("RequestURL: ", url)
    response = requests.get(url, verify=False, headers=header)
    data = response. json()
    assert data['id'] == 151

def test_addNewPet():
    url = baseURI
    header = {'Content-Type': 'application/json'}
    payload = {"id": 191, "name": "Cutie", "status": "available"}
    response = requests.post(url, verify=False, json=payload, headers=header)
    data = response.json()
    assert data['id'] == 191
    assert len(data) > 0
    print(data)