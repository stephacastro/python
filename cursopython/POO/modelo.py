
class Filme:
    
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title() 
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property # permite que faça alteração no atributo privado sem quebrar o cod 
    def likes(self):
        return self.__likes
    
    def dar_like(self):
        self.__likes += 1
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

   
class Serie:

    def __init__(self, nome, ano, temporada):
        self.__nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes
    
    def dar_like(self):
        self.__likes += 1
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


shazan = Filme('shazan 2', 2023, 160)
shazan.dar_like()
shazan.dar_like()
print(f'Nome: {shazan.nome} / Ano de lançamento: {shazan.ano} / duração: {shazan.duracao} / likes: {shazan.likes}')

print('\n')

greys = Serie('grays anatomy', 2004, 19)
greys.dar_like()
print(f'Nome: {greys.nome} / Ano de lançamento: {greys.ano} / temporadas: {greys.temporada} / likes: {greys.likes}')