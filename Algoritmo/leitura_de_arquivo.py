class Dados:
    """
    Classe para armazenar as informações do problema de entregas.
    """
    def __init__(self):
        self.n = 0  # Número de clientes.
        self.k = 0  # Número de veículos (não usado no exemplo).
        self.c = []  # Matriz de custos entre os pontos.

def ler_arquivo(caminho):
    """
    Lê um arquivo contendo a matriz de custos e os dados do problema.

    :param caminho: Caminho do arquivo de entrada.
    :return: Dicionário com o número de pontos e a matriz de custos.
    """
    try:
        with open(caminho, "r") as arquivo:
            linhas = arquivo.readlines()
        
        n = int(linhas[0].strip())  # Número de pontos no primeiro linha.
        matriz = [list(map(int, linha.strip().split())) for linha in linhas[2:]]  # Matriz de custos.

        return {"n": n, "c": matriz}
    
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None