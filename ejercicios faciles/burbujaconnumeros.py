"""

Ejercicio: Implementar el algoritmo de burbuja para ordenar una lista de números ingresados por el usuario.
El programa solicitará al usuario la cantidad de números a ingresar, luego pedirá cada número y finalmente
mostrará la lista ordenada en orden descendente.

"""


# Algoritmo de ordenamiento burbuja (Bubble Sort) en orden descendente

# El usuario ingresa el tamaño del arreglo
tamano = int(input("Indique el tamaño del arreglo: "))
arreglo = [] # Crear un arreglo vacío

# Llenar el arreglo con los valores ingresados por el usuario
for i in range(tamano):
    valor = int(input (f"Introduzca el numero a registrar ({i+1}) : "))
    arreglo.append(valor) # Agregar el valor al arreglo

print("Arreglo original: ", arreglo) # Mostrar el arreglo original

# Algoritmo de ordenamiento burbuja en orden descendente
# Recorre el arreglo varias veces, comparando elementos contiguos

for i in range(len(arreglo)):
    for j in range(0, len(arreglo) - i - 1):
        if arreglo[j] < arreglo[j+1]: # Si el elemento actual es menor que el siguiente
            aux = arreglo[j] # Intercambiar los elementos
            arreglo[j] = arreglo[j+1]
            arreglo[j+1] = aux



print("Arreglo ordenado: ", arreglo) # Mostrar el arreglo ordenado


