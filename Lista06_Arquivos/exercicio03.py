import csv
from pathlib import Path

pasta = Path(__file__).parent
arquivo_clientes = pasta / "clientes.csv"
arquivo_recebimentos = pasta / "recebimentos.csv"


def ler_csv(caminho):
    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo, delimiter=";"))


def cliente_existe(cod_cli):
    for cliente in ler_csv(arquivo_clientes):
        if cliente["cod_cli"] == cod_cli:
            return True
    return False


def cadastrar_recebimento(valor_doc, data_emissao, data_vencimento, cod_cli):
    if not arquivo_clientes.exists() or not arquivo_recebimentos.exists():
        print("Arquivos não existem. Rode o exercício 1 primeiro.")
        return
    if not cliente_existe(cod_cli):
        print("Cliente não encontrado.")
        return

    recebimentos = ler_csv(arquivo_recebimentos)
    if len(recebimentos) == 0:
        num_doc = 1
    else:
        num_doc = int(recebimentos[-1]["num_doc"]) + 1

    with open(arquivo_recebimentos, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow([num_doc, valor_doc, data_emissao, data_vencimento, cod_cli])
    print(f"Recebimento registrado com o número {num_doc}.")


cod_cli = input("Código do cliente: ").strip()
valor_doc = float(input("Valor do documento: "))
data_emissao = input("Data de emissão (dd/mm/aaaa): ").strip()
data_vencimento = input("Data de vencimento (dd/mm/aaaa): ").strip()
cadastrar_recebimento(valor_doc, data_emissao, data_vencimento, cod_cli)
