def deslocar_direita(lista, n):
    if len(lista) == 0:
        return []
    n = n % len(lista)
    return lista[-n:] + lista[:-n]


valores = [1, 2, 3, 4, 5]
print(deslocar_direita(valores, 2))
