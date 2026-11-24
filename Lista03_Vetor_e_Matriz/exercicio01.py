n = int(input("Quantos números deseja cadastrar? "))

numeros = []
for i in range(n):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

maior = numeros[0]
menor = numeros[0]
soma = 0
pares = 0

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero
    if numero % 2 == 0:
        pares += 1

print("Maior valor:", maior)
print("Menor valor:", menor)
print("Média:", soma / n)
print("Quantidade de pares:", pares)
