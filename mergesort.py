from multiprocessing import Process, Manager
from random import randint
import time

umbral = 5000  

def parallel_merge_sort(arr):
    if len(arr) <= umbral:
        return merge_sort(arr)
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    with Manager() as manager:
        return_dict = manager.dict()

        p1 = Process(target=sort_and_save, args=(left_half, 'left', return_dict))
        p2 = Process(target=sort_and_save, args=(right_half, 'right', return_dict))

        p1.start()
        p2.start()
        p1.join()
        p2.join()

        left_sorted = return_dict['left']
        right_sorted = return_dict['right']

        return merge(left_sorted, right_sorted)

def sort_and_save(subarr, key, return_dict):
        sorted_subarr = parallel_merge_sort(subarr)
        return_dict[key] = sorted_subarr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    datos = [randint(0, 100000) for _ in range(20000)]
    print("Lista creada con 20000 números aleatorios.")
    print("Lista inicial:", datos)
    start_time = time.time()
    sorted_datos = parallel_merge_sort(datos)
    end_time = time.time()
    print("Lista ordenada:", sorted_datos)

    print(f"Lista ordenada en {end_time - start_time:.4f} segundos.")
    print("La lista fue ordenada correctamente." if sorted_datos == sorted(datos) else "Error en el ordenamiento.")