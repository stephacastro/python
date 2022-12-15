"""
Exercício - sistema de perguntas e repostas
"""

perguntas = [{
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1', '3', '4', '5'],
    'Resposta': '4',
 },
 {  
    'Pergunta': 'Quanto é 5x5?',
    'Opções': ['25', '55', '10', '51'],
    'Resposta': '25',
 },
 {
    'Pergunta': 'Quanto é 10/2?',
    'Opções': ['4', '5', '2', '1'],
    'Resposta': '5',

 },
]

for pergunta in perguntas:
    print(f'Pergunta: ',pergunta['Pergunta'])
    print()
    

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})',opcao)

    print()
    resposta = input('Escolha uma opção: ')

    if resposta == ['Resposta']:
        print('Você acertou!')
    else:
         print('Você errou X')

    print()

    break