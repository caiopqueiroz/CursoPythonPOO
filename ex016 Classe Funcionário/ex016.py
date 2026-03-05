from rich import print
from rich import inspect


class Funcionario:
    # Atributos de classe
    empresa = 'Acess Info'

    
    def __init__(self, nome, setor, cargo):
        # Atributos de instância 
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    
    def apresentaçao(self) -> str:
        print(f':handshake: Bom dia! Meu nome é [green bold]{self.nome}[/], trabalho no setor {self.setor} e meu cargo é {self.cargo}. Sou parte do time [bold blue]{Funcionario.empresa}!')
    

pessoa1 = Funcionario('Caio', 'Vendas', 'Atendente')
pessoa2 = Funcionario('Júlia', 'Atendimento', 'Faz-Tudo')
pessoa3 = Funcionario('Carla', 'Ensino', 'Professora')
pessoa1.apresentaçao()
print()
pessoa2.apresentaçao()
print()
pessoa3.apresentaçao()
# inspect(pessoa1)