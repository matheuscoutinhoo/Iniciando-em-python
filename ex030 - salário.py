'''Faça um programa que leia o salário de um funcionário e calcule o valor do seu aumento.
- Para salários superiores a R$1250.00, calcule um aumento de 10%.
- Para salários inferios ou iguais a R$ 1250.00, o aumento será de 15%'''

s = float(input('Insira o salário do funcionário: '))
if s > 1250:
    print('O aumento será de 10%, PORTANTO R$ {:.2f}'.format(s*0.10))
    print('Seu salário agora será R$ {:.2f}'.format(s+(s*0.10)))
else: 
    print('O aumento será de 15%, PORTANTO R$ {:.2f}'.format(s*0.15))
    print('Seu slário agora é de R$ {:.2f}'.format(s+(s*0.15)))