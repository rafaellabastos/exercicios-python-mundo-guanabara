valores = []

for i in range(10):
    valor = int(input('Digite um número: '))
    valores.append(valor)

print(f'Quantidade de números digitados: {len(valores)}')

valores.sort(reverse=True)
print(f'Números em ordem decrescente: {valores}')

if 5 in valores: 
    print('Número 5 foi digitado.')
else:
    print('Número 5 não foi digitado.')