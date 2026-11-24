import csv
from pathlib import Path

pasta = Path(__file__).parent
arquivo_clientes = pasta / "clientes.csv"
arquivo_recebimentos = pasta / "recebimentos.csv"


def ler_csv(caminho):
    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        return leitor.fieldnames, list(leitor)


def salvar_csv(caminho, campos, linhas):
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos, delimiter=";")
        escritor.writeheader()
        escritor.writerows(linhas)


def excluir_cliente(cod_cli):
    campos_cli, clientes = ler_csv(arquivo_clientes)
    restantes = [c for c in clientes if c["cod_cli"] != cod_cli]

    if len(restantes) == len(clientes):
        print("Cliente não encontrado.")
        return
    salvar_csv(arquivo_clientes, campos_cli, restantes)

    campos_rec, recebimentos = ler_csv(arquivo_recebimentos)
    rec_restantes = [r for r in recebimentos if r["cod_cli"] != cod_cli]
    salvar_csv(arquivo_recebimentos, campos_rec, rec_restantes)

    removidos = len(recebimentos) - len(rec_restantes)
    print(f"Cliente excluído junto com {removidos} recebimento(s).")


cod_cli = input("Código do cliente a excluir: ").strip()
excluir_cliente(cod_cli)
