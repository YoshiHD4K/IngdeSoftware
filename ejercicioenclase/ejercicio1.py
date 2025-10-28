class Boleto:
    def __init__(self):
        self.edad = 0
        self.destino = ""
        self.tarjeta = False
        self.precio = 0.0
        self.descuento = 0.0


def comprar_boletos(ListaBoletos, num_boletos):
    for i in range(num_boletos):
        boleto = Boleto()
        print(f"\nComprando boleto {i + 1}:")
        boleto.edad = int(input("Ingrese la edad del pasajero: "))
        boleto.destino = input("Ingrese el destino: ")
        boleto.tarjeta = input("¿Este boleto se paga con tarjeta? (s/n): ").lower() == "s"
        boleto.precio = 50.0  # Precio base del boleto
        if boleto.edad < 18:
            boleto.descuento += boleto.precio * 0.2  # 20% de descuento para menores de edad
        elif boleto.edad >= 65:
            boleto.descuento += boleto.precio * 0.3  # 30% de descuento para adultos mayores
        if boleto.tarjeta:
            boleto.descuento += boleto.precio * 0.1  # 10% de descuento por pago con tarjeta
        ListaBoletos.append(boleto)
        print("Boleto comprado con éxito.")

def ver_boletos_comprados(ListaBoletos):
    if not ListaBoletos:
        print("No se han comprado boletos aún.")
        return
    for i, boleto in enumerate(ListaBoletos, start=1):
        precio_final = boleto.precio - boleto.descuento
        print(f"Boleto {i}: Destino: {boleto.destino}, Edad: {boleto.edad}, "
              f"Pago con tarjeta: {'Sí' if boleto.tarjeta else 'No'}, "
              f"Precio final: ${precio_final:.2f}")

def ver_reporte_ventas(ListaBoletos):
    if not ListaBoletos:
        print("No se han vendido boletos aún.")
        return
    total_ventas = sum(boleto.precio - boleto.descuento for boleto in ListaBoletos)
    print(f"Total de ventas: ${total_ventas:.2f}")
    

def menu():
    ListaBoletos = []
    while True:
        print("\n\nOpciones:")
        print("1. Comprar Boletos")
        print("2. Ver Boletos Comprados")
        print("3. Ver Reporte de Ventas")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        match opcion:
            case "1":
                num_boletos = int(input("¿Cuántos boletos desea comprar? "))
                comprar_boletos(ListaBoletos, num_boletos)
            case "2":
                ver_boletos_comprados(ListaBoletos)
            case "3":
                #ver_reporte_ventas()
                pass
            case "4":
                print("Saliendo del programa.")
                return
            case _:
                print("Opción no válida. Intente de nuevo.")


menu()

