"""Exercício Python 52: Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo."""
tot = 0
n = int(input('digite um numero inteiro :'))
for c in range(1, n + 1,):
    if n % c == 0:
     print('\033[34m', end=' ')
     print('{}'.format(c), end=' ')
     tot += 1
    else:
     print('\033[33m', end=' ')
     print('{}'.format(c), end=' ')
print('\n\033[m o numero {} foi divisivel {} vezes '.format(n, tot))
if tot == 2:
  print('E por isso ele é PRIMO')
else:
  print('E por isso ele NÂO é PRIMO')