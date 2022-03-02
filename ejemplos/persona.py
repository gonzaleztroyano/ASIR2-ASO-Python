#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#-*- coding:cp1252 -*-

"""
    Autor: Pablo González 
    Fecha: 15/02/2022
    Keys:  Clases.

Enunciado:
Crear una clase llamada PERSONA, cuyos atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura.
Los métodos que se implementaran son: 

    - calcularIMC(): calculará si la persona está en su peso ideal (peso en kg/(altura^2  en m)). Dicho método devolverá el texto que indique si está por debajo de su peso ideal, en su peso ideal o si tiene sobrepeso.
        •	Si el imc es superior a 40, se considera “obesidad mórbida”
        •	Si el imc es superior a 35, se considera “obesidad moderada”
        •	Si el imc es superior a 30, se considera “obesidad leve”
        •	Si el imc es superior a 25, se considera “sobrepeso”
        •	Entre 20 y 25 se considera el peso ideal
        •	Si el imc es inferior a 20, se considera “anorexia nerviosa”

    - esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.

Dicha clase se creará en un fichero independiente, del script que vaya a utilizarla. Crear el script que utilice dicha clase y crea un objeto para comprobar su funcionamiento

"""

class persona():
    def __init__(self, nombre, edad, dni, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def esMayorDeEdad(self):
        if  self.edad < 18:
            return False
        else:
            return True
    
    def getIMC(self):
        #(altura^2  en m)
        return float((self.peso) / float(self.altura**2))

    def calcularIMC(self):
        if self.sexo == "M":
            if self.getIMC() < 20:
                return "Anorexia Nerviosa"
            elif self.getIMC() < 23.9:
                return "Peso Ideal"
            elif self.getIMC() < 28.9:
                return "Obesidad Leve"
            elif self.getIMC() < 37:
                return "Obesidad Severa"
            else:
                return "Obesidad Muy Severa"
        elif self.sexo == "H":
            if self.getIMC() < 20:
                return "Anorexia Nerviosa"
            elif self.getIMC() < 24.9:
                return "Peso Ideal"
            elif self.getIMC() < 29.9:
                return "Obesidad Leve"
            elif self.getIMC() < 40:
                return "Obesidad Severa"
            else:
                return "Obesidad Muy Severa"
        else:
            return "ERROR"

maria = persona("María",25,"88776655A","M",68,1.84)


print(maria.esMayorDeEdad())

print(maria.getIMC())

print(maria.calcularIMC())