# Um print especial
'''Faça um programa que tenha uma FUNÇÃO
chamada escreva(), que receba um texto qualquer
como PARÂMETRO e mostre uma mensagem com tamanho adaptável
Ex: escreva(Olá, Mundo!)
SAÍDA:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~'''

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('José Luiz Brits')
escreva('\033[1:35m''Parangaricutirimirruaro''\033[m')
escreva('Ok')
