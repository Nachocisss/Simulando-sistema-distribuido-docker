#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys
import struct
import threading

def principal():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("", 5001)
    sock.bind(server_address)

    # --------- CONEXION CON SERVIDOR---------

    sock.listen(1)
    print('Esperando para conectarse')
    connection, client_address  = sock.accept() 
    print('conexion desde servidor IP ='+ client_address[0])

    log = open("data.txt","a")
    databyte = connection.recv(1024)
    data = databyte.decode()
    print('conexion servidor? : '+ data)
    print('RESPONDIENDO')
    mensaje = "te has conectado al nodo 1 "
    mensajebyte = mensaje.encode('utf-8')
    connection.send(mensajebyte)

    # --------- MENSAJE DE SERVIDOR ---------
    try: 
        databyte = connection.recv(1024)
        data = databyte.decode()
        print('Mensaje del cliente -> servidor: '+ data)
        print('RESPONDIENDO')
        log.write(data + "\n")
        mensaje = "MENSAJE RECIBIDO"
        mensajebyte = mensaje.encode('utf-8')
        connection.send(mensajebyte)

    except:
        mensaje = "NODO 1 DICE: NO SE RECIBIO NADA "
        mensajebyte = mensaje.encode('utf-8')
        connection.send(mensajebyte)

    finally:
        sock.close()
        connection.close()
        log.close()
#-------------------------------------------------------------------
#-------------------------------- Thread 2 -------------------------
#-------------------------------------------------------------------
def chequeo():
    MCAST_GRP = '224.3.29.71'
    MCAST_PORT = 5007

    sock_mcast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock_mcast.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_mcast.bind((MCAST_GRP, MCAST_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

    sock_mcast.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

#----- Seteo socket para respuesta al Multicast a Servidor -----
    multicast_group = '224.3.29.71'
    server_address = ('', 5001)
    sock_pr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_pr.bind(server_address)
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock_pr.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        #----- Se recibe solicitud de multicast -----#
        print('----- ...esperando solicitudes... -----')
        data, address = sock_mcast.recvfrom(1024)
        print(data)
        if(data=="MC"):
            print('Enviando respuesta confirmando mi estado activo.')
            sock_pr.sendto('1', address)

threads = []

t = threading.Thread(target=principal)
threads.append(t)
t.start()

t2 = threading.Thread(target=chequeo)
threads.append(t2)
t2.start()
