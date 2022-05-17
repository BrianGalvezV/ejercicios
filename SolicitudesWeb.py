import requests

response = requests.get('https://www.platzi.com')

print(dir(response))