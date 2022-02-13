# Sistema interativo de ajuda em Python
'''Faça um MINI-SISTEMA que utilize o Interactive
Help do Python. O usuário vai digitar o COMANDO e
o MANUAL vai aparecer. Quando o usuário digitar a
palavra 'FIM', o programa se ENCERRARÁ
OBS: Use CORES'''

def mensagem(txt):
    print('\033[43m''~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))


def interactiveHelp(opc):
    print('\033[47m''~' * (len(opc) + 34))
    print(f"  Acessando manual do comando '{opc}'")
    print('~' * (len(opc) + 34))
    return f'{help(opc)}'


while True:
    mensagem('SISTEMA DE AJUDA PyHELP')
    opcao = str(input('\033[m''Função ou Biblioteca > ')).strip().lower()
    if opcao in 'fim':
        mensagem('ATÉ LOGO!')
        break
    manual = interactiveHelp(opcao)
