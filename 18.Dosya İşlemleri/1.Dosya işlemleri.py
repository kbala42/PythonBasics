'''
---------------------------------------------------------tw:@tek_elo
Programın yerleştirildiği klasörde ki dosyayı açmak için open
fonksiyonu kullanılır
--------------------------------------------------------------------
'''
# open fonksiyonunda merhaba.txt dosyanın adı,
# 'r' parametresi yalnızca okuma işlemi yapıldığını gösterir
dosya=open("merhaba.txt",'r')
print(type(dosya))

#read metodu dosya nesnesinin içeriğini okuyarak veri nesnesinde saklıyoruz
veri=dosya.read()

# dönüüşüm string şeklinde
print(type(veri))
# str tipinde ki 'veri' yi yazdırıyoruz
print(veri)

print('_____________________')

# veri yi boşluklardan ayırarak liste'ye dönüştürüyoruz
ayrik=veri.split(' ')
# ayrik tipini yazdırıyoruz
print(type(ayrik))
# ayrik listesini yazdırıyoruz
print(ayrik)

print('_____________________')

# ayrik liste şeklinde olduğundan herbir elemanına ulabiliyoruz
print("ilk kelime:",ayrik[0])
print("ikinci kelime:",ayrik[1])
# İşlemlerimiz bittikten sonra dosya'yı kapatıyoruz
dosya.close()