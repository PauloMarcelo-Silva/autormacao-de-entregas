import random
from calcula_custo import calcular_custo

def inicializar_populacao(dados, tamanho_populacao):
    """
    Gera uma população inicial de rotas aleatórias.

    Args:
        dados: Objeto com atributos 'n' (número de clientes) e 'c' (matriz de custos).
        tamanho_populacao: Tamanho da população.

    Returns:
        list: Lista de rotas.
    """
    pontos = list(range(1, dados.n + 1))  # Lista de pontos sem o depósito (0)
    return [[0] + random.sample(pontos, len(pontos)) + [0] for _ in range(tamanho_populacao)]

def selecionar_pais(populacao, dados):
    """
    Seleciona dois pais usando torneio.

    Args:
        populacao: Lista de rotas.
        dados: Objeto com atributos 'n' e 'c'.

    Returns:
        tuple: Dois pais selecionados.
    """
    torneio = random.sample(populacao, 5)  # Escolhe 5 indivíduos aleatórios
    torneio.sort(key=lambda r: calcular_custo(r, dados))  # Ordena pelo menor custo
    return torneio[0], torneio[1]  # Retorna os dois melhores

def cruzamento(pai1, pai2):
    """
    Aplica cruzamento de ordem (OX).

    Args:
        pai1: Rota do primeiro pai.
        pai2: Rota do segundo pai.

    Returns:
        list: Rota do filho gerado.
    """
    tamanho = len(pai1)
    inicio, fim = sorted(random.sample(range(1, tamanho - 1), 2))  # Sorteia dois pontos de corte

    filho = [-1] * tamanho  # Inicia com rota vazia
    filho[inicio:fim] = pai1[inicio:fim]  # Copia o segmento do pai1
    
    pos = fim
    for gene in pai2[1:-1]:  # Preenche com elementos do pai2
        if gene not in filho:
            if pos >= tamanho - 1:
                pos = 1  # Reinicia se chegar ao final
            filho[pos] = gene
            pos += 1

    return filho

def mutacao(rota):
    """
    Troca dois pontos aleatoriamente para mutação.

    Args:
        rota: Rota a ser mutada.

    Returns:
        list: Rota mutada.
    """
    i, j = random.sample(range(1, len(rota) - 1), 2)
    rota[i], rota[j] = rota[j], rota[i]
    return rota

def algoritmo_genetico(dados, geracoes=1000, tamanho_populacao=50):
    """
    Executa o algoritmo genético para encontrar uma boa rota.

    Args:
        dados: Objeto com atributos 'n' e 'c'.
        geracoes: Número de gerações.
        tamanho_populacao: Tamanho da população.

    Returns:
        tuple: Melhor rota e seu custo.
    """
    populacao = inicializar_populacao(dados, tamanho_populacao)
    melhor_rota = min(populacao, key=lambda r: calcular_custo(r, dados))
    melhor_custo = calcular_custo(melhor_rota, dados)

    sem_melhoria = 0
    for geracao in range(geracoes):
        nova_populacao = [melhor_rota]  # Preserva a melhor rota

        for _ in range(tamanho_populacao // 2):
            pai1, pai2 = selecionar_pais(populacao, dados)
            filho1 = cruzamento(pai1, pai2)
            filho2 = cruzamento(pai2, pai1)

            if random.random() < 0.2:  # 20% de chance de mutação
                filho1 = mutacao(filho1)
                filho2 = mutacao(filho2)

            nova_populacao.extend([filho1, filho2])

        populacao = nova_populacao
        nova_melhor_rota = min(populacao, key=lambda r: calcular_custo(r, dados))
        nova_melhor_custo = calcular_custo(nova_melhor_rota, dados)

        if nova_melhor_custo < melhor_custo:
            melhor_rota, melhor_custo = nova_melhor_rota, nova_melhor_custo
            sem_melhoria = 0
        else:
            sem_melhoria += 1

        if sem_melhoria >= 100:  # Parar após 100 gerações sem melhoria
            break

    return melhor_rota, melhor_custo