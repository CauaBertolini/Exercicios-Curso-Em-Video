#Crie um código em Python que teste se o site Pudim está
#acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URÇError:
    print('O site Pudim não está acessível no momento!')
else:
    print('Acessei o site Pudim com sucesso!')
    print(site.read())