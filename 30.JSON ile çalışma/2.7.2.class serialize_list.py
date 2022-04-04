class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

p1=Product("Samsung S10",5000)
p2=Product("Samsung S11",6000)
products=[p1.__dict__,p2.__dict__]

print(products)

import  json
with open("urunler.json","w") as file:
    json.dump(products,file)