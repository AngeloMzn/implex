import random

def criar_vetor_ordenado(inicio, fim, stp):
    return list(range(inicio, fim + 1, stp))

def criar_vetor_aleatorio(vetor_ordenado):
    
    vetor_aleatorio = vetor_ordenado[:]
    tamanho_desordem = int(len(vetor_ordenado))
    indices_desordenados = random.sample(range(len(vetor_ordenado)), tamanho_desordem)
    for idx in indices_desordenados:
        vetor_aleatorio[idx] = random.choice(vetor_ordenado) 
    
    return vetor_aleatorio

def criar_vetor_reverso(inicio, fim, stp):
    return list(range(fim, inicio - 1, -stp))

def criar_vetor_quase_ordenado(vetor_ordenado, porcentagem_desordem):
    tamanho_desordem = int(len(vetor_ordenado) * porcentagem_desordem)
    indices_desordenados = random.sample(range(len(vetor_ordenado)), tamanho_desordem)
    
    vetor_quase_ordenado = vetor_ordenado[:]
    
    for idx in indices_desordenados:
        vetor_quase_ordenado[idx] = random.choice(vetor_ordenado)
    
    return vetor_quase_ordenado

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key








#################################################EXECUÇÃO####################################################
inc = int(input('Digite o valor de início do vetor: '))
fim = int(input('Digite o valor final do vetor: '))
stp = int(input('Digite o intervalo de soma entre as posições do vetor: '))
rpt = int(input('Digite o número de vezes que o teste deve se repetir: '))

tamanho_vetor = (fim - inc) // stp + 1

# Criar o vetor ordenado
vetor_ordenado = criar_vetor_ordenado(inc, fim, stp)

# Criar os outros vetores
vetor_aleatorio = criar_vetor_aleatorio(vetor_ordenado)
vetor_reverso = criar_vetor_reverso(inc, fim, stp)
vetor_quase_ordenado = criar_vetor_quase_ordenado(vetor_ordenado, 0.2)  # Exemplo de 20% de desordem
# prints para ver os vetores
# print('Vetor Ordenado:', vetor_ordenado)
# print('Vetor Aleatório:', vetor_aleatorio)
# print('Vetor Reverso:', vetor_reverso)
# print('Vetor Quase Ordenado:', vetor_quase_ordenado)
