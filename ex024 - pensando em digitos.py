'''ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSAR EM UM NÚMERO INTEIRO
ENTRE 0 E 5 E PEÇA PARA UM USUÁRIO DESCOBRIR QUAL FOI ESSE NÚMERO.
O PROGRAMA DEVE ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.'''

from random import randint
from time import sleep
num = randint(0, 5)
chute = int(input('Escolha um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
print('O número sorteado foi {} e o número escolhido foi {}'.format(num, chute))
if chute == num:
    print('VOCÊ VENCEU!')
else:
    print('VOCÊ PERDEU!')
