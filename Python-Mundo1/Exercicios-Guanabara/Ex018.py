import math

angulo = float(input("Digite o angulo que deseja: "))

tangente = math.tan(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))

print(f"Angulo digitado: {angulo}º\nSeno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}")