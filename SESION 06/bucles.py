# Ejemplo 1: Función que utiliza un bucle for para calcular la suma de una lista de números
def suma_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

# Ejemplo 2: Función que utiliza un bucle while para contar hasta un número dado
def contar_hasta(n):
    contador = 1
    while contador <= n:
        print(contador)
        contador += 1

# Ejemplo 3: Función que utiliza un bucle for para generar una lista de cuadrados
def generar_cuadrados(n):
    cuadrados = []
    for i in range(1, n + 1):
        cuadrados.append(i ** 2)
    return cuadrados

# Ejemplo 4: Función que utiliza un bucle while para encontrar el primer número divisible por 7 en un rango
def encontrar_divisible_por_7(inicio, fin):
    numero = inicio
    while numero <= fin:
        if numero % 7 == 0:
            return numero
        numero += 1
    return None  # Si no se encuentra ningún número divisible por 



# Ejemplo de invocación de las funciones anteriores
numeros = [1, 2, 3, 4, 5]
print("Suma de la lista:", suma_lista(numeros))

print("Contar hasta 5:")
contar_hasta(5)

print("Lista de cuadrados hasta 5:", generar_cuadrados(5))

print("Primer número divisible por 7 entre 10 y 20:", encontrar_divisible_por_7(10, 20))