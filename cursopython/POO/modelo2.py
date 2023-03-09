
class Programa: 
    def __init__(self, nome, ano):
        self._nome = nome.title() 
        self.ano = ano
        self._likes = 0

    @property 
    def likes(self):
        return self._likes
    
    def dar_like(self):
        self._likes += 1
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    def __str__(self):
        return f'{self._nome} / {self.ano} / {self._likes} likes'


class Filme(Programa): # herdando atributos da classe programa
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # super acessa atributos da classe mae
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} / {self.ano} / {self.duracao} min / {self._likes} likes'
        

class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'{self._nome} / {self.ano} / {self.temporada} temporadas / {self._likes} likes'
       

shazan = Filme('shazan 2', 2023, 160)
shazan.dar_like()
greys = Serie('grays anatomy', 2004, 19)
greys.dar_like()
greys.dar_like()
elite = Serie('Elite', 2018, 4)
elite.dar_like()
filmes_series = [shazan, greys, elite]

for programa in filmes_series:
    print(programa)