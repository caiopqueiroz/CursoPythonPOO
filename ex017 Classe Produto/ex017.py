class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço


    def __str__(self):
        return f'{self.nome} custa R${self.preço:_.2f}'


    def etiquetar(self):
        from rich import print
        from rich.panel import Panel
        

        # A função '.center()' pode receber a quantidade de caracteres em que se deve centralizar um texto e também pode receber um caractere para ficar na frente e após o conteúdo, como um hífen. Por exemplo: 'Caio'.center(20, '_') vai retornar ________Caio________
        
        
        conteudo = f'[bold blue]{self.nome.center(30, ' ')}[/]'
        conteudo += f'{'-' * 30}'
        preçoformatado = f'[bold blue]R${self.preço:_.2f}[/]'.replace('.', ',').replace('_', '.')
        conteudo += f'{preçoformatado.center(44, '-')}'
        return print(Panel(conteudo, title='[bold purple]Produto', width=34))
    

produto1 = Produto('Garrafa de Água', 39.90)
produto2 = Produto('Nintendo 3ds', 1299.90)
produto3 = Produto('iPhone 17 Pro Max', 25000)
produto1.etiquetar()
produto2.etiquetar()
produto3.etiquetar()

