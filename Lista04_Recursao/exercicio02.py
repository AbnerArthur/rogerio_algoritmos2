def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)


print("2^10 =", potencia(2, 10))
print("3^4 =", potencia(3, 4))
print("7^0 =", potencia(7, 0))
