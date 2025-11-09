#Encontrar todas las tripletas pitagoricas primitivas donde la hipotenusa sea N
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

