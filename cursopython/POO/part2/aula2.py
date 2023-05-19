# self

class Animal():

    def __init__(self, nome):
        self.nome = nome

        variavel = 'testando' # variavel dentro instância só pode ser acessada na instância
        print(variavel) 

    def comendo(self, alimento):
        return f'{self.nome} está comento {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    

urso = Animal('Urso')
print(urso.nome)
print(urso.comendo('Melância'))
print(urso.executar('Bambu'))
    