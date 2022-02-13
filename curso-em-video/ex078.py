# Maior e Menor valores na Lista
'''Faça um programa que leia 5 VALORES NUMÉRICOS
e guarde-os em uma lista. No final, mostre qual
foi o MAIOR e o MENOR valor digitado e as suas
respectivas POSIÇÕES na lista'''

valores = []
maior = 0
menor = 0
for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {pos}: ')))
    if pos == 0:
        maior = menor = valores[pos]
    else:
        if valores[pos] > maior:
            maior = valores[pos]
        if valores[pos] < menor:
            menor = valores[pos]
print('\033[1:34m''=-''\033[m' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == maior:
        print(f'{posicao}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == menor:
        print(f'{posicao}... ', end='')
print()
