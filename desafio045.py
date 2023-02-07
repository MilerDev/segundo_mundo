"""Exercício Python 45: Crie um programa
que faça o computador jogar Jokenpô com você."""
from time import sleep
from random import randint
itens = ('pedra ', 'papel', 'tesoura')
computador = randint(0, 2)
print("""suas opções :
[0]pedra
[1]papel
[2]tessora""")
jogador = int(input('qual é sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('Po')
if jogador != 0 and jogador != 1 and jogador != 2:
    print('jogada invalida')

print('-='*11)
print('o computador jogou {}'.format(itens[computador]))
print('o jogador jogou {}'.format(itens[jogador]))
print('=-'*11)

if computador == 0:
    if jogador == 0:
        print('empade')

    elif jogador == 1:
        print('jogador vence')

    elif jogador == 2:
      print('compudador vence')

elif computador == 1:
    if jogador == 0:
        print('compudaor vence')
    elif jogador == 1:
            print('empade')
    elif jogador == 2:
        print('jogador vence')

elif computador == 2:
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('compodaor vence')
    elif jogador == 2:
        print('empade')


