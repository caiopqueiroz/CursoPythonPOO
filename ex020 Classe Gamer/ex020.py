class Gamer:
    def __init__(self, nome, nick, *jogosFavoritos):
        self.nome = nome
        self.nick = nick
        self.favoritos = list(jogosFavoritos)

    
    def ficha(self):
        from rich import print
        from rich.panel import Panel


        return print(Panel(f'Nome: {self.nome}\nNick: {self.nick}', title='!Ficha Gamer!'))


gamer1 = Gamer('Caio', 'ciainutricao', 'Pokemon', 'Mario', 'Minecraft')
gamer1.ficha()