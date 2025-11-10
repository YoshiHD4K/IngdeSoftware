"""

Ejercicio: Determinar si un número de hasta 5 cifras es un palíndromo.
El programa solicitará al usuario un número entre 1 y 99999
y verificará si es un palíndromo.

"""


def es_palindromo(numero):
    str_num = str(numero)
    return str_num == str_num[::-1]

while True:
    try:
        numero = int(input("Ingrese un numero entre 1 y 99999: "))
        if 1 <= numero <= 99999:
            if es_palindromo(numero):
                print(f"El numero {numero} es un palindromo.")
            else:
                print(f"El numero {numero} no es un palindromo.")
            break
        else:
            print("El numero debe estar entre 1 y 99999. Intente de nuevo.")
    except ValueError:
        print("Entrada invalida. Por favor ingrese un numero entero.")