#Angelo Vinicius Hernandez Mazarin
import random
from unittest import result
#criação de vetores
def criar_vetor_ordenado(inicio, fim, stp):
    return list(range(inicio, fim + 1, stp))

def criar_vetor_aleatorio(vetor_ordenado):
    vetor_aleatorio = vetor_ordenado[:]
    tamanho_desordem = int(len(vetor_ordenado))
    indices_desordenados = random.sample(range(len(vetor_ordenado)), tamanho_desordem)
    numeros_usados = set()
    for idx in indices_desordenados:
        numero_escolhido = random.choice(vetor_ordenado)
        while numero_escolhido in numeros_usados:
            numero_escolhido = random.choice(vetor_ordenado)
        
        numeros_usados.add(numero_escolhido)
        vetor_aleatorio[idx] = numero_escolhido 
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
#insertionsort
def insertion_sort(vetor):
    result = vetor.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and key < result[j]:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result
#selectionsort
def selection_sort(vetor):
    result = vetor.copy()
    n = len(result)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if result[j] < result[min_index]:
                min_index = j      
        result[i], result[min_index] = result[min_index], result[i]
    return result
#mergesort
def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

def merge_sort(vetor):
    if len(vetor) <= 1:
        return vetor
    mid = len(vetor) // 2
    left_half = vetor[:mid]
    right_half = vetor[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

#heapsort
def heapify(result, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and result[left] > result[largest]:
        largest = left
    if right < n and result[right] > result[largest]:
        largest = right
    if largest != i:
        result[i], result[largest] = result[largest], result[i]
        heapify(result, n, largest)

def heap_sort(vetor):
    result = vetor.copy()
    n = len(result)
    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)
    for i in range(n - 1, 0, -1):
        result[i], result[0] = result[0], result[i]
        heapify(result, i, 0)
    return result
#quicksort
def partition(result, low, high):
    pivo = result[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and result[left] <= pivo:
            left += 1
        while result[right] >= pivo and right >=left:
            right -= 1
        if right < left:
            done= True
        else:
            result[left], result[right] = result[right], result[left]
    result[low], result[right] = result[right], result[low]
    return right

def quick_sort(vetor, low, high):
    result = vetor.copy()
    if low < high:
        pivo_index = partition(result, low, high)
        quick_sort(result, low, pivo_index)
        quick_sort(result, pivo_index + 1, high)
    return result
#countingsort
def counting_sort(vetor):
    max_val = max(vetor)
    min_val = min(vetor)
    range = max_val - min_val + 1
    count_vetor = [0] * range
    for num in vetor:
        count_vetor[num - min_val] += 1  
    for i in range(1, len(count_vetor)):
        count_vetor[i] += count_vetor[i - 1]
    result = [0] * len(vetor)
    for num in reversed(vetor):
        result[count_vetor[num - min_val] - 1] = num
        count_vetor[num - min_val] -= 1
    return result

#################################################EXECUCAO####################################################
inc = int(input('Digite o valor de início do vetor: '))
fim = int(input('Digite o valor final do vetor: '))
stp = int(input('Digite o intervalo de soma entre as posições do vetor: '))
rpt = int(input('Digite o número de vezes que o teste deve se repetir: '))

tamanho_vetor = (fim - inc) // stp + 1

#criar vetores
vetor_ordenado = criar_vetor_ordenado(inc, fim, stp)
vetor_aleatorio = criar_vetor_aleatorio(vetor_ordenado)
vetor_reverso = criar_vetor_reverso(inc, fim, stp)
vetor_quase_ordenado = criar_vetor_quase_ordenado(vetor_ordenado, 0.1)  

# prints para ver os vetores
#print('Vetor Ordenado:', vetor_ordenado)
print('Vetor Aleatório:', vetor_aleatorio)
# print('Vetor Reverso:', vetor_reverso)
# print('Vetor Quase Ordenado:', vetor_quase_ordenado)
for i in range(rpt):
    #insertions
    result_vetor_aleatorio_insertion = insertion_sort(vetor_aleatorio)
    #selection
    result_vetor_aleatorio_selection = selection_sort(vetor_aleatorio)
    print(result_vetor_aleatorio_selection)
    print(vetor_aleatorio)

    
