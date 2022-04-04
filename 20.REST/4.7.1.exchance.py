import requests
import json

API_KEY = "8e0ec9e8c2304b020bdeb2905b35f2f3"
api_url="http://api.exchangeratesapi.io/v1/latest?access_key="+API_KEY

result = requests.get(api_url)
result = json.loads(result.text)
print(result)

