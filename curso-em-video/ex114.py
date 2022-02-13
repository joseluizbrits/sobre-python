# Site está acessível?
'''Crie um código em Python que teste se o site
pudim.com.br está acessível pelo computador usado'''

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31m''O site Pudim não está acessível no momento')
else:
    print('\033[32m''Consegui acessar o site Pudim com sucesso!')
