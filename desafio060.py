"""Exercício Python 060: Faça um programa que leia um número qualquer
 e mostre o seu fatorial."""
from math import factorial
print('caculando o fatorial')
n = int(input('digite o numero: '))
c = n
f = 1
m = factorial(n)
print('CALCULANDO {}! =  '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' =', end='')
    f *= c
    c -= 1
print(' {}'.format(f))