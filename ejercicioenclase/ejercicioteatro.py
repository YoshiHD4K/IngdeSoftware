from time import sleep
from os import system
from re import match

class Boleto:
    def __init__(self):
        self.asiento = ""
        self.precio = 0.0
        self.descuento = 0.0
        self.edad = 0
        
def imprimir_asientos(asientos):
    print("="*25)
    print("\n\n        Sala de Teatro\n")

    for fila in asientos:
        for asiento in fila:
            print(asiento, end=" ")
        print()
    print("\n")
    print("="*25)
    print("\n")

def cancelarboletos(teatro_asientos, listaboletos):
    print("="*55)
    print("\n")
    for i, boleto in enumerate(listaboletos):
        print(f"{i+1}. Asiento: {boleto.asiento} - Precio: {boleto.precio} - Descuento: {boleto.descuento} - Edad: {boleto.edad} - Tarjeta: {'Si' if boleto.tarjeta else 'No'}")
    try:
        numboleto = int(input("Ingrese el numero de boleto a cancelar: "))
        boleto_cancelado = listaboletos.pop(numboleto -1)
        columna = ord(boleto_cancelado.asiento[0]) - ord('A') +1
        fila = int(boleto_cancelado.asiento[-1])
        teatro_asientos[fila][columna] = "O"
        print("Boleto cancelado exitosamente.")
    except IndexError:
        print("El numero de boleto ingresado es invalido.")

def reporteventas(listaboletos):
    total_ventas = 0.0
    total_descuentos = 0.0
    print("="*55)
    print("\n")
    print("Reporte de Ventas:\n")
    for boleto in listaboletos:
        total_ventas += boleto.precio
        total_descuentos += boleto.descuento
        print(f"Asiento: {boleto.asiento} - Precio: {boleto.precio} - Descuento: {boleto.descuento} - Edad: {boleto.edad} - Tarjeta: {'Si' if boleto.tarjeta else 'No'}")
    print("\n")
    print(f"Total de ventas: {total_ventas}")
    print(f"Total de descuentos otorgados: {total_descuentos}")
    input("Presione enter para continuar...")

def menu():
    listaboletos = []
    while True:
        print("="*55)
        print("\n                Gestor de boletos de teatro\n")
        print("       1. Ver disponibilidad de asientos.")
        print("       2. Comprar Boletos.")
        print("       3. Cancelar asientos.")
        print("       4. Reporte de ventas.")
        print("       5. Salir.\n")
        print("="*55)
        opc = input("\n       Elige una opcion: ")

        match opc:
            case "1":
                sleep(2)
                system("cls")
                imprimir_asientos(teatro_asientos)
                input("Presione enter para continuar...")
                sleep(2)
                system("cls")

            case "2":
                sleep(2)
                system("cls")
                comprarboletos(teatro_asientos, listaboletos)
                sleep(2)
                system("cls")
            case "3":
                sleep(2)
                system("cls")
                cancelarboletos(teatro_asientos, listaboletos)
                sleep(2)
                system("cls")
            case "4":
                sleep(2)
                system("cls")
                reporteventas(listaboletos)
                sleep(2)
                system("cls")
            case "5":
                sleep(2)
                system("cls")
                print("Saliendo del sistema...")
                sleep(2)
                system("cls")
            case _:
                sleep(1)
                system("cls")
                print("Valor incorrecto, intente nuevamente.")
                sleep(1)
                system("cls")

def validarasiento(asiento, teatro_asientos):
    if match(r'^[A-J][1-5]+$',asiento):
        columna = ord(asiento[0]) - ord('A') +1
        fila = int(asiento[-1])

        if teatro_asientos[fila][columna] == "O":
            teatro_asientos[fila][columna] = "X"
            return True
        else:
            print(fila,columna)
            print("El asiento esta ocupado.")
            return False
    else:
        print("El asiento ingresado es invalido.")
        return False

def comprarboletos(teatro_asientos, listaboletos):
    print("="*55)
    print("\n")
    try:
        numboletos = int(input("Introduce el numero de boletos a escoger: "))
    except:
        print("Ingrese un numero natural.")
    sleep(2)
    system("cls")
    for i in range(0,numboletos):
        boleto = Boleto()
        print("="*55)
        print("\n")
        print(f"Comprando Boleto: Nro{i+1}.")
        print("\n\n")
        imprimir_asientos(teatro_asientos)
        asiento = ""
        while True:
            asiento = input("Ingrese el asiento a escoger (Ejemplo: A1) (A-J)(1-5): ")
            if validarasiento(asiento, teatro_asientos) == True:
                break
        boleto.asiento = asiento
        boleto.edad = int(input("Ingrese la edad del espectador: "))
        tarjeta = input("Pagara con tarjeta? (S/N)")
        boleto.tarjeta = True if tarjeta == "S" else False
        if int(asiento[-1]) == 1 or int(asiento[-1]) == 2:
            boleto.precio = 80
        else:
            boleto.precio = 50

        if boleto.edad < 25:
            boleto.descuento = boleto.precio * 0.15
        elif boleto.edad > 65:
            boleto.descuento = boleto.precio * 0.25

        if boleto.tarjeta:
            boleto.descuento -= (boleto.precio - boleto.descuento)*0.05
        
        listaboletos.append(boleto)
        print("Boleto Comprado!")
        sleep(2)
        system("cls")
        
teatro_asientos = [
    [" ","A","B","C","D","E","F","G","H","I","J"],
    ["1","O","O","O","O","O","O","O","O","O","O"],
    ["2","O","O","O","O","O","O","O","O","O","O"],
    ["3","O","O","O","O","O","O","O","O","O","O"],
    ["4","O","O","O","O","O","O","O","O","O","O"],
    ["5","O","O","O","O","O","O","O","O","O","O"],
]

menu()