preco = float(input("Digite o preço do produto: R$"))

desconto =  preco - (preco*5/100)

print(f"O produto custa: R${preco} e com desconto de 5% ficará R${desconto:.2f}")