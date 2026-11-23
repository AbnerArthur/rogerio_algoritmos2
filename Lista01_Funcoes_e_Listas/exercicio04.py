def merge_ordenado(lista_a, lista_b):
    resultado = []
    i = 0
    j = 0

    while i < len(lista_a) and j < len(lista_b):
        if lista_a[i] <= lista_b[j]:
            resultado.append(lista_a[i])
            i += 1
        else:
            resultado.append(lista_b[j])
            j += 1

    resultado += lista_a[i:] + lista_b[j:]
    return resultado


a = [1, 4, 7, 10]
b = [2, 3, 8, 12, 15]
print(merge_ordenado(a, b))
