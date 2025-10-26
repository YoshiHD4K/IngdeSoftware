"""
/* Elabora un programa que ingrese el usuario cualquier cantidad de numeros, generelo de forma aleatoria y guardelo en un arreglo,
que se ordene de mayor a menos, buscar el promedio, buscar el numero primo superior e inferior mas cercano, estos dos numeros
sacarle el maximo comun divisor*/

"""
import random
import math

def generarnumerosrandom(arreglo, tamaño):

    for num in range(tamaño):
        numrand = random.randint(1,100)
        arreglo.append(numrand)
        print(f"{num+1}) Numero {numrand} ingresado en la lista.")

    return arreglo

def ordernararreglo(arreglo):

    for i in range(len(arreglo)):
        for j in range(0, len(arreglo) - i - 1):
            if arreglo[j] < arreglo[j+1]: # Si el elemento actual es menor que el siguiente
                aux = arreglo[j] # Intercambiar los elementos
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = aux
                
    return arreglo

def buscarpromedio(arreglo):
    suma = 0
    for num in range(len(arreglo)):
        suma += arreglo[num]
    return suma // len(arreglo)

def buscarprimos(promedio):
    primos = []
    prombajo = promedio - 1
    promalto = promedio + 1
    while prombajo > 0:
        if esprimo(prombajo):
            primos.append(prombajo)
            break
        prombajo -= 1
    while promalto < 100:
        if esprimo(promalto):
            primos.append(promalto)
            break
        promalto += 1
    return primos

def esprimo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

while True:
    try:
        tamaño = int(input("Ingrese la cantidad de numeros a generar: "))
        if tamaño > 0:
            arreglo = []
            arreglo = generarnumerosrandom(arreglo, tamaño)
            arreglo = ordernararreglo(arreglo)
            print("Arreglo ordenado de mayor a menor: ", arreglo)
            promedio = buscarpromedio(arreglo)
            print(f"Promedio: {promedio}")
            primos = buscarprimos(promedio)
            print(f"Numero primo inferior mas cercano al promedio: {primos[0]}")
            print(f"Numero primo superior mas cercano al promedio: {primos[1]}")
            mcd = math.gcd(primos[0], primos[1])
            print(f"Maximo Comun Divisor: {mcd}")
            break
        else:
            print("Error, ingrese un numero natural.")
    except ValueError:
        print("Error, ingrese un valor valido.")