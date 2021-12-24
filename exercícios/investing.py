inv = float(input('Quanto você quer investir: '))
taxa = float(input('Qual a taxa de rendimento anual esperada: '))
tempo = int(input('Por quantos anos você quer investir: '))
rentabilidade = inv * (1 + taxa) ** tempo
juros = rentabilidade - inv
print('Investindo R$ {:.2f}, você terá como rentabilidade R$ {:.2f}\nOs juros foram de R$ {:.2f}'.format(inv, rentabilidade, juros))