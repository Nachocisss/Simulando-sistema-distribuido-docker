#!/usr/bin/python
# -*- coding: utf-8 -*-
  
import socket
import sys
import random
import struct
import threading
import time

def principal():
    #------------------------- CONECTAR CLIENTE -------------------------------

    # Creando el socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlace de socket y puerto
    server_address = ("", 5000)
    print('empezando a levantar %s puerto %s' % server_address)
    sock.bind(server_address)
        
    # Escuchando conexiones entrantes
    sock.listen(1)
    while True:
        # Esperando conexion cliente
        log = open("registro_server.txt","a")
        print('Esperando para conectarse')
        connection, client_address  = sock.accept()
        try:
            print('conexion desde '+client_address[0])
            while True:
                databyte = connection.recv(19)  
                data = databyte.decode()
                print('recibido '+ data)
                log.write("IP: " + str(client_address[0]) +" "+ data + "\n")
                print('enviando respuesta a cliente')
                mensaje = "Servidor dice: Bienvenido"
                mensajebyte = mensaje.encode('utf-8')
                connection.sendall(mensajebyte)
                break

            # ------------------- VERIFICAR NODOS DISPONIBLES ---------------------
            listanodos = [False,False,False]

            registro = open("hearbeat_server","r")
            lineList = registro.readlines()
            registro.close()
            estado = lineList[-1].split("/")
            for i in range (3):
                if estado[i][-14:] == "Activo        ":
                    listanodos[i] = True

            # ------------------- SI NO HAY NINGUNO DISPONIBLE ---------------------
            print("lista nodos disponibles:")
            print (listanodos)
            noHayNodos = True
            for i in range(3):
                if listanodos[i]:
                    noHayNodos = False
            
            if noHayNodos:
                log.write("No hay nodos activos para mensaje de " + client_address[0] )
                print("no se encuentran nodos activos")
                respuesta = "No existen nodos activos para guardar su mensaje :("
                respuestabyte = respuesta.encode('utf-8')
                connection.sendall(respuestabyte)
            else:
                # ------------------- ESCOGER NODO AZAR ---------------------
                salir = False
                azar = random.randint(0, 2) 
                while not salir:
                    if listanodos[azar]:
                        salir = True
                    else:
                        azar = random.randint(0, 2)
                    # ------------------------------------- CONECTAR NODO 1 ---------------------------------
                print ("valor de azar:")    
                print (azar)

                if azar == 0:
                    try:
                        socknodo1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        server_address = ('', 5001)
                        print ('conectando a nodo 1')
                        socknodo1.connect(server_address)
                        # Enviando datos
                        messagenodo1 = 'Hola soy el servidor '
                        messagenodo1Byte = messagenodo1.encode('utf-8')
                        socknodo1.sendall(messagenodo1Byte)
                        databytenodo1 = socknodo1.recv(1024)
                        datanodo1 = databytenodo1.decode()
                        print("RESPUESTA NODO1: " + datanodo1 )
                        disponible1 = True
                        #respuestas.write("RESPUESTA NODO1: " + data + "\n")
                    except:
                        print("no se ha podido conectar con nodo 1 ")
                        disponible1 = False

                    # ------------------------------------- CONECTAR NODO 2 ---------------------------------
                elif azar == 1:
                    try:
                        socknodo2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        # Conecta el socket en el puerto cuando el servidor este escuchando
                        server_address = ('', 5002)
                        print ('conectando a nodo 2')
                        socknodo2.connect(server_address)

                        # Enviando datos
                        messagenodo2 = 'Hola soy el servidor '
                        messagenodo2Byte = messagenodo2.encode('utf-8')
                        socknodo2.sendall(messagenodo2Byte)
                        databytenodo2 = socknodo2.recv(1024)
                        datanodo2 = databytenodo2.decode()
                        print("RESPUESTA NODO2: " + datanodo2 )
                        disponible2 = True
                        #respuestas.write("RESPUESTA NODO2: " + data + "\n")
                    except:
                        print("no se ha podido conectar con nodo 2 ")
                        disponible2 = False

                    # -------------------------------------  CONECTAR NODO 3 ---------------------------------
                elif azar == 2:
                    try:
                        socknodo3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        
                        # Conecta el socket en el puerto cuando el servidor este escuchando
                        server_address = ('', 5003)
                        print ('conectando a nodo 3')
                        socknodo3.connect(server_address)

                        # Enviando datos
                        messagenodo3 = 'Hola soy el servidor '
                        messagenodo3Byte = messagenodo3.encode('utf-8')
                        socknodo3.sendall(messagenodo3Byte)
                        databytenodo3 = socknodo3.recv(1024)
                        datanodo3 = databytenodo3.decode()
                        print("RESPUESTA NODO3: " + datanodo3 )
                        disponible3 = True
                        #respuestas.write("Respuesta desde el servidor: " + data + "\n")
                    except:
                        print("no se ha podido conectar con nodo 3 ")
                        disponible3 = False
                        
                # ------------------- ENVIAR NODO 1  ---------------------
                if azar == 0:
                    messagenodo1 = data
                    messagenodo1Byte = messagenodo1.encode('utf-8')
                    socknodo1.sendall(messagenodo1Byte)
                    databytenodo1 = socknodo1.recv(1024)
                    datanodo1 = databytenodo1.decode()
                    print("ENVIADO A NODO? 1 " + datanodo1 )
                    
                    if datanodo1 == "MENSAJE RECIBIDO":
                        log.write("mensaje de " + client_address[0] + " exitosamente guardado en nodo 1")
                        respuestacliente = "su mensaje se guado en nodo 1"
                        respuestaclientebyte = respuestacliente.encode('utf-8')
                        connection.sendall(respuestaclientebyte)
                    else:
                        log.write("Se intento guardar mensaje de " + client_address[0] + "en nodo 1 pero no se pudo")
                    
                    # ------------------- ENVIAR NODO 2  ---------------------
                if azar == 1:
                    messagenodo2 = data
                    messagenodo2Byte = messagenodo2.encode('utf-8')
                    socknodo2.sendall(messagenodo2Byte)
                    databytenodo2 = socknodo2.recv(1024)
                    datanodo2 = databytenodo2.decode()
                    print("ENVIADO A NODO? 2 " + datanodo2 )
                    
                    if datanodo2 == "MENSAJE RECIBIDO":
                        log.write("mensaje de " + client_address[0] + " exitosamente guardado en nodo 2")
                        respuestacliente2 = "su mensaje se guado en nodo 2"
                        respuestacliente2byte = respuestacliente2.encode('utf-8')
                        connection.sendall(respuestacliente2byte)
                    else:
                        log.write("Se intento guardar mensaje de " + client_address[0] + "en nodo 1 pero no se pudo")
                    

                    # ------------------- ENVIAR NODO 3  ---------------------
                if azar == 2:
                    messagenodo3 = data
                    messagenodo3Byte = messagenodo3.encode('utf-8')
                    socknodo3.sendall(messagenodo3Byte)
                    databytenodo3 = socknodo3.recv(1024)
                    datanodo3 = databytenodo3.decode()
                    print("ENVIADO A NODO? 3 " + datanodo3 )
                    
                    if datanodo3 == "MENSAJE RECIBIDO":
                        log.write("mensaje de " + client_address[0] + " exitosamente guardado en nodo 3")
                        respuestacliente3 = "su mensaje se guado en nodo 3"
                        respuestacliente3byte = respuestacliente3.encode('utf-8')
                        connection.sendall(respuestacliente3byte)
                    else:
                        log.write("Se intento guardar mensaje de " + client_address[0] + "en nodo 3 pero no se pudo")

        finally:
            log.close()
            connection.close()
    sock.close()
#-------------------------------------------------------------------
#-------------------------------- Thread 2 -------------------------
#-------------------------------------------------------------------
def chequeo():    #¡¡¡ multicast !!!!
    MCAST_GRP = '224.3.29.71'
    MCAST_PORT = 5007
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.settimeout(0.2)

#----- Los nodos deben setearse en "False" -----#
    message_mc = b'MC'
    while True:
        time.sleep(4.6)
        disponible1 = False
        disponible2 = False
        disponible3 = False
        listanodos = [disponible1,disponible2,disponible3]
        listaaddress = [0,0,0]
            
#----- Se consulta los nodos disponibles -----#
        print('enviando {!r}'.format(message_mc))
        sent = sock.sendto(message_mc, (MCAST_GRP, MCAST_PORT))
		
		#----- Los nodos disponibles responden hasta que transcurre un tiempo de inactividad 
		#----- y se deja de esperar respuestas de los nodos -----#
        estado_actual = True
        lista_random = []
        print('----- ...esperando... -----')
        for i in range(3):
            try:
                #----- Se recibe la información de un nodo que respondió -----#
                data_mc, server = sock.recvfrom(16)
                print('recibiendo {!r} de {}'.format(data_mc, server))
                if(data_mc =='1'):
                    disponible1 = True
                    listaaddress[0] = server
                    lista_random.append(0)
                    time.sleep(0.19)
                elif(data_mc == '2'):
                    disponible2 = True
                    listaaddress[1] = server
                    lista_random.append(1)
                    time.sleep(0.19)
                elif(data_mc == '3'):
                    disponible3 = True
                    listaaddress[2] = server
                    lista_random.append(2)
                    time.sleep(0.19)

                else:
                    print("Se recibió información del cliente")
                #----- Se actualiza el estado de los nodos en la lista de nodos -----#
                listanodos = [disponible1,disponible2,disponible3]
                print("Estado de los nodos", listanodos)
            except socket.timeout:
                print('----- ...tiempo exedido, no hay más nodos... -----')
                estado_actual = False

                #----- registro de nodos acitvos -----
        log = open("hearbeat_server","a")
        # Registro nodo 1   
        log.write("Nodo 1:")
        if disponible1:
            log.write("Activo        /")
        else:
            log.write("No disponible /")
        # Registro nodo 2 
        log.write("Nodo 2:")
        if disponible2:
            log.write("Activo        /")
        else:
            log.write("No disponible /")
        # Registro nodo 3 
        log.write("Nodo 3:")
        if disponible3:
            log.write("Activo        /")
        else:
            log.write("No disponible /")
        log.write("\n")
        log.close()            
    return

threads = []
t = threading.Thread(target=principal)
threads.append(t)
t.start()
t2 = threading.Thread(target=chequeo)
threads.append(t2)
t2.start()
