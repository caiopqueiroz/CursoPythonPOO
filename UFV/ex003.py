# Faça um programa que calcule a média aritmética de 5 números fornecidos pelo usuário. Mostre o resultado na tela.


print('Calculadora de Média Aritmética')
numeros = list()
for contador in range(0, 5):
    numeros.append(float(input(f'Digite o {contador + 1}º número: ')))
print(f'A média aritmética desses 5 números é igual a {sum(numeros) / 5}')