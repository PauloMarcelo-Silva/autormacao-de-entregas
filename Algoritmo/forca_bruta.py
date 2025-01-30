from itertools import permutations
from calcula_custo import calcular_custo

def forca_bruta(dados, ponto_partida):
    """
    Encontra a melhor rota testando todas as combinações possíveis (força bruta).

    :param dados: Objeto contendo a matriz de custos e número de clientes.
    :param ponto_partida: Índice do ponto inicial.
    :return: Melhor rota encontrada e seu custo.
    """
    pontos = list(range(dados.n + 1))  # Criamos uma lista de pontos [0, 1, 2, ..., n]
    pontos.remove(ponto_partida)  # Removemos o ponto de partida

    melhor_rota = None
    menor_custo = float('inf')

    # Gerar todas as permutações possíveis dos pontos
    for perm in permutations(pontos):
        rota = [ponto_partida] + list(perm) + [ponto_partida]  # Sempre começa e termina no mesmo ponto
        custo = calcular_custo(rota, dados)

        if custo < menor_custo:
            menor_custo = custo
            melhor_rota = rota

    return melhor_rota, menor_custo
