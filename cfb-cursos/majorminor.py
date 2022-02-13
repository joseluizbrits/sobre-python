numeros = []
maior = 0
menor = 0
for n in range(0, 5):
    numeros.append(int(input(f'Digite um número: ')))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
