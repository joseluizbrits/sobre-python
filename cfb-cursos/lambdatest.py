# Cálculo de Hipotenusa

print('-' * 30)
print('\033[1m'f'{"CALCULO DE HIPOTENUSA":^30}''\033[m')
print('-' * 30)
cat1 = int(input('Cateto maior: '))
cat2 = int(input('Cateto menor: '))
hip = lambda a, b: (a ** 2 + b ** 2) ** (1 / 2)
res = hip(cat1, cat2)
print('-' * 30)
print(f'A hipotenusa entre os catetos {cat1} e {cat2} é {res:.2f}')
