while True:
    numero_tarjeta = input("Ingrese el número de tarjeta de crédito (o 'salir' para terminar): ")
    if numero_tarjeta.lower() == 'salir':
        break
    if len(numero_tarjeta) != 16 or not numero_tarjeta.isdigit():
        print("Número de tarjeta inválido. Debe tener 16 dígitos.")
        continue
    else:
        suma = 0
        for caracter in numero_tarjeta[::-2]:
            caracter_doble = int(caracter) * 2
            if caracter_doble > 9:
                caracter_doble -= 9
            suma += caracter_doble
        for caracter in numero_tarjeta[-2::-2]:
            suma += int(caracter)
        if suma % 10 == 0:
            print("Número de tarjeta válido.")
        else:
            print("Número de tarjeta inválido.")

