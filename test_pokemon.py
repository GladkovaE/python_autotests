import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'абракадабра'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN}

response = requests.get(url = f'{URL}/trainers?trainer_id=12742', headers = HEADER)
print(response)
