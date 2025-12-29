numeros = []

for i in range (10):
    num = int(input('Digite um número: '))

    if num not in numeros:
        numeros.append(num)
    else:
        print('Esse número já foi adicionado')

numeros.sort()

print(f'Números digitados em ordem crescente: {numeros}')