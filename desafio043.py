"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
 calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida"""

peso = float(input('qual é seu peso?(kg)'))
altura = float(input('qual é sua altura?(m)'))
imc = peso / (altura**2)
print('o IMC dessa pessoa é de  {:.1f}'.format(imc))
if imc < 18.5:
    print('VOce está Abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('VOce esta em Sobrepeso')
elif 30 <= imc <= 40:
    print('Voce esta em Obesidade')
elif imc >= 40:
    print('Obesidade morbida')