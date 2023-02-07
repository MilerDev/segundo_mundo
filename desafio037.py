""" Conversor de bases numericas
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
"""
numero = int(input('digite um numero inteiro: '))
print('Escolha uma das bases para conversão:')
print('[1]converter para binario ')
print('[2]converter para OCTAL')
print('[3]converter para HEXADECIMAL')
o = int(input('sua opção:'))
if o == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero, bin(numero)[2:]))
elif o == 2:
    print('{} convertido para OCTAL é iqual a {}'.format(numero, oct(numero)[2:]))
elif o == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('opição envalita! tente novamente')