try:
    tamaño_vector = int(input("Ingrese el tamaño del vector a crear: "))
except:
    print("Ingresa un numero entero valido: ")

for i in range(0,tamaño_vector):
    print(f"{i}")

