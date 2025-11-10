"""

Ejercicio 6: Tripletas pitagóricas primitivas.
Desarrolla un programa en Python que encuentre todas las tripletas pitagóricas primitivas (a, b, c)
donde c es un número entero positivo dado por el usuario. Una tripleta pitagórica primitiva satisface la
ecuación a^2 + b^2 = c^2, y a, b, c son coprimos (su máximo común divisor es 1).

"""

import math

def tripletas_pitagoricas_primitivas(N):
    tripletas = []
    for m in range(2, int(math.sqrt(N)) + 1):
        for n in range (1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                if c == N:
                    tripletas.append((a, b, c))
    return tripletas

Numero = int(input("Ingrese un numero entero positivo para la hipotenusa: "))
tripletas = tripletas_pitagoricas_primitivas(Numero)

for tripleta in tripletas:
    print(tripleta)

