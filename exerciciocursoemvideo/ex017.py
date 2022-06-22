# fazendo sem biblioteca porque não consegui entender usando uma
# calcula a hipotenusa
ca = float(input('Digite o cateto adjacente:'))
co = float(input('Digite o cateto oposto:'))
hp = (ca**2 +co**2)**(1/2)
print(f'A hipotenusa é:{hp:.2f}')

import math
hi = math.hypot(co, ca)
print(f'A hipotenusa é:{hi:.2f}')