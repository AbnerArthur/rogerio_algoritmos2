def verificar_colisao(obstaculos, jogador):
    jog_x, jog_y, jog_raio = jogador
    colisoes = 0

    for pos_x, pos_y, raio in obstaculos:
        distancia = abs(pos_x - jog_x) + abs(pos_y - jog_y)
        if distancia < raio + jog_raio:
            colisoes += 1

    return colisoes > 0, colisoes


def main():
    obstaculos = [
        (10, 10, 3),
        (14, 10, 2),
        (50, 50, 5),
        (12, 13, 2),
        (80, 20, 4),
    ]
    jogador = (12, 10, 2)

    colidiu, quantidade = verificar_colisao(obstaculos, jogador)
    if colidiu:
        print("Impacto Detectado!")
    else:
        print("Caminho Livre")
    print("Obstáculos atingidos:", quantidade)


main()
