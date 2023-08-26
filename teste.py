import random

def desordenar_parcialmente(vetor_ordenado, percentual_desordem):
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

# Exemplo de uso
vetor_original = [10, 15, 20, 25, 30, 35, 40, 45, 50]
percentual_desordem = 30
novo_vetor = desordenar_parcialmente(vetor_original, percentual_desordem)
print("Vetor Original:", vetor_original)
print("Novo Vetor:", novo_vetor)
