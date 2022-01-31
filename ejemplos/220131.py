
"""
    Autor: Pablo González 
    Fecha: 31/01/2022
    Keys:  matrices, hash, cosas con datos. Programas inutiles. 
"""

# alumnos = {
#            'dni':{'nombre':'XXXX','ape':'YYYYY','edad':ZZ,'curso':NN,'notas':[MM,AA,BB]},
#            'dni':{'nombre':'XXXX','ape':'YYYYY','edad':ZZ,'curso':NN,'notas':[MM,AA,BB]},
#            'dni':{'nombre':'XXXX','ape':'YYYYY','edad':ZZ,'curso':NN,'notas':[MM,AA,BB]}
#           }

import os
alumnos = {
    'dni': {'nombre': 'JOSE', 'ape': 'LOPEZ', 'edad': 19, 'curso': 2, 'notas': [3.7, 5, 7]},
    'dni': {'nombre': 'EVA', 'ape': 'MARTIN', 'edad': 18, 'curso': 1, 'notas': [3, 4, 6]}
}

op = 0
while op != 6:
    os.system("clear")
    print("   GESTION ALUMNOS")
    print()
    print("       1. ALTAS")
    print("       2. BAJAS")
    print("       3. MODIFICAR NOTAS")
    print("       4. CONSULTAR NOTAS")
    print("       5. LISTADO")
    print("       6. SALIR")

    op = int(input("       Seleccione opción:"))

    if op == 1:
        print("     ALTAS     ")
        print("---------------")
        dni = input("DNI:")
        nombre = input("NOMBRE:")
        apellido = input("APE:")
        edad = int(input("EDAD:"))
        curso = int(input("CURSO:"))
        nota1 = float(input("NOTA-1:"))
        nota2 = float(input("NOTA-2:"))
        nota3 = float(input("NOTA-3:"))
        # Añadir un valor a un diccionario
        alumnos.update({dni: {}})
        # Cargamos los datos del diccionario
        alumnos[dni]['nom']   = nombre.upper()
        alumnos[dni]['ape']   = apellido.upper()
        alumnos[dni]['edad']  = edad
        alumnos[dni]['curso'] = curso
        # Creamos una lista temporal con los datos correspondientes a la llista que forma nuestra tercera dimensión.
        temp = []
        temp.append(nota1)
        temp.append(nota2)
        temp.append(nota3)
        # Enviamos el contenido de la lista temporal al campo notas del diccionario.
        alumnos[dni]['notas'] = temp
    elif op == 2:
        print("BAJAS")
    elif op == 3:
        print("MODIFICAR NOTAS")
    elif op == 4:
        print("CONSULTAR NOTAS")
    elif op == 5:
        print("LISTADO")
