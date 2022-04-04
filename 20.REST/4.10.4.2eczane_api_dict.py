import requests

url="https://api.collectapi.com/health/dutyPharmacy?ilce=%C3%87ankaya&il=Ankara&authorization=apikey 7y6402nf3JlgOOXjpHrC6l:0ntMNqbmC6oDidBA5xCLEs&content-type=application/json"

response=requests.get(url)

#haberler= response.json()

print(response)