print("======== BEM-VINDO A LOCADORA RECIFE ========")

kmRodados = float(input("Quantos quilômetros  o carro andou? "))
diasAlugado = int(input("Quantos dias o carro passou alugado? "))

precoTotal = 0.15 * kmRodados + 60 * diasAlugado

print(f"O preço final do aluguel será R${precoTotal}")