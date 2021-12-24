'''Faça um programa que leia um número inteiro e mostre na tela o seu
sucessor e seu antecesor.'''

num = int(input("Digite um número: "))
#s = num + 1
#a = num - 1 -> Possível fazer com variáveis a e s.
print('O sucessor de {} é {}\nO antecessor de {} é {}'.format(num, num + 1, num, num - 1))