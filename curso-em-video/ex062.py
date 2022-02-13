# Super Progressão Aritmética v3.0
'''Melhore o DESAFIO 061, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 TERMOS'''

print('\033[1m''-=' * 10)
print('\033[1:35m''Gerador de PA''\033[m')
print('\033[1m''-=' * 10)
n = int(input('\033[m''Primeiro termo: '))
r = int(input('Razão: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[1:35m''{}''\033[m ➔ '.format(termo), end='')
        termo += r
        cont += 1
    print('\033[1:37m''PAUSA''\033[m')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com \033[1:35m''{}''\033[m termos mostrados.'.format(total))
