while True:
    n = int(input('Digite um número entre zero e 10: '))
    if 0 <= n <= 10:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {n}')
