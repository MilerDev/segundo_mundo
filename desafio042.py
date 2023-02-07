"""Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
 acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes"""

a = float(input('primeiro segmento:'))
b = float(input('segundo segmento:'))
c = float(input('teceiro segmento:'))

if a < b + c and b < a + c and c < a + b:
    print('os segmentos acima Podem formar Um triângulo ', end='')
    if a == b and b == c:
        print('Equilatero')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('Isosceles')

else:
    print('os segmentos acima não podem formar triângulo')