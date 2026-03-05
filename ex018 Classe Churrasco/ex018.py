class Churrasco:
    def __init__(self, nome, convidados=0):
        self.nome = nome
        self.convidados = convidados

    
    def analisar(self):
        from rich import print
        from rich.panel import Panel
        
        
        return print(Panel(f'Analisando [blue]{self.nome}[/] com [purple]{self.convidados} convidados[/]\nCada amigão comerá 0.4 kg de carne - preço do kg - R$82.40\nRecomendo comprar [yellow bold]{0.4 * self.convidados:.2f} kg[/] \nO custo total será [yellow bold]R${0.4 * self.convidados * 82.40:.2f}[/]\nValor total para cada um: [green bold]R${(0.4 * self.convidados * 82.40) / self.convidados:.2f}[/]', title=f'{self.nome}', width=70))
    

churrasco1 = Churrasco('Churrasco dos Amigões', 2)
churrasco1.analisar()
