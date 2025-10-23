def quickselect(arr, k):
    
    if k<1 or k>len(arr):
        return "Posición k fuera de rango"
    
    k_index = k - 1  # Convertir a índice basado en 0

    left = []
    right = []
    equals = []
    pivot = arr[len(arr) // 2]
    
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equals.append(i)
    
    if k_index >= len(left) and k_index < len(left) + len(equals): # El pivote es el k-ésimo más pequeño
        return pivot
    elif k_index < len(left): # Buscar en la parte izquierda
        return quickselect(left, k)
    else: # Buscar en la parte derecha
        return quickselect(right, k - len(left) - len(equals))
         
k_buscar = int(input("Ingrese la posicion k (ej. 4 para el 4to mas pequeño): "))
lista_numeros = [34, 7, 23, 7, 32, 5, 62]
resultado = quickselect(lista_numeros, k_buscar)

print(f"El {k_buscar}º número más pequeño es: {resultado}")