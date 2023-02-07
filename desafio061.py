# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo
# e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.

primeiro = int(input('primeiro termo:'))
razao = int(input('razao da PA'))
termo = primeiro
cot = 1
while cot <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cot += 1
print('FIM')