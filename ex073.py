brasileirao = ["Flamengo", "Palmeiras", "Cruzeiro", "Mirassol", "Fluminense", "Botafogo", "Bahia", "São Paulo", "Grêmio", 
               "Red Bull", "Atlético Mineiro", "Santos", "Corinthians", "Vasco", "Vitoria", "Internacional", "Ceará", 
               "Fortaleza", "Juventude", "Recife"]

print(f"Os cinco primeiros colocados são {brasileirao[0:4]}")

print(f"Os quatro últimos colocados são {brasileirao[-4:]}")

print(f"Os times em ordem alfabetica: {sorted(brasileirao)}")

if "Chapecoense" in brasileirao: 
    posicao = brasileirao.index("Chapecoense")
    print(f"Posição da Chapecoense: {posicao+1}")
else:
    print("O time não está na série A")