resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número qualquer: '))
    print(f'Você digitou o número {n}')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
