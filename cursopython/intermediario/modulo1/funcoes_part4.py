# variaveis estão no escopo global da aplicação
# são acessiveis de todos os locais

var = 'valor'

def func():
    print(var)

def func2():
    global var # tornando a variavel global, ela pode ser alterada dentro de qualquer escopo **não é uma boa pratica**
    var = 'outro valor' 
    print(var) 

func()
func2()

print(var)

# variavel criada dentro de uma função se torna local
# não pode ser acessada em outras funções ou em escopo global