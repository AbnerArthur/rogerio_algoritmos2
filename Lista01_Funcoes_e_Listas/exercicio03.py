def concatenar_alternado(lista_a, lista_b):
    resultado = []
    menor = min(len(lista_a), len(lista_b))

    for i in range(menor):
        resultado.append(lista_a[i])
        resultado.append(lista_b[i])

    resultado += lista_a[menor:] + lista_b[menor:]
    return resultado


a = [1, 3, 5]
b = [2, 4, 6, 8, 10]
print(concatenar_alternado(a, b))
