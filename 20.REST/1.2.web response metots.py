import requests

responce=requests.get('https://jsonplaceholder.typicode.com/todos')

sonuc=responce

print(sonuc)
print(type(sonuc))
print(sonuc.status_code)
print(sonuc.headers)
print(sonuc.headers["Content-Type"])
print(sonuc.url)
print(sonuc.encoding)
print(sonuc.text)
print(type(sonuc.text))