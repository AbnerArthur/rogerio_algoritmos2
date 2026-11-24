def calcular_media(notas):
    return sum(notas) / len(notas)


def adicionar_aluno(alunos):
    nome = input("Nome do aluno: ").strip()
    if nome == "":
        print("Nome inválido.")
        return
    if nome in alunos:
        print("Aluno já cadastrado.")
        return

    notas = []
    for i in range(4):
        nota = float(input(f"Nota {i + 1}: "))
        notas.append(nota)

    alunos[nome] = notas
    print(f"{nome} cadastrado com sucesso.")


def remover_aluno(alunos):
    nome = input("Nome do aluno a remover: ").strip()
    if nome in alunos:
        del alunos[nome]
        print(f"{nome} removido.")
    else:
        print("Aluno não encontrado.")


def mostrar_medias(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    for nome, notas in alunos.items():
        print(f"{nome}: média {calcular_media(notas):.2f}")


def maior_media(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    melhor_nome = ""
    melhor_media = -1
    for nome, notas in alunos.items():
        media = calcular_media(notas)
        if media > melhor_media:
            melhor_media = media
            melhor_nome = nome

    print(f"Maior média: {melhor_nome} ({melhor_media:.2f})")


def exibir_alunos(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    for nome, notas in alunos.items():
        print(f"{nome} | Notas: {notas} | Média: {calcular_media(notas):.2f}")


def main():
    alunos = {}
    opcao = ""

    while opcao != "6":
        print("\n1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Calcular média de todos os alunos")
        print("4. Aluno com a maior média")
        print("5. Exibir todos os alunos")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno(alunos)
        elif opcao == "2":
            remover_aluno(alunos)
        elif opcao == "3":
            mostrar_medias(alunos)
        elif opcao == "4":
            maior_media(alunos)
        elif opcao == "5":
            exibir_alunos(alunos)
        elif opcao == "6":
            print("Saindo do sistema...")
        else:
            print("Opção inválida.")


main()
