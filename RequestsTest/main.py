import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = '9a0d0276787ae9c3fd032734878dcabb'
HEADER = {'Content-Type':'application/json','trainer_token':'9a0d0276787ae9c3fd032734878dcabb' }
body_pokemons = {
    "name": "Бульбазавр",
    "photo_id": 12
}
body_put = {
    "pokemon_id": "362768",
    "name": "New Name",
    "photo_id": 2
}
body_add = {
    "pokemon_id": "362768"
}

response = requests.post(url= f'{URL}/v2/pokemons',headers = HEADER, json = body_pokemons )
print(response.text)

response_1 = requests.put(url= f'{URL}/v2/pokemons',headers = HEADER, json = body_put )
print(response_1.json())

response_2 = requests.post(url= f'{URL}/v2/trainers/add_pokeball',headers = HEADER, json = body_add )
print(response_2.json())