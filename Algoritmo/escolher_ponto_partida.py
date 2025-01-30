def escolher_ponto_partida(nomes):
    """
    Permite ao usuário escolher o ponto de partida para as entregas.

    :param nomes: Lista de nomes dos pontos.
    :return: Índice do ponto escolhido.
    """
    print("Escolha o ponto de partida para as entregas:")
    for i, nome in enumerate(nomes):
        print(f"{i}: {nome}")  # Exibe as opções de pontos.

    while True:
        try:
            escolha = int(input("Digite o número correspondente ao ponto de partida: "))
            if 0 <= escolha < len(nomes):  # Valida se a escolha está dentro do intervalo válido.
                return escolha
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")  # Captura erros de entrada.
