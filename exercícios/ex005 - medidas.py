'''CRIE UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO
EM CENTÍMETROS E MILÍMETROS.'''

m1 = float(input('Digite um valor em metros: '))
cm = m1 * 100
mm = m1 * 1000
print('{} metros equivalem a {} centímetros e {} milímetros.'.format(m1, cm, mm))