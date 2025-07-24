import requests
import pytest


URL = 'https://api.pokemonbattle.ru'
HEADER = {'Content-Type':'application/json','trainer_token':'9a0d0276787ae9c3fd032734878dcabb' }
body_pokemons = {
    "name": "Бульбазавр",
    "photo_id": 12
}
def test_status_code():
    response = requests.get(url= f'{URL}/v2/trainers',headers = HEADER)
    assert response.status_code == 200

def test_status_code_id():
    response_1 = requests.get(url= f'{URL}/v2/trainers/38130',headers = HEADER)
    assert response_1.status_code == 200