import random

apresentacao = []

for i in range(4):
    nome = input(f'Digite o nome do aluno {i + 1}: ')
    apresentacao.append(nome)

for i in range(4):
    escolhido = random.choice(apresentacao)
    print(f'Apresentação {i + 1}: {escolhido}')
    apresentacao.remove(escolhido)
    print(f'Restantes: {apresentacao}')