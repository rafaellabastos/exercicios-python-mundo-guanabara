import random

jogadores = []
dado = (1, 2, 3, 4, 5, 6)

for i in range(4):
    resultado = {}

    resultado['jogador'] = str(input(f'Nome do jogador {i+1}: '))
    resultado['dados'] = random.choice(dado)

    jogadores.append(resultado)

jogadores.sort(key=lambda x: x['dados'], reverse=True)

print ('-' * 30)

for i, j in enumerate(jogadores, start=1):
    print(f'Jogador {j["jogador"]}: número {j["dados"]}')

print ('-' * 30)

print(f'''
      Jogador 1: {jogadores[0]}
        Jogador 2: {jogadores[1]}
        Jogador 3: {jogadores[2]}
        Jogador 4: {jogadores[3]}
      ''')

