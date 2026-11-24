import csv
from pathlib import Path

arquivo_notas = Path(__file__).parent / "notas.csv"


def criar_arquivo():
    if arquivo_notas.exists():
        print("O arquivo já existe.")
        return
    with open(arquivo_notas, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(["numero", "nome", "nota_1", "nota_2"])
    print("Arquivo criado.")


def ler_registros():
    with open(arquivo_notas, "r", newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo, delimiter=";"))


def incluir():
    if not arquivo_notas.exists():
        print("Crie o arquivo primeiro (opção 1).")
        return

    nome = input("Nome: ").strip()
    if nome == "":
        print("Nome inválido.")
        return
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))

    registros = ler_registros()
    numero = len(registros) + 1

    with open(arquivo_notas, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow([numero, nome, nota_1, nota_2])
    print("Registro incluído.\n")

    for registro in ler_registros():
        media = (float(registro["nota_1"]) + float(registro["nota_2"])) / 2
        print(f"{registro['numero']} - {registro['nome']} | "
              f"Notas: {registro['nota_1']} e {registro['nota_2']} | Média: {media:.2f}")


def main():
    opcao = ""
    while opcao != "3":
        print("\n1. Criar arquivo")
        print("2. Incluir")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_arquivo()
        elif opcao == "2":
            incluir()
        elif opcao == "3":
            print("Saindo...")
        else:
            print("Opção inválida.")


main()
