# Validando expressões matemáticas
'''Crie um programa onde o usuário digite
uma EXPRESSÃO qualquer que use PARÊNTESES.
Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados
na ORDEM CORRETA'''

expressao = str(input('Digite a expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\033[32m''Sua expressão está valida!')
else:
    print('\033[31m''Sua expressão está errada!')
