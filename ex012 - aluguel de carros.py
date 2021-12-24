'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
 pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

kms = float(input('Quantidade de kms pecorridos: '))
dias = int(input('Quantidade de dias de locação: '))
preco = (dias*60) + (kms * 0.15)
print('O valor do aluguel do carro será de R$ {:.2f}.'.format(preco))
