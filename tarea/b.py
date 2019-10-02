import os
hostname = "nombre" #example
response = os.system("ping -c 1 " + hostname)

if response == 0:
  print hostname, 'en funcionamiento'
else:
  print hostname, 'no hay conexion'