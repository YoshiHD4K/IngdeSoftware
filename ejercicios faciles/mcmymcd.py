"""

Ejercicio: Calcular el MCM y MCD de una lista de números aleatorios generados entre 2500 y 2723.
El programa solicitará al usuario la cantidad de números a generar, luego generará los números aleatorios,
y finalmente mostrará el MCM y MCD de cada número con respecto a 13 y 26.

"""

from random import randint
from math import lcm, gcd

tamano = int(input("Ingrese la cantidad de numeros a ingresar: "))
arreglo = []

for i in range(tamano):
    numero_random = randint(2500, 2723)
    arreglo.append(numero_random)
    print(f"{i}) Numero random {numero_random} agregado.")

print(f"\nArreglo completo: {arreglo}")

for i in range(len(arreglo)):
    print(f"El MCM de {arreglo[i]} es: {lcm(arreglo[i], 13, 26)}")
    print(f"El MCD de {arreglo[i]} es: {gcd(arreglo[i], 13, 26)}")
