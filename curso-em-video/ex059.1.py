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

n1 = int(input('\033[1m''Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('''Escolha a operação que você deseja efetuar:
\033[1;36m[ 1 ]\033[m somar
\033[1;36m[ 2 ]\033[m multiplicar
\033[1;36m[ 3 ]\033[m maior
\033[1;36m[ 4 ]\033[m novos números
\033[1;36m[ 5 ]\033[m sair do programa''')
iteracao = False
while not iteracao:
    option = int(input('\033[1m''Sua opção:\033[m '))
    if 0 < option <= 5:
        if option == 1:
            r = n1 + n2
            print('A soma de \033[1;35m{}\033[m com \033[1;35m{}\033[m é igual a \033[1;35m{}\033[m'.format(n1, n1, r))
        elif option == 2:
            r = n1 * n2
            print('O produto de \033[1;35m{}\033[m com \033[35m{}\033[m é igual a \033[1;35m{}\033[m'.format(n1, n2, r))
        elif option == 3:
            if n1 > n2:
                print('O número \033[1;35m{}\033[m é maior do que o número \033[1;35m{}\033[m'.format(n1, n2))
            else:
                print('O número \033[1;35m{}\033[m é maior do que o número \033[1;35m{}\033[m'.format(n2, n1))
        elif option == 4:
            print('\033[1m''Informe os números novamente: ')
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: \033[m'))
        elif option == 5:
            iteracao = True
            print('\033[32m''Programa finalizado com sucesso!')
    else:
        print('\033[31m''Opção inválida. Tente novamente.\033[m')