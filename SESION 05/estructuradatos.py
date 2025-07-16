print("================== estructura de datos ===================")
'''
numeros = [1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,1,12,13,4,6]

frutas =["manzana","mango","pera"]

numeros.append(140) # agregamos un elemento

numeros.remove(9) #remover elemento

numeros.pop()

numeros.sort()

numeros.reverse()

x = len(frutas)



tnumeros = (1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,1,12,13,4,6)

tnumeros.append(140)

x = tnumeros.count(9)
print("========== el valor es ======: ", x)

y = tnumeros.index(5)

print("========== el valor es y ======: ", y)

d = len(tnumeros)

print("========== la cantidad es :  ======: ", d)




print("================== conjuntos ===================")


conjunto = {1,2,3,4,5,6,7,7,7,8,9}


#conjunto.add(18)

#conjunto.remove(5)


#valor = conjunto.intersection({5,6,89,23})
conjunto2 = {5,6,89,23}

valor = conjunto.union(conjunto2)

print(valor)


print(persona.get("nombre"))

nombre2= persona2.get("nombre")
'''

#=================== Diccionario =============
'''
listaPersonas = [
 {
    "nombre" : "Alejandro",
    "edad" : 56 ,
    "ciudad" : "Lima"
} ,
 {
    "nombre" : "Sofia",
    "edad" : 23 ,
    "ciudad" : "Lima"
} ,
 {
    "nombre" : "Patty",
    "edad" : 21 ,
    "ciudad" : "Piura"
}
]

print(listaPersonas[0])

'''

persona =  {
    "nombre" : "Alejandro",
    "edad" : 56 ,
    "ciudad" : "Lima",
    "curso" : "Python"
}


#print(persona.get("nombre"))
#print(persona.keys())

#print(persona.values())

'''
for clave,valor in persona.items():
    print(clave , ":" , valor)

'''

#persona.update({"edad" : 69,"profesion": "medico"})


#ciudad =  persona.pop("ciudad")   

#ultimo = persona.popitem()

#persona.popitem()

#persona.clear()


for clave,valor in persona.items():
    print(clave , ":" , valor)



