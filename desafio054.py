"""Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade
 e quantas já são maiores."""
from datetime import date
atual = date.today().year
menores = 0
maiores = 0
for c in range(1, 8):
    n = int(input('em que ano a {}º pessoa nasceu'.format(c)))
    idade = atual - n
    if idade >= 21:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
print('E tambem tivimos {} pessoas menores de idade'.format(menores))


