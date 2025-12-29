from datetime import datetime, date

funcionarios = []

for i in range(3):
    trabalhador = {}

    trabalhador['nome'] = str(input('Nome: '))
    trabalhador['nasc'] = input('Data de nascimento: ')
    trabalhador['ctps'] = int(input('Carteira de trabalho: '))

    if (trabalhador['ctps'] != 0):
        trabalhador['anoContratacao'] = int(input('Ano de contratação: '))
        trabalhador['salario'] = float(input('Salário: '))


    trabalhador['nascimento'] = datetime.strptime(trabalhador['nasc'], "%d/%m/%Y").date()
    hoje = date.today()

    trabalhador['idade'] = hoje.year - trabalhador['nascimento'].year
    
    if (hoje.month, hoje.day) < (trabalhador['nascimento'].month, trabalhador['nascimento'].day):
        trabalhador['idade'] -= 1

    funcionarios.append(trabalhador)

print('-' * 30)

for i, j in enumerate(funcionarios, start=1):
    if (j['ctps'] != 0):
        print(f'''
                Nome: {j['nome']}
                Data de nascimento: {j['nasc']}
                CTPS: {j['ctps']}
                Ano Contratação: {j['anoContratacao']}
                Salário: {j['salario']}
                Idade: {j['idade']}
              ''')
    else:
        print(f'''
              Nome: {j['nome']}
              Data de nascimento: {j['nasc']}
              CTPS: {j['ctps']}
              Idade: {j['idade']}
            ''')  

# print(funcionarios)

