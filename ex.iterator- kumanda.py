class Kumanda:
    def __init__(self,kanalListesi):
        self.kanalListesi = kanalListesi
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index < len(self.kanalListesi):
            return self.kanalListesi[self.index]
        else:
            self.index = -1
            raise StopIteration

liste=["Atv", "Trt","Star", "Show"]
for i in liste:
    print(i)
kumanda = Kumanda(liste)

iterator = iter(kumanda)

print("-----------------------")
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
