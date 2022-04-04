'''
---------------------------------------------------------tw:@tek_elo
Dosyaya yazma işlemi
--------------------------------------------------------------------
'''
# 'merhaba.txt' dosyasını yalnızca okunur olarak açıyoruz
dosya=open('merhaba.txt','r')
# dosyanın içeriğini yazdırıyoruz
print(dosya.read())
#dosyayı kapatıyoruz
dosya.close()

# Yazma işlemini hemen geçmemesi için kullanıcının herhangi bir tuşa basması için bekletiyoruz
input("bekle")

# dosyaya write metodunda verilen stringi yazıyoruz. Yazma sırasında önce ki içerik siliniyor
dosya=open('merhaba.txt','w')
dosya.write('bu dosya silinip yeniden yazildi')
dosya.close()

# Yazma işlemini hemen geçmemesi için kullanıcının herhangi bir tuşa basması için bekletiyoruz
input("bekle")

# 'merhaba.txt' dosyasını yalnızca okunur olarak açıyoruz
dosya=open('merhaba.txt','r')
# dosyanın içeriğini yazdırıyoruz
print(dosya.read())
#dosyayı kapatıyoruz
dosya.close()
