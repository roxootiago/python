from math import hypot

catetoAdjacente = float(input("Digite o cateto adjacente: "))
catetoOposto = float(input("Digite o cateto oposto: "))

print(f"{catetoAdjacente}² + {catetoOposto}² = {hypot(catetoAdjacente,catetoOposto):.2f}")