#!/usr/bin/env python3

def carrito(nom,ape,*datos_cliente,**productos):
    print("Carrito de",nom,ape)
    for p in productos:
        print(p)

    for clave in productos:
        print (productos[clave])


nombre = "Pepe"
apellido = "Sanchez"
prod1 = "tomates"
prod2 = "pepinos"
prod3 = "pan"
prod4 = "leche"
direccion = "Calle Mayor"
telf = "85554455"

carrito(nombre,apellido,direccion,telf,prod1=2,prod2=4,prod3=3) 