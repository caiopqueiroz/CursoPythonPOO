from rich import print
from rich.panel import Panel


#Estrutura de criação e leitura de arquivo de texto:
    #nomeArquivo = 'JavaScript.txt'
    #arquivo = open(nomeArquivo, 'at')
    #arquivo.write('Teste\n')
    #arquivo = open(nomeArquivo, 'rt')
    #for linha in arquivo:
    #    print(linha)


def menu(listaOpcoes):
    print(Panel('Opções:', width=30))
    for contador, opcao in enumerate(listaOpcoes):
        print(f'[ {contador} ]  {opcao}')
    print()
    resposta = int(input('Opção Escolhida: '))
    print()
    return resposta


def lerArquivoJS():
    nomeArquivo = 'JavaScript.txt'
    arquivo = open(nomeArquivo, 'at')
    arquivo = open(nomeArquivo, 'rt')
    print(Panel('Comandos JavaScript:', width=30))
    for linha in arquivo:
        dadosJS = linha.split(';')
        print(f'{dadosJS[0]:<70}{dadosJS[1]:<150}')


def editarArquivoJS():
    nomeArquivo = 'JavaScript.txt'
    arquivo = open(nomeArquivo, 'at')
    comando = input('Digite aqui o comando: ')
    print()
    explicaçao = input('O que esse comando faz? ')
    arquivo.write(f'{comando};{explicaçao}\n')
    print(Panel('[green bold]Comando Cadastrado com Sucesso![/]', width=30))


def lerArquivoPY():
    nomeArquivo = 'Python.txt'
    arquivo = open(nomeArquivo, 'at')
    arquivo = open(nomeArquivo, 'rt')
    print(Panel('Comandos Python:', width=30))
    for linha in arquivo:
        dadosPY = linha.split(';')
        print(f'{dadosPY[0]:<70}{dadosPY[1]:<150}')


def editarArquivoPY():
    nomeArquivo = 'Python.txt'
    arquivo = open(nomeArquivo, 'at')
    comando = input('Digite aqui o comando: ')
    print()
    explicaçao = input('O que esse comando faz? ')
    arquivo.write(f'{comando};{explicaçao}\n')
    print(Panel('[green bold]Comando Cadastrado com Sucesso![/]', width=30))