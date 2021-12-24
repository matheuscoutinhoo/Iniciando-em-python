'''CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR.'''

num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número {} é um número par'.format(num))
else:
    print('O número {} é um número ímpar'.format(num))