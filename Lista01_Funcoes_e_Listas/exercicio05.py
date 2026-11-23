def classificar_macas(pesos, peso_minimo, peso_maximo):
    aprovados = []
    descartados = []

    for peso in pesos:
        if peso_minimo <= peso <= peso_maximo:
            aprovados.append(peso)
        else:
            descartados.append(peso)

    perda = len(descartados) / len(pesos) * 100
    return aprovados, descartados, perda


safra = [150, 180, 95, 210, 175, 260, 160, 120]
aprovados, descartados, perda = classificar_macas(safra, 130, 200)
print("Aprovados:", aprovados)
print("Descartados:", descartados)
print(f"Perda: {perda:.2f}%")
