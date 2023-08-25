import random
inc = int(input('digite o valor de inicio do vetor:'))
fim = int(input('digite o valor final do vetor:'))
stp = int(input('digite o intervalo de soma entre as posicoes do vetor:'))
rpt = int(input('digite o numero de vezes que o teste deve se repetir:'))
ordenado = []
aleatorio = []
reverso = []
quaseOrdenado = []
count = 0
value = inc
while value <= fim:
    ordenado.append(value)
    value = value + stp

while count != (fim - inc) + stp:
    number = random.randrange(inc, fim + 1, stp)
    aleatorio.append(number)
    count += stp
value = fim
while value != inc-stp:
    reverso.append(value)
    value = value - stp

quaseOrdenado = ordenado
n = len(quaseOrdenado)
numShuffle = n * 0.1  # 10% do vetor
indicesShuffle = random.sample(range(n), numShuffle)
for i in indicesShuffle:
    j = random.choice(indicesShuffle)
    quaseOrdenado[i], quaseOrdenado[j] = quaseOrdenado[j], quaseOrdenado[i]
for i in range(len(quaseOrdenado)):
    print(quaseOrdenado[i])
