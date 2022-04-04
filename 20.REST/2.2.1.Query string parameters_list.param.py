import requests

response=requests.get('https://jsonplaceholder.typicode.com/todos',params={
    'userId':1,
    'completed':'true'
})

list=response.json()

print(list[0]["title"])


