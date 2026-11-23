def verificar_manutencao(trajetos, limite):
    total = 0
    dia_limite = None

    for dia in range(len(trajetos)):
        total += trajetos[dia]
        if total > limite and dia_limite is None:
            dia_limite = dia

    recolher = dia_limite is not None
    return total, dia_limite, recolher


trajetos = [320, 410, 280, 500, 390, 450]
total, dia, recolher = verificar_manutencao(trajetos, 1500)
print("Total:", total, "km")
print("Dia em que passou do limite:", dia)
print("Recolher:", recolher)
