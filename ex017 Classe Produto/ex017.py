class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = f'R${preço}'


    def etiquetar(self):
        from rich import print
        from rich.panel import Panel
        return print(Panel(f'{self.nome.center(45)}\n{'-' * 46}\n{self.preço.center(45)}', title='Produto', width=50))
    

produto1 = Produto('Garrafa de Água', '39.90')
produto1.etiquetar()
produto2 = Produto('Nintendo 3ds', '1299.90')
produto2.etiquetar()