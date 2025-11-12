from re import match

parrafo = input("Ingrese el texto a analizar: ")

vocales, consonantes, espacio, charespecial = 0,0,0,0

for c in parrafo:
    if match(r'[aeiou]',c): 
        vocales += 1;
    elif match(r'[bcdfghjklmnñpqrstvwxyz]', c):
        consonantes += 1;
    elif match(r' ', c):
        espacio += 1;
    else:
        charespecial +=1;

print(f"Total de Vocales: {vocales}")
print(f"Total de Consonantes: {consonantes}")
print(f"Total de Espacios en Blanco: {espacio}")
print(f"Total de Caracteres especiales: {charespecial}")
