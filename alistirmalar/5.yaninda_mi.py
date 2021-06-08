"""
    Yanında Mı?
    Vural ve Fatih yakın arkadaşlar. Listede yan yana duruyorlarsa fonksiyon True döndürmeli.
    Aralarında isim varsa False döndürmeli.
"""
def arkadas(liste):
    if liste.index("Vural") == liste.index("Fatih")+1:
        return True
    if liste.index("Vural") == liste.index("Fatih")-1:
        return True
    return False

print(arkadas(["Ali","Vural","Fatih","Ekrem"]))
print("----------------------------------------")
print(arkadas(["Ali","Vural","Ekrem","Fatih"]))