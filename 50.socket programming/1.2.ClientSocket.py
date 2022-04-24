# -*- coding: utf-8 -*-
"""
Client Uygulaması
"""

import socket

#Bir socket nesnesi üretiyoruz
client_socket = socket.socket()

client_socket.connect(('localhost', 50000))

mesaj = 'Sunucu, merhaba '

cikis_mesaji = mesaj

client_socket.send(bytes(cikis_mesaji,'utf-8'))


