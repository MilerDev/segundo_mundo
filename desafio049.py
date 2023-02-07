"""Exercício Python 49: Refaça o DESAFIO 9,
 mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for."""
n = int(input('digite um numero '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))