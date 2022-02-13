algo = input('Digite algo: ')
cor = {'preta': '\033[30m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'roxona': '\033[35m',
       'turquesa': '\033[36m',
       'cinza': '\033[37m',
       'limpar': '\033[m',}
print('Você digitou: {}{}'.format(cor['preta'], algo))
