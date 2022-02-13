# Analisando e gerando Dicionários
'''Faça um programa que tenha uma FUNÇÃO
notas() que pode receber várias notas de alunos e
vai retornar um DICIONÁRIO com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)'''

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dic = {}
    cont = soma = maior = menor = 0
    for pos, num in enumerate(n):
        if pos == 0:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        cont += 1
        soma += num
    dic['total'] = cont
    dic['maior'] = maior
    dic['menor'] = menor
    dic['media'] = soma / cont
    if sit:
        if dic['media'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['media'] < 5:
            dic['situação'] = 'RUIM'
        else:
            dic['situação'] = 'RAZOÁVEL'
    return f'\033[1m'f'{dic}'


# Programa Principal
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
