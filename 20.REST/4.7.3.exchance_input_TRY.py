import requests
import json

API_KEY = "8e0ec9e8c2304b020bdeb2905b35f2f3"
api_url="http://api.exchangeratesapi.io/v1/latest?access_key="+API_KEY

bozulan_doviz = input("Bozulan döviz türü: ")
alinan_doviz = input("Alınan döviz türü: ")
miktar=int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

apiURL=api_url+"&"+ "symbols =" + bozulan_doviz
result = requests.get(apiURL)
result = json.loads(result.text)
print("1 {0} = {1} {2}".format(bozulan_doviz, result["rates"][alinan_doviz],alinan_doviz))

print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar * result["rates"][alinan_doviz],alinan_doviz))
