"""Exercício Python 53: Crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

frase = str(input('digite uma frase')).strip().upper()
palvras = frase.split()
junto = ''.join(palvras)
inverso = junto[::-1]
"""for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]"""
print('O inveso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palindromo!')
else:
    print('A frase nao é um polindromo')


