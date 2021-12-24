''' Faça um programa que leia o nome completo de uma pessoa, mostrando
 em seguida o primeiro e o último nome separadamente.'''

nome = str(input('Digite seu nome completo: ')).split()
print('O primeiro nome é {}'.format(nome[0]))
print('O último nome é {}'.format(nome.pop()))
