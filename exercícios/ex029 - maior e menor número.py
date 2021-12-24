'''Crie um programa que leia três números e mostre qual é o maior e qual é o menor.'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
print('O maior número é {}'.format(max(num1, num2, num3)))
print('O menor número é {}'.format(min(num1, num2, num3)))