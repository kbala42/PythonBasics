"""
 Girilen sayının carpanlarını yazdıran "carpanlar" adında bir fonksiyon yazdırın
"""
def carpanlar(sayi):
    carpan_listesi=[]
    for i in range(1,sayi+1):
        if sayi%i == 0:
            carpan_listesi.append(i)
    return carpan_listesi
    
print(carpanlar(144))