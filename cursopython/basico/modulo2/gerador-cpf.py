from random import randint
numero = str(randint(100000000, 999999999))  # gerando numero aleatórios

novo_cpf = numero  # elimina os dois ultimos digitos do CPF
reverso = 10  # contador reverso
total = 0

# loop do CPF
for index in range(19):
    if index > 8:  # primeiro indice vai de 0 a 9
        index -= 9  # são os primeiros digitos do CPF

    total += int(novo_cpf[index]) * reverso  # valor total da multiplicação

    reverso -= 1  # decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)



