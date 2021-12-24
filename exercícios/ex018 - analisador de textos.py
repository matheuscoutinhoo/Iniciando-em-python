'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = input('Digite seu nome completo: ').strip()
print('Seu nome com letras maiúsculas é {} e com letras minúsculas é {}'.format(nome.upper(), nome.lower()))
print('Seu nome possui, ao todo e sem espaços, {} letras'.format(len(nome) - nome.count(' ')))
#print('O primeiro nome possui {} letras'.format(nome.find(' '))) - conta qnts letras tem até o primeiro espaço.
nome1 = nome.split()
print('Seu nome inicial possui {} letras.'.format(len(nome1[0])))