#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor
# www.pythondiario.com
 
import socket
import sys
 
# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace de socket y puerto
server_address = ("", 5000)
print('empezando a levantar %s puerto %s' % server_address)
sock.bind(server_address)
	
# Escuchando conexiones entrantes
sock.listen(1)
	
while True:
    # Esperando conexion
    log = open("log_servidor.txt","a")
    print('Esperando para conectarse')
    connection, client_address  = sock.accept()
 
    try:
        print('conexion desde '+client_address[0])
        while True:
            databyte = connection.recv(19)
            data = databyte.decode()
            print('recibido '+ data)
            log.write("IP: " + str(client_address[0]) + data + "\n")
            #if data:
            print('enviando respuesta a cliente')
            mensaje = "Bienvenido, cliente "
            mensajebyte = mensaje.encode('utf-8')
            connection.sendall(mensajebyte)
            #else:
            break
             
    finally:
        log.close()
        connection.close()
