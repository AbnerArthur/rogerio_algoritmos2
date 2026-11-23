def processar_imagem(pixels):
    imagem_cinza = []
    pretos = 0

    for r, g, b in pixels:
        imagem_cinza.append((r + g + b) // 3)
        if (r, g, b) == (0, 0, 0):
            pretos += 1

    return imagem_cinza, pretos


def main():
    foto = [
        (255, 255, 255),
        (0, 0, 0),
        (120, 60, 30),
        (0, 0, 0),
        (10, 200, 90),
        (0, 0, 1),
    ]
    imagem, pretos = processar_imagem(foto)
    print("Imagem processada:", imagem)
    print("Pixels totalmente pretos:", pretos)


main()
