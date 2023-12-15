import requests


params = {
    'pokemon':'pokemon',
    '_quantity':25
}
url = 'https://fakerapi.it/api/v1/custom'
response = requests.get(url,params=params)

print(response.json())
