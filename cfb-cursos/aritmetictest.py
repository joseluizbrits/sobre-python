n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
dr = n1 % n2
e = n1 ** n2
# Dentro das chaves da divisão tem o termo :.2f que significa formatar o resultado para duas casas decimais;
# No meio da linha há o termo \n que é para quebrar a linha;
# No fim da linha há o termo end=', ' que é para não quebrar a linha.
print(' A soma é {}, o produto é {}; \n a divisão é {:.2f}'.format(s, m, d), end=', ')
print('a divisão inteira é {}, o resto da divisão é {} e a potência é {}'.format(di, dr, e))
