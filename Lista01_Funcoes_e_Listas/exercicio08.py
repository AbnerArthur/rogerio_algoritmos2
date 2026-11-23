def apurar_votos(votos):
    ids = []
    for voto in votos:
        if voto not in ids:
            ids.append(voto)

    resumo = []
    for candidato in ids:
        resumo.append([candidato, votos.count(candidato)])

    vencedor = None
    maior = 0
    for candidato, total in resumo:
        if candidato != 0 and total > maior:
            maior = total
            vencedor = candidato

    brancos = votos.count(0) / len(votos) * 100
    return resumo, vencedor, brancos


urna = [13, 45, 0, 13, 22, 13, 45, 0, 13, 22, 45, 13]
resumo, vencedor, brancos = apurar_votos(urna)
print("Resumo:", resumo)
print("Vencedor:", vencedor)
print(f"Brancos: {brancos:.2f}%")
