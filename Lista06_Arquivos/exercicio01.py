import csv
from pathlib import Path

pasta = Path(__file__).parent
arquivo_clientes = pasta / "clientes.csv"
arquivo_recebimentos = pasta / "recebimentos.csv"

campos_clientes = ["cod_cli", "nome", "endereco", "fone"]
campos_recebimentos = ["num_doc", "valor_doc", "data_emissao", "data_vencimento", "cod_cli"]


def criar_arquivo(caminho, campos):
    if caminho.exists():
        print(f"{caminho.name} já existe.")
        return
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(campos)
    print(f"{caminho.name} criado.")


criar_arquivo(arquivo_clientes, campos_clientes)
criar_arquivo(arquivo_recebimentos, campos_recebimentos)
