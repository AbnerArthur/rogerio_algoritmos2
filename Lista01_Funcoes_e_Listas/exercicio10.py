def decodificar_sinal(bits):
    inicios = []
    for i in range(len(bits) - 2):
        if bits[i] == 1 and bits[i + 1] == 0 and bits[i + 2] == 0:
            inicios.append(i)
    return len(inicios), inicios


sinal = [1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0]
total, posicoes = decodificar_sinal(sinal)
print("Pacotes válidos:", total)
print("Posições:", posicoes)
