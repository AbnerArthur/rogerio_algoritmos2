def dia_mais_critico(disponibilidade, dias_no_mes):
    dia_critico = 1
    menor = len(disponibilidade) + 1

    for dia in range(1, dias_no_mes + 1):
        quantidade = 0
        for dias_medico in disponibilidade:
            if dia in dias_medico:
                quantidade += 1
        if quantidade < menor:
            menor = quantidade
            dia_critico = dia

    medicos = []
    for i in range(len(disponibilidade)):
        if dia_critico in disponibilidade[i]:
            medicos.append(i)

    return dia_critico, medicos


escala = [
    [1, 2, 3, 5, 6],
    [1, 3, 4, 6, 7],
    [2, 3, 5, 6, 7],
    [1, 2, 4, 5, 7],
]
dia, medicos = dia_mais_critico(escala, 7)
print("Dia mais crítico:", dia)
print("Médicos:", medicos)
