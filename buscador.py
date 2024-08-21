import random
import time
import tracemalloc

def criar_arquivo_streaming(nome_arquivo, total_numeros, bloco_tamanho=10**7):
    with open(nome_arquivo, 'w') as arquivo:
        for inicio in range(1, total_numeros + 1, bloco_tamanho):
            fim = min(inicio + bloco_tamanho - 1, total_numeros)
            # Gerar e escrever números em bloco
            for i in range(inicio, fim + 1):
                arquivo.write(f"{i}\n")
    print(f"{nome_arquivo} criado com sucesso.")

def buscar_numero_arquivo(nome_arquivo, numero_a_buscar):
    # Iniciar monitoramento de tempo e memória
    tracemalloc.start()
    inicio_tempo = time.time()
    
    encontrado = False
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if int(linha.strip()) == numero_a_buscar:
                encontrado = True
                break
    
    # Finalizar monitoramento de tempo e memória
    tempo_total = time.time() - inicio_tempo
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Busca no arquivo {nome_arquivo}")
    print(f"Número {numero_a_buscar} {'encontrado' if encontrado else 'não encontrado'}.")
    print(f"Tempo total de execução: {tempo_total:.2f} segundos")
    print(f"Memória atual usada: {memoria_atual / (1024 * 1024):.2f} MB")
    print(f"Pico de memória: {memoria_pico / (1024 * 1024):.2f} MB\n")
    
    return encontrado

# Criar arquivos usando streaming de dados
criar_arquivo_streaming('um_milhao_numeros.txt', 10**6)
criar_arquivo_streaming('um_bilhao_numeros.txt', 10**9)
# criar_arquivo_streaming('um_trilhao_numeros.txt', 10**12) # Este código pode levar muito tempo

# Busca nos arquivos
numero_para_buscar_1m = random.randint(1, 10**6)
buscar_numero_arquivo('um_milhao_numeros.txt', numero_para_buscar_1m)

numero_para_buscar_1b = random.randint(1, 10**9)
buscar_numero_arquivo('um_bilhao_numeros.txt', numero_para_buscar_1b)

# Para o arquivo de um trilhão de números:
# numero_para_buscar_1t = random.randint(1, 10**12)
# buscar_numero_arquivo('um_trilhao_numeros.txt', numero_para_buscar_1t)
