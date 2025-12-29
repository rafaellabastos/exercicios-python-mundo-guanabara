km = int(input('Quantidade de km percorridos pelo carro alugado: '))
dias = int(input('Quantidade de dias que ele foi alugado: '))

preco = (km * 0.15) + (dias * 60)

print(f'O preço do aluguel é R${preco}')