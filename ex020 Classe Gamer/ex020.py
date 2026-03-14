class Gamer:
    def __init__(self, nome, nick, *jogosFavoritos):
        self.nome = nome
        self.nick = nick
        self.favoritos = list(jogosFavoritos)

    
    def ficha(self):
        from rich import print
        from rich.panel import Panel

        conteudo = f'[bold blue]Nome: {self.nome}\n'
        conteudo += f'[bold green]Jogos favoritos:[/]\n'
        for jogo in self.favoritos:
            conteudo += f' 👾  {jogo}\n'
        print(Panel(conteudo, title=f'[bold purple]{self.nick} 🎮', width=35))


gamer1 = Gamer('Caio Queiroz', 'ciainutricao', 'Pokémon', 'Mario', 'Minecraft', 'Digimon', 'Chrono Trigger')
gamer2 = Gamer('Júlia Mansur 😘', 'jujulinda13', 'Clash of the Titans', 'Scooby-Doo! First Frights', 'Yu-Gi-Oh!', 'Munchkin', 'Minecraft')
gamer1.ficha()
gamer2.ficha()
