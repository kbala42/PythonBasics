import requests

headlines_url="https://newsapi.org/v2/top-headlines"
api_key="394e51ddf87843fea39a574c04c846a4"

response=requests.get(headlines_url,params={
    "apiKey":api_key,
    "country":"tr"
})

haberler= response.json()["articles"]

for i in haberler:
    print(i["source"]["name"])
    print(i["title"])
    print(i["url"])
