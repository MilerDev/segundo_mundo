"""Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores"""

numeros = 0
maior = 0
menor = 0
numero = 0
soma = 0
d = 0
while numeros != 999:
    numeros = int(input('digite um numero[parar 999]: '))
    if numeros != 999:
      d += 1
      soma += numeros

      if numeros >= numero:
        maior = numeros
      if numeros <= numero:
          menor = numeros
media = soma / d
print('A media dos numeros é {}, o maior numero digitado foi {}, o menor foi {}'.format(media, maior, menor))