from Modulos import menu
from Modulos import lerArquivoJS
from Modulos import editarArquivoJS
from Modulos import lerArquivoPY
from Modulos import editarArquivoPY
from time import sleep


while True:
    resposta = menu(['Ver Comandos Python', 'Ver Comandos JavaScript', 'Cadastrar Novo Comando Python', 'Cadastrar Novo Comando JavaScript', 'Encerrar o Programa'])
    if resposta == 0:
        lerArquivoPY()
    if resposta == 2:
        editarArquivoPY()
    if resposta == 1:
        lerArquivoJS()
    if resposta == 3:
        editarArquivoJS()
    if resposta == 4:
        break
    print()
    sleep(1)