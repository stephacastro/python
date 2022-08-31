"""
Pass e elipsis como Placeholders
pass - utilizado para substuir uma linha de cog que sera escrita posteriomente
permite que não ocorra erro mesmo que não tinha uma linha de comando
'...' tbm faz a mesma coisa que o pass
"""
valor = True

if valor:
    pass
elif valor:
    ...
else:
    print('Tchau')