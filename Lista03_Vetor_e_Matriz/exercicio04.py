import numpy as np

array = np.arange(10, 51, 5)
quadrados = array ** 2
maiores_500 = quadrados[quadrados > 500]

print("Array:", array)
print("Ao quadrado:", quadrados)
print("Maiores que 500:", maiores_500)
