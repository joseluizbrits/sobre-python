# Lista ordenada sem repetições
'''Crie um programa onde o usuário possa digitar
cinco VALORES NUMÉRICOS e cadastre-os em uma LISTA,
JÁ NA POSIÇÃO CORRETA de inserção (sem usar o sort()).
No final, mostre a LISTA ORDENADA na tela'''

valores = []
for v in range(0, 5):
    n = int(input('Digite um valor: '))
    if v == 0 or n > valores[-1]:   # valores[-1] é o último valor da lista
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('\033[1:34m''-=''\033[m' * 30)
print(f'Os valores digitados em ordem foram {valores}')
