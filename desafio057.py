"""Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
 mas só aceite os valores ‘M’ ou ‘F’.
 Caso esteja errado, peça a digitação novamente até ter um valor correto."""
c = 0
sexo = str(input('informe seu sexo: [M/F]')).strip().upper()[0]

while sexo not in "MnFf":
    sexo = str(input('dados invalidos. por favor, informe seu sexo: '))
print('sexo {} registado com sucesso'.format(sexo))


