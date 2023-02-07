"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

numero1 = int(input('digite um munero: '))
numero2 = int(input('digite outro numero: '))
print("\u0001F60E")
sair = False
while not sair:
    menu = int(input("""MENU
    =================
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novo numero
    [5]Sair do programa
    ================== 
    >>Escola sua opção: """))
    if menu == 1:
        soma = numero1 + numero2
        print('A soma dos dois numeros é {}'.format(soma))
    elif menu == 2:
        mut = numero1 * numero2
        print('A multiplicaçao dos dois numeros São {}'.format(mut))
    elif menu == 3:
        if numero1 > numero2:
            print('o Maior numero é {}'.format(numero1))
        elif numero2 > numero1:
            print('o mair numero é {}'.format(numero2))
        else:
            print('os numeros são inguais,portando nao a numero maior')
    elif menu == 4:
        numero1 = int(input('digite o novo numero'))
        numero2 = int(input('digite o outro numero'))
    elif menu == 5:
        sair = True
    else:
        print('Opção invalida!')
print('fim')