def es_palindromo(palabra):
    palabra = palabra.lower()
    if palabra.isalpha() == False:
        return False
    if len(palabra) < 2:
        return False
    return palabra == palabra[::-1]

while True:
    parrafo = input("Ingrese un párrafo con mínimo 100 caracteres: ")
    if len(parrafo) <= 100:
        break
    print("El párrafo debe tener al menos 100 caracteres. Intente nuevamente.")

cantidad_vocales = 0
cantidad_consonantes = 0
palindromos = []
palindromos_largos = []

palabras = parrafo.split()

for palabra in palabras:
    if es_palindromo(palabra):
        palindromos.append(palabra)
        if len(palabra) > 7:
            palindromos_largos.append(palabra)
    for char in palabra:
        if char.isalpha():
            if char.lower() in 'aeiouáéíóúü':
                cantidad_vocales += 1
            else:
                cantidad_consonantes += 1

print("Resultados:")
print(f"Párrafo ingresado: {parrafo}")
print(f"Cantidad de vocales: {cantidad_vocales}")
print(f"Cantidad de consonantes: {cantidad_consonantes}")
print(f"Palíndromos: {palindromos}")
print(f"Palíndromos largos: {palindromos_largos}")
