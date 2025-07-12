'''
Crea un juego donde el programa genera un número aleatorio entre 1 y 100, 
y el usuario debe adivinarlo. El programa debe dar pistas ("muy alto" o "muy bajo")
hasta que el usuario acierte.

Dificultad
===============================

1: Nivel pollito
    : 20 intentos 
    el rango del numero adivinado sea de 1 al 50   
2 : Nivel basico
    : 10 intentos 
    el rango del numero adivinado sea de 1 al 100 
3: Nivel Intermedio
    :7 intentos 
    el rango del numero adivinado sea de 1 al 200   

4: Nivel Dificil
    :5 intentos 
    el rango del numero adivinado sea de 1 al 1000           

'''

import random

print("los niveles son : Nivel Pollito (o) , Nivel Basico (b), Nivel Inermedio (i), Nivel Dificil (d)")
nivel = input("escribe tu nivel de juego")
limiteInferior = 1
limiteSuperior = 0
intentoMaximo = 0
contador= 0
if nivel=="o":
    limiteSuperior = 50
    intentoMaximo = 20
if nivel=="b":
    limiteSuperior = 100
    intentoMaximo = 10
if nivel=="i":
    limiteSuperior = 200
    intentoMaximo = 7
if nivel=="d":
    limiteSuperior = 1000
    intentoMaximo = 5

numero_secreto = random.randint(limiteInferior, limiteSuperior)

bandera = False

while contador < intentoMaximo:
   
    intento = int(input("Adivina el número (1-{}): ".format(limiteSuperior)))
    if intento < numero_secreto:
        print("Muy bajo")
    elif intento > numero_secreto:
        print("Muy alto")
    else:
        
        bandera= True
        break
    contador = contador + 1

if bandera :
    print("¡Correcto! El número era", numero_secreto)
else:
    print("has perdido")    