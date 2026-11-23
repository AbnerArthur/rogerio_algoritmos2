import numpy as np

notas = np.array([[5.0, 7.5, 6.0], [8.0, 9.0, 4.0], [3.5, 5.0, 6.5], [7.0, 6.0, 8.5]])

medias_alunos = notas.mean(axis=1)
for i in range(len(medias_alunos)):
    print(f"Média do aluno {i + 1}: {medias_alunos[i]:.2f}")

medias_avaliacoes = notas.mean(axis=0)
melhor = np.argmax(medias_avaliacoes)
print(f"Avaliação com maior média: Avaliação {melhor + 1} ({medias_avaliacoes[melhor]:.2f})")

notas[notas < 6.0] = 6.0
print("Notas após o reajuste:")
print(notas)

notas = np.delete(notas, 2, axis=1)
print("Notas sem a Avaliação 3:")
print(notas)
