precoProduto = float(input("Digite o preço do produto: R$"))
formaPag = int(input("Qual será a forma de pagamento?\n1- A vista\n2 - Cartão (até 12x)\n"))

match formaPag:
    case 1:
        desconto = precoProduto - (precoProduto*20/100)
        print(f"Produto a vista ficará R${desconto} com 20% de desconto")
    case 2:
        aumento = (precoProduto*10/100) + precoProduto
        print(f"Produto terá um acréscimo de 10% e custará R${aumento}")

    case _:
        print("Digite uma opção válida!")