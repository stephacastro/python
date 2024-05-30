while True:
    print('\n************ ATLETISMO ************')
    nome = input('\nAtleta: ')

    if nome == '':
        break
    else:

        s1 = float(input('Distância salto 1: '))
        s2 = float(input('Distância salto 2: '))
        s3 = float(input('Distância salto 3: '))
        s4 = float(input('Distância salto 4: '))
        s5 = float(input('Distância salto 5: '))

        media = (s1 + s2 + s3 + s4 + s5) / 5

        print(nome)
        print(f'\nPrimeiro Salto: {s1} m')
        print(f'Segundo Salto: {s2} m')
        print(f'Terceiro Salto: {s3} m')
        print(f'Quarto Salto: {s4} m')
        print(f'Quinto Salto: {s5} m')

        print('\n************ Resultado Final ************')
        print(f'Atleta: {nome}')
        print(f'Saltos: {s1} - {s2} - {s3} - {s4} - {s5}')
        print(f'Média dos saltos: {media}')

