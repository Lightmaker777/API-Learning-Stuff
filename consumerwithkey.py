import requests

url = 'https://api.nettoolkit.com/v1/account/test-api-keys'
headers = {'X-API-KEY':'test_wSJAzw1HB4xDxw5QObiJCaKXOupQCxAfi5gjif0N'}


response = requests.get(url,headers=headers)
data = response.json()

print('status ',response.status_code)
print('content ',response.content)
print('text ',response.text)
print('json ',response.json())
print('data ',data['code'])
print('results',data['results'])
print('results',data['results'][0])