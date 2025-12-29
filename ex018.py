import math

angulo = float(input('Digite o valor do ângulo: '))

radiano = math.radians(angulo)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f'''O ângulo {angulo} equivale ao radiano {radiano} e representa:
      Seno: {seno:.2f} 
      Cosseno: {cosseno:.2f} 
      Tangente: {tangente:.2f}''')