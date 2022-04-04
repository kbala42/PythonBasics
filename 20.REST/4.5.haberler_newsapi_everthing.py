import requests

everything_url="https://newsapi.org/v2/everything"
api_key="394e51ddf87843fea39a574c04c846a4"

response=requests.get(everything_url,params={
    "apiKey":api_key,
    "q":"futbol",
    "language":"tr",
    "sortBy":"publishedAt"
})

haberler= response.json()["articles"]

for i in haberler:
    print(i["source"]["name"])
    print(i["title"])
    print(i["url"])
