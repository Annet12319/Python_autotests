import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Бульба",
    "photo_id": 1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json)

pokemon_id = response_create.json() ['id']

body_changename = {
    "pokemon_id": pokemon_id,
    "name": "Бимба",
    "photo_id": 1
}

response_changename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changename)
print(response_changename.json)

body_addpokeball = {
    "pokemon_id": pokemon_id
}

response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeball)
print(response_addpokeball.json)