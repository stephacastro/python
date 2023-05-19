# matendo estado dentro da classe

class Camera:
    
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando == True:
            print(f'{self.nome} Já esta filmando...')
            return
        
        print(f'{self.nome} está filmando...')

    def parar_filmar(self):
        if not self.filmando == True:
            print(f'{self.nome} Não esta filmando...')
            return
        
        print(f'{self.nome} está parando de filmando...')

    def fotografar(self):
        if self.filmando == True:
            print(f'{self.nome} não pode fotografar filmando...')
            return
        
        print(f'{self.nome} está fotografando...')


c1 = Camera('Canon')
c2  = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()


c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()