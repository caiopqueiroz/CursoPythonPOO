# Graus celsius = (Farenheit - 32) / 1.8
# Faça um programa para converter uma temperatura em graus Fahrenheit para graus Celsius. A temperatura em Fahrenheit é fornecida pelo usuário e a temperatura em Celsius deve ser exibida na tela. Faz parte do exercício pesquisar pela fórmula de conversão.


print('Conversor de °F para °C')
print('-'*50)
valor = int(input('Valor em °F: '))
c = (valor - 32) / 1.8 
print(f'{valor}°F equivalem à {c}°C')