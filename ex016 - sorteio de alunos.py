'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça 
um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random
nome1 = input('Insira o nome do primeiro aluno: ')
nome2 = input('Insira o nome do segundo aluno: ')
nome3 = input('Insira o nome do terceiro aluno: ')
nome4 = input('Insira o nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
sort = random.choice(lista)
print('O aluno escolhido é {}.'.format(sort))