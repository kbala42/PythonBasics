import requests

url="http://api.weatherapi.com/v1/current.json"
api_key=" 530d7feb5bc24ef8a7073612212207"

response=requests.get(url,params={
    "key":api_key,
    "q":"Konya",
    "lang":"tr"
})

sonuc = response.json()

print(sonuc)
print("----------------------")
print(sonuc["location"]["region"])
print("----------------------")
sehir=sonuc["location"]["region"]
havaDurumu=sonuc["current"]["temp_c"]
print(havaDurumu)
text = sonuc["current"]["condition"]["text"]
print(text)
print("----------------------")
print(f"{sehir} şu anda {havaDurumu} derece ve {text}.")