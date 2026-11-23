def filtrar_filmes(catalogo, genero_alvo, nota_corte):
    aprovados = []
    mais_antigo = None

    for titulo, ano, genero, nota in catalogo:
        if genero == genero_alvo and nota >= nota_corte:
            aprovados.append(titulo)
            if mais_antigo is None or ano < mais_antigo[1]:
                mais_antigo = (titulo, ano)

    return aprovados, mais_antigo


def main():
    catalogo = [
        ("Matrix", 1999, "Ficção", 8.7),
        ("Interestelar", 2014, "Ficção", 8.6),
        ("Toy Story", 1995, "Animação", 8.3),
        ("Blade Runner", 1982, "Ficção", 8.1),
        ("Lucy", 2014, "Ficção", 6.4),
    ]
    genero_alvo = "Ficção"
    nota_corte = 8.0

    aprovados, mais_antigo = filtrar_filmes(catalogo, genero_alvo, nota_corte)
    print("Filmes aprovados:", aprovados)
    print(f"O filme mais antigo é {mais_antigo[0]}, de {mais_antigo[1]}.")


main()
