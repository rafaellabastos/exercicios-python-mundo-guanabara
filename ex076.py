catalogo = [
    'Conselho', 6.00,
    'Pergunta Avulsa', 12.00,
    'Tiragem da Luz', 14.00,
    'Alecrim Dourado', 18.00,
    'Análise de sonhos', 18.00,
    'Leitura Pet', 20.00,
    'Tio Patinhas', 20.00,
    'O Executivo', 20.00
]

print('-' * 40)
print('MÉTODOS E VALORES')
print('-' * 40)

for i in range (0, len(catalogo), 2):
    nome = catalogo[i]
    preco = catalogo[i + 1]
    print(f'{nome:.<30} R${preco:>7.2f}')

print('-' * 40)