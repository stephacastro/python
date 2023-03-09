
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

class Playlist:
    def __init__(self, nome, programa):
       self.nome = nome
       self._programa = programa

    def __getitem__(self, item):
        return self._programa[item]

    @property
    def listagem(self):
        return self._programa
    
    @property
    def tamanho(self):
        return len(self._programa)

shazan = Filme('shazan 2', 2023, 160)
greys = Serie('grays anatomy', 2004, 19)
elite = Serie('Elite', 2018, 4)
vingadores = Filme('vingadores - guerra infinita', 2018, 160)

shazan.dar_like()
greys.dar_like()
greys.dar_like()
elite.dar_like()
vingadores.dar_like()
elite.dar_like()

filmes_series = [shazan, greys, elite, vingadores]

playlist_fds = Playlist('Fim de semana', filmes_series)

print(f'Tamanho do playlist: {len(playlist_fds.listagem)}')

for programa in playlist_fds:
    print(programa)

