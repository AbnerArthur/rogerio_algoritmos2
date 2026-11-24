import csv
from pathlib import Path

arquivo_clientes = Path(__file__).parent / "clientes.csv"


def ler_clientes():
    with open(arquivo_clientes, "r", newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo, delimiter=";"))


def cadastrar_cliente(nome, endereco, fone):
    if not arquivo_clientes.exists():
        print("Arquivo de clientes não existe. Rode o exercício 1 primeiro.")
        return
    if nome == "" or endereco == "" or fone == "":
        print("Preencha todos os campos.")
        return

    clientes = ler_clientes()
    for cliente in clientes:
        if cliente["nome"] == nome and cliente["endereco"] == endereco and cliente["fone"] == fone:
            print("Cliente já cadastrado.")
            return

    if len(clientes) == 0:
        codigo = 1
    else:
        codigo = int(clientes[-1]["cod_cli"]) + 1

    with open(arquivo_clientes, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow([codigo, nome, endereco, fone])
    print(f"Cliente cadastrado com o código {codigo}.")


nome = input("Nome: ").strip()
endereco = input("Endereço: ").strip()
fone = input("Telefone: ").strip()
cadastrar_cliente(nome, endereco, fone)
