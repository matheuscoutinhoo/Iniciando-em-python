''' CRIE UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU
TIPO PRIMITIVO, E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE.'''

v = input('Digite algo: ')
print(type(v))
print('É alfabético? ' , v.isalpha())
print('É numérico? ', v.isnumeric())
print('É alfanumérico? ', v.isalnum())
print('Está em letras maiúsculas? ', v.isupper())
print('Está em letras minúsculas', v.islower())
print('Possui espaços? ', v.isspace())
print('Está capitalizado? ', v.istittle())
