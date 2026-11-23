def verificar_sensores(leituras):
    alertas = []
    maior_temperatura = leituras[0][1]
    menor_umidade = leituras[0][2]

    for id_sensor, temperatura, umidade in leituras:
        if temperatura > 35 or umidade < 20:
            alertas.append(id_sensor)
        if temperatura > maior_temperatura:
            maior_temperatura = temperatura
        if umidade < menor_umidade:
            menor_umidade = umidade

    return alertas, (maior_temperatura, menor_umidade)


def main():
    sensores = [
        (1, 28.5, 45.0),
        (2, 37.2, 40.0),
        (3, 30.0, 15.5),
        (4, 25.0, 60.0),
    ]
    alertas, picos = verificar_sensores(sensores)
    print("Sensores em alerta:", alertas)
    print("Maior temperatura:", picos[0], "°C")
    print("Menor umidade:", picos[1], "%")


main()
