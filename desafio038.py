"""Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais"""

a = int(input('digite um numero inteiro:'))
b = int(input('digite outro numero inteiro'))

if a > b:
    print('o primeiro valor é maior')
elif b > a:
    print('o segunto valor é maior')
else:
    print('nao existe valor maior , os dois sao iguais')