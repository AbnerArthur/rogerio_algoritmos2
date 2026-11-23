def calcular_compra(recibo):
    total = 0
    mais_caro = None

    for codigo, quantidade, preco in recibo:
        valor_item = quantidade * preco
        total += valor_item
        if mais_caro is None or valor_item > mais_caro[1]:
            mais_caro = (codigo, valor_item)

    return total, mais_caro


def main():
    carrinho = [
        (101, 2, 4.50),
        (102, 1, 32.90),
        (103, 3, 12.00),
        (104, 5, 2.75),
    ]
    total, mais_caro = calcular_compra(carrinho)
    total_formatado = f"{total:.2f}".replace(".", ",")
    item_formatado = f"{mais_caro[1]:.2f}".replace(".", ",")
    print(f"Total da nota: R$ {total_formatado}")
    print(f"Item mais caro: produto {mais_caro[0]}, R$ {item_formatado}")


main()
