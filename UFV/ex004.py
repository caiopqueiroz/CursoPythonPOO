# Elabore um programa que realize o cálculo dos juros para o pagamento de uma conta em atraso. Para isso, solicite ao usuário para fornecer o valor inicial da conta e o percentual de juros. Você deve calcular e mostrar na tela: os juros calculados e o valor total a ser pago.


print('Calculadora de juros')
valor = float(input('Valor da conta: '))
juros = int(input('Porcentagem de juros: '))
acrescimo = valor * (juros / 100)
final = valor + acrescimo
print(f'O total de juros que devem ser pagos é R${acrescimo:.2f}. O valor final é R${final:.2f}')