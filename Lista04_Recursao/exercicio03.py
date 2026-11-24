def contagem_regressiva(n):
    if n < 1:
        print("Lançar!")
        return
    print(n)
    contagem_regressiva(n - 1)


contagem_regressiva(5)
