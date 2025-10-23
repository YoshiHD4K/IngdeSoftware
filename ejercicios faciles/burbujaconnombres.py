tamaño = int(input("Introduce la cantidad de nombres que seran ingresados: "))

arreglo = []

for i in range(tamaño):
    nombre = input(f"Ingrese el Nombre separado por un espacio ({i+1}): ")
    arreglo.append(nombre)

for i in range(len(arreglo)):
    for j in range(0, len(arreglo)- i - 1):
        palabra1 = arreglo[j]
        palabra2 = arreglo[j + 1]
        letra1 = palabra1[0:2]
        letra2 = palabra2[0:2]
        if letra1 > letra2:
            arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]


print("Arreglo ordenado: ", arreglo)
