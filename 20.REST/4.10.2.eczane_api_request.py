import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 7y6402nf3JlgOOXjpHrC6l:0ntMNqbmC6oDidBA5xCLEs"
    }

il=input("ili giriniz: ")
ilce=input("İlçe giriniz: ")
sorgu= "/health/dutyPharmacy?ilce="+ilce+"&il="+il

conn.request("GET",sorgu , headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

