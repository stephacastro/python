
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


class Filme(Programa): # herdando atributos da classe programa
    
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title() 
        self.ano = ano
        self.duracao = duracao
        self._likes = 0

class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        self._nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self._likes = 0


shazan = Filme('shazan 2', 2023, 160)
shazan.dar_like()
print(f'Nome: {shazan.nome} / Ano de lançamento: {shazan.ano} / duração: {shazan.duracao} / likes: {shazan.likes}')

print('\n')

greys = Serie('grays anatomy', 2004, 19)
greys.dar_like()
print(f'Nome: {greys.nome} / Ano de lançamento: {greys.ano} / temporadas: {greys.temporada} / likes: {greys.likes}')