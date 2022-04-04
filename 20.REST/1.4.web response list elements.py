import requests
import json

responce=requests.get('https://jsonplaceholder.typicode.com/todos')

sonuc=responce

todos=json.loads(sonuc.text)
print(todos)

print(todos[0])

print(todos[0]['title'])

print("\n-------------------------\n")
for item in todos:
    print(item["title"])
