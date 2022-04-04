class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

p1=Product("Samsung S10",5000)
print(p1)
print("-------------------")
print(p1.__dict__)
print("-------------------")

import json
with open("urunler.json","w") as file:
    json.dump(p1.__dict__,file)