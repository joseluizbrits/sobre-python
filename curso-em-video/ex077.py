# Contando vogais em Tupla
'''Crie um progama que tenha uma TUPLA com VÁRIAS
PALAVRAS (não usar acentos). Depois disso, você
deve mostrar, para cada palavra, quais são as sua vogais'''

lista = ('aprender', 'programar', 'linguagem', 'python',
            'praticar', 'planejar', 'desenvolver', 'fazer',
            'projeto', 'software', 'aplicativo', 'startup')
for palavra in lista:
    print(f'\nNa palavra {palavra.upper()} temos ', end='') # o comando .upper() joga a
                                                            # string para maiúsculas
    for letra in palavra:
        if letra.lower() in 'aeiou': # o comando .lower() joga string para minúsculas
            print(f'\033[1:34m{letra}\033[m', end=' ')
