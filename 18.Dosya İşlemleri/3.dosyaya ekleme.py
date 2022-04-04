'''
---------------------------------------------------------tw:@tek_elo
Dosyaya yazma işlemi
--------------------------------------------------------------------
'''
def dosya_oku():
    dosya = open("kayitlar.txt", "r")
    belge=dosya.read()
    print(belge)
    dosya.close()

dosya_oku()
input("bekle")

dosya=open("kayitlar.txt","a")
dosya.write("001 hasan kara 00001233\n")
dosya.close()

dosya_oku()
input("bekle")

dosya=open("kayitlar.txt","a")
for i in range(5):
    dosya.write("2021"+str(i)+ " hasan kara 00001233 \n")
dosya.close()

dosya_oku()
input("bekle")