"""
    Autor: Pablo González 
    Fecha: 26/01/2022
    Keys:  print() // Diccionarios/Hashes
"""

#!/usr/bin/env python3

capitales = {'Espanna':'Madrid','Italia':'Roma','Francia':'Paris','Polonia':'Varsovia','Austria':'Viena','Egipto':'El Cairo','Lituania':'Vilna','Portugal':'Lisboa','Peru':'Lima','Venezuela':'Caracas'}

respuesta = input("Dime la capital de Portugal: ")

print("La capital de Portugal es", capitales["Portugal"])

if respuesta == capitales['Portugal']:
    print("Respuesta correcta.")
else:
    print("Estúdia, por favor.")

paises = capitales.keys()
print(paises)

solo_capitales = capitales.values()
print(solo_capitales)

for clave,valor in capitales.items():
    print("La capital de",clave,"es:",valor)

pais_nuevo    = input("País: ")
capital_nueva = input("Capital: ")

capitales[pais_nuevo] = capital_nueva

print(capitales)