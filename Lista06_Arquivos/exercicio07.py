import csv
from pathlib import Path

arquivo_produtos = Path(__file__).parent / "produtos.csv"
campos = ["codigo", "descricao", "preco"]


def ler_produtos():
    with open(arquivo_produtos, "r", newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo, delimiter=";"))


def salvar_produtos(produtos):
    with open(arquivo_produtos, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos, delimiter=";")
        escritor.writeheader()
        escritor.writerows(produtos)


def buscar(produtos, codigo):
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None


def criar_arquivo():
    if arquivo_produtos.exists():
        print("O arquivo já existe.")
        return
    salvar_produtos([])
    print("Arquivo criado.")


def cadastrar():
    produtos = ler_produtos()
    codigo = input("Código: ").strip()
    if codigo == "" or buscar(produtos, codigo) is not None:
        print("Código vazio ou já cadastrado.")
        return
    descricao = input("Descrição: ").strip()
    preco = float(input("Preço: "))

    produtos.append({"codigo": codigo, "descricao": descricao, "preco": preco})
    salvar_produtos(produtos)
    print("Produto cadastrado.")


def listar_todos():
    produtos = ler_produtos()
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    for produto in produtos:
        print(f"{produto['codigo']} | {produto['descricao']} | R$ {float(produto['preco']):.2f}")


def listar_um():
    produto = buscar(ler_produtos(), input("Código: ").strip())
    if produto is None:
        print("Produto não encontrado.")
    else:
        print(f"{produto['codigo']} | {produto['descricao']} | R$ {float(produto['preco']):.2f}")


def atualizar():
    produtos = ler_produtos()
    produto = buscar(produtos, input("Código: ").strip())
    if produto is None:
        print("Produto não encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")
    descricao = input(f"Descrição ({produto['descricao']}): ").strip()
    preco = input(f"Preço ({produto['preco']}): ").strip()
    if descricao != "":
        produto["descricao"] = descricao
    if preco != "":
        produto["preco"] = float(preco)

    salvar_produtos(produtos)
    print("Produto atualizado.")


def deletar():
    produtos = ler_produtos()
    produto = buscar(produtos, input("Código: ").strip())
    if produto is None:
        print("Produto não encontrado.")
        return
    produtos.remove(produto)
    salvar_produtos(produtos)
    print("Produto deletado.")


def main():
    opcao = ""
    while opcao != "7":
        print("\n1. Criar arquivo")
        print("2. Cadastrar produto")
        print("3. Listar todos os produtos")
        print("4. Listar um produto")
        print("5. Atualizar produto")
        print("6. Deletar produto")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_arquivo()
        elif opcao in ["2", "3", "4", "5", "6"] and not arquivo_produtos.exists():
            print("Crie o arquivo primeiro (opção 1).")
        elif opcao == "2":
            cadastrar()
        elif opcao == "3":
            listar_todos()
        elif opcao == "4":
            listar_um()
        elif opcao == "5":
            atualizar()
        elif opcao == "6":
            deletar()
        elif opcao == "7":
            print("Saindo...")
        else:
            print("Opção inválida.")


main()
