"""Exercício Python 041: A Confederação Nacional de Natação
 precisa de um programa que leia o ano de nascimento de um atleta e
 mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER"""

from datetime import date
n = int(input('qual é seu ano de nascimento?'))
ano = date.today().year
idade = ano - n
print('sua idade é {} anos'.format(idade))
if idade <= 9:
    print(' voce é da categoria Mirim')
elif idade <= 14:
    print('voce é da categoria Infantil')
elif idade <= 19:
    print('voce é da categoria Junior')
elif idade <= 25:
    print('voce é da categoria Senior')
elif idade > 25:
    print('voce é da categoria Mester')