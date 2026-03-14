class Livro:
    def __init__(self, titulo, paginas):
        from rich import print
        
        
        self.titulo = titulo
        self.paginas = paginas
        print(f':open_book: Você iniciou o livro "{self.titulo}"! Ele possui {self.paginas} páginas. Você está agora na página 1. [blue bold]Boa leitura![/]')
        self.atual = 1


    def passarPaginas(self, avanço=1):
        from rich import print
        from time import sleep
        
        
        if self.atual + avanço > self.paginas:
            print(f'[red bold]Não é possível avançar essa quantidade[/]. O livro só possui {self.paginas} páginas. Avançando até o final.')
            avanço = self.paginas - self.atual
        print(f'Avançando {avanço} páginas! ', end='')
        for contador in range(0, avanço, 1): # Significa: Começando do 0, conte até o número igual ao avanço, com o passo 1
            self.atual += 1
            sleep(0.3)
            print(f'Pág {self.atual} ➤  ', end='')
        print(f'Agora está na página {self.atual}')
        print()
        if self.atual == self.paginas:
            print('[green bold]:closed_book: Parabéns! Você chegou ao fim do livro![/]')


livro1 = Livro('10 Coisas que Aprendi', 20)
livro1.passarPaginas(5)
livro1.passarPaginas(10)
livro1.passarPaginas(50)
livro1.passarPaginas(5)




