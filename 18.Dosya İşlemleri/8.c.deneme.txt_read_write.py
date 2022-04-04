"""
okuma ve yazma kipi
"""
dosya=open("deneme.txt","r+")
belge=dosya.read()
print(belge)
dosya.write("\n bu metin sona eklendi")
dosya.close()