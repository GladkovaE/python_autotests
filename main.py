import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'абракадабра'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN}
body = {
    "name": "olen",
    "photo_id": 1
    }
name_change = {
    "pokemon_id": "190118",
    "name": "Olen2",
    "photo_id": 1
}
pokeball = {
    "pokemon_id": "190115"
}
'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body)
print(response.text)'''

'''response_change = requests.put(url= f'{URL}/pokemons',headers = HEADER, json = name_change)
print(response_change.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = pokeball)
print(response_pokeball.text)
