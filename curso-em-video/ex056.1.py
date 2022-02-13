# Analisador completo
'''Desenvolva um programa que leia o NOME, IDADE
e SEXO de 4 PESSOAS. No final do programa, mostre:
> A MÉDIA DE IDADE do grupo
> Qual é o nome do homem MAIS VELHO
> Quantas mulheres têm MENOS DE 20 ANOS'''

pessoas = 0
somaidade = 0
mulheres = 0
homemvelho = 0
homemnome = ''
for p in range(1, 5):
    nome = str(input('\033[1:34m''Digite o nome da {}ª pessoa: \033[m'.format(p)))
    idade = int(input('\033[1m''Digite a idade da {}ª pessoa: '.format(p)))
    print('Qual é o sexo da {}ª pessoa?''\033[m'.format(p))
    sexo = int(input('Digite \033[32m''0''\033[m para homem e \033[32m''1''\033[m para mulher: '))
    pessoas += 1
    somaidade += idade
    if p == 1 and sexo == 0: # verificando a primeira pessoa
        homemvelho += idade
        homemnome += nome
    elif sexo == 0 and idade > homemvelho:
        homemvelho += idade
        homemnome += nome
    elif sexo == 1 and idade < 20:
        mulheres += 1
media = somaidade / pessoas
print('\033[1m''A média de idade do grupo é {}'.format(media))
print('O homem mais velho se chama {}'.format(homemnome))
print('Há {} mulheres no grupo com menos de 20 anos'.format(mulheres))
