def anagrama(palabra1:str, palabra2:str):
    palabra_uno = palabra_uno.lower()
    palabra_dos = palabra_dos.lower()

    if palabra_dos == palabra_uno:
        return True

    letras_palabra_uno = []
    letras_palabra_dos = []

    for c in palabra_uno:
        letras_palabra_uno.append(c)

    for c in palabra_dos:
        letras_palabra_dos.append(c)

    letras1 = sorted(letras1)
    letras2 = sorted(letras2)
    
    return letras1 == letras2

palabra_uno = input("Escribe la primera palabra: ")
palabra_dos = input("Escribe la segunda palabra: ")

if anagrama(palabra_uno, palabra_dos):
    print("SI SON")
else:
    print("NO SON")
