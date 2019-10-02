#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import socket
import sys
import time
 
# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(7)
# Conecta el socket en el puerto cuando el servidor este escuchando
server_address = ('127.0.0.1', 5000)
print ('conectando a ' + str(server_address[0]) + ' puerto '+ str(server_address[1]))
sock.connect(server_address)
log = open("registro_cliente.txt","a")
try:
    # Enviando datos
    message = 'Hola soy ' + server_address[0]
    messageByte = message.encode('utf-8')
    sock.sendall(messageByte)
    databyte = sock.recv(1024)
    data = databyte.decode()
    print ("Respuesta desde el servidor: " + data)
    log.write("Respuesta desde el servidor: " + data + "\n")
    databyte2 = sock.recv(1024)
    data2 = databyte2.decode()
    print ("servidor dice: " + data2)

    log.write(data2 + "\n")

finally:
    print('cerrando socket')
    log.close()
