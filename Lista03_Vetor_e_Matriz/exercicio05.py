import numpy as np

notas = np.array([5.5, 8.0, 4.5, 9.0, 6.5])
print("Notas iniciais:", notas)

notas = np.insert(notas, 2, 7.0)
print("Após inserir 7.0 no índice 2:", notas)

notas[notas < 6.0] = 6.0
print("Após a recuperação:", notas)

notas = np.delete(notas, 4)
print("Após remover o índice 4:", notas)
