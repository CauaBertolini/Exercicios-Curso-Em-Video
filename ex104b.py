#Crie um programa que tenha a função leiaInt(). que vai funcionar de forma semelhante à função input() do Python,
#só que fazendo a validação para aceitar apenas um valor numérico.

#Ex:
#n=leiaInt('Digite um n')
def LeiaInt(msg='Digite um número: '):
    ok = False
    valor = 0
    while True:
        n = str(input(f'{msg}'))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


n = LeiaInt('Digite um Número: ')
print(f'Você acabou de digitar o número {n}')
