#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Cliente
# www.pythondiario.com
 
import socket
import sys
 
# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Conecta el socket en el puerto cuando el servidor este escuchando
server_address = ('127.0.0.1', 5000)
print ('conectando a ' + str(server_address[0]) + ' puerto '+ str(server_address[1]))
sock.connect(server_address)
respuestas = open("respuestas.txt","a") 
try:
    message = 'Hola soy ' + server_address[0]
    messageByte = message.encode('utf-8')
    sock.sendall(messageByte)
    databyte = sock.recv(19)
    data = databyte.decode()
    print("Respuesta desde el servidor: " + data)
    respuestas.write("Respuesta desde el servidor: " + data + "\n")

finally:
    print('cerrando socket')
    respuestas.close()
    sock.close()