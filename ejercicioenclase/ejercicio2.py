while True:
    numero_tarjeta = input("Ingrese el número de tarjeta de crédito (o 'salir' para terminar): ") # Solicita al usuario que ingrese un número de tarjeta de crédito o 'salir' para terminar
    if numero_tarjeta.lower() == 'salir':
        break
    if len(numero_tarjeta) != 16 or not numero_tarjeta.isdigit(): # Verifica si el número tiene 16 dígitos y si todos son numéricos
        print("Número de tarjeta inválido. Debe tener 16 dígitos.")
        continue
    else:
        suma = 0
        for caracter in numero_tarjeta[::-2]: # Procesa los dígitos en posiciones pares desde el final
            caracter_doble = int(caracter) * 2 # Duplica el valor del dígito
            if caracter_doble > 9: # Si el valor duplicado es mayor que 9, suma los dígitos del resultado (resta 9 que es equivalente)
                caracter_doble -= 9
            suma += caracter_doble # Suma el valor ajustado a la suma total
        for caracter in numero_tarjeta[-2::-2]: # Procesa los dígitos en posiciones impares desde el final
            suma += int(caracter) # Suma directamente el valor del dígito a la suma total
        if suma % 10 == 0: # Verifica si la suma total es múltiplo de 10, lo que indica validez según el algoritmo de Luhn
            print("Número de tarjeta válido.")
        else:
            print("Número de tarjeta inválido.")

