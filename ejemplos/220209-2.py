#!/usr/bin/python3

class humano():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_nombre(self):
        print(self.nombre.upper())
    def adulto(self):
        if self.edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")

class alumno(humano): # Hereda de humano
    def __init__(self, nota, nombre, edad):
        humano.__init__(self, nombre, edad) # Pilla cosas de tu padre. 
        self.nota = nota
    def obtener_nota(self):
        if self.nota < 5:
            print("Suspenso")
        elif self.nota < 7:
            print("Bien")
        elif self.nota < 9:
            print("Notable")
        elif self.nota <=10:
            print("Sobresaliente")
        else:
            print("Nota no válida")

alum = alumno(8, "Rigoberto", 17)
alum.mostrar_nombre()
alum.adulto()
alum.obtener_nota()