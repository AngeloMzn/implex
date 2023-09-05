import matplotlib.pyplot as plt

# Dados
num_elementos = [1000, 2000, 3000, 4000, 5000]  # Número de elementos
tempo_selection_sort = [1.23, 4.56, 9.87, 16.43, 25.67]  # Tempos para o Selection Sort
tempo_insertion_sort = [0.98, 3.45, 7.89, 13.21, 22.34]  # Tempos para o Insertion Sort
tempo_merge_sort = [0.45, 1.23, 2.67, 4.32, 7.89]  # Tempos para o Merge Sort
tempo_heap_sort = [0.56, 1.78, 3.21, 5.67, 9.01]  # Tempos para o Heap Sort
tempo_quick_sort = [0.34, 0.98, 2.12, 3.76, 6.43]  # Tempos para o Quick Sort
tempo_counting_sort = [0.21, 0.45, 1.09, 1.98, 3.12]  # Tempos para o Counting Sort

# Crie o gráfico
plt.figure(figsize=(10, 6))  # Defina o tamanho da figura

# Plote as curvas para cada algoritmo
plt.plot(vet_tamanhos, vet_tempo_selections_ordenado, label='Selection Sort', marker='o')
plt.plot(vet_tamanhos, vet_tempo_insertions_ordenado, label='Insertion Sort', marker='o')
plt.plot(vet_tamanhos, vet_tempo_mergesorts_ordenado, label='Merge Sort', marker='o')
plt.plot(vet_tamanhos, vet_tempo_heapsorts_ordenado, label='Heap Sort', marker='o')
plt.plot(vet_tamanhos, vet_tempo_quicksorts_ordenado, label='Quick Sort', marker='o')
plt.plot(vet_tamanhos, vet_tempo_countingsorts_ordenado, label='Counting Sort', marker='o')

# Adicione rótulos aos eixos x e y, e um título
plt.xlabel('Número de Elementos')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Tempo de execução por numero de elementos do vetor ordenado')

# Mostre a legenda
plt.legend()

# Exiba o gráfico
plt.grid(True)  # Adicione uma grade para melhorar a leitura
plt.show()
