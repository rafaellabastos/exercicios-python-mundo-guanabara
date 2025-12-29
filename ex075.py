lista = []
pares = []

for i in range (4):
    numero = int(input('Digite um número: '))
    lista.append(numero)

print(f'Quantidade de vezes que o número 9 apareceu: {lista.count(9)}')


if 3 in lista:
    print(f'Posição que o primeiro 3 foi digitado: {lista.index(3) + 1}')
else:
    print('O número 3 não foi digitado.')


for i in lista:
    if i % 2 == 0:
        pares.append(i)


print(f'Números pares: {pares}')
