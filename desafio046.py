""" faça um programa que mostre na tela uma contagem regressiva
para o astouro de fogo de artificio indo de 10 ate 0,
com  uma pausa de 1 segunto entre eles ."""
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)

print("""BUM!!BUM!!!!POOW!!*************""")