def calcular_custo(rota, dados):
    """
    Calcula o custo total de uma rota com base na matriz de custos.
    :param rota: Lista de pontos na ordem em que serão visitados.
    :param dados: Objeto contendo a matriz de custos.
    :return: Custo total da rota.
    """
    custo = 0 # inicializa o custo total
    # percorre a rota e soma os custos entre os pontos consecutivos.
    for i in range(len(rota) - 1):
        custo += dados.c[rota[i]][rota[i + 1]]

    return custo # retorna o csuto total