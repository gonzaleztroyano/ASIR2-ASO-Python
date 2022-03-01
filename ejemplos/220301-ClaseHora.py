#!/usr/bin/env python3  
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

class hora():
	def __init__(self,hora=00,minutos=00,segundos=00):
		self.hora = int(hora)
		self.mint = int(minutos)
		self.seg = int(segundos)

	def valida(self):
		hora = self.hora
		minu = self.mint
		seg = self.seg
		ok = 's'
		cadena = ""
		if hora < 0:
			print("Hora no válida. NO puede ser negativa")
			ok='n'
		elif hora > 23:
			print("Hora no válida. NO puede ser mayor a 23")
			ok='n'
		
		if minu < 0:
			print("Minutos no válidos. NO pueden ser negativos")
			ok='n'
		elif minu > 59:
			print("Minutos no válidos. NO pueden ser mayor a 59")
			ok='n'
			
		if seg < 0:
			print("Segundos no válidos. NO pueden ser negativos")
			ok = 'n'
		elif seg > 59:
			print("Segundos no válidos. NO pueden ser mayor a 59")
			ok = 'n'
		
		if ok=='s':
			cadena = str(hora) + ":"
			cadena = cadena + str(minu) + ":"
			cadena = cadena + str(seg)
			print(cadena, " Hora correcta")
		return ok
		
	def a_minutos(self):
		#ahora.valida()
		hora = self.hora
		minu = self.mint
		seg = self.seg
		total = 0
		total = (hora * 60) + minu
		print("La hora",hora,":",minu,":",seg, "corresponde a",total,"minutos y",seg,"segundos")

	
	def a_segundos(self):
		hora = self.hora
		minu = self.mint
		seg = self.seg
		total = 0
		total = (hora * 60 *60) + (minu*60) + seg
		print("La hora",hora,":",minu,":",seg, "corresponde a",total,"segundos")
		
	def segundos_desde(self,hora):
		hora_pasada = self.hora
		from datetime import datetime
		now = datetime.now()
		hora_actual=now.hour
		if hora_pasada > hora_actual:
			dif=hora_pasada - hora_actual
		else:
			dif = hora_actual - hora_pasada
		total = dif * 60 * 60
		print("Los segundos entre la hora",hora_actual,"y la hora",hora_pasada,"es:",total)
		

h = input("Indica una hora: ")
m = input("Minutos: ")
s = input("Segundos: ")
ahora = hora(h,m,s)
ok = ahora.valida()
if ok == 's':
	ahora.a_minutos()
	ahora.a_segundos()
	ahora.segundos_desde(h)