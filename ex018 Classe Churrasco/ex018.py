class Churrasco:
    # Atributos de Classe (Devem ser indicados por 'Nome da classe.Nome do atributo')
    consumopadrao:float = 0.4
    preçokg:float = 82.40 
    # Forma de indicar que o valor recebido será do tipo float   
    
    
    def __init__(self, nome, convidados=0):
        # Atributos de Instância (Devem ser indicados por 'self.Nome do atributo')
        self.nome = nome
        self.convidados = convidados

    
    def __str__(self):
        return f'Esse é o {self.nome} com {self.convidados} pessoas participando'


    def quantidadecarne(self) -> float:
        return Churrasco.consumopadrao * self.convidados
        # Uso de funções próprias dentro da classe deve ser indicado por 'self.Nome da Função()'


    def analisar(self):
        from rich import print
        from rich.panel import Panel
        
        
        conteudo = f'Analisando [blue]{self.nome}[/] com [purple]{self.convidados} convidados[/]\n'
        conteudo += f'Cada amigão comerá 0.4 kg de carne - preço do kg - R$82,40\n'
        conteudo += f'Recomendo comprar [yellow bold]{self.quantidadecarne():.2f} kg[/]\n'
        conteudo += f'O custo total será [yellow bold]R${self.consumopadrao * self.convidados * self.preçokg:.2f}[/]\n'.replace('.', ',')
        conteudo += f'Valor total para cada um: [green bold]R${(self.consumopadrao * self.convidados * self.preçokg) / self.convidados:.2f}[/]'.replace('.', ',')
        return print(Panel(conteudo, title=f'{self.nome}', width=70))
    

churrasco1 = Churrasco('Churrasco dos Amigões', 15)
churrasco2 = Churrasco('Meninas Super Poderosas', 3)
churrasco1.analisar()
churrasco2.analisar()