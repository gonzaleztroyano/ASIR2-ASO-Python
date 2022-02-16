#!/usr/bin/env python
#-*- coding:utf-8 -*-
#-*- coding:cp1252 -*-

"""
    Autor: Pablo González 
    Fecha: 15/02/2022
    Keys:  Menú extraño e inútil con YAD y conexión a Base de datos
"""

import os
from sqlite3 import Cursor
import MySQLdb

os.system("clear")

conn = MySQLdb.connect('localhost','root','Londres2012','instituto')
cursor = conn.cursor()

os.system("yad --form --title='Alta de registro' --field='Nombre' --field='Apellido' --field='Teléfono' --field='Correo electrónico' --field='DNI' --width=200 --height=300 --center > /tmp/py_alta.txt 2> /dev/null ; echo $? > /tmp/py_codreg.txt") 


fichero_codigo_error = open("/tmp/py_codreg.txt")
registro = int(fichero_codigo_error.readline())

if registro == 0:
    fichero_datos_alta = open("/tmp/py_alta.txt","r")
    registro = fichero_datos_alta.read()
    fichero_datos_alta.close()
    campo = registro.split("|")
    nom = campo[0].upper()
    ape = campo[1].upper()
    tel = campo[2].upper()
    ema = campo[3].upper()
    dni = campo[4].upper()

    query = "INSERT INTO ALUMNOS (dni,nombre,apellido,telefono,email) values ('%s','%s','%s','%s')" % ( dni nom ape tel ema ) 
    cursor.execute()
    conn.commit()
else:
    print("Has pulsado candelar.")

cursor.close()
conn.close()


query = "SELECT dni,nombre,apellido,telefono,email from alumnos"
cursor.execute(query)
resultado = cursor.fetchall()
for r in resultado:
    print "NOMBRE", r[1]
    print "APELLIDO",r[2]
    print "DNI",r[3]
    print "TELEFONO",r[4]
    print "EMAIL",r[5]

    cadena = "Aquí mostraría lo anterior.  "

os.environ['mensaje'] = cadena