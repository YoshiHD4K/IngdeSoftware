"""

Ejercicio: Convertir un número en su representación en letras. 
El programa solicitará al usuario un número entre 0 y 9999
y mostrará su equivalente en palabras.

"""


def numero_a_letra(numero):
    strunidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    strdecenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    strcentenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    strmiles = ["", "mil", "dos mil", "tres mil", "cuatro mil", "cinco mil", "seis mil", "siete mil", "ocho mil", "nueve mil"]

    if numero == 0:
        return "cero"

    miles = int(numero // 1000)
    centenas = int((numero % 1000) // 100)
    decenas = int((numero % 100) // 10)
    unidades = int(numero % 10)

    resultado = ""

    if miles > 0:
        resultado += strmiles[miles] + " "

    if centenas > 0:
        if centenas == 1 and decenas != 0 and unidades != 0:
            resultado += "ciento "
        elif centenas == 1:
            resultado += "cien "
        else:
            resultado += strcentenas[centenas] + " "

    if decenas > 0:
        if decenas == 1:
            if unidades == 0:
                resultado += "diez "
            elif unidades == 1:
                resultado += "once "
            elif unidades == 2:
                resultado += "doce "
            elif unidades == 3:
                resultado += "trece "
            elif unidades == 4:
                resultado += "catorce "
            elif unidades == 5:
                resultado += "quince "
            else:
                resultado += "dieci"
        elif decenas == 2:
            if unidades == 0:
                resultado += "veinte "
            else:
                resultado += "veinti"
        else:
            resultado += strdecenas[decenas] + " "
            if unidades > 0:
                resultado += "y "


    if unidades > 0:
        resultado += strunidades[unidades] + " "

    return resultado.strip()


while True:
    try:
        numero = int(input("Ingrese un número entre 0 y 9999: "))
        if 0 <= numero <= 9999:
            print(f"El numero {numero} en letras es: {numero_a_letra(numero)}")
            break
        else:
            print("Número fuera de rango. Intente de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")