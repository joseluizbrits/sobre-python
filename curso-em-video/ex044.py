# Gerenciador de Pagamentos
'''Elabore um program que calcule o valor a ser pago por um
produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
- À vista DINHEIRO/CHEQUE: 10% de desconto
- À vista no CARTÃO: 5% de desconto
- Em até 2x NO CARTÃO: preço normal
- 3x OU MAIS no cartão: 20% de juros'''

print('\033[1:35:40m''{:=^40}''\033[m'.format(' SUPER LOJAS '))
price = float(input('\033[1:40m''Preço das compras: R$ '))
print('''Escolha a forma de pagamento:\033[m
\033[1:35m[ 1 ]\033[m à vista no dinheiro ou cheque
\033[1:35m[ 2 ]\033[m à vista no cartão
\033[1:35m[ 3 ]\033[m em até 2x no cartão
\033[1:35m[ 4 ]\033[m 3x ou mais no cartão''')
option = int(input('\033[1:30:45m''Sua opção:\033[m '))
print('\033[1:40m''O valor das compras foram R$ {:.2f}''\033[m'.format(price))
if option == 1:
    pay = price - (price * 0.10)
    print('\033[1:40m''Pagando à vista no dinheiro ou cheque, você ganha 10% de desconto!\033[m')
    print('\033[1:40m''O valor total ficará R$ {:.2f}'.format(pay))
elif option == 2:
    pay = price - (price * 0.05)
    print('\033[1:40m''Pagando à vista no cartão, você ganha 5% de desconto!\033[m')
    print('\033[1:40m''O valor total ficará R$ {:.2f}''\033[m'.format(pay))
elif option == 3:
    pay = price / 2
    print('\033[1:40m''Você pagará duas paracelas de R$ {:.2f} SEM JUROS!\033[m'.format(pay))
elif option == 4:
    pay = price + (price * 0.20)
    nparcela = int(input('\033[1:30:45m''Informe a quantidade de parcelas:\033[m '))
    parcela = price / nparcela
    print('\033[1:40m''Sua compra será parcelada em {}x COM JUROS!\033[m'.format(nparcela))
    print('\033[1:40m''O valor das parcelas será de R$ {:.2f}''\033[m'.format(parcela))
    print('\033[1:40m''O valor total ficará R$ {:.2f}''\033[m'.format(pay))
else:
    print('\033[31m''Opção inválida. Tente novamente')
