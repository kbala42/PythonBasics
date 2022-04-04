class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price


import  json
with open("urunler.json") as file:
    data=json.load(file)

urunler=[]

for p in data:
    urunler.append(Product(p["name"],p["price"]))

print(urunler)
print("------------")
print(urunler[0].name)