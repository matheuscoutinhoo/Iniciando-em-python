'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import radians, sin, cos, tan
an = float(input('Digite um ângulo qualquer: '))
s = sin(radians(an))
c = cos(radians(an))
t = tan(radians(an))
print('O seno de {:.2f} é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}.'.format(an, s, c, t))