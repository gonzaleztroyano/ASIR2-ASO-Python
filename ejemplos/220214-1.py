#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#-*- coding:cp1252 -*-

"""
    Autor: Pablo González 
    Fecha: 14/02/2022
    Keys:  Menú extraño e inútil con YAD
"""

import os
from turtle import heading

def func_altas():
    os.system("clear")
    os.system("yad --form --title='Alta de registro' --field='Nombre' --field='Apellido' --field='Domicilio' --field='Teléfono' --field='Correo electrónico' --width=200 --height=300 --center > /tmp/py_alta.txt" )
    fichero_datos_alta = open("/tmp/py_alta.txt","r")
    registro = fichero_datos_alta.read()
    fichero_datos_alta.close()
    # Lo normal, útil y común para el resto de los mortales sería cambiar el separador en YAD. ¡Pero claro! 

    campo = registro.split("|")
    nombre = campo[0].upper
    apellido = campo[1].upper
    direccion = campo[2].upper
    telefono = campo[3].upper
    email = campo[4].upper
    cadena = nombre+"#"+apellido+"#"+direccion+"#"+telefono+"#"+email+"\n"

    fichero_datos = open("/tmp/agenda.txt","a")
    fichero_datos.write(cadena)
    fichero_datos.close()

    input("Pulse cualquier tecla para continuar...")

def func_bajas():
    os.system("clear")
    print("BAJAS")
    input("No hay nada. Pulse cualquier tecla para continuar...")

def func_consultas():
    os.system("clear")
    print("CONSULTAS")
    input("No hay nada. Pulse cualquier tecla para continuar...")

def func_modif():
    os.system("clear")
    print("MODIFICACIONES")
    input("No hay nada. Pulse cualquier tecla para continuar...")

def func_listado():
    os.system("clear")
    print("LISTADO")
    input("No hay nada. Pulse cualquier tecla para continuar...")

op = 0
while op != 6:
    os.system("yad --list --title='Gestion Fichero' --column='' --column='' 1 ALTAS 2 BAJAS 3 CONSULTAS 4 MODIFICACIONES 6 LISTADOS 6 SALIR --width=200 --height=300 --center > /tmp/py_op.txt" )
    fichero_opt = open("/tmp/py_op.txt","r")
    linea = fichero_opt.read()
    op = linea.split("|")
    op = int(op[0])

    if op == 1:
        func_altas()
    elif op == 2:
        func_bajas()
    elif op == 3:
        func_consultas()
    elif op == 4:
        func_modif()
    elif op == 5:
        func_listado()
    
