n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 6.0:
    sit = 'Parabéns, você está aprovado!'
else:
    sit = 'Infelizmente você está reprovado!'
print('A sua média é {:.1f}\n{}'.format(m, sit))
