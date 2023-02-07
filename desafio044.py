"""Exercício Python 44: Elabore um programa que calcule o valor a ser pago
 por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros"""

preço = float(input('qual o preço do produto?R$'))
print("""como deseja pagar 
[ 1 ]á vista Dinheiro/cheque:10% de desconto
[ 2 ]a vista no cartão:5% de desconto
[ 3 ]em ate 2x no cartão:preço formal
[ 4 ]3x ou mais no catão:20% de juro""")
opcao = int(input('QUAl é a opção'))
if opcao == 1:
    total = preço-(preço * 10 / 100)
    print('o total para pagar é {:.2f}'.format(total))
elif opcao == 2:
    total = preço - (preço * 5 / 100)
    print('o total a pagar é {:.2f}'.format(total))
elif opcao == 3:
    print('sua compra sera paselada 2x de  {:.2f}, a sua compra vai custar {:.2f}'.format(preço / 2,preço))

elif opcao == 4:
    total = preço + (preço * 20 / 100)
    tp = int(input('quantas parcelas'))
    passela = total / tp
    print('sua compra sera pacelada em {}x de R${} com juros'.format(tp, passela))
    print('sua compra de R${} vai custar R${} no final '.format(preço, total))
