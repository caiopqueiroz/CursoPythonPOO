class controleRemoto:
    def __init__(self):
        self.ligado = False
        self.canal = 1
        self.volume = 2
    

    def tv(self):
        from rich import print
        from rich.panel import Panel
        import os


        os.system('cls' if os.name == 'nt' else 'clear')
        if self.ligado:
            if self.canal == 1:
                print(Panel('Canais: [bold on yellow] 1 [/] 2  3  4  5\nVolume: [on white]     [/]', title='Tv', width=30))
            if self.canal == 2:
                print(Panel('Canais:  1 [bold on yellow] 2 [/] 3  4  5\nVolume: [on white]     [/]', title='Tv', width=30))
            if self.canal == 3:
                print(Panel('Canais:  1  2 [bold on yellow] 3 [/] 4  5\nVolume: [on white]     [/]', title='Tv', width=30))   
            if self.canal == 4:
                print(Panel('Canais:  1  2  3 [bold on yellow] 4 [/] 5\nVolume: [on white]     [/]', title='Tv', width=30))
            if self.canal == 5:
                print(Panel('Canais:  1  2  3  4 [bold on yellow] 5 [/]\nVolume: [on white]     [/]', title='Tv', width=30)) 
        else:
            print(Panel('Tv Desligada', title='Tv', width=30))
        self.apertarBotao()

    
    def ligarDesligar(self):
        if self.ligado:
            self.ligado = False
        else:
            self.ligado = True
        self.tv()


    def apertarBotao(self):
        comando = input(f'< CH{self.canal} >  - VOL{self.volume} + ')
        if comando == '@':
            self.ligarDesligar()
        if comando == '>':
            self.canalDireito()
        if comando == '<':
            self.canalEsquerdo()
        if comando == '+':
            self.aumentarVolume()
        if comando == '-':
            self.abaixarVolume()


    def canalDireito(self):
        if self.canal == 5:
            self.canal = 1
        else:
            self.canal += 1
        self.tv()

        
    def canalEsquerdo(self):
        if self.canal == 1:
            self.canal = 5
        else:
            self.canal -= 1
        self.tv()


    #def aumentarVolume(self):


    #def abaixarVolume(self):

controle1 = controleRemoto()
controle1.tv()