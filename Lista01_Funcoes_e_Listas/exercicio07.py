def analisar_turbulencia(altitudes):
    maior_queda = 0

    for i in range(1, len(altitudes)):
        queda = altitudes[i - 1] - altitudes[i]
        if queda > maior_queda:
            maior_queda = queda

    return maior_queda > 500, maior_queda


voo = [10000, 10050, 9900, 9300, 9350, 9200, 9250]
turbulencia, queda = analisar_turbulencia(voo)
print("Turbulência severa:", turbulencia)
print("Maior queda:", queda, "m")
