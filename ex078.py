valores = []

for i in range(5):
    valor = int(input('Digite um número: '))
    valores.append(valor)

print(f'Maior número digitado: {max(valores)}. Ele está na posição {valores.index(max(valores)) + 1}')
print(f'Menor número digitado: {min(valores)}. Ele está na posição {valores.index(min(valores)) + 1}')