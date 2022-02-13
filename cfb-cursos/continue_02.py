while True:
    n = int(input('Digite um número qualquer: '))
    print(f'Você digitou o número {n}')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
