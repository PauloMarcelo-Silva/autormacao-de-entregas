import sys
import os

class Dados:
    def __init__(self):
        self.n = 0  # Número de clientes
        self.k = 0  # Número de veículos
        self.c = []  # Matriz de custos

def arquivo_existe(nome_arquivo):
    return os.path.exists(nome_arquivo)

def ler_arquivo(nome_arquivo):
    dados = Dados()

    if not arquivo_existe(nome_arquivo):
        print(f"Arquivo não encontrado: {nome_arquivo}")
        return dados

    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados.n = int(arquivo.readline().strip())
            dados.k = int(arquivo.readline().strip())

            if dados.n <= 0 or dados.k <= 0:
                print("Dados inválidos no arquivo.")
                return dados

            dados.c = []
            for _ in range(dados.n + 1):
                linha = list(map(int, arquivo.readline().strip().split()))
                dados.c.append(linha)

            # Verifica se a matriz de custos tem o tamanho correto
            if len(dados.c) != dados.n + 1 or any(len(linha) != dados.n + 1 for linha in dados.c):
                print("Matriz de custos com tamanho incorreto.")
                return Dados()

    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

    return dados

# Função para calcular o custo de uma rota
def calcular_custo(rota, dados):
    custo = 0
    for i in range(len(rota) - 1):
        custo += dados.c[rota[i]][rota[i + 1]]
    return custo

# Função do algoritmo guloso modificado
def algoritmo_guloso(dados):
    todas_rotas = []
    melhor_rota = []
    menor_custo_total = float('inf')

    for inicio in range(1, dados.n + 1):
        rota = []
        visitado = [False] * (dados.n + 1)

        atual = inicio
        rota.append(0)  # Começa no depósito
        rota.append(atual)  # Visita o primeiro cliente

        while len(rota) < dados.n + 1:
            visitado[atual] = True

            # Encontrar o próximo cliente não visitado com menor custo
            proximo = -1
            menor_custo = float('inf')

            for i in range(1, dados.n + 1):
                if not visitado[i] and dados.c[atual][i] < menor_custo:
                    menor_custo = dados.c[atual][i]
                    proximo = i

            if proximo != -1:
                atual = proximo
                rota.append(atual)
                visitado[atual] = True
            else:
                break

        rota.append(0)  # Volta para o depósito

        todas_rotas.append(rota)

        custo_atual = calcular_custo(rota, dados)
        if custo_atual < menor_custo_total:
            menor_custo_total = custo_atual
            melhor_rota = rota

    return melhor_rota

# Função para salvar a melhor rota em um arquivo
def salvar_rota(nome_arquivo, rota, dados):
    try:
        with open(nome_arquivo, 'w') as arquivo_saida:
            custo_total = calcular_custo(rota, dados)
            arquivo_saida.write(f"Valor total da solução: {custo_total}\n")

            nomes = ["Rodoviária", "renato", "Lenildo", "Sertãozinho", "Edson", "Paulo", "Rodrigo", "Guilerme", "Casa"]

            arquivo_saida.write("Rota 1: ")
            for i in range(len(rota)):
                arquivo_saida.write(nomes[rota[i]])
                if i < len(rota) - 1:
                    arquivo_saida.write(" -> ")
            arquivo_saida.write("\n")

    except Exception as e:
        print(f"Erro ao abrir o arquivo para escrita: {e}")

def main():
    dados = ler_arquivo("Instancias/instacia 01.txt")

    if dados.n == 0 or dados.k == 0:
        print("Dados insuficientes para continuar.")
        return

    rota = algoritmo_guloso(dados)

    nomes = ["Rodoviária", "renato", "Lenildo", "Sertãozinho", "Edson"]
    print("Melhor rota encontrada: ", end="")
    for i in range(len(rota)):
        print(nomes[rota[i]], end="")
        if i < len(rota) - 1:
            print(" -> ", end="")
    print()

    salvar_rota("saida_test.txt", rota, dados)

if __name__ == "__main__":
    main()

