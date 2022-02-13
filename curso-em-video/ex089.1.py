# Boletim com listas compostas
'''Crie um programa que leia NOME e DUAS
NOTAS de vários alunos e guarde tudo em
uma LISTA COMPOSTA. No final, mostre um
BOLETIM contendo a MÉDIA de cada um e
permita que o usuário possa mostrar as
NOTAS de cada aluno individualmente'''

lista = []
while True:
    alunos = []
    notas = []
    alunos.clear()
    notas.clear()
    alunos.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos.append(notas)
    lista.append(alunos)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('\033[1:37m''-=''\033[m' * 30)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>9}')   # :<4, :<10 e :>8 são Códigos de alinhamento
print('\033[1:37m''-''\033[m' * 32)
for i, aluno in enumerate(lista):
    nota1 = lista[i][1][0]
    nota2 = lista[i][1][1]
    media = (nota1 + nota2) / 2
    print(f'{i:<3}  {lista[i][0]:<8}     {media:>5.1f}')
while True:
    print('\033[1:37m''-''\033[m' * 35)
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        print('FINALIZANDO...')
        break
    if n <= len(lista) - 1:
        print(f'Notas de {lista[n][0]} são {lista[n][1]}')
print('<<< VOLTE SEMPRE >>>')
