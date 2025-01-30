from calcula_custo import calcular_custo

def salvar_rota(nome_arquivo, rota_gulosa, custo_guloso, nomes):
    """
    Salva a rota gerada e seu custo total em um arquivo.

    :param nome_arquivo: Nome do arquivo de saída.
    :param rota_gulosa: Lista representando a ordem dos pontos visitados pelo algoritmo guloso.
    :param custo_guloso: Custo total da rota gerada pelo algoritmo guloso.
    :param nomes: Lista de nomes correspondentes aos pontos.
    """
    try:
        with open(nome_arquivo, 'w') as arquivo_saida:
            arquivo_saida.write("=== Algoritmo Guloso ===\n")
            arquivo_saida.write(f"Custo: {custo_guloso} minutos\n")
            arquivo_saida.write(" -> ".join(nomes[i] for i in rota_gulosa) + "\n")

    except Exception as e:
        print(f"Erro ao abrir o arquivo para escrita: {e}")

