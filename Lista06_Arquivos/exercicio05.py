import csv
from pathlib import Path

arquivo_clientes = Path(__file__).parent / "clientes.csv"


def atualizar_cliente(cod_cli):
    with open(arquivo_clientes, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        campos = leitor.fieldnames
        clientes = list(leitor)

    for cliente in clientes:
        if cliente["cod_cli"] == cod_cli:
            print("Deixe em branco para manter o valor atual.")
            nome = input(f"Nome ({cliente['nome']}): ").strip()
            endereco = input(f"Endereço ({cliente['endereco']}): ").strip()
            fone = input(f"Telefone ({cliente['fone']}): ").strip()

            if nome != "":
                cliente["nome"] = nome
            if endereco != "":
                cliente["endereco"] = endereco
            if fone != "":
                cliente["fone"] = fone

            with open(arquivo_clientes, "w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.DictWriter(arquivo, fieldnames=campos, delimiter=";")
                escritor.writeheader()
                escritor.writerows(clientes)
            print("Cliente atualizado.")
            return

    print("Cliente não encontrado.")


cod_cli = input("Código do cliente a atualizar: ").strip()
atualizar_cliente(cod_cli)
