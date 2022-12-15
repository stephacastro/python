"""
Métodos úteis dos dicionários em Python
* len - quantas chaves (tamanho)
* keys - iterável com as chaves
* values - iterável com os valores
* items - iterável com chaves e valores
* setdefault - adiciona valor se a chave não existe
* copy - retorna uma cópia rasa (shallow copy)
* get - obtém uma chave
* pop - apaga um item com a chave especifica (del)
* popitem - apaga o último item adicionado
* update - atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Stephanie',
    'sobrenome': 'Castro',
    'idade': 25,
    'números': [1,2,3]
}

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
pessoa.setdefault('Altura', 1.67)

dic = pessoa.copy()
print(dic)

print(pessoa.get('nome'))

nome = pessoa.pop('nome')
print(pessoa)

ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

pessoa.update({
    'nome': 'Manu',
    'altura': 1.67
})

pessoa.update(nome = 'Maria', idade = 26)

print(pessoa)