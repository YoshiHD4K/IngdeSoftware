"""

Ejercicio: Convertir un número de 5 a 7 cifras en su representación en números romanos.
El programa solicitará al usuario un número entre 10000 y 9999999
y mostrará su equivalente en números romanos.

"""


def convertir_a_romano(numero):
    romano = ""
    numeros_romanos = {
        10000000 : "X\u0305\u0305",
        9000000 : "I\u0305\u0305X\u0305\u0305",
        8000000 : "V\u0305\u0305I\u0305\u0305I\u0305\u0305I\u0305\u0305",
        7000000 : "V\u0305\u0305I\u0305\u0305I\u0305\u0305",
        6000000 : "V\u0305\u0305I\u0305\u0305",
        5000000 : "V\u0305\u0305",
        4000000 : "I\u0305\u0305V\u0305\u0305",
        3000000 : "M̅M̅M̅",
        2000000 : "C̅C̅",
        1000000 : "M̅",
        900000 : "C̅M̅",
        500000 : "D̅",
        400000 : "C̅D̅",
        100000 : "C̅",
        90000 : "X̅C̅",
        50000 : "L̅",
        40000 : "X̅L̅",
        10000 : "X̅",
        9000 : "I̅X̅",
        5000 : "V̅",
        4000 : "I̅V̅",
        1000 : "M",
        900 : "CM",
        500 : "D",
        400 : "CD",
        100 : "C",
        90 : "XC",
        50 : "L",
        40 : "XL",
        10 : "X",
        9 : "IX",
        5 : "V",
        4 : "IV",
        1 : "I"
    }

    for valor, simbolo in numeros_romanos.items():
        while numero >= valor:
            romano += simbolo
            numero -= valor
    return romano

while True:
    numero = input("Ingrese un numero de 5 a 7 cifras: ")
    if numero.isdigit() and 10000 <= int(numero) <= 9999999:
        numero = int(numero)
        break
    else:
        print("Entrada invalida. Por favor, intente de nuevo.")

romano = convertir_a_romano(numero)
print(f"El numero {numero} en numeros romanos es: {romano}")