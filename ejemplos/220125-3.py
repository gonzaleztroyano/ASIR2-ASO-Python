"""
    Autor: Pablo González 
    Fecha: 25/01/2022
    Keys:  print() // TUPLAS // LISTAS
"""

#!/usr/bin/env python3

from xml.dom.minidom import Element


TUPLA = ('hola',12,3.4,True,'caracola')

print("Trabajando con TUPLAS")
print("=====================")

print(TUPLA[2])
print("Obtenemos un elemento:", TUPLA[4])

# TUPLA[$inicio,$fin_sin_incluir]
print("Seccion de tupla:",TUPLA[1:4])

# Desde elemento n hasta el final
print("Seccion de tupla:",TUPLA[2:])

# Desde inicio hasta elemento m
print("Los primeros dos elementos:", TUPLA[:2])

print("El último elemento:", TUPLA[-1])

print("El penúltimo elemento", TUPLA[-2])


print("================================")
print("================================")
print("Trabajando con LISTAS")
print("=====================")

lista = ['hola',12,3.4,True,'caracola']

print("Obtenemos un elemento:", lista[4])
print("Seccion de tupla:",lista[1:4])
print("Seccion de tupla:",lista[2:])
print("El último elemento:", lista[-1])
print("El penúltimo elemento", lista[-2])

print(lista[0])
lista[0] = "hola mari puri"
print(lista[0])
lista.append("pepe")
print(lista[-1])

# Insertar elementos en listas.
print(lista[0:3])
print(lista.count("pepe"))
lista.insert(1,"cadena")
print(lista[0:3])


nombres = ["Jose","Eva","Ana","Eva","Luis","Eva","Fernando","Eva","Susana"]
print(nombres.count("Eva"))
print(nombres.index("Jose"))
print(nombres.index("Eva"))
print(nombres.index("Eva",4,7))

