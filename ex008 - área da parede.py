'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a
sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de
tinta pinta uma área de 2m². '''

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
if(l == a):
    area = l**2
else: 
   area = l*a
tinta = area/2
print('A quantidade de tinta necessária para pintar {} m² de parede é de {} litros'.format(area, tinta))



