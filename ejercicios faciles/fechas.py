import validaciones as val
import datetime as dt

def contardias(fecha):
    fecha_actual = dt.date.today()
    contador = 0
    # Ajustar la fecha al día 15 del mes correspondiente
    if fecha.day > 15:
        # Avanzar al siguiente mes si el día es mayor a 15
        if fecha.month == 12:
            fecha = dt.date(fecha.year + 1, 1, 15)
        else:
            fecha = dt.date(fecha.year, fecha.month + 1, 15)
    else:
        fecha = dt.date(fecha.year, fecha.month, 15)

    while fecha <= fecha_actual:
        if fecha.day == 15 and fecha.weekday() == 5:  # 5 representa sábado
            contador += 1
        # Avanzar al siguiente mes
        if fecha.month == 12:
            fecha = dt.date(fecha.year + 1, 1, 15)
        else:
            fecha = dt.date(fecha.year, fecha.month + 1, 15)
    return contador


while True:
    while True:
        dia = int(input("Ingrese el día (1-31): "))
        if 1 <= dia <= 31:
            break
        print("Día inválido. Intente nuevamente.")
    while True:
        mes = int(input("Ingrese el mes (1-12): "))
        if 1 <= mes <= 12:
            break
        print("Mes inválido. Intente nuevamente.")
    while True:
        año = int(input("Ingrese el año (positivo): "))
        if año > 0:
            break
        print("Año inválido. Intente nuevamente.")
    if val.is_valid_date(dia, mes, año):
        print(f"La fecha {dia}/{mes}/{año} es válida.")
        break
    else:
        print(f"La fecha {dia}/{mes}/{año} es inválida. Intente nuevamente.")

fecha_ingresada = dt.date(año, mes, dia)
dias_transcurridos = contardias(fecha_ingresada)
print(f"Han transcurrido {dias_transcurridos} sábados 15 desde la fecha ingresada hasta hoy.")