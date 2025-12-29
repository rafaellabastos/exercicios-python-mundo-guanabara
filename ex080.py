valores = []

for i in range(5):
    valor = int(input('Digite um número: '))

    if len(valores) == 0 or valor > valores[-1]:
        valores.append(valor)
    else:
        pos = 0
        while pos < len(valores) and valor > valores[pos]:
            pos += 1
        valores.insert(pos, valor)

print(f'Valores digitados em ordem: {valores}')

