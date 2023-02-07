"""Exercício Python 58: Melhore o jogo do DESAFIO 28
onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar,
  mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
from time import sleep
c = randint(0, 10)
print('pensei em um numero entre 0 e 10.')
print('sera que voce consegue  adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('qual é seu palpite? '))
    palpite += 1
    if jogador == c:
        acertou = True
    else:
        if jogador < c:
            print('Mais...tente mais uma vez.')
        elif jogador > c:
            print('menos... tente mais uma vez.')
print('acertou com {} tentativas, Parabens!'.format(palpite))


