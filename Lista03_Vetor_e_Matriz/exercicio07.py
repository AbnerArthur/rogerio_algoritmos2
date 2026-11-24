def transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = []
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        resultado.append(nova_linha)
    return resultado


matriz = [[1, 2], [3, 4], [5, 6]]
print("Matriz original:", matriz)

matriz[1][0] = int(input("Novo valor para a linha 1, coluna 0: "))
print("Matriz atualizada:", matriz)

print("Matriz transposta:", transposta(matriz))
