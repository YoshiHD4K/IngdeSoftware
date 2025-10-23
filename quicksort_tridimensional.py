class objeto:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        pass

def mayor_que(obj1, obj2):
        if obj1.a > obj2.a:
            return True
        elif obj1.a == obj2.a:
            if obj1.b > obj2.b:
                return True
            elif obj1.b == obj2.b:
                if obj1.c > obj2.c:
                    return True
        return False

def quicksort(arr):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(arr) <= 1:
        return arr

    # Elegimos el pivote (puede ser el primero, último, medio, aleatorio, etc.)
    pivot = arr[0]

    # Partimos la lista en tres partes:
    menores = []
    iguales = []
    mayores = []
    for x in arr:
        if mayor_que(pivot, x):
            menores.append(x)
        elif mayor_que(x, pivot):
            mayores.append(x)
        else:
            iguales.append(x)

    # Aplicamos quicksort recursivamente y combinamos los resultados
    return quicksort(menores) + iguales + quicksort(mayores)

tamaño = int(input("Ingrese el tamaño de la lista: "))
lista = []
for i in range(tamaño):
    obj = objeto()
    obj.a = int(input(f"Ingrese el valor a del objeto {i+1}: "))
    obj.b = int(input(f"Ingrese el valor b del objeto {i+1}: "))
    obj.c = int(input(f"Ingrese el valor c del objeto {i+1}: "))
    lista.append(obj)

lista_ordenada = quicksort(lista)
print("Lista ordenada:")
for i, obj in enumerate(lista_ordenada, start=1):
    print(f"Objeto Nro {i}, a: {obj.a}, b: {obj.b}, c: {obj.c}")