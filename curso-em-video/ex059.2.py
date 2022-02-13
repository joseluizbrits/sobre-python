# Criando um Menu de Opções
'''Crie um programa que leia DOIS VALORES
e mostre um MENU, como o exemplificado abaixo:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
Seu programa deverá realizar a
operação solicitada em cada caso'''

from time import sleep
n1 = int(input('\033[1m''Primeiro valor: '))
n2 = int(input('Segundo valor: \033[m'))
opcao = 0
while opcao != 5:
    print('''    \033[1;36m[ 1 ]\033[m somar
    \033[1;36m[ 2 ]\033[m multiplicar
    \033[1;36m[ 3 ]\033[m maior
    \033[1;36m[ 4 ]\033[m novos números
    \033[1;36m[ 5 ]\033[m sair do programa''')
    opcao = int(input('\033[1;36m>>>>>\033[m \033[1m'' Qual é a sua opção? \033[m'))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre \033[35m{}\033[m + \033[35m{}\033[m é \033[35m{}\033[m'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de \033[35m{}\033[m x \033[35m{}\033[m é \033[35m{}\033[m'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre \033[35m{}\033[m e \033[35m{}\033[m o maior valor é \033[35m{}\033[m'.format(n1, n2, maior))
    elif opcao == 4:
        print('\033[1m''Informe os números novamente: ')
        n1 = int(input('Primero valor: '))
        n2 = int(input('Segundo valor: \033[m'))
    elif opcao == 5:
        print('\033[1m''Finalizando...\033[m')
    else:
        print('\033[31m''Opção inválida. Tente novamente''\033[m')
    print('\033[1;36m''=-=''\033[m' * 10)
    sleep(2)
print('\033[1;32m''Fim do programa! Volte sempre!')
