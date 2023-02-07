"""Exercício Python 040: Crie um programa que leia duas
 notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO"""

nome = str(input('Qual é seu nome?'))
a = float(input('digite a primeira nota:'))
b = float(input('digite a segunta nota:'))

n = (a + b) / 2
print('a media foi {}'.format(n))
if n < 5:
    print('{},você foi reprovado'.format(nome))
elif 7 > n >= 5:
    print('{}, você esta de recuperação'.format(nome))
elif n >= 7:
    print('Parabens {}, você foi aprovado'.format(nome))

