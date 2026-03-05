class Livro:
    def __init__(self, titulo, paginas):
        from rich import print
        
        
        self.titulo = titulo
        self.paginas = paginas
        print(f'Você iniciou o livro "{self.titulo}"! Ele possui {self.paginas} páginas. Você está agora na página 1. [blue bold]Boa leitura![/]')
        self.atual = 1


    def passarPaginas(self, avanço):
        from rich import print
        
        
        if self.atual + avanço > self.paginas:
            print(f'[red bold]Não é possível avançar essa quantidade[/]. O livro só possui {self.paginas} páginas. Avançando até o final.')
            avanço = self.paginas - self.atual
        print(F'Avançando {avanço} páginas! ', end='')
        for contador in range(0, avanço):
            print(f'Pág {self.atual + 1} -> ', end='')
            self.atual += 1
        print(f'Agora está na página {self.atual}')
        print()
        if self.atual == self.paginas:
            print('[green bold]Parabéns! Você chegou ao fim do livro![/]')


livro1 = Livro('A Volta dos que Não Foram', 100)
livro1.passarPaginas(18)

