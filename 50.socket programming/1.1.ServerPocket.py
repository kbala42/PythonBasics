# -*- coding: utf-8 -*-
"""

TCP SERVER SOCKET Programı

"""

import socket

#socket nesnesi oluşturuyoruz
server_socket = socket.socket()

server_socket.bind(('localhost', 50000))

# soketimi 5 istemciyi dinlemeye başlıyor
server_socket.listen()
print('Soket oluşturuldu. Bağlantı bekleniyor...')

while True:
    #istemciden istek gelinceye kadara bekler, istek geldiğinde accept metodu
    # bir soket oluşturur
    client_socket, adres = server_socket.accept()
    print(adres, ' isimli bilgisayar ile bağlantı kuruldu')
    
    # gelen 1024 bayt mesaj decode edilerek stringe çevrilir
    gelen_mesaj = client_socket.recv(1024).decode()
    
    #mesajı ekrana yazdırıyoruz 
    print(gelen_mesaj)
    
    # soketi kapatıyoruz
    client_socket.close()
    
    # exit mesajı gelmişse sunucu sonlandırıyoruz
    if(gelen_mesaj == 'exit'):
        break

print('Hoşçakalın...')
server_socket.close()



