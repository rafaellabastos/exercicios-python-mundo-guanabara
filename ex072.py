numeros = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", 
           "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"]

while True:
    numero = int(input("Digite um número: "))

    if 0 <= numero <= 20:
        print(f"O número {numero} é {numeros[numero]}")
    else:
        print("O número deve estar entre zero e vinte")
