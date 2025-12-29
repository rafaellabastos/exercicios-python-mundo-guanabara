alunos = []

for i in range(3):
    notas = {}
    notas['nome'] = str(input('Nome do aluno: '))
    notas['media'] = int(input(f'Media de {notas["nome"]}: '))
    alunos.append(notas)

print(alunos)