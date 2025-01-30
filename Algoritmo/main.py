import os
from leitura_de_arquivo import ler_arquivo
from escolher_ponto_partida import escolher_ponto_partida
from algoritmo_guloso import algoritmo_guloso
from forca_bruta import forca_bruta
from algoritmo_genetico import algoritmo_genetico
from salvar_rota import salvar_rota

class Dados:
    """Classe para armazenar os dados lidos do arquivo"""
    def __init__(self, dados_dict):
        self.n = dados_dict["n"]
        self.c = dados_dict["c"]

def main():
    dados_dict = ler_arquivo("Instancias/intancias guilherme.txt")
    if not dados_dict:
        return

    dados = Dados(dados_dict)  # Converte para um objeto da classe Dados

    nomes = ["casa", "rodrigo", "emporio matuto", "Sertaozinho", "produtos regionais", "paulo", "casa da ilha", "Rivani", "transportadora"]

    # O usuário escolhe o ponto inicial
    ponto_partida = escolher_ponto_partida(nomes)

    # Executa o algoritmo guloso
    rota_gulosa, custo_guloso = algoritmo_guloso(dados, ponto_partida, nomes)

    # Cria a pasta 'resultados' se não existir
    pasta_resultados = "resultados"
    if not os.path.exists(pasta_resultados):
        os.makedirs(pasta_resultados)

    # Caminho completo do arquivo de saída
    caminho_saida = os.path.join(pasta_resultados, "saida_teste_4.txt")

    # Salva os resultados no arquivo dentro da pasta 'resultados'
    salvar_rota(caminho_saida, rota_gulosa, custo_guloso,nomes)

if __name__ == "__main__":
    main()




