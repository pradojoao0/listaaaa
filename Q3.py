def lerMatriz():
    m, ler_linha = [], input()
    while ler_linha:
        m.append([int(i) for i in ler_linha.split(" ") if i])
        ler_linha = input()
    return m
def escreverMatriz(m):
    for linha in m:
        print(*linha)



vetor = [int(i) for i in input().split(" ") if i]
matriz = lerMatriz()

contador = 0

for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[0])):
        for itt in range(0, len(vetor)):
            if(matriz[linha][coluna] == vetor[itt]):
                del(vetor[itt])
                contador += 1
                break

print(contador)
