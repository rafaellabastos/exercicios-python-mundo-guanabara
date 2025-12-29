import math

compCatetoOposto = float(input('Comprimento do cateto oposto: '))
compCatetoAdjascente = float(input('Comprimento do cateto adjascente: '))

somaCatetos = ((compCatetoOposto**2)+(compCatetoAdjascente**2))
compHipotenusa = math.sqrt(somaCatetos)

print(f'O comprimento da hipotenusa é {compHipotenusa}')