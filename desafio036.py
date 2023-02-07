""" A Provando Empréstimo
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
valor = float(input('Qual o valor da casa?'))
salario = float(input('Quanto é seu salario?'))
anos = int(input('em quantos anos vai pagar?'))

r = valor / (anos * 12)
minimo = salario * 30 / 100

print('para pagar uma casa de R${:.2f} em {} anos '.format(valor, anos))
print(' a prestação sera de R${:.2f}'.format(r))
if r <= minimo:
    print('Emprestimo pode ser Concedido!')
else:
    print('Envelismente o Emprestimo Negado! ')


