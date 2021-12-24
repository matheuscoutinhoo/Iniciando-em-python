'''CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE
QUANTOS DÓLARES ELA PODE COMPRAR'''

# OBS: 1 US$ = R$ 5,69

din = float(input('Quantos reais você tem?: '))
print('Você possui R$ {}'.format(din))
dol = din/5.69
print('Você pode comprar ', round(dol, 2), 'dólares!')