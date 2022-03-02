#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#-*- coding:cp1252 -*-

# Pablo González Troyano - 2º ASIR
# Ejercicio 1 - Examen Python ASO
# Fecha: 02/03/2022


import math

class figura(): 
	def __init__(self,lado1,lado2,lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3
        
	def validar(self):
		if (float(self.lado1) == 0) or (float(self.lado2) == 0) or (float(self.lado3) == 0):
			return "error"
		else:
			return "OK"
	
	def IndicarFigura(self):
		if self.validar() == "OK":
			if (self.lado1 == self.lado2 and self.lado1 == self.lado3):
				return "Equilátero"
			if ((self.lado1 == self.lado2) or (self.lado2 == self.lado3) or (self.lado3 == self.lado1)):
				return "Isósceles"
			if ((self.lado1 != self.lado2) and (self.lado2 != self.lado3) and (self.lado3 != self.lado1)):	
				return "Escaleno"
			if ((self.lado1 + self.lado2 < self.lado3) or (self.lado2 + self.lado3 < self.lado1) or (self.lado1 + self.lado3 < self.lado2)):
				return "Imposible"
		else:
			return "Medidas introducidas no válidas"

	def calcularArea(self):
		if self.validar() == "OK":
			calcular_area_p = float(self.lado1) + float(self.lado2) + float(self.lado3)
			calcular_area_p = (calcular_area_p / 2)
			calcular_area_a = (calcular_area_p * (calcular_area_p - float(self.lado1)) * (calcular_area_p - float(self.lado2)) * (calcular_area_p - float(self.lado3)))
			calcular_area_a = math.sqrt(calcular_area_a)
			return calcular_area_a
		else:
			return "Medidas introducidas no válidas"
			
			
# Equilátero
triangulo_pruebas = figura(1.5,1.5,1.5)
print(triangulo_pruebas.validar())
print(triangulo_pruebas.IndicarFigura())
print(triangulo_pruebas.calcularArea())

# No debe validar
triangulo_pruebas_dos = figura(1.5,1.5,0)
print(triangulo_pruebas_dos.IndicarFigura())
print(triangulo_pruebas_dos.calcularArea())

# Debe salir isósceles
triangulo_pruebas_tres = figura(1.5,1.5,2)
print(triangulo_pruebas_tres.IndicarFigura())
print(triangulo_pruebas_tres.calcularArea())

# Debe salir escaleno
triangulo_pruebas_cuatro = figura(3,1.5,2)
print(triangulo_pruebas_cuatro.IndicarFigura())
print(triangulo_pruebas_cuatro.calcularArea())
