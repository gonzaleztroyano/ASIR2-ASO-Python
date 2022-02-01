
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
    '11223344A': {'nombre': 'JOSE', 'ape': 'LOPEZ', 'edad': 19, 'curso': 2, 'notas': [3.7, 5, 7]},
    '11223344B': {'nombre': 'EVA', 'ape': 'MARTIN', 'edad': 18, 'curso': 1, 'notas': [3, 4, 6]}
}


def listar():
    cuenta_alu = 1
    for dni in alumnos.keys():
        print(cuenta_alu, "-", dni)
        cuenta_alu = cuenta_alu + 1
    
def altas():
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
    alumnos[dni]['nom'] = nombre.upper()
    alumnos[dni]['ape'] = apellido.upper()
    alumnos[dni]['edad'] = edad
    alumnos[dni]['curso'] = curso
    # Creamos una lista temporal con los datos correspondientes a la llista que forma nuestra tercera dimensión.
    temp = []
    temp.append(nota1)
    temp.append(nota2)
    temp.append(nota3)
    # Enviamos el contenido de la lista temporal al campo notas del diccionario.
    alumnos[dni]['notas'] = temp
    print ("Registro añadido correctamente")
    input("Pulse cualquier tecla para volver al menú...")

def bajas():
    #os.system("clear")
    print("     BAJAS     ")
    print("---------------")
    print("")
    print("Estos son los registros de la BDD: ")
    listar()
    
    alu_a_borrar = input("DNI del alumno a borrar: ")
    if alu_a_borrar in alumnos:
        print("¡Atención! Se va a borrar el alumno ", alu_a_borrar,".",sep='')
        conf_bajas = input("Escriba 'b' para borrar el registro: ")
        if conf_bajas == 'b':
            del alumnos[alu_a_borrar]
            input("Se ha borrado. Pulse cualquier tecla para volver al menú...")
        else:
            print("¡Recibido! No se ha eliminado el registro")
            opt_bajas = input("Pulse cualquier tecla para reintentarlo. O 's' para salir ")
            print(opt_bajas)
            input("P")
            if opt_bajas.lower() != "s":
                input("X")
                #bajas()
            else:
                input("Y")
                print("")
    else:
        print("El registro no se ha encontrado.")
        opt_bajas = input("Pulse cualquier tecla para reintentarlo. O 's' para salir ")
        if opt_bajas.lower != 's':
            bajas()
        else:
            return
    return

def modificar():
    print("   MODIFICAR   ")
    print("---------------")

def consultar():
    print("   CONSULTAR   ")
    print("---------------")


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
        altas()
    elif op == 2:
        bajas()
    elif op == 3:
        modificar()
    elif op == 4:
        consultar()
    elif op == 5:
        print("     LISTADO     ")
        print("-----------------")
        listar()
        print("")
        input("Pulsa cualquier tecla para volver al menú...")
    elif op == 6:
        os.system("clear")
        input("Pulsa cualquier tecla para salir...")
