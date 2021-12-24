'''ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80KM/H
MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.'''
#OBS: A MULTA VAI CUSTAR R$ 7.00 PARA CADA KM ACIMA DO LIMITE

v = float(input('Qual a velocidade do carro em km/h? '))
print('A velocidade do carro é de {} km/h'.format(v))
if v > 80:
    print('Você será multado em R$ {:.2F}'.format((v-80)*7))
else:
    print('Pode passar!')