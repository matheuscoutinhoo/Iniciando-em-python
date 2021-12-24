'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece
 a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece inicialmente em {}'.format(frase.find('A')))
print('A letra "A" aparece por último em {}'.format(frase.rfind('A')))
