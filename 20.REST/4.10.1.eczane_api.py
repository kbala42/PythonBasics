import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 7y6402nf3JlgOOXjpHrC6l:0ntMNqbmC6oDidBA5xCLEs"
    }

conn.request("GET", "/health/dutyPharmacy?ilce=%C3%87ankaya&il=Ankara", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))