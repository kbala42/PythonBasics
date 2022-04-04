import requests
import json

responce=requests.get('https://jsonplaceholder.typicode.com/todos')

sonuc=responce

print(sonuc.text)
print(type(sonuc.text))
print(json.loads(sonuc.text))
print(type(json.loads(sonuc.text)))