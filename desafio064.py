"""Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
  No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""
n = 0
p = 999
d = 0
soma = 0
while n != p:
    n = int(input('digite um numero [parar 999]'))
    if n != p:
     d += 1
     soma += n

print('foram digitados {} numeros,a soma dos numeros digitados é {}'.format(d, soma))