from pathlib import Path

import pandas as pd

arquivo_vendas = Path(__file__).parent / "vendas.csv"

print("=" * 60)
print("RELATÓRIO: A BIBLIOTECA PANDAS")
print("=" * 60)

print("""
O pandas é uma biblioteca do Python para trabalhar com dados em
forma de tabela. A estrutura principal é o DataFrame, que funciona
como uma planilha: tem linhas, colunas e um índice.

Instalação: python -m pip install pandas
""")

vendas = pd.DataFrame({
    "vendedor": ["Ana", "Bruno", "Ana", "Carla", "Bruno", "Carla"],
    "regiao": ["Norte", "Sul", "Norte", "Centro", "Sul", "Centro"],
    "valor": [1500.0, 900.0, 2100.0, 1200.0, 650.0, 1800.0],
})

print("1. Criando um DataFrame a partir de um dicionário:")
print(vendas)

print("\n2. Informações gerais (linhas, colunas e tipos):")
vendas.info()

print("\n3. Estatísticas da coluna 'valor' com describe():")
print(vendas["valor"].describe())

print("\n4. Filtrando vendas acima de R$ 1000:")
print(vendas[vendas["valor"] > 1000])

print("\n5. Ordenando pelo valor, do maior para o menor:")
print(vendas.sort_values("valor", ascending=False))

print("\n6. Total vendido por região com groupby():")
print(vendas.groupby("regiao")["valor"].sum())

print("\n7. Criando uma coluna nova (comissão de 5%):")
vendas["comissao"] = vendas["valor"] * 0.05
print(vendas)

print("\n8. Salvando e lendo um arquivo CSV:")
vendas.to_csv(arquivo_vendas, sep=";", index=False)
lido = pd.read_csv(arquivo_vendas, sep=";")
print(lido.head(3))

print("""
CONCLUSÃO
Com poucas linhas, o pandas lê e grava arquivos (CSV, Excel, JSON),
filtra, ordena, agrupa e cria novas colunas. Isso daria muito mais
trabalho com listas e o módulo csv, por isso ele é tão usado em
análise de dados.
""")
