'''Faça um programa que leia um número real qualquer e exiba sua parte inteira.'''

# USANDO O MÉTODO COM IMPORT

import math
num = float(input('Digite um número real: '))
print('A parte inteira de {} é {}'.format(num, math.trunc(num)))

# USANDO O MÉTODO COM INT

'''num = float(input('Digite um número real qualquer: '))
print('A parte inteira de {} é {}.'.format(num, int(num)))'''