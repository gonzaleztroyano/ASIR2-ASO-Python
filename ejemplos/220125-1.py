"""
    Autor: Pablo González 
    Fecha: 25/01/2022
    Keys:  print
"""

nombre = 'Pepe'
apellidos = 'García'

# Muestra "Tu nombre es Pepe"
print("Tu nombre es",nombre,apellidos)

# El separador será un retorno de carro
print("Tu nombre es",nombre,sep="\n")

# El separador será un retorno de carro y terminará con "--"
print("Tu nombre es",nombre,apellidos,sep="\n",end="--")

# El serparador será un retorno de carro y terminará con "--" seguido de un retorno de carro. 
print("Tu nombre es",nombre,sep="\n",end="--\n ")
