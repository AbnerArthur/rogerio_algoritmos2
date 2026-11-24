produtos = []
quantidades = []

opcao = ""
while opcao != "5":
    print("\n1. Cadastrar Produto")
    print("2. Listar Estoque")
    print("3. Atualizar Quantidade")
    print("4. Excluir Produto")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        if nome in produtos:
            print("Produto já cadastrado.")
        else:
            quantidade = int(input("Quantidade: "))
            produtos.append(nome)
            quantidades.append(quantidade)
            print("Produto cadastrado.")

    elif opcao == "2":
        if len(produtos) == 0:
            print("Estoque vazio.")
        for i in range(len(produtos)):
            print(f"{produtos[i]}: {quantidades[i]}")

    elif opcao == "3":
        nome = input("Nome do produto: ")
        if nome in produtos:
            i = produtos.index(nome)
            quantidades[i] = int(input("Nova quantidade: "))
            print("Quantidade atualizada.")
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        nome = input("Nome do produto: ")
        if nome in produtos:
            i = produtos.index(nome)
            produtos.pop(i)
            quantidades.pop(i)
            print("Produto excluído.")
        else:
            print("Produto não encontrado.")

    elif opcao == "5":
        print("Saindo...")

    else:
        print("Opção inválida.")
