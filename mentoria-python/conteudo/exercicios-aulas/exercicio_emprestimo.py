print("======================== Steph's Bank ======================== ")

negativado = int(input('''Possui nome negativado?\n
    [0] Sim
    [1] Não
    '''))
carteira_assinada = int(input('''Possui carteira assinada?\n
    [0] Sim
    [1] Não
    '''))
casa_propria = int(input('''Possui casa própria?\n
    [0] Sim
    [1] Não
    '''))

if not negativado and carteira_assinada and casa_propria:
    print('Empréstimo liberado!')
else:
    print('Não pode realizar empréstimo ;(')
    
