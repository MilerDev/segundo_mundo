"""Exercício Python 39:
Faça um programa que leia o ano de nascimento de um joveme informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date
n = int(input('Qual é seu ano de nascimento?'))
idade = date.today().year - n
print('a pessoa que nasceu no ano {} tem {} anos em {}'.format(n, idade, date.today().year))
if idade < 18:
    print('voce ainda vai se alistar ao serviço militar e falta {} ano para isso acontecer '.format(18-idade))
elif idade > 18:
    print('''ja passou do tempo de voce se alistar ao serviço militar 
    ja passou {} anos'''.format(idade - 18))
elif idade == 18:
    print('voce ja pode se alistar ao serviço militar')