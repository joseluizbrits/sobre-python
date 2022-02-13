# Analisador completo
'''Desenvolva um programa que leia o NOME, IDADE
e SEXO de 4 PESSOAS. No final do programa, mostre:
> A MÉDIA DE IDADE do grupo
> Qual é o nome do homem MAIS VELHO
> Quantas mulheres têm MENOS DE 20 ANOS'''

somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('\033[7:1:32m---- {}ª PESSOA ----\033[m'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm': # "in" significa se está dentro de "Mm", ou seja, se possui M ou m na string
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de \033[32m''{}''\033[m anos'.format(mediaidade))
print('O homem mais velho tem \033[32m''{}''\033[m anos e se chama \033[32m''{}''\033[m'.format(maioridadehomem, nomevelho))
print('Ao todo são \033[32m''{}''\033[m mulheres com menos de 20 anos'.format(totmulher20))
