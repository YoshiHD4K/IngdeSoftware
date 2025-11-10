"""

Ejercicio: Conteo de palabras en un párrafo.

Desarrolla un programa en Python que cuente la frecuencia de cada palabra en un párrafo dado.
El programa debe ignorar mayúsculas, minúsculas y signos de puntuación. 
Solo se deben contar las palabras que tengan más de dos letras.
El resultado debe mostrarse en orden descendente de frecuencia.

"""

import re

parrafo = "El Avila, majestuoso guardian de la ciudad, se alza imponente. Sus senderos, repletos de vida, invitan a la aventura. La neblina envuelve las laderas, regalando postales unicas. El Pico Naiguata, el punto mas alto, desafia a los montañistas con su cumbre. La caminata es un ejercicio para el alma. Se respira paz. Caracas amanece, y el cerro, silencioso testigo de la vida urbana, sigue esperando al proximo excursionista."
parrafo = parrafo.lower()
parrafo = re.sub(r'[^\w\s]','',parrafo)

palabras = parrafo.split()

contador_palabras = {}


for palabra in palabras:
    if len(palabra) > 2:
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        else:
            contador_palabras[palabra] = 1

print("Ordenando...\n")

contador_palabras = dict(sorted(contador_palabras.items(), key=lambda item: item[1], reverse=True))

print("Conteo de palabras en el parrafo:\n")
for palabra, conteo in contador_palabras.items():
    print(f"{palabra}: {conteo}")