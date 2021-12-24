'''CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SUA TABUADA'''

n = int(input('Digite um número qualquer: '))
n1 = int()
while (n1 < 10):
    n1 += 1
    print('{} x {} = {}'.format(n, n1, n*n1))