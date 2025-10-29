def fibonacci_enesimo(n): # Función para calcular el n-ésimo término de la secuencia de Fibonacci
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_enesimo(n - 1) + fibonacci_enesimo(n - 2)

def esprimo(num):  # Función para verificar si un número es primo
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def buscar_fibonacci_enesimo(inicio, fin): # Función para buscar términos de Fibonacci en un rango dado
    print(f"{'-'*40}")
    if inicio < 0 or fin < 0 or inicio > fin:
        raise ValueError("\n\nLos valores de inicio y fin deben ser no negativos y inicio debe ser menor o igual a fin.")
    print(f"\n\nFibonacci desde el término {inicio} hasta el término {fin}:")
    primos=0
    suma_primos=0
    suma_primos_3=0
    suma_fibonacci=0
    for i in range(inicio, fin + 1):
        fibonacci=fibonacci_enesimo(i)
        suma_fibonacci += fibonacci
        print(f"\nTérmino {i}: {fibonacci}")
        if esprimo(fibonacci):
            print(f"El término {i} es un número primo.")
            primos+=1
            suma_primos+=fibonacci
            if fibonacci % 3 == 0:
                print(f"El término {i} es un número primo y múltiplo de 3.")
                suma_primos_3+=fibonacci

    promedio_fibonacci = suma_fibonacci / (fin - inicio + 1)

    """No se puede realizar el maximo comun divisor (MCD) de números primos ya que el MCD 
    de dos números primos distintos es siempre 1."""
    
    # Resultados finales
    print(f"{'-'*40}")
    print(f"\n\nPromedio de los números de Fibonacci desde el término {inicio} hasta el término {fin}: {promedio_fibonacci}")
    print(f"Total de números primos encontrados: {primos}")
    print(f"Suma de los números primos encontrados: {suma_primos}")
    print(f"Suma de los números primos múltiplos de 3 encontrados: {suma_primos_3}")

# Solicitar al usuario los términos inicial y final
while True:
    try:
        inicio = int(input("Ingrese el término inicial (número no negativo): "))
        fin = int(input("Ingrese el término final (número no negativo): "))
        if inicio < 0 or fin < 0 or inicio > fin:
            print("Error: Los valores de inicio y fin deben ser no negativos y inicio debe ser menor o igual a fin. Intente nuevamente.")
            continue
        else:
            break
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese números enteros no negativos.")
# Llamar a la función con los valores proporcionados por el usuario
buscar_fibonacci_enesimo(inicio, fin)