'''FAÇA UM PROGRAMA QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM UM DESCONTO DE 5%.'''

preco = float(input('Insira o preço do produto: '))
print('O valor do produto é de R$ {}.'.format(preco))
desconto = preco - (preco*0.75)
print('O valor do produto, com 75 por cento de desconto, é de R$ {:.2f}.'.format(desconto))
