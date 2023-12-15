import requests

url = 'https://api.breakingbadquotes.xyz/v1/quotes'

response = requests.get(url)
data = response.json()

print('status ',response.status_code)
print('content ',response.content)
print('text ',response.text)
print('json ',response.json())
print(data[0])
print(data[0]['author'])
