import requests

response=requests.get('https://jsonplaceholder.typicode.com/todos?completed=true&userId=1')

list=response.json()

print(list)
print("-----------------")
print(list[0]["title"])


