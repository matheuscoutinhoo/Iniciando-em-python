'''CRIE UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0.50 POR KM PARA VIAGENS DE ATÉ 200 KM
E R$0.45 PARA VIAGENS MAIS LONGAS'''

d = float(input('A distância da viagem é de: '))
if d <= 200:
    print('O preço da passagem é de R$ {:.2f}'.format(d*0.50))
else:
    print('O preço da passagem será de R$ {:.2f}'.format(d*0.45))