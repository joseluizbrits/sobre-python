# Dissecando uma Variável
'''Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas
as informações possíveis sobre ela'''

a = input('Digite algo: ')
print('\033[1;30m''O tipo primitivo deste valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabeto?', a.isalpha())
print('É alfanumério?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Éstá em minúsculas?', a.islower())
print('Éstá capitalizada?', a.istitle())
