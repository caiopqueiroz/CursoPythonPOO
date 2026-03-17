from rich.panel import Panel
from rich import print
import os


espaco = '👾'
contador = 0
print(Panel(espaco, title='Espaço', width=20))
comando = input('(1 ou 2) : ')
while True:
    if comando == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
        contador += 1
        espaco = ''
        espaco += (' '*contador + '👾')
        print(Panel(espaco, title='Espaço', width=20))
        comando = input('(1 ou 2) : ')
    if comando == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
        if contador > 0:
            contador -= 1
        espaco = (' '*(contador) + '👾')
        print(Panel(espaco, title='Espaço', width=20))
        comando = input('(1 ou 2) : ')
        