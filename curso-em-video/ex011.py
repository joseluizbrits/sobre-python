# Pintando Parede
'''Faça um programa que leia a largura e a
altura de uma parede em metros, calcule a sua
área e a quantidade de tinta necessária para pinta-lá,
sabendo que cada litro de tinta pinta uma área de 2m²'''

x = float(input('Digite a largura da parede em metros: '))
y = float(input('Digite a altura da parede em metros: '))
s = x * y
r = s % 2
t = s // 2
if r > 0:
    t = t + 1
print('A área da parede é \033[1m{:.2f} m²\033[m e você precisará de'.format(s), end=' ')
print('\033[7;40m''{:.0f} latas\033[m de tinta para pintá-la.'.format(t))
