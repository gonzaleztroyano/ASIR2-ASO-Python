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

os.system("yad --form --title='Alta de registro' --field='Nombre' --field='Apellido' --field='Teléfono' --field='Correo electrónico' --width=200 --height=300 --center > /tmp/py_alta.txt 2> /dev/null")

fichero_datos_alta = open("/tmp/py_alta.txt","r")
registro = fichero_datos_alta.read()
fichero_datos_alta.close()
campo = registro.split("|")
nombre = campo[0].upper
apellido = campo[1].upper
telefono = campo[2].upper
email = campo[3].upper