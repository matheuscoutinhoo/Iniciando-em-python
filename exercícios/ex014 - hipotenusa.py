'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
    de um triângulo retângulo e exiba o comprimento da sua hipotenusa'''

# MÉTODO SIMPLES
'''ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
h = (ca**2 + co**2)**1/2
print('O valor da hipotenusa é {}'.format(h))'''

# MÉTODO COM IMPORT
from math import hypot
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
h = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}.'.format(h))
