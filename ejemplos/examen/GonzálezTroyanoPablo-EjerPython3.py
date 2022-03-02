#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#-*- coding:cp1252 -*-


# Pablo González Troyano - 2º ASIR
# Ejercicio 3 - Examen Python ASO
# Fecha: 02/03/2022

import os
from random import randint


def stats():
	fichero_indicado = input("Introduzca el archivo deseado: ")
	
	if os.name == 'nt':
		os.system("dir %s > datos.txt" % (fichero_indicado))
		ident_fecha = open("datos.txt","r")
		fecha = ident_fecha.readline()
		
	elif os.name == 'posix':
		os.system('clear')
	
	# Abro el fichero indicado
	ident_fichero = open(fichero_indicado,"r")
	
	# Ejecuto la orden para saber la fecha
	os.system("ls -la %s > datos.txt" % (fichero_indicado))
	
	# Abro el fichero que tiene la fecha
	ident_fecha = open("datos.txt","r")
	# Leo la línea
	fecha = ident_fecha.readline()
	# Me quedo solo con la parte que me interesa --> "'feb 23 12:12'"
	fecha = fecha[26:40]

	
	numero_lineas = 0
	numero_palabras = 0
	numero_letras = 0
	for linea in ident_fichero.readlines():
		numero_lineas = numero_lineas + 1
		numero_palabras_linea = len(linea.split(" "))
		numero_palabras = numero_palabras + numero_palabras_linea
		numero_letras_linea = len(linea)
		numero_letras = numero_letras + numero_letras_linea
		
	print("fecha:", fecha,", letras:", numero_letras, ", palabras:", numero_palabras, "y lineas:", numero_lineas)
	input("Pulse cualquier tecla para volver al menú...")


def password():
	caracteres = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","ñ","Ñ","o","O","p","P","q","Q","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z","1","2","3","4","5","6","7","8","9","0"]
	longitud = int(input("Indica la longitud de la contraseña: "))
	
	if longitud < 8 or longitud > 16:
		print("ERROR. La contraseña debe estar entre 8 y 16 caracteres")
		input("Pulse cualquier tecla para continuar...")
	rand_passwd = ""
	
	iteracion = 0
	while iteracion < longitud:
		n = randint(0,len(caracteres)-1)
		rand_passwd = caracteres[n] + rand_passwd
		#print(rand_passwd)
		iteracion = iteracion + 1
	
	print("\n","\n","Contraseña generada: ", rand_passwd,"\n","\n")
	input("Pulse cualquier tecla para volver al menú...")


def menu():
	if os.name == 'nt':
		os.system('cls')
	elif os.name == 'posix':
		os.system('clear')
	op = ""
	while op != 3:
		print("Bienvenido a la aplicación","   Opciones:","     1. Estadístcas de un fichero","     2. Generar contraseña","     3. Salir","",sep="\n")
		op = int(input("        Seleccione opción: "))
		if op == 1:
			stats()
		elif op == 2:
			password()
		elif op == 3:
			input("Saliendo. Pulse cualquier tecla para continuar...")
			quit()

menu()
 
