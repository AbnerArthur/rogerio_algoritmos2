matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:5}", end="")
    print()

diagonal_principal = []
diagonal_secundaria = []
for i in range(3):
    for j in range(3):
        if i == j:
            diagonal_principal.append(matriz[i][j])
        if i + j == 2:
            diagonal_secundaria.append(matriz[i][j])

print("\nDiagonal principal:", diagonal_principal)
print("Diagonal secundária:", diagonal_secundaria)
