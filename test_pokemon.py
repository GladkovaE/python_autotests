import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9316663ac6d6f2e589f7928fe94e6473'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN}

response = requests.get(url = f'{URL}/trainers?trainer_id=12742', headers = HEADER)
print(response)