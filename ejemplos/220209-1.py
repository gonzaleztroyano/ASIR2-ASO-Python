#!/usr/bin/python3

class canino():
    def __init__(self,nom,color,tam,constitucion,caracter,edad,raza,hambriento,cansado):
        self.nom = nom
        self.color = color
        self.tam = tam
        self.const = constitucion
        self.carac = caracter
        self.edad = edad
        self.raza = raza
        self.hambriento = hambriento
        self.cansado = cansado
    
    def comer(self):
        if self.hambriento:
            print("Tengo hambre... Ñam, Ñam.")
        else:
            print("Toy lleno")
    
    def dormir(self):
        if self.cansado:
            print("Guay, guay, a dormir")
        else:
            print("Sal a correr, humano vago. Stoy a full de energía.")
    
    def ladrar(self):
        if self.carac == 'grunon':
            print("GRRRRRR, guau guau")
        elif self.carac == 'tranquilo':
            print("Dame comida, excelentísimo humano")
        elif self.carac == 'loco':
            print("Planearé como robar toda la comida de la nevera, humano inútil")
        else:
            print("No tengo claro como soy, llévame al médico.")

perro = canino("Archie","marron", "pequeño", "rechoncho", "grunon", 8, "RazaEje", False,True)

print("Mi nombre es", perro.nom)
print("En estos momentos mu estaado espritual es:",perro.carac)
perro.comer()
perro.dormir()
perro.ladrar()