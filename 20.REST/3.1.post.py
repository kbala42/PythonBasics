import requests

response=requests.post("https://jsonplaceholder.typicode.com/posts",data={
    "title": "deneme",
    "body": 'deneme',
    "userId": 1,
})

sonuc=response

print(sonuc)
print("---------------")
print(sonuc.text)
print("---------------")
print(sonuc.json())
print("---------------")
print(sonuc.headers)