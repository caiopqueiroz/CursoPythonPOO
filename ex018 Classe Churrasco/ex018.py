class Churrasco:
    # Atributos de Classe
    consumopadrao = 0.4
    preçokg = 82.40    
    
    
    def __init__(self, nome, convidados=0):
        # Atributos de Instância
        self.nome = nome
        self.convidados = convidados

    
    def __str__(self):
        return f'Esse é o {self.nome} com {self.convidados} pessoas participando'


    def analisar(self):
        from rich import print
        from rich.panel import Panel
        
        
        conteudo = f'Analisando [blue]{self.nome}[/] com [purple]{self.convidados} convidados[/]\n'
        conteudo += f'Cada amigão comerá 0.4 kg de carne - preço do kg - R$82.40\n'
        conteudo += f'Recomendo comprar [yellow bold]{self.consumopadrao * self.convidados:.2f} kg[/]\n'
        conteudo += f'O custo total será [yellow bold]R${self.consumopadrao * self.convidados * self.preçokg:.2f}[/]\n'
        conteudo += f'Valor total para cada um: [green bold]R${(self.consumopadrao * self.convidados * self.preçokg) / self.convidados:.2f}[/]'
        return print(Panel(conteudo, title=f'{self.nome}', width=70))
    

churrasco1 = Churrasco('Churrasco dos Amigões', 15)
print(churrasco1)
churrasco1.analisar()
