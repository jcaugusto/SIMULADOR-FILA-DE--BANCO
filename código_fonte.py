último = 10
fila = list(range(1, último + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"fila atual; {fila}")
    print("Digite F para adicionar um clinte ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")

    operação = input("operação ( F, A ou S):")

    if operação == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"cliente {atendido} atendido")

        else:
            print("fila vazia! ninguém para atender.")

    elif operação == "F":
        último += 1   # Incrementa o ticket do novo cleinte
        fila.append(último)

    elif operação == "S":
        break

    else:
        print("Operação Inválida Digite apenas F, A ou S!")