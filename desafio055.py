"""Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
 No final, mostre qual foi o maior e o menor peso lidos"""
maior = 0  # menor
menor = 0  # maior
for c in range(1, 6):
    n = float(input('Qual é o peso da {}º pessoa?'.format(c)))
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('o maior peso lido é  de {}Kg,'.format(maior))
print('o menor peso lido é de {}Kg '.format(menor))