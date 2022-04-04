import requests
import json

api_url="http://api.exchangeratesapi.io/v1/latest?access_key=8e0ec9e8c2304b020bdeb2905b35f2f3"

result = requests.get(api_url)
print(result)
print("------------------------------------------")
result = json.loads(result.text)
print(result)