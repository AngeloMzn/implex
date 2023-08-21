import random
inc = int(input('digite o valor de inicio do vetor:'))
fim = int(input('digite o valor final do vetor:'))
stp = int(input('digite o intervalo de soma entre as posicoes do vetor:'))
rpt = int(input('digite o numero de vezes que o teste deve se repetir:'))
ordenado = []
aleatorio = []
reverso = []
count = 0
value = inc
while inc <= fim:
    ordenado.append(value)
    value = value + stp
while count != (fim - inc):
    number = random.randrange(inc, fim + 1, stp)
    aleatorio.append(number)
    count += 1
value = fim
while value != inc:
    reverso.append(value)
    value = value - stp

for i in range(len(reverso)):
    print(reverso[i])
