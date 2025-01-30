def algoritmo_guloso(dados, ponto_inicial, nomes):
    """
    Implementação do algoritmo guloso para encontrar a solução de entrega.
    
    :param dados: Objeto contendo a matriz de custos.
    :param ponto_inicial: Índice do ponto inicial para a rota.
    :param nomes: Lista de nomes dos pontos.
    :return: Rota ótima e o custo total.
    """
    pontos_visitados = [False] * dados.n
    rota = [ponto_inicial]
    custo_total = 0
    pontos_visitados[ponto_inicial] = True
    
    ponto_atual = ponto_inicial
    
    while len(rota) < dados.n - 1:  # Menos o ponto 'casa'
        menor_custo = float('inf')
        proximo_ponto = -1
        
        # Encontra o próximo ponto não visitado com o menor custo
        for i in range(dados.n):
            if not pontos_visitados[i] and dados.c[ponto_atual][i] < menor_custo:
                menor_custo = dados.c[ponto_atual][i]
                proximo_ponto = i
        
        # Adiciona o próximo ponto na rota
        rota.append(proximo_ponto)
        pontos_visitados[proximo_ponto] = True
        custo_total += menor_custo
        ponto_atual = proximo_ponto
    
    # Adiciona o ponto "casa" no final da rota
    casa = nomes.index("casa")  # Ponto final
    custo_total += dados.c[ponto_atual][casa]
    rota.append(casa)
    
    return rota, custo_total

