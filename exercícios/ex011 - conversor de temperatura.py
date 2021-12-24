'''FAÇA UM PROGRAMA QUE LEIA UMA TEMPERATURA EM ºC E COONVERTA PARA FARENHEIT E KELVIN'''

c = int(input('Insira uma temperatura em ºC: '))
k = c + 273.0
f = (1.8*c) + 32
print('A temperatura em ºC é {}, em Farenheit é {} e em Kelvin é {}.'.format(c, f, k))
