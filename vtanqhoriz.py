#### Cálculo do volume de líquido em um tanque na horizontal, quando conhecemos
#### a altura molhada (nível do líquido). #####################################

#### Autor: José Menescal Neto  Data: 21/01/2023 ##############################

# Importação de funções da biblioteca math - Python
from math import pi, sin, acos

"""
Dados do tanque
Comprimento em metro -> variável = c
Raio do tanque em metro -> variável = r
Altura molhada em metro -> variável = hm
Volume total do tanque em litro
Volume para a altura molhada em litro -> variável = vm
"""

# Entrada dos dados do tanque cilíndrico, na posição horizontal
c = float(input('Digite o comprimento do tanque em (m): '))
r = float(input('Digite o raio do tanque em (m): '))
hm = float(input('Digite a altura molhada em (m): '))

# Saída -> Volume total em litro
print(f'O volume total do tanque é: {(pi * r ** 2) * c * 1000:.2f} l ')

# 1o. Caso -> Altura molhada <= ao raio
if hm <= r:
    # Área do setor circular
    beta = acos((r - hm) / r)
    alfa = 2 * beta
    a_set = ((r ** 2) * alfa) / 2  # a_set = (pi * r^2 * alfa) / 2pi -> a_set = r^2 * alfa / 2

    # Área dos triangulos sobre o setor circular
    a_tri = (r - hm) * (r * sin(beta)) # a_tri = 2 * [(r-hm)*(r*seno(beta)/2] -> a_tri=(r-hm)*(r*seno(beta))

    # volume molhado
    vm = c * (a_set - a_tri) * 1000
    print(f'Para a altura molhada {hm:.2f}m, o volume de líquido atualmente no tanque é: {vm:.2f} l')

# 2o. Caso -> Altura molhada r < hm <= 2r
elif r < hm <= 2 * r:
    # área so setor circular
    beta = acos((hm - r) / r)
    alfa = 2 * (pi - beta) # alfa = 2pi - 2*beta -> alfa = 2 * (pi - beta)
    a_set = (r ** 2) * alfa / 2  # a_set = (pi * r^2 * alfa) / 2pi -> a_set = r^2 * alfa / 2

    # Área dos triangulos sobre o setor circular
    a_tri = (hm - r) * (r * sin(beta)) # a_tri = 2 * [(r-hm)*(r*seno(beta)/2] -> a_tri=(r-hm)*(r*seno(beta))
    vm = c * (a_set + a_tri) * 1000
    print(f'Para a altura molhada {hm:.2f}m, o volume de líquido atualmente no tanque é: {vm:.2f} l')
else:
    print(f'Dados inválidos: Altura molhada informada {hm:.2f}m, é maior que o diametro do tanque.')
