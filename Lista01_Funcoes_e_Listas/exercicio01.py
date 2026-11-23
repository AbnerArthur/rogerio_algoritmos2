def media_movel(numeros, k):
    medias = []
    for i in range(len(numeros) - k + 1):
        soma = sum(numeros[i:i + k])
        medias.append(soma / k)
    return medias


valores = [2, 4, 6, 8, 10, 12]
print(media_movel(valores, 3))
