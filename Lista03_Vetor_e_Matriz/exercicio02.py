salarios = [2500.0, 3200.0, 1800.0, 4500.0, 2100.0]

salarios[2] = 2300.0
print("Após atualizar o índice 2:", salarios)

valor = float(input("Digite um salário para buscar: "))
if valor in salarios:
    salarios.remove(valor)
    print("Salário encontrado e removido:", salarios)
else:
    print("Salário não encontrado.")

removido = salarios.pop()
print("Último elemento removido:", removido)
print("Lista final:", salarios)
