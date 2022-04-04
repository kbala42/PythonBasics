"""
Rastgele elli sayı üreten program
"""
import random
sayilar=[]
for i in range (50):
    sayi=str(random.randint(0,1000))+"\n"
    sayilar.append(sayi)
dosya=open("sayi.txt","w")
dosya.writelines(sayilar)
dosya.close()