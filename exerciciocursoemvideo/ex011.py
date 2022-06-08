print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de '
      'tinta necessária para pintá-la,\nsabendo que cada litro de tinta, pinta uma área de 2m²')
l = float(input('Informe a largura em metros:'))
a = float(input('Informe a altura em metros:'))
a2 = l * a  # área da parade
t = a2 / 2  # tinta gasta por m²
print(f'Sua parede tem {a2}m², e para pintar ela você irá gastar {t} litros de tinta')
