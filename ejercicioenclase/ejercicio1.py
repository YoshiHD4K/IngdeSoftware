"""

Ejercicio 1: Sistema de Venta de Boletos de Viaje

Desarrolla un programa en Python que permita a los usuarios comprar boletos de viaje.
El programa debe incluir las siguientes funcionalidades:

1. Comprar Boletos:
- Solicitar al usuario la cantidad de boletos que desea comprar.
- Para cada boleto, solicitar la edad del pasajero, el destino y si el pago será con tarjeta.
- Calcular el precio del boleto considerando:
  - Precio base: $50
  - Descuento del 20% para menores de 18 años.
  - Descuento del 30% para adultos mayores (65 años o más).
  - Descuento adicional del 10% si el pago es con tarjeta.
- Almacenar los detalles de cada boleto en una lista.
2. Ver Boletos Comprados:
- Mostrar una lista de todos los boletos comprados con sus detalles (edad, destino, método de pago, precio final).
3. Ver Reporte de Ventas:
- Calcular y mostrar el total de ventas y el total de descuentos otorgados.
- Mostrar el promedio de ventas por boleto vendido.

"""

class Boleto: # Clase para representar un boleto de viaje
    def __init__(self):
        self.edad = 0
        self.destino = ""
        self.tarjeta = False
        self.precio = 0.0
        self.descuento = 0.0


def comprar_boletos(ListaBoletos, num_boletos): # Función para comprar boletos
    for i in range(num_boletos):
        boleto = Boleto()
        print(f"\nComprando boleto {i + 1}:")
        boleto.edad = int(input("Ingrese la edad del pasajero: "))
        boleto.destino = input("Ingrese el destino: ")
        while True: # Solicita si el pago será con tarjeta, validando la entrada
            tarjeta_input = input("¿Pagará con tarjeta? (s/n): ").lower()
            if tarjeta_input in ['s', 'n']:
                boleto.tarjeta = tarjeta_input == 's'
                break
            else:
                print("Entrada no válida. Por favor ingrese 's' o 'n'.")
        boleto.precio = 50.0  # Precio base del boleto
        if boleto.edad < 18:
            boleto.descuento += boleto.precio * 0.2  # 20% de descuento para menores de edad
        elif boleto.edad >= 65:
            boleto.descuento += boleto.precio * 0.3  # 30% de descuento para adultos mayores
        if boleto.tarjeta:
            boleto.descuento += (boleto.precio - boleto.descuento) * 0.1  # 10% de descuento por pago con tarjeta, aplicado sobre el precio después de otros descuentos
        ListaBoletos.append(boleto) # Agrega el boleto a la lista de boletos comprados
        print("Boleto comprado con éxito.")

def ver_boletos_comprados(ListaBoletos): # Función para ver los boletos comprados
    print("\n\n")
    if not ListaBoletos: # Verifica si la lista de boletos está vacía
        print("No se han comprado boletos aún.")
        return
    for i, boleto in enumerate(ListaBoletos, start=1): # Muestra los detalles de cada boleto comprado
        precio_final = boleto.precio - boleto.descuento # Calcula el precio final después de descuentos
        print(f"Boleto {i}: Destino: {boleto.destino}, Edad: {boleto.edad}, "
              f"Pago con tarjeta: {'Sí' if boleto.tarjeta else 'No'}, "
              f"Precio final: ${precio_final:.2f}")

def ver_reporte_ventas(ListaBoletos): # Función para ver el reporte de ventas
    if not ListaBoletos: # Verifica si la lista de boletos está vacía
        print("No se han vendido boletos aún.")
        return

    total_ventas = sum(boleto.precio - boleto.descuento for boleto in ListaBoletos) / len(ListaBoletos) # Promedio de ventas totales (precio menos descuento)
    total_descuentos = sum(boleto.descuento for boleto in ListaBoletos) # Suma total de descuentos otorgados

    print(f"Total de ventas: ${total_ventas:.2f}") 
    print(f"Total de descuentos: ${total_descuentos:.2f}")

def menu(): # Función del menú principal
    ListaBoletos = []
    while True: # Bucle infinito para mostrar el menú hasta que el usuario decida salir
        print("\n\nOpciones:")
        print("1. Comprar Boletos")
        print("2. Ver Boletos Comprados")
        print("3. Ver Reporte de Ventas")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        match opcion:
            case "1": # Opción para comprar boletos
                num_boletos = int(input("¿Cuántos boletos desea comprar? "))
                comprar_boletos(ListaBoletos, num_boletos)
            case "2": # Opción para ver los boletos comprados
                ver_boletos_comprados(ListaBoletos)
            case "3": # Opción para ver el reporte de ventas
                ver_reporte_ventas(ListaBoletos)
            case "4": # Opción para salir del programa
                print("Saliendo del programa.")
                return
            case _: # Opción inválida
                print("Opción no válida. Intente de nuevo.")


menu()

