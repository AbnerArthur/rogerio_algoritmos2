import numpy as np

matriz = np.random.randint(10, 100, size=(4, 4))
print("Matriz 4x4:")
print(matriz)

print("Soma de cada linha:", matriz.sum(axis=1))
print("Média de cada coluna:", matriz.mean(axis=0))

nova_matriz = matriz.reshape(2, 8)
print("Matriz 2x8:")
print(nova_matriz)
