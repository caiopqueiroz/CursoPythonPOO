from math import sqrt


a = float(input('Valor a: '))
b = float(input('Valor b: '))
c = float(input('Valor c: '))
delta = (b**2) - (4 * a * c)
if delta > 0:
    resultado = list()
    resultado.append((-b + sqrt(delta)) / (2 * a))
    resultado.append((-b - sqrt(delta)) / (2 * a))
elif delta == 0: 
    resultado = -b / (2 * a) 
else:
    resultado = 'Impossível calcular'
print(f'O resultado é {resultado}')