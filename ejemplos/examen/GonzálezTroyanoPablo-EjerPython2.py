 
#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#-*- coding:cp1252 -*-

# Pablo González Troyano - 2º ASIR
# Ejercicio 2 - Examen Python ASO
# Fecha: 02/03/2022

import os

personas = {'manuel':'123456789','pepe':'222222222'}

def altas():
	print("Creando una nueva entrada en el archivo","",sep="\n")
	nombre = input("  Nombre: ")
	telefono = input("  Teléfono: ")
	
	if nombre in personas.keys():
		input(" -- ERROR -- ", "El nombre introducido ya se encuentra en a agenda. Voldiendo al menú", sep="\n")
		menu()
	elif len(telefono) < 9:
		input(" -- ERROR -- ", "El teléfono introducido tiene menos de 9 caracteres. Voldiendo al menú", sep="\n")
		menu()
	else:
		personas[nombre] = telefono
		print("Se ha añadido a", nombre, "a la agenda.")
		#print(personas.keys())
		input("Pulse cualquier tecla para volver al menú")
		menu()

def listar():
	for nom,tel in personas.items():
		print("Nombre:",nom)
		print("TELEFONO:", tel)
		print("-------------------------------")

	input("Pulse cualquier tecla para volver al menú... ")
	menu()

def salir():
	print("Se ha iniciado el proceso de cierrre. Copiando datos...")
	# Abrir documento escritura
	ident_fichero = open("agenda.txt","w")
	# Con for pasar datos
	for nom,tel in personas.items():
		registro = nom + ":" + tel + "\n"
		ident_fichero.write(registro)
	# Cerrar
	ident_fichero.close()
	input("Se ha completado el proceso. Pulse cualquier tecla para continuar...")
	exit()
	

def menu():
	os.system("clear")
	op = ""
	while op != 3:
		print("Bienvenido a la aplicación","   Opciones:","     1. Nuevo","     2. Listar","     3. Salir","",sep="\n")
		op = int(input("        Seleccione opción: "))
		if op == 1:
			altas()
		elif op == 2:
			listar()
		elif op == 3:
			salir()
			
menu()
