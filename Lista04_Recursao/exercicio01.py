def soma_recursiva(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma_recursiva(lista[1:])


numeros = [5, 10, 3, 8, 2]
print("Lista:", numeros)
print("Soma:", soma_recursiva(numeros))
