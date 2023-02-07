# Exercício Python 62: Melhore o DESAFIO 61,
# perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('primeiro termo:'))
razao = int(input('razao da PA:'))
termo = primeiro
cot = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cot <= total:
      print('{} ->'.format(termo), end='')
      termo += razao
      cot += 1
    print('Pausa')
    mais = int(input('quanto termos você quer mostra a mais?'))
print('progressao finalizada com {} termos mostrados'.format(total))
