#Angelo Vinicius Hernandez Mazarin
import random
import time
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
def criar_vetor_parcialmente_ordenado(vetor_ordenado, percentual_desordem):
    if percentual_desordem <= 0 or percentual_desordem > 100:
        raise ValueError("O percentual de desordem deve estar entre 0 e 100.")
    num_elementos = len(vetor_ordenado)
    num_elementos_desordenar = int(num_elementos * percentual_desordem / 100)
    novo_vetor = vetor_ordenado.copy()
    while True:
        indices_desordenar = random.sample(range(num_elementos), num_elementos_desordenar)
        indices_desordenar.sort()
        valores_desordenados = [novo_vetor.pop(i) for i in reversed(indices_desordenar)]
        random.shuffle(valores_desordenados)
        for i, indice in enumerate(indices_desordenar):
            novo_vetor.insert(indice, valores_desordenados[i])
        if novo_vetor != sorted(vetor_ordenado):
            break
    return novo_vetor
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
    result = vetor.copy()
    if len(result) <= 1:
        return result
    mid = len(result) // 2
    left_half = result[:mid]
    right_half = result[mid:]
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
def quick_sort(vetor):
    result = vetor.copy()
    if len(result) <= 1:
        return result
    else:
        pivot = result[len(result) // 2]
        left = [x for x in result if x < pivot]
        middle = [x for x in result if x == pivot]
        right = [x for x in result if x > pivot]
        
        return quick_sort(left) + middle + quick_sort(right)
#countingsort
def counting_sort(vetor):
    aux = vetor.copy()
    max_val = max(aux)
    count = [0] * (max_val + 1)
    result = [0] * len(aux)
    
    for num in aux:
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for num in aux:
        result[count[num] - 1] = num
        count[num] -= 1
    
    return result
#################################################EXECUCAO####################################################
inc = int(input('Digite o valor de início do vetor: '))
fim = int(input('Digite o valor final do vetor: '))
stp = int(input('Digite o intervalo de soma entre as posições do vetor: '))
rpt = int(input('Digite o número de vezes que o teste deve se repetir: '))
#criar vetores
vetor_ordenado = criar_vetor_ordenado(inc, fim, stp)
vetor_aleatorio = criar_vetor_aleatorio(vetor_ordenado)
vetor_reverso = criar_vetor_reverso(inc, fim, stp)
vetor_quase_ordenado = criar_vetor_parcialmente_ordenado(vetor_ordenado, 30)  
# prints para ver os vetores
print('Vetor Ordenado:', vetor_ordenado)
print('Vetor Aleatório:', vetor_aleatorio)
print('Vetor Reverso:', vetor_reverso)
print('Vetor Quase Ordenado:', vetor_quase_ordenado)
for i in range(rpt):
    #===============================insertions========================================
    #ordenado
    inicio = time.time()
    result_vetor_ordenado_insertion = insertion_sort(vetor_ordenado)
    fim = time.time()
    tempo_vetor_ordenado_insertion = fim - inicio
    #aleatorio
    inicio = time.time()
    result_vetor_aleatorio_insertion = insertion_sort(vetor_aleatorio)
    fim = time.time()
    tempo_vetor_aleatorio_insertion = fim - inicio
    #reverso
    inicio = time.time()
    result_vetor_reverso_insertion = insertion_sort(vetor_reverso)
    fim = time.time()
    tempo_vetor_reverso_insertion = fim - inicio
    #quase ordenado
    inicio = time.time()
    result_vetor_quase_ordenado_insertion = insertion_sort(vetor_quase_ordenado)
    fim = time.time()
    tempo_vetor_quase_ordenado_insertion = fim - inicio
    #================================selections=======================================
    #ordenado
    inicio = time.time()
    result_vetor_ordenado_selection= selection_sort(vetor_ordenado)
    fim = time.time()
    tempo_vetor_ordenado_selection = fim - inicio
    #aleatorio
    inicio = time.time()
    result_vetor_aleatorio_selection = selection_sort(vetor_aleatorio)
    fim = time.time()
    tempo_vetor_aleatorio_selection = fim - inicio
    #reverso
    inicio = time.time()
    result_vetor_reverso_selection = selection_sort(vetor_reverso)
    fim = time.time()
    tempo_vetor_reverso_selection = fim - inicio
    #quase ordenado
    inicio = time.time()
    result_vetor_quase_ordenado_selection = selection_sort(vetor_quase_ordenado)
    fim = time.time()
    tempo_vetor_quase_ordenado_selection = fim - inicio
    #==============================mergesorts=========================================
    #ordenado
    inicio = time.time()
    result_vetor_ordenado_mergesort = merge_sort(vetor_ordenado)
    fim = time.time()
    tempo_vetor_ordenado_mergesort = fim - inicio
    #aleatorio
    inicio = time.time()
    result_vetor_aleatorio_mergesort = merge_sort(vetor_aleatorio)
    fim = time.time()
    tempo_vetor_aleatorio_mergesort = fim - inicio
    #reverso
    inicio = time.time()
    result_vetor_reverso_mergesort = merge_sort(vetor_reverso)
    fim = time.time()
    tempo_vetor_reverso_mergesort = fim - inicio
    #quase ordenado
    inicio = time.time()
    result_vetor_quase_ordenado_mergesort = merge_sort(vetor_quase_ordenado)
    fim = time.time()
    tempo_vetor_quase_ordenado_mergesort = fim - inicio
    #===============================heapsorts=========================================
    #ordenado
    inicio = time.time()
    result_vetor_ordenado_heapsort = heap_sort(vetor_ordenado)
    fim = time.time()
    tempo_vetor_ordenado_heapsort = fim - inicio
    #aleatorio
    inicio = time.time()
    result_vetor_aleatorio_heapsort = heap_sort(vetor_aleatorio)
    fim = time.time()
    tempo_vetor_aleatorio_heapsort = fim - inicio
    #reverso
    inicio = time.time()
    result_vetor_reverso_heapsort = heap_sort(vetor_reverso)
    fim = time.time()
    tempo_vetor_reverso_heapsort = fim - inicio
    #quase ordenado
    inicio = time.time()
    result_vetor_quase_ordenado_heapsort = heap_sort(vetor_quase_ordenado)
    fim = time.time()
    tempo_vetor_quase_ordenado_heapsort = fim - inicio
    #===============================quicksorts=========================================
    #ordenado
    inicio = time.time()
    result_vetor_ordenado_quicksort = quick_sort(vetor_ordenado)
    fim = time.time()
    tempo_vetor_ordenado_quicksort = fim - inicio
    #aleatorio
    inicio = time.time()
    result_vetor_aleatorio_quicksort = quick_sort(vetor_aleatorio)
    fim = time.time()
    tempo_vetor_aleatorio_quicksort = fim - inicio
    #reverso
    inicio = time.time()
    result_vetor_reverso_quicksort = quick_sort(vetor_reverso)
    fim = time.time()
    tempo_vetor_reverso_quicksort = fim - inicio
    #quase ordenado
    inicio = time.time()
    result_vetor_quase_ordenado_quicksort = quick_sort(vetor_quase_ordenado)
    fim = time.time()
    tempo_vetor_quase_ordenado_quicksort = fim - inicio
    #===============================countingsorts======================================
    #ordenado
    inicio = time.time()
    result_vetor_ordenado_countingsort = counting_sort(vetor_ordenado)
    fim = time.time()
    tempo_vetor_ordenado_countingsort = fim - inicio
    #aleatorio
    inicio = time.time()
    result_vetor_aleatorio_countingsort = counting_sort(vetor_aleatorio)
    fim = time.time()
    tempo_vetor_aleatorio_countingsort = fim - inicio
    #reverso
    inicio = time.time()
    result_vetor_reverso_countingsort = counting_sort(vetor_reverso)
    fim = time.time()
    tempo_vetor_reverso_countingsort = fim - inicio
    #quase ordenado
    inicio = time.time()
    result_vetor_quase_ordenado_countingsort = counting_sort(vetor_quase_ordenado)
    fim = time.time()
    tempo_vetor_quase_ordenado_countingsort = fim - inicio
    #print tempo
    print('tempo vetor ordenado insertion',tempo_vetor_ordenado_insertion)
