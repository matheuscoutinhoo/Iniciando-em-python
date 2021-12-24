'''FAÇA UM PROGRAMA QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE O VALOR COM 15% DE AUMENTO'''

salario = float(input('Insira o valor do seu salário mensal: '))
print('Seu salário atual é de R$ {}'.format(salario))
aumento = salario + (salario*0.15)
print('Seu salário, com 15% de aumento, é de R$ {}'.format(aumento))