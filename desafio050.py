"""Exercício Python 50: Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
 Se o valor digitado for ímpar, desconsidere-o."""
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('digite um numero'))
    if n % 2 == 0:
        cont = cont + 1
        soma = soma + n

print('dos valore digitados  {} são  valore par e soma dos valore par são {}'.format(cont, soma))