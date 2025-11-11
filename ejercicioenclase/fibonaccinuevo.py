def fibonacci(limite:int, digito:int):
    a, b = 0, 1

    while a + b <= limite:
        c = a + b
        if c % 10 == digito:
            print(f"Fibonacci: {c}")
        a=b
        b=c

try:
    numero = int(input("Ingrese un numero entero positivo: "))
    if numero < 0:
        raise ValueError("El numero debe ser positivo.")
    digito = int(input("Ingrese un digito (0-9): "))
    if digito < 0 or digito > 9:
        raise ValueError("El digito debe estar entre 0 y 9.")
except ValueError as e:
    print("Error:", e)

fibonacci(numero, digito)

