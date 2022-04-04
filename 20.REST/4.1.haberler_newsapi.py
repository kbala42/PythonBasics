import requests

url="https://newsapi.org/v2/top-headlines?country=us&apiKey=394e51ddf87843fea39a574c04c846a4"

response=requests.get(url)

haberler= response.json()

print(haberler)
print("---------------------")
print(haberler["articles"][0])
print("---------------------")