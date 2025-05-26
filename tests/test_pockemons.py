import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '33537'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200 

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id':TRAINER_ID})
    data = response_get.json()["data"]
    assert data[0]["trainer_name"] == "Anita"

@pytest.mark.parametrize('key, value', {('trainer_name', 'Anita'), ('id', TRAINER_ID), ('level', '5')})
def test_parametrize(key, value):
       response_parametrize = requests.get(url = f'{URL}/trainers', params= {'trainer_id':TRAINER_ID})
       assert response_parametrize.json()["data"][0][key] == value