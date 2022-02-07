#!/usr/bin/env python3

def carrito(nom,ape,*datos_cliente,**productos):
    print("Carrito de",nom,ape)
    for p in productos:
        print(p)



nombre = "Pepe"
apellido = "Sanchez"
prod1 = "tomates"
prod2 = "pepinos"
prod3 = "pan"
prod4 = "leche"

carrito(nombre,apellido,direccion,telf,prod1=X,prod2=Y,prod3=Z) 