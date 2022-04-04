import requests

response=requests.get('https://jsonplaceholder.typicode.com/todos?completed=true&userId=1')

print(response)
print("---------------------")
print(response.text)
print("---------------------")
print(response.json())

