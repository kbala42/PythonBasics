dosya=open("dene.txt", "w+")
dosya.write("olmayan dosya oluşturuldu")
dosya.seek(0)
print(dosya.read(10))
dosya.close()