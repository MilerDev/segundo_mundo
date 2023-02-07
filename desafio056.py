"""Exercício Python 56: Desenvolva um programa que leia o nome
, idade e sexo de 4 pessoas. No final do programa, mostre:
 a média de idade do grupo, qual é o nome do homem mais velho
 e quantas mulheres têm menos de 20 anos."""

soma = 0
media = 0
maiorM = 0
nvelho = 0
mulhe = 0
for p in range(1, 5):
    print('-----{}º pessoa -----'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('[M/F]:')).strip().upper()
    soma += idade
    # idade do homem mais velho
    if p == 1 and sexo in 'Mn':
        maiorM = idade
        nvelho = nome
    # nome do homem mais velho
    if sexo in 'Mm' and idade > maiorM:
        nvelho = nome
        maiorM = idade
    # todal de mulher
    if sexo in 'Ff'and idade < 20:
        mulhe += 1
# media das idades
media = soma / 4
print('A media de idade do grupo é de {} anos '.format(media))
print('o homem mais velho tem {} anos e se chama {}'.format(maiorM, nvelho))
print('Ao todo são {} mulheres de menor idade '.format(mulhe))
