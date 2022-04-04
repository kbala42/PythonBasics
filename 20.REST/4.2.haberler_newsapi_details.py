import requests

url="https://newsapi.org/v2/top-headlines?country=us&apiKey=394e51ddf87843fea39a574c04c846a4"

response=requests.get(url)

haberler= response.json()["articles"]

for i in haberler:
    print(i["source"]["name"])
    print(i["title"])
    print(i["url"])
