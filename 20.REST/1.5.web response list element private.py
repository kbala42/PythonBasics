import requests
import json

responce=requests.get('https://jsonplaceholder.typicode.com/todos')

sonuc=responce

todos=json.loads(sonuc.text)


for item in todos:
    if (item["userId"]==1):
        print(item["title"])
